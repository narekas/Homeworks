# Then find the maximum gap size and the percentage of gaps that have size 2.
L = [x for x in range(2, 48) if x % 2 != 0]
L.insert(0, 2)
print(f'{L}\nMaximum gap size = {L[-1] - L[0]}\nPercentage of gaps that have size 2 = {(22 / 23) * 100}')

