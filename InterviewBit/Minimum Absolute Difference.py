def Minimum_Absolute_Value(value_container):
    final_pair_vals = []
    value_container = sorted(value_container)

    def min_value_check(arr):
        minimum_difference = float('inf')
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < minimum_difference:
                minimum_difference = arr[i] - arr[i - 1]
                print(minimum_difference)
        return minimum_difference

    min_val_diff = min_value_check(value_container)
    for i in range(1, len(value_container)):
        if value_container[i] - value_container[i - 1] == min_val_diff:
            final_pair_vals.append([value_container[i - 1], value_container[i]])
            print(final_pair_vals)
    return final_pair_vals


value_container = list(map(int, input().split()))
print(Minimum_Absolute_Value(value_container))