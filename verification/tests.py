"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[], [1, 2, 3]],
            "answer": None
        },
        {
            "input": [[1], [1]],
            "answer": 1
        },
        {
            "input": [[3], [1, 2, 3]],
            "answer": 3
        }, 
        {
            "input": [[1, 3, 4, 6], [2, 9, 4, 6]],
            "answer": 4
        },
    ],
    "Extra": [
        {
            "input": [[], []],
            "answer": None
        },
        {
            "input": [[3, 4, 5], [1, 2, 3, 4, 5]],
            "answer": 3
        },
        {
            "input": [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
            "answer": 1
        },
        {
            "input": [[1, 2, 3, 4, 5], []],
            "answer": None
        }, 
        {
            "input": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
            "answer": None
        },
        {
            "input": [[1, 2, 3, 4, 5], [1, 7, 3, 4, 5]],
            "answer": 3
        }
    ]
}
