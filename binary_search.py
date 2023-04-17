tests =[
    {
    'input':{'cards':[],'query':7},
    'output':-1
    },
    {
    'input':{'cards':[7],'query':7},
    'output':0
    },
    {
    'input':{'cards':[4],'query':5},
    'output':-1
    },
    {
    'input':{'cards':[9,7,6,6,6,5,4,2,1,0],'query':6},
    'output':2
    },
    {
    'input':{'cards':[10,9,5,4,4,3,2,1,1,0],'query':10},
    'output':0
    },
    {
    'input':{'cards':[10,9,5,4,4,3,2,1,1,0],'query':0},
    'output':9
    },
    {
    'input':{'cards':[8,7,7,6,6,5,4,3,2,1,0],'query':7},
    'output':1
    },
    ]
def locate_position(cards,query, mid_index):
    if cards[mid_index] == query:
        #checks to ensure that the query is the first occurance of tht value
        if mid_index-1 >= 0 and cards[mid_index -1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid_index] > query:
        return "right"
    else: return "left"


def binary(cards,query):
    left, right = 0, len(cards)-1
    # next line ensures tht the virtual sublist we are working with 
    #is neve empty
    while left <= right:
        mid_index = (left + right) // 2
        result = locate_position(cards,query,mid_index) 
        if result == "found":
            return mid_index
        elif result == "left":
            right = mid_index - 1
        elif result == "right":
            left = mid_index + 1

    return -1


for test in tests:
    if binary(**test['input']) == test['output']:
        print("passed")
    else: print("failed")