package org.example

class GKP {
    def steps

    GKP(final steps){
        this.steps = steps
    }

    Map CLUSTER_NS_APPS_MAP = [:]
    String SNOW_ID = null
    String egressConfigYmlPath = "egress-config.yaml"

    void gkpOps(Map params, Map otherParams) {
        String platformEnv = params.Environment
        steps.echo("Params: ${params}, Other Params: ${otherParams}")

        Map actionParams = [:]
        steps.stage('Validating Action Parameters') {
            if(otherParams.isEmpty()) {
                actionParams = getActionParams(platformEnv)
            } else {
                actionParams = otherParams
            }
            steps.echo("Action Params: ${actionParams}")
        }

        steps.node("jules-deployer") {
            setActionParams(actionParams, platformEnv)
            performAction(actionParams)
        }
    }

    void setActionParams(Map actionParams, String platformEnv) {
        SNOW_ID = (platformEnv.equalsIgnoreCase('prod')) ? actionParams.SNOW_ID : null
        CLUSTER_NS_APPS_MAP = getClustersNsAndAppsDetails(actionParams)

        if (CLUSTER_NS_APPS_MAP.isEmpty()) {
            steps.error("Something went wrong ... CLUSTERS_NS_APPS_MAP is Empty : ${CLUSTER_NS_APPS_MAP}")
        }
        steps.echo("CLUSTER_NS_APPS_MAP: " + CLUSTER_NS_APPS_MAP)
    }

    void performAction(Map actionParams) {
        CLUSTER_NS_APPS_MAP.each { cluster, appsAndNamespaceInCluster ->
            String gkpDashboardApiEP = "https://api.${cluster}.gkp.pavan.net:6443"
            final String k8sPath = "./kube/config"
            steps.withEnv(["KUBECONFIG=${k8sPath}"]) {
                steps.jules_jeti_withGkpCredentials(gkpDashboardApiEP, SNOW_ID, false)
                String namespaceQuotaLimits = getQuotaLimits(actionParams.Namespace as String)
                steps.echo("Namespace quota: ${namespaceQuotaLimits}")
                switch ("${actionParams['Action']}") {
                    case "stop":
                        executeStop(actionParams.Action as String, cluster as String, appsAndNamespaceInCluster as Map, actionParams.Namespace as String)
                        break
                    case "restart":
                        appsAndNamespaceInCluster.apps.each { String appName ->
                            executeRestart (actionParams.Action as String, cluster as String, appName, actionParams.Namespace as String)
                        }
                        break
                    case "scale_replicas":
                        executeScaleReplicas (actionParams.Action as String, cluster as String, apps AndNamespaceInCluster as Map, actionParams.Namespace as String, actionParams.Replicas as Integer)
                        break
                    case "delete_pods":
                        executeDeletePods (actionParams.Action as String, cluster as String, actionParams.Namespace as String, apps AndNamespaceInCluster as Map)
                        break
                    case "delete_application":
                        executeDeleteApp(actionParams.Action as String, cluster as String, appsAndNamespaceInCluster as Map, actionParams.Namespace as String)
                        break
                    case "delete_namespace":
                        executeDeleteNS (actionParams.Action as String, cluster as String, actionParams.Namespace as String)
                        break
                    case "enable-egress-to-photon-insights":
                        enableEgressToPhotonInsights (actionParams.Action as String, cluster as String, actionParams.Namespace as String, appsAndNamespaceInCluster as Map)
                        break
                    default:
                        steps.error("Aborting. Invalid Action: ${actionParams["Action"]}")
                }

            }
        }
    }

