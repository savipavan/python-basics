import subprocess
import time
import re

# Function to run a kubectl command and return the output
def run_kubectl_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e.output)
        return None

# Function to monitor pod status and delete if in ContainerCreating or Pending state
def monitor_and_delete_pod(namespace, timeout=600):
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        # Fetch all pods in the namespace
        output = run_kubectl_command(f"kubectl get po -n {namespace} -w")
        
        if output:
            print(f"Checking pod statuses in namespace {namespace}...")
            
            # Extract the pod name and status from the output
            match = re.search(r'^(\S+)\s+\S+\s+\S+\s+\S+\s+(ContainerCreating|Pending)', output, re.MULTILINE)
            if match:
                pod_name = match.group(1)
                pod_status = match.group(2)
                print(f"Pod {pod_name} is in {pod_status} state. Deleting the pod...")
                
                # Delete the pod
                delete_output = run_kubectl_command(f"kubectl delete po {pod_name} -n {namespace}")
                print(f"Pod {pod_name} deletion output: {delete_output}")
                
                # Wait for a short time before checking again
                time.sleep(5)
            else:
                print(f"No pods in ContainerCreating or Pending state. Continuing to monitor...")
        else:
            print(f"No pods found in namespace {namespace}.")
            return
        
        time.sleep(2)  # Wait for 2 seconds before checking again

    print(f"Monitoring of pods in namespace {namespace} completed after {timeout} seconds.")

if __name__ == "__main__":
    namespace = "<your-namespace>"
    monitor_and_delete_pod(namespace)
