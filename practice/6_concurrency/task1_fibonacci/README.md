## Task 1. Find Fibonacci numbers by ordinal numbers in the sequence

In this task, you need to write two functions 
(you can write more functions to implement the logic of the two required functions):

1. The **first** function takes a list of numbers, which are ordinal numbers 
in the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number). 
The function must calculate the value for each ordinal number of the sequence and write it to a separate file. 
The ordinal numbers can be large.

Example:

    The Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

    Input: [5, 1, 8, 10]

    Output: 
      file 5.txt with content ‘5’, 
      file 1.txt with content ‘1’, 
      file 8.txt with content ‘21’, 
      file 10.txt with content ‘55’.

2. The **second** function takes the path to the folder where the files are located after starting the first function. 
The function should read values from each file and make one common csv file 
with the ordinal number and its value in the Fibonacci sequence.
	
Example:
   
      Input: folder with 5.txt, 1.txt, 8.txt, 10.txt files.

      Output: 
         csv file:
         5,5
         1,1
         8,21
         10,55

You should use parallelism or concurrency techniques to improve efficiency of your code. 
Try to understand what kinds of tasks the functions perform and choose the right type of technique.
