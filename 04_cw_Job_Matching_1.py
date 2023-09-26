# Let's give this a try. We'll create a function match (job_matching in Python) which takes a candidate and a job,
# which will return a Boolean indicating whether the job is a valid match for the candidate.
# A candidate will have a minimum salary, so it will look like this:
# candidate = {
#   'min_salary': 120000}
# A job will have a maximum salary, so it will look like this:
# job = {
#   'max_salary': 140000}
# If either the candidate's minimum salary or the job's maximum salary is not present, throw an error.
# For a valid match, the candidate's minimum salary must be less than or equal to the job's maximum salary.
# However, let's also include 10% wiggle room (deducted from the candidate's minimum salary)
# in case the candidate is a rockstar who enjoys programming on Codewars in their spare time.
# The company offering the job may be able to work something out.
def job_matching(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Salary information not provided")

    min_salary = candidate['min_salary']
    max_salary = job['max_salary']

    if min_salary <= 0 or max_salary <= 0:
        raise ValueError("Invalid salary value")

    wiggle_room = min_salary * 0.1
    min_salary_with_wiggle = min_salary - wiggle_room

    return min_salary_with_wiggle <= max_salary