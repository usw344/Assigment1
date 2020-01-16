from a1q1 import *

def tester(data_set,func):
    for data_set in data_set:

        inputs = data_set["input"]
        expect = data_set["output"]
        reason = data_set["reason"]
        got = func(inputs)

        if (got != expect):
            print("error for this reason " + reason + " on these inputs ", inputs)


## for diagonal function
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
    ,
    {"input": [[5, 5, 5], [5, 5, 5], [0, 5, 5]],
     "output": False,
     "reason": "Up-right diagonal does not sum to 15"
     }

]
test_columns = [

    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
     "output": True,
     "reason": "All three columns sum to 15"
     },
    {"input": [[5, 5, 5], [5, 5, 5], [0, 5, 5]],
     "output": False,
     "reason": "First column does not sum to 15"
     }
    ,
    {"input": [[5, 5, 5], [5, 5, 5], [5, 0, 5]],
     "output": False,
     "reason": "Second column does not sum to 15"
     }
    ,
    {"input": [[5, 5, 5], [5, 5, 5], [5, 5, 0]],
     "output": False,
     "reason": "Third column does not sum to 15"
     }

]
test_rows = [

    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
     "output": True,
     "reason": "All three rows sum to 15"
     },
    {"input": [[1, 2, 3], [5, 5, 5], [5, 5, 5]],
     "output": False,
     "reason": "First row does not sum to 15"
     }
    ,
    {"input": [[5, 5, 5], [3, 2, 1], [5, 5, 5]],
     "output": False,
     "reason": "Second row does not sum to 15"
     }
    ,
    {"input": [[5, 5, 5], [5, 5, 5], [6, 2, 4]],
     "output": False,
     "reason": "Third row does not sum to 15"
     }

]
test_range = [

    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
     "output": True,
     "reason": "All entries in range are present"
     },
    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 4]],
     "output": False,
     "reason": "Entries in correct range, one missing value last row"
     }
    ,
    {"input": [[8, 1, 6], [1, 5, 7], [4, 9, 2]],
     "output": False,
     "reason": "Entries in correct range, one missing value middle row"
     }
    ,
    {"input": [[4, 1, 6], [1, 5, 7], [4, 9, 2]],
     "output": False,
     "reason": "Entries in correct range, one missing value first row"
     }
    ,
    {"input": [[8, -1, 6], [1, 5, 7], [4, 9, 2]],
     "output": False,
     "reason": "Entry out of range first row "
     },
    {"input": [[8, 1, 6], [1, 5, 0], [4, 9, 2]],
     "output": False,
     "reason": "Entry out of range second row "
     }
    ,
    {"input": [[8, 1, 6], [1, 5, 7], [4, 9, -2]],
     "output": False,
     "reason": "Entry out of range last row "
     }
]
test_square = [

    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
     "output": True,
     "reason": "All entries in range are present"
     },
    {"input": [[8, 1, 6], [3, 5, 7], [4, 9, 4]],
     "output": False,
     "reason": "Entries in correct range, one missing value last row"
     }
    ,
    {"input": [[8, 1, 6], [1, 5, 7], [4, 9, 2]],
     "output": False,
     "reason": "Entries in correct range, one missing value middle row"
     }
    ,
    {"input": [[4, 1, 6], [1, 5, 7], [4, 9, 2]],
     "output": False,
     "reason": "Entries in correct range, one missing value first row"
     }
    ,
    {"input": [[8, -1, 6], [1, 5, 7], [4, 9, 2]],
     "output": False,
     "reason": "Entry out of range first row "
     },
    {"input": [[8, 1, 6], [1, 5, 0], [4, 9, 2]],
     "output": False,
     "reason": "Entry out of range second row "
     }
    ,
    {"input": [[8, 1, 6], [1, 5, 7], [4, 9, -2]],
     "output": False,
     "reason": "Entry out of range last row "
     }
]


##run the tester function on all relevent functions
tester(test_diagonal,check_diagonals)
tester(test_columns,check_columns)
tester(test_rows,check_rows)
tester(test_range,check_range)