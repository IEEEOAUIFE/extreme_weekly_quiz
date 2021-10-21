def shortest_subarray(arr, n):
    ans = n - 1
    arg_max = 0
    arg_min = 0
    
    for i in range(len(arr)):
        if arr[i] > arr[arg_max]:
            arg_max = i
            ans = abs(arg_min - arg_max)
        elif arr[i] == arr[arg_max]:
            arg_max = i
            ans = min(abs(arg_min - arg_max), ans)
            
        if arr[i] < arr[arg_min]:
            arg_min = i
            ans = abs(arg_min - arg_max)
        elif arr[i] == arr[arg_min]:
            arg_min = i
            ans = min(abs(arg_min - arg_max), ans)
            

    return ans + 1

# time : O(N) -> linear
print(shortest_subarray([1,5,9,7,1,9,4], 7))
print(shortest_subarray([5,5,5,5], 4))
print(shortest_subarray([55,23,99,10,23,55,7,99,5,1,2], 11))
print(shortest_subarray([5,6,7,9], 4))
print(shortest_subarray([1,9,3,2,5,1], 6))
