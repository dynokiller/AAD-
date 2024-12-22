def find_closest_sum_pair(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_pair = (arr[left], arr[right])
    min_sum = arr[left] + arr[right]

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            closest_pair = (arr[left], arr[right])
        
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair

arr1 = [15, 5, -20, 30, -45]
result1 = find_closest_sum_pair(arr1)
print(f"Closest sum pair: {result1}")  

arr2 = [15, 5, -20, 30, 25]
result2 = find_closest_sum_pair(arr2)
print(f"Closest sum pair: {result2}")  
