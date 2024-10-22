def timesTable(num):
    list = []
    for i in range(1, num+1):
        # print(i)
        list.append([])
        # print(list)
        for j in range(1, num+1):
            temp = i*j
            (list[i-1]).append(temp)

    return list



nums = int(input())
print(timesTable(nums))
