##Muhammad Usman Ahmed
##mua942
##11275853
##Assigment 1 Question 3
from a1q3 import *

test_diagonal = [

    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
     "output": True,
     "reason": "Both diagonal entries sum to 15"
     },
    {"input": [[1, 9, 6], [5, 3, 7], [4, 8, 2]],
     "output": False,
     "reason": "Both diagonal entries do not sum to 15"
     }
    ,
    {"input": [[5, 5, 5], [5, 5, 5], [5, 5, 0]],
     "output": False,
     "reason": "Down-right diagonal does not sum to 15"
     }

]
for data in test_diagonal:

    inputs = data["input"]
    expect = data["output"]
    reason = data["reason"]
    got = get_square(inputs)

    if (got != expect):
        print("error for this reason " + reason + " on these inputs ", inputs)