    Map getActionParams(String platformEnv) {
        List parametersList = []
        if (platformEnv.equalsIgnoreCase('prod')) {
            parametersList.add([[$class: 'StringParameterDefinition', name: 'SNOW_ID', defaultValue: '', description: 'Specify SNOW Change ID']])
        }

        List actions = ['Select', 'stop', 'restart', 'scale_replicas', 'delete_pods', 'delete_application', 'delete_namespace', 'enable-egress-to-photon-insights']
        List parametersList1 = [
                [$class: 'ChoiceParameterDefinition', name: 'Action', choices: actions, description: 'Select Action to perform'],
                [$class: 'StringParameterDefinition', name: 'Cluster', defaultValue: '', description: 'Specify Cluster(s) name (comma separated) e.g. mt-t1.na-mw-c01']
        ]

        parametersList = parametersList + parametersList1
        Map actionParams = steps.input(id: 'GKP_INPUT', message: 'GKP Action Params', ok: 'SUBMIT', submitterParameter: 'targetSubmitterID', parameters: parametersList)

        validateActionParams(platformEnv, actionParams)

        List parametersList2 = []
        switch (actionParams['Action']) {
            case 'delete_pods':
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Namespace', defaultValue: '', description: 'Specify Namespace']])
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Pods', defaultValue: '', description: 'Specify Pod names (comma separated)']])
                break
            case 'stop':
            case 'restart':
            case 'delete_application':
            case 'enable-egress-to-photon-insights':
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Namespace', defaultValue: '', description: 'Specify Namespace']])
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Application', defaultValue: '', description: 'Specify Application names (comma separated)']])
                break
            case 'delete_namespace':
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Namespace', defaultValue: '', description: 'Specify Namespace']])
                break
            case 'scale_replicas':
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Namespace', defaultValue: '', description: 'Specify Namespace']])
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Application', defaultValue: '', description: 'Specify Application names (comma separated)']])
                parametersList2.add([[$class: 'StringParameterDefinition', name: 'Replicas', defaultValue: '', description: 'Select No of Replicas']])
                break
            default:
                steps.error("Aborting. Invalid GKP Action: ${actionParams['Action']}")
        }
        if (!parametersList2.isEmpty()) {
            Map actionParamsL2 = steps.input(id: 'ADDL_GKP_INPUT', message: 'Addl. GKP Action Params', ok: 'SUBMIT', submitterParameter: 'targetSubmitterID', parameters: parametersList2)
            actionParams = actionParams + actionParamsL2
        }
        validateActionParams(platformEnv, actionParams)
        return actionParams
    }

    void confirmAction(String platformEnv, String action) {
        if (action in ['delete_application', 'delete_namespace', 'delete_pods']) {
            steps.stage('Waiting for Confirmation') {
                String confirmDialog = "$action Action selected for ${platformEnv} env. Please Confirm?"
                steps.input(message: confirmDialog, submitterParameter: 'releaseApprover')
            }
        }
    }

    void validateActionParams(String platformEnv, Map actionParams) {
        List missingParams = []
        actionParams.findAll {
            if ((it.value.toString().isEmpty() || it.value.toString().equalsIgnoreCase('Select'))) {
                if (!((it.key.equalsIgnoreCase('Application') && ("${actionParams['Action']}" in ['restart', 'stop', 'scale_replicas', 'delete_application', 'enable-egress-to-photon-insights'])))) {
                    if (!((it.key.equalsIgnoreCase('Replicas') && ("${actionParams['Action']}" in ['scale_replicas'])))) {
                        if (!(it.key.equalsIgnoreCase('SNOW_ID') && (!platformEnv.equalsIgnoreCase('Prod')))) {
                            missingParams.add(it.key)
                        }
                    }
                }
            }
        }
        if (!missingParams.isEmpty()) {
            steps.error("Aborting. Action Input parameters cannot be empty for: ${missingParams}")
        }
        if (actionParams.Namespace && !actionParams.Namespace.matches(Constants.NAME_SPACE_PATTERN)) {
            steps.error("Invalid NameSpace: ${actionParams.Namespace}")
        }
        confirmAction(platformEnv, actionParams['Action'] as String)
    }

