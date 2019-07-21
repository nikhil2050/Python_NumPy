 import numpy as np

int_ones = np.ones((2,2), dtype=np.int8) # array([[1, 1],[1, 1]], dtype=int8)
int_ones

int_ones.dtype  # dtype('int8')

float_ones = np.ones((2,2), dtype=np.float16)
float_ones[0,1] = -10/3                  # array([[1.,-3.334],[1.,1.], dtype=float16)
float_ones

uint_ones = np.ones((2,3), dtype=np.uint8)
uint_ones[0,1] = -8                      # array([[1,248,1],[1,1,1]], dtype=uint8)
uint_ones

string_arr = np.array(["Aam","Bam", 'Cam'])
# dType : Set to size 3. Use np.array(["Aam","Bam", 'Cam'], dType='<U16')
string_arr[1] = 'AKHIL'
string_arr

vec1 = np.array([1,-1,0], dtype=np.float16) # Set array-size to 16  
vec2 = vec1/0         # RuntimeWarning: divide by zero encountered in true_divide
vec2

# vec2 => array([ inf, -inf,  nan], dtype=float16)
for i in vec2:
    print(i)
    print('---')
    print('Inf:' + str(i == np.inf))
    print('-Inf:' + str(i == -np.inf))
    print('Nan:' + str(np.isnan(i)))     # nan == nan :: Doesn't work. Use np.isnan(var)
    print()
    
# inf = infinite; -inf = infinite; nan = Not-finite, Not-infinite
for i in vec2:
    print(i)
    print(' is finite?  :' + str(np.isfinite(i)))
    print(' is infinite?:' + str(np.isinf(i)))
    print()

np.inf + 1     # inf
np.inf * -1    # -inf
(-np.inf) +1   # -inf
np.nan + 1     # nan
2 ** (-np.inf) # 0.0
2 ** (np.inf)  # inf
np.inf - np.inf# nan

vec3 = np.array([999], dtype=np.float64)
vec3[0] ** vec3[0]    # inf
vec3

vec4 = np.ones(5)
vec4[0] = np.nan
vec4

np.sum(vec4)       # nan
np.nansum(vec4)    # 4.0 Ignores nan

all_zeroes = np.zeros((2,2), np.float16)  # array([[0., 0.],[0.,0.]], dtype=float16)
all_zeroes


## ###############################################################
## ################### SLICING ARRAYS IN NUMPY ###################
## ###############################################################
arr3D = np.array([[["Joey", "Bob", "Sarah"],
                 ["Margaret", "Rachel", "Jim"],
                 ["Wayne", "Joey", "Liam"]],
                
                 [["Max", "Maxine", "Richard"],
                 ["Harold", "Curtis", "Simon"],
                 ["Bob", "Liam", "Simon"]],
                 
                 [["Wayne", "Sarah", "Lucy"],
                 ["Lucy", "Kurtis", "Yu"],
                 ["Joey", "Lex", "Alex"]]
                ])
arr3D = np.array([[["A000", "A001", "A002"],
                 ["A010", "A011", "A012"],
                 ["A020", "A021", "A022"]],
                
                 [["B100", "B101", "B102"],
                 ["B110", "B111", "B112"],
                 ["B120", "B121", "B122"]],
                 
                [["C200", "C201", "C202"],
                 ["C210", "C211", "C212"],
                 ["C220", "C221", "C222"]]
                ])
print(arr3D.shape)          # (3, 3, 3)

arr2D = arr3D[:,:,0].copy()  # copy = View of arr3D. Not changing original array.
arr2D
#array([['A000', 'A010', 'A020'],
#       ['B100', 'B110', 'B120'],
#       ['C200', 'C210', 'C220']], dtype='<U4')


#Manually choose "cross" elements
#[['B100' 'B110' 'B120']
# ['B100' 'B110' 'B120']
# ['B100' 'B110' 'B120']
# ['A000' 'A010' 'A020']
# ['C200' 'C210' 'C220']]
print(arr2D[[1,1,1,0,2]])   # Row #1, Row #1, Row #1, Row #0, Row #2

