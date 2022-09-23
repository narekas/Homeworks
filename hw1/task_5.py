# a program that prints the following image on the screen. Use cycles.
''' *****
    *   *
    *   *
    *   *
    ***** '''

for i in range(1, 6):
    print('*' * 5 if i == 1 or i == 5 else '*' + ' ' * 3 + '*')