    Map getClustersNsAndAppsDetails (Map actionParams) {
        Map clustersNamespaceAndApps = [:]
        Map invalidClustersNamespaceAndApps = [:]
        (actionParams['Cluster'] as Map).split(',').findAll {
            String cluster = it.toString().trim()
            String gkpDashboardApiEP = "https://api.${cluster}.gkp.pavan.net:6443"
            final String k8sPath = "./.kube/config"
            steps.withEnv(["KUBECONFIG=${k8sPath}"]) {
                steps.jules jeti_withGkpCredentials(gkpDashboardApiEP, SNOW_ID, false)

                Map validNamespaceAndAppsInCluster = [:]
                Map invalidNamespaceAndAppsInCluster = [:]

                if (actionParams.Namespace) {
                    steps.echo("Validating Namespace: ${actionParams['Namespace']}")
                    String status = getNamespaceStatus(actionParams.Namespace as String)
                    if (!status.equalsIgnoreCase("active")) {
                        invalidNamespaceAndApps InCluster.put('nsNotFound', actionParams['Namespace'])
                    } else {
                        validNamespaceAndApps InCluster.put('ns', actionParams['Namespace'])
                    }
                }
                if (actionParams.Application)
                    List validAppNames = []
                List invalidAppNames = []
                (actionParams['Application'] as String).split(',').findAll {
                    String appName = it.toString().trim()
                    steps.echo("Validating AppName: ${appName}")
                    Integer status = checkAppStatus(appName, actionParams.Namespace as String)
                    if (status != 0) {
                        invalidAppNames.add(appName)
                    } else {
                        validAppNames.add(appName)
                    }
                }
                if (!validAppNames.isEmpty()) {
                    validNamespaceAndApps InCluster.put('apps', validAppNames)
                }
                if (!invalidAppNames.isEmpty()) {
                    invalidNamespaceAndApps InCluster.put('appsNotFound', invalidAppNames)
                }
            }
            if (actionParams['Pods'])
                List validPodNames = []
            List invalidPodNames = []
            (actionParams['Pods'] as String).split(',').findAll {
                String podName = it.toString().trim()
                String namespace = actionParams.Namespace
                String kubeCommand = "kubectl get pod ${podName} -n ${namespace} -o jsonpath={.status.phase}"
                def podExists = isResourceExists(kubeCommand)
                podExists ? validPodNames.add(podName) : invalid PodNames.add(podName)
            }
            if (!validPodNames.isEmpty()) {
                validNamespaceAndApps InCluster.put('pods', validPodNames)
            }
            if (!invalidPodNames.isEmpty()) {
                invalidNamespaceAndApps InCluster.put('podsNotFound', invalidPodNames)
            }
        }

        if (actionParams.Pods) {
            List validPodNames = []
            List invalidPodNames = []
            (actionParams['Pods'] as String).split(',').findAll {
                String podName = it.toString().trim()
                String namespace = actionParams.Namespace
                String kubeCommand = "kubectl get pod ${podName} -n ${namespace} -o jsonpath={.status.phase}"
                def podExists = isResourceExists(kubeCommand)
                podExists ? validPodNames.add(podName) : invalid PodNames.add(podName)
            }
            if (!validPodNames.isEmpty()) {
                validNamespaceAndAppsInCluster.put('pods', valid PodNames)
            }
            if (!invalidPodNames.isEmpty()) {
                invalidNamespaceAndAppsInCluster.put('podsNotFound', invalidPodNames)
            }
        }

        if (!validNamespaceAndAppsInCluster.isEmpty()) {
            clustersNamespaceAndApps.put(cluster, validNamespaceAndApps InCluster)
        }
        if (!invalidNamespaceAndApps InCluster.isEmpty()) {
            invalidClustersNamespaceAndApps.put(cluster, invalidNamespaceAndApps InCluster)
        }

        if (!invalidClustersNamespaceAndApps.isEmpty()) {
            clustersNamespaceAndApps.put(cluster, validNamespaceAndApps InCluster)
        }
        steps.echo("Validated Requested Inputs. clustersNamespaceAndApps: " + clustersNamespaceAndApps)
        return clustersNamespaceAndApps
    }


    boolean isResourceExists(String controllerKind, String appName, String namespace) {
        String command = "kubectl get ${controllerKind} --namespace=${namespace} -o-jsonpath='{.items[*].metadata.name}'"
        def cmdResult = steps.sh(script: command, returnStdout: true)
        if (!cmdResult?.isEmpty()) {
            def resources = cmd Result.trim().split('\\s+')
            if (resources.contains(appName)) {
                return true
            }
        }
        return false
    }

    String getControllerKind(String namespace, String appName) {
        try {
            List controllerKinds = ['deployments', 'replicaset', 'statefulset']
            String controllerType = controllerKinds.find { controllerKind -> isResourceExists(controllerKind, appName, namespace) }
                    ?.with { it.equalsIgnoreCase('deployments') ? 'deployment' : it }
            if (!controllerType) {
                throw new IllegalStateException("Unable to determine controller kind for the given inputs Namespace: ${namespace}, Appname: ${appName}")
            }
            return controllerType
        } catch (IllegalStateException e) {
            throw e
        } catch ( Exception e) {
            steps.echo("Exception Occured while determining the controller type Namespace: ${namespace}, Appname: ${appName}, Exception: ${e}")
            steps.error("Aborting: Unable to determine controller kind for Namespace - ${namespace}, Appname - ${appName}")
        }
    }

