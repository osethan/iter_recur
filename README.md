# iter_recur

All iteration can be changed to recursion, and all recursion can be changed to iteration.

## Iteration to Recursion
Iteration can be changed to tail recursion, and tail recursion is recursion with recursion as the last step. Iteration condition becomes recursion base case, iteration body becomes recursion step, and iteration local variables become recursion parameters.

## Tail Recursion to Iteration
Tail recursion can be changed to iteration, and tail recursion is recursion with recursion as the last step. Recursion base case becomes iteration condition, recursion step becomes iteration body, and recursion parameters becomes iteration local variables.
