def isValidSubsequence(array, sequence):
    seq_index = 0
    for i in range(len(array)):
        if array[i] == sequence[seq_index]:
            seq_index += 1
            if seq_index == len(sequence):
                return True
    return False
            