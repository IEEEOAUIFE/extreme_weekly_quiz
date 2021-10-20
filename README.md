## Variables
MinMax Subarray max variables are set to minimum values and min variables are set to max values by default using Integer.MAX_VALUE and Integer.MIN_VALUE
Maximum and Minimum Value Current Index are set to -1 by default
An Array of capacity give in the input is created to store the values

## Algorithm
Given the data constraints, it shows that the ideal data type to store the values is "int"
For better speed of the program, maximum and minimum values in the data given are updated immediately after the input to the program.

After storing the maximum and the minimum values of the datas in the array, I loop through the array and update the most recent minimum and maximum value position in the array.
Then update the shortest length of the subarray if the absolute difference of the maximum and minimum position is less that the previous value stored in that variable, after looping (FOR LOOP) through the data once more, the updated values in the shortest length variable now reveals the length of the shortest subarray of the maximum and minimum array