def calculate_max(i,j,Value_Container):
    return abs(Value_Container[i] - Value_Container[j]) + abs(i-j)

def Maximum_Absolute_Difference(Value_Container):
    if len(Value_Container) <= 1:
        return 0
    elif len(Value_Container) > 1:
        result = 0
        for i in range(0,len(Value_Container)):
            for j in range(i,len(Value_Container)):
                if calculate_max(i,j,Value_Container) > result:
                    result = calculate_max(i,j,Value_Container)
        return result


if __name__ == "__main__":
    Value_Container = [1,3,-1]
    print(Maximum_Absolute_Difference(Value_Container))