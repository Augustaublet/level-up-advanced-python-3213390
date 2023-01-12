def pairwise_offset(sequence, fillvalue="*", offset=0):
    first = sequence
    second = sequence
    if isinstance(sequence, str):
        first = sequence
        second = sequence
        for x in range(offset):
            first += fillvalue
            second = fillvalue + second
    if isinstance(sequence, list):
        first = sequence.copy()
        second = sequence.copy()
        for x in range(offset):
            first.append(fillvalue)
            second.insert(0, fillvalue)
        print(first)
        print(second)
    final = []
    for i in range(len(first)):
        final.append((first[i], second[i]))
    return final
