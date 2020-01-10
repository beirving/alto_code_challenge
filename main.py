# data stuct
tasks = [
    {
        "type": "communication",
        "created": 10,
        "time_to_complete": 120,
        "complete": False
    },
    {
        "type": "communication",
        "created": 20,
        "time_to_complete": 30,
        "complete": False
    },
    {
        "type": "fill_scripts",
        "created": 0,
        "time_to_complete": 0,
        "complete": True
    },
    {
        "type": "fill_scripts",
        "created": 20,
        "time_to_complete": 30,
        "complete": False
    },
    {
        "type": "fill_scripts",
        "created": 0,
        "time_to_complete": 0,
        "complete": True
    }, {
        "type": "talk_to_client",
        "created": 20,
        "time_to_complete": 30,
        "complete": False
    },
    {
        "type": "talk_to_client",
        "created": 0,
        "time_to_complete": 0,
        "complete": True
    }
]

employee = {
    "id": 1,
    "name": "bob",
    "department": "customer_service"
}


def get_departments() -> list:
    return [
        {
            "name": "customer_service",
            "task_types": ["communication", "phone_calls", "etc"]
        },
        {
            "name": "pharms",
            "task_types": ["talk_to_client", "fill_scripts"]
        },
    ]


def filter_tasks_by_employee(task: dict, employee: dict) -> list:
    output = []
    # get department
    for department in get_departments():
        if department["name"] == employee["department"]:
            # set task types employee can do
            task_types = department['task_types']

    for task in tasks:
        # filter by complete
        if task['complete'] is True:
            continue
        # filter out by department
        if task['type'] in task_types:
            # append to the end of list
            output.insert(len(output), task)

    return output


def get_current_time():
    return 45


def select_task(tasks: list) -> dict:
    return_task = None
    due_time = None
    current_time = get_current_time()

    # loop through the tasks to order by starttime
    for task in tasks:
        current_due_time = None

        # generate a due time
        time_left = current_time - task['created']
        complete_time = current_time + task['time_to_complete']
        current_due_time = complete_time - time_left

        # look at timeleft and pick the smallest number
        if due_time is None:
            due_time = current_due_time
            return_task = task

        # if time_to_complete is small and time_lest is small set the task
        if current_due_time < due_time:
            due_time = current_due_time
            return_task = task
    return return_task


# task 1 has been waiting for 35 min requires 20 min to complete - urgent
# task 2 has been waiting for 15 min and reqiires 30 min to complete - most urgent


filtered_tasks = filter_tasks_by_employee(tasks, employee)

output = select_task(filtered_tasks)

print(output)

#
# Your previous Plain Text content is preserved below:
# 
# We've built a web platform that powers our pharmacy and one of its core services is the Task system. A task is a single unit of work for an employee. There are many types of tasks, such as responding to a patient message or updating a prescription.
# 
# An employee can get the next task they should work on, with the following requirements:
# - Each employee has a role that determines the types of tasks they can complete. For example, a pharmacist can respond to a message or update a prescription, but a customer service representative can only respond to a patient message.
# - Each type of task has an expected completion time. For example, the expected completion time for responding to a patient message could be 30 minutes, which means we want to complete that type of task within 30 minutes of being created. An employee should get the task that is closest to exceeding its completion time.
# 
# Given an employee and a collection of tasks, your challenge is to write the code for a method that returns the correct task for that employee. By the end, you should have running code that you can show meets the requirements with functional examples or tests.
# 

# updates information to patient from employee
# time to do task - needs a timestamp
# tasks have types
# return most urgent task
