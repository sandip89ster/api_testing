USERS = [
    {
        "name": "john",
        "job": "developer",
    },
    {
        "name": "mark",
        "job": "sales",
    },
    {
        "name": "anton",
        "job": "finance",
    },
]

INVALID_USER_DATA = [
    {},
    {
        "name": " ",  # Scenario 1 : Empty name & job
        "job": " ",
    },
    {
        "job": "finance",  # Scenario 2 : No name
    },
    {
        "name": "mark",  # Scenario 3 : no job
    },
    {
        "name": 12345,  # Scenario 4 : Numeric name & job
        "job": 6789,
    },
    {
        "name": "@#$%",  # Scenario 5 : Special characters in name & job
        "job": "!@#$%^",
    },
    {
        "hello": "@#$%",  # Scenario 6 : Invalid JSON objects
        "world": "!@#$%^",
        "id": 1212,
        "createdAt": 12243434,
    },
    {
        "hello": "@#$%",  # Scenario 7 : Invalid duplicating JSON objects
        "world": "!@#$%^",
        "id": 1212,
        "createdAt": 12243434,
        "hello": "@#$%",
        "world": "!@#$%^",
        "id": 1212,
        "createdAt": 12243434,
        "name": "@#$%",
        "job": "!@#$%^",
    },
]