    void executeStop(String action, String cluster, Map appsInCluster, String namespace) {
        appsInCluster.apps.each { String appName ->
            steps.stage("Executing Action - ${action} Cluster -${cluster} Namespace - ${namespace} Appname -${appName}") {
                try {
                    String controllerKind = getControllerKind(namespace, appName)
                    Integer available
                    Replicas = getReplicas(appName as String, namespace, controllerKind)
                    Integer readyReplicas = 0
                    steps.sh "kubectl scale --replicas=0 ${controllerKind}/${appName} --namespace=${namespace}"
                    validateReadyReplicas(readyReplicas, availableReplicas, appName, namespace, controllerKind)
                } catch (FlowInterruptedException e) {
                    steps.echo("Timeout Occurred: ${e} : Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname ${appName}")
                    stageFailed("Timeout Occurred Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname -${appName}")
                } catch (Exception e) {
                    steps.echo("Aborting: Exception Occurred : ${e} : Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname -${appName}")
                    steps.error("Aborting: Exception Occurred Action - ${action}, Cluster -${cluster}, Namespace - ${namespace}, Appname - ${appName}.Please check console log for details.")
                }
            }
        }
    }

    void executeRestart(String action, String cluster, String appName, String namespace) {
        steps.stage("Executing Action - ${action} Cluster - ${cluster} Namespace - ${namespace} Appname -${appName}") {
            try {
                String controllerKind = getControllerKind(namespace, appName)
                Integer availableReplicas = getReplicas(appName as String, namespace, controllerKind)
                steps.echo("available Replicas: $available Replicas")
                Integer readyReplicas = 0
                if (controllerkind.equalsIgnoreCase('replicaset')) {
                    //replicas setting to Zero for restart and scaling back to available replicas
                    steps.sh "kubectl scale --replicas=${readyReplicas} ${controllerKind}/${appName} --namespace=${namespace}"
                    validateReadyReplicas(readyReplicas, availableReplicas, appName, namespace, controllerKind)
                    steps.sh "kubectl scale --replicas=${availableReplicas} ${controllerKind}/${appName} --namespace=${namespace}"
                    validateReadyReplicas(availableReplicas, readyReplicas, appName, namespace, controllerKind)
                } else {
                    steps.sh "kubectl rollout restart ${controllerKind}/${appName} --namespace=${namespace}"
                    steps.timeout(time: Constants.ROLLOUT_STATUS_TIMEOUT, unit: 'SECONDS') {
                        steps.sh "kubectl rollout status ${controllerKind}/${appName} --namespace=${namespace}"
                    }
                }
            } catch (FlowInterruptedException e) {
                steps.echo("Timeout Occurred: ${e} : Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname ${appName}")
                stageFailed("Timeout Occurred Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname -${appName}")
            } catch (Exception e) {
                steps.echo("Aborting: Exception Occurred: ${e} : Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname -${appName}")
                steps.error("Aborting: Exception Occurred Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}, Appname ${appName}. Please check console log for details.")
            }
        }
    }

    private void validateReadyReplicas (int availableReplicas, int readyReplicas, appName, String namespace, String controllerKind) {
        steps.timeout(time: Constants.ROLLOUT_STATUS_TIMEOUT, unit: 'SECONDS') {
            while (availableReplicas != readyReplicas ) {
                readyReplicas = getReplicas(appName as String, namespace, controllerKind)
                if (available Replicas != readyReplicas) {
                    steps.sleep(time: 15, unit: 'SECONDS')
                }
            }
        }
    }

