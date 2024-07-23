# Default arguments
def create_person_info(name, age, job=None, sal=300):
    info = {'name': name, 'age': age, 'salary': sal } #dictionary

    # Add 'job' key only if it is provided as parameter
    if job:
        info.update(dict(job=job))

    return info

person1 = create_person_info('pavan', 30) # use default values for the job and sal
person2 = create_person_info('sri', 27, 'homemaker', 1000)
print(person1)
print(person2)
