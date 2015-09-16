def numbers_in_lists(string):
    # YOUR CODE
    result = []
    subList = []
    intStr = []
    for s in string:
        intStr.append(int(s))
    #print intStr
    result.append(intStr[0])
    z = intStr[0]
    for i in range(1, len(intStr)):
        if intStr[i] <= z:
            subList.append(intStr[i])
        else:
            if subList != []:
                result.append(subList)
            result.append(intStr[i])
            subList = []
            z = intStr[i]
    if subList != []:
        result.append(subList)
    return result


print numbers_in_lists('543987')
print numbers_in_lists('987654321')
print numbers_in_lists('455532123266')
print numbers_in_lists('123456789')