    void executeScaleReplicas (String action, String cluster, Map appsInCluster, String namespace, Integer replicas) {
        appsInCluster.apps.each { String appName ->
            steps.stage("Executing Action ${action} Cluster ${cluster} Namespace - ${namespace} Appname ${appName}") {
                try {
                    String controllerKind = getControllerKind (namespace, appName)
                    Integer readyReplicas = 0
                    steps.sh "kubectl scale --replicas=${replicas} ${controllerKind}/${appName} --namespace=${namespace}"
                    validateReadyReplicas (replicas, readyReplicas, appName, namespace, controllerKind)
                } catch (FlowInterruptedException e) {
                    steps.echo("Timeout Occurred: ${e} : Action - ${action}, Cluster ${cluster}, Namespace - ${namespace}, Appname -${appName}")
                    stageFailed("Timeout Occurred Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}, Appname -${appName}")
                } catch (Exception e) {
                    steps.echo("Aborting: Exception Occurred ${e} : Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}, Appname ${appName}")
                    steps.error("Aborting: Exception Occurred Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname ${appName}. Please check console log for details.")
                }
            }
        }
    }

    void executeDeletePods (String action, String cluster, String namespace, Map podsInCluster) {
        podsInCluster.pods.each { podName ->
            steps.stage("Executing Action - ${action} Cluster - ${cluster} Namespace - ${namespace} Pod - ${podName}") {
                String deletePodCommand = "kubectl delete pod ${podName} -n ${namespace}"
                def output = runCommand(deletePodCommand)
                if (output.endsWith('deleted')) {
                    steps.echo("Successful: Action")
                } else {
                    steps.echo("Failed. Command output")
                    stageFailed("Failed. Command Output")
                }
            }
        }
    }


    void executeDeleteApp (String action, String cluster, Map appsInCluster, String namespace) {
        appsInCluster.apps.each { String appName ->
            steps.stage("Executing Action - ${action} Cluster - ${cluster}, Namespace - ${namespace}, Appname -${appName}") {
                try {
                    String controllerKind = getControllerKind (namespace, appName)
                    steps.sh "kubectl delete ${controllerKind}/${appName} --namespace=${namespace}"
                    Integer status = 0
                    Integer counter = 0
                    while (status != 1 && counter <= 60) {
                        steps.sleep(time: 30, unit: 'SECONDS')
                        counter += 1
                        status = appExists(controllerKind, appName as String, namespace) as Integer
                    }
                    if (status == 0) {
                        steps.error("Failed in executing Action ${action} on ${cluster} for Namespace ${namespace} and Appname ${appName}")
                    }
                } catch (Exception e) {
                    steps.echo("Aborting: Exception Occurred: ${e} : Action - ${action}, Cluster ${cluster}, Namespace ${namespace}, Appname -  ${appName}")
                    steps.error("Aborting: Exception Occurred Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}, Appname, ${namespace}, Appname - ${appName}")
                }
            }
        }
    }

    void executeDeleteNS (String action, String cluster, String namespace) {
        steps.stage("Executing Action - ${action} Cluster - ${cluster} Namespace ${namespace}") {
            try {
                steps.sh "kubectl delete namespace ${namespace}"
                String status = ''
                Integer counter = 0
                while (!status.equalsIgnoreCase("Terminating") && !status.equalsIgnoreCase("Error from server") && counter <= 60) {
                    steps.sleep(time: 30, unit: 'SECONDS')
                    counter += 1
                    status = getNamespaceStatus(namespace)
                }
                if (status.equalsIgnoreCase("active")) {
                    steps.error("Failed in executing Action ${action} on ${cluster} for Namespace ${namespace}")
                }
            } catch (Exception e) {
                steps.echo("Aborting: Exception Occurred: ${e} : Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}")
                steps.error("Aborting: Exception Occurred Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}")
            }
        }
    }

    void enableEgressToPhotonInsights (String action, String cluster, String namespace, Map appsInCluster) {
        appsInCluster.apps.each {appName ->
            steps.stage("Executing Action - ${action} Cluster - ${cluster} Namespace - ${namespace}") {
                try {
                    def yaml = buildEgress Yaml(namespace, appName as String)
                    steps.echo("Updated Egress yml:\n$yam1")

                    def ymlFileName = getFileNameFromPath(egressConfigYmlPath)
                    writeYmlToFile(ymlFileName, yaml)

                    String addEgressConfigCmd = "kubectl apply -f ./temp/$ymlFileName"
                    String output = runCommand(addEgressConfigCmd)

                    if (output.endsWith('configured') || output.endsWith('created')) {
                        steps.echo("Successfully Enabled Egress to Photon-Insights")
                        executeRestart(action, cluster, appName as String, namespace)
                    } else {
                        steps.echo("Failed in executing Action ${action} on ${cluster} for Namespace ${namespace} and Appname ${appName}")
                        stageFailed("Failed in executing Action ${action} on ${cluster} for Namespace ${namespace} and Appname ${appName}")
                    }
                }catch (Exception e) {
                    steps.echo("Aborting: Exception Occurred: ${e} : Action - ${action}, Cluster - ${cluster}, Namespace - ${namespace}, Appname -${appName}")
                    steps.error("Aborting: Exception Occurred Action - ${action}, Cluster - ${cluster}, Namespace ${namespace}, Appname - ${appName}")
                }
            }
        }
    }