# ['B100' 'B110' 'B120' 'A010' 'C210']
print(arr2D[[1,1,1,0,2],[0,1,2,1,1]])

# Middle column, All rows
# ['A010' 'B110' 'C210']
print(arr2D[:, 1])

# Middle column, All rows. But don't flatten, keep Matrix shape
# When a list is used for choosing the column the dimension is kept
#[['A010']
# ['B110']
# ['C210']]
print(arr2D[:,[1]])

# last 2 rows of middle column
#['B110' 'C210']
print(arr2D[1:,1])

# Reverse row/column order
print(arr2D)
#[['A000' 'A010' 'A020']
# ['B100' 'B110' 'B120']
# ['C200' 'C210' 'C220']]

print("\nReverse row order")
print(arr2D[::-1, :]) # Reverse row order
#[['C200' 'C210' 'C220']
# ['B100' 'B110' 'B120']
# ['A000' 'A010' 'A020']]

print("\nReverse column order")
print(arr2D[:, ::-1]) # Reverse column order
#[['A020' 'A010' 'A000']
# ['B120' 'B110' 'B100']
# ['C220' 'C210' 'C200']]

# Selecting odd numbered columns
print(arr2D[:, 0:3:2])
#[['A000' 'A020']
# ['B100' 'B120']
# ['C200' 'C220']]

#3D sliced to 2D
#[['A010' 'A011' 'A012']
# ['B110' 'B111' 'B112']
# ['C210' 'C211' 'C212']]
print(arr3D[:, 1,:])

#3D sliced to 3D
print("Original")
print(arr3D)
#[[['A000' 'A001' 'A002']
#  ['A010' 'A011' 'A012']
#  ['A020' 'A021' 'A022']]
#
# [['B100' 'B101' 'B102']
#  ['B110' 'B111' 'B112']
#  ['B120' 'B121' 'B122']]
#
# [['C200' 'C201' 'C202']
#  ['C210' 'C211' 'C212']
#  ['C220' 'C221' 'C222']]]

print("\n3D sliced to 3D. i.e. Add with extra dimension")
print(arr3D[:, 1,np.newaxis, :])
#[[['A010' 'A011' 'A012']]
#
# [['B110' 'B111' 'B112']]
#
# [['C210' 'C211' 'C212']]]
 

## ###############################################################
## ################### SLICING ARRAYS IN NUMPY ###################
## ###############################################################
arr3D = np.array([[["Joey", "Bob", "Sarah"],
                 ["Margaret", "Rachel", "Jim"],
                 ["Wayne", "Joey", "Liam"]],
                
                 [["Max", "Maxine", "Richard"],
                 ["Harold", "Curtis", "Simon"],
                 ["Bob", "Liam", "Simon"]],
                 
                 [["Wayne", "Sarah", "Lucy"],
                 ["Lucy", "Kurtis", "Yu"],
                 ["Joey", "Lex", "Alex"]]
                ])
arr2D = arr3D[:,:,0].copy()  # copy = View of arr3D. Not changing original array.
print(arr2D)
#[['Joey' 'Margaret' 'Wayne']
# ['Max' 'Harold' 'Bob']
# ['Wayne' 'Lucy' 'Joey']]

# Select ALL entries that are not Wayne
print(arr2D[arr2D != "Wayne"])
#['Joey' 'Margaret' 'Max' 'Harold' 'Bob' 'Lucy' 'Joey']

# See internally generated indexing boolean array 
print(arr2D != "Wayne")
#[[ True  True False]
# [ True  True  True]
# [False  True  True]]


idx0 = np.array([[0,0],
                [2,2]])
idx1 = np.array([[0,2],
                [0,2]])
print(arr2D[idx0, idx1]) # Generate from arr2D : [(0,0),(0,2)],[(2,0),(2,2)]
#[['Joey' 'Wayne']
# ['Wayne' 'Joey']]






