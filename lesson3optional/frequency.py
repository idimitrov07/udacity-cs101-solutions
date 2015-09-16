def freq_analysis(message):
    ##
    # Your code here
    ##
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphaDict = {}
    freq_list = []
    for alpha in alphabet:
        alphaDict[alpha] = 0
    for s in alphabet:
        counter = 0
        for letter in message:
            if letter == s:
                counter += 1
        alphaDict[s] = counter
        freq = alphaDict[s] / (len(message) + 0.0)
        freq_list.append(freq)

    return freq_list



print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