    def buildEgress Yaml(String namespace, String appName) {
        String yaml = steps.libraryResource(egressConfigYmlPath)
        yaml yaml.replace('REPLACE_WITH_YOUR_NAMESPACE', namespace).replace('REPLACE_WITH_YOUR_APP_NAME', appName)
        def ymlData = steps.readyaml text: yaml as String
        return ymlData
    }

    def static getFileNameFromPath(String ymlURL) {
        def list = ymlURL.split('/')
        def last = list[-1]
        def split_list = last.contains('.yml') ? last.split('.yml') : last.split('.yaml')
        def fileName = split_list[0] + '.yml'
        return fileName
    }

    def writeYmlToFile(final ymlFileName, final contents) {
        steps.sh 'rm -rf temp'//delete temp if found already
        steps.sh 'mkdir temp'
        steps.writeYaml file: "temp/$ymlFileName", data: contents
        steps.sh '1s'
    }

    List buildParametersList (String clusters) {
        List parametersList = []
        parametersList.add(string(name: 'commitHashToRun', value: "<latest>"))
        parametersList.add(string (name: 'deploy Targets', value: "${clusters}"))
        parametersList.add(string (name: 'pipelineUUID', value: "None"))
        parametersList.add(string(name: 'cicdStagesToRun', value: "REDEPLOY"))
        return parametersList
    }

    def isResourceExists (String command) {
        String output = runCommand(command)
        // Exception for failed commands will be - 'hudson. AbortException: script returned exit code 1'
        return !output.contains('exit code 1')
    }

    def runCommand(String command) {
        steps.echo('Running command: ' + command)
        def output
        try {
            output = steps.sh(script: command, returnstdout: true).trim()
        } catch (Exception e) {
            output = e.getMessage()
            steps.jules logger.info("Resource not found. Message: ${output}, exception: ${e}")
            steps.echo("Output: ${output}")
        }
        return output
    }

    def checkAppStatus (String appName, String namespace) {
        try {
            String kind = getControllerKind(namespace, appName)
            if (kind != "Unknown") {
                String command = "kubectl get ${kind}.apps/${appName} -n ${namespace} -o json"
                def exitCode = steps.sh(script: command, returnStatus: true)
                steps.echo("Exit Code: ${exitCode}")
                return exitCode
            } else {
                return 1
            }
        } catch (Exception e) {
            steps.error("Aborting: checkAppStatus: Exception Occurred: ${e} : Appname -${appName}, Namespace - ${namespace}")
        }
    }

    def appExists(String controllerKind, String appName, String namespace) {
        Integer isAppExists
        try {
            String command = "kubectl get ${controllerKind}.apps/${appName} -n ${namespace} -o json"
            def exitCode = steps.sh(script: command, returnStatus: true)
            isAppExists = exitCode
        } catch (Exception e) {
            steps.echo("appExists: Exception Occurred ${e} : Appname - ${appName}, Namespace - ${namespace}")
            isApp Exists = 1
        }
        return isAppExists
    }

    Integer getReplicas (String appName, String namespace, String controllerKind) {
        try {
            String command = "kubectl get ${controllerKind}.apps/${appName} -n ${namespace} -o jsonpath={.status.readyReplicas}}"
            String response = steps.sh(script: command, returnstdout: true).trim()
            steps.echo("getReplicas: Command Response: ${response}")
            return response.isEmpty() ? 0 : response.toInteger()
        } catch (Exception e) {
            steps.echo("Aborting: getReplicas: Exception Occurred: ${e} : Appname ${appName}, Namespace - ${namespace}")
            steps.error("Aborting: getReplicas Exception Occurred Appname -${appName}, Namespace - ${namespace}")
        }
    }