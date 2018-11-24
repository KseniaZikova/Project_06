""" Sum mark """
def poisk_third_krit(first_krit, second_krit):
    return first_krit + second_krit
""" Dividing line """
def line_stolb(simvol):
    return simvol*64
def line_stolb_1(simvol_1):
    return simvol_1*44

file_in = open("spisok.txt", 'r')
line = file_in.read().splitlines()
line_1 = line[0]
line_2 = line[1]
line_3 = line[2]
line_4 = line[3]
line_5 = line[4]
file_in.close()

import ru_local

first_krit = int(input(ru_local.SEMESTR))
second_krit = int(input(ru_local.EXZAMEN))
third_krit = poisk_third_krit(first_krit,second_krit)
resalt = third_krit

if third_krit >= 100:
    resalt = ru_local.YES
else:
    resalt = ru_local.NO


first_krit_1 = int(input(ru_local.SEMESTR))
second_krit_1 = int(input(ru_local.EXZAMEN))
third_krit_1 = poisk_third_krit(first_krit_1, second_krit_1)
resalt_1 = third_krit_1

if third_krit_1 >= 100:
    resalt_1 = ru_local.YES
else:
    resalt_1 = ru_local.NO

first_krit_2 = int(input(ru_local.SEMESTR))
second_krit_2 = int(input(ru_local.EXZAMEN))
third_krit_2 = poisk_third_krit(first_krit_2, second_krit_2)
resalt_2 = third_krit_2

if third_krit_2 >= 100:
    resalt_2 = ru_local.YES
else:
    resalt_2 = ru_local.NO

first_krit_3 = int(input(ru_local.SEMESTR))
second_krit_3 = int(input(ru_local.EXZAMEN))
third_krit_3 = poisk_third_krit(first_krit_3, second_krit_3)
resalt_3 = third_krit_3

if third_krit_3 >= 100:
    resalt_3 = ru_local.YES
else:
    resalt_3 = ru_local.NO

first_krit_4 = int(input(ru_local.SEMESTR))
second_krit_4 = int(input(ru_local.EXZAMEN))
third_krit_4 = poisk_third_krit(first_krit_4, second_krit_4)
resalt_4 = third_krit_4

if third_krit_4 >= 100:
    resalt_4 = ru_local.YES
else:
    resalt_4 = ru_local.NO

first_krit_5 = int(input(ru_local.SEMESTR))
second_krit_5 = int(input(ru_local.EXZAMEN))
third_krit_5 = poisk_third_krit(first_krit_5, second_krit_5)
resalt_5 = third_krit_5

if third_krit_5 >= 100:
    resalt_5 = ru_local.YES
else:
    resalt_5 = ru_local.NO

print(line_stolb("-"))
print('| {:^20} | {:^7} | {:^7} | {:^7} | {:^7} |'.format(ru_local.NAME, ru_local.ONE,
                                                   ru_local.TWO,
                                                   ru_local.THREE, ru_local.FORE))

print(line_stolb("|"))
print('| {:^20} | {:^7} | {:^7} | {:^7} | {:^7} |'.format(line_1, first_krit,
                                                          second_krit, third_krit,
                                                          resalt))
print(line_stolb("|"))
print('| {:^20} | {:^7} | {:^7} | {:^7} | {:^7} |'.format(line_2, first_krit_1,
                                                          second_krit_1, third_krit_1,
                                                          resalt_1))
print(line_stolb("|"))
print('| {:^20} | {:^7} | {:^7} | {:^7} | {:^7} |'.format(line_3, first_krit_2,
                                                          second_krit_2, third_krit_2,
                                                          resalt_2))
print(line_stolb("|"))
print('| {:^20} | {:^7} | {:^7} | {:^7} | {:^7} |'.format(line_4, first_krit_3,
                                                          second_krit_1, third_krit_3,
                                                          resalt_3))
print(line_stolb("|"))
print('| {:^20} | {:^7} | {:^7} | {:^7} | {:^7} |'.format(line_5, first_krit_4,
                                                          second_krit_4, third_krit_4,
                                                          resalt_4))
print(line_stolb("-"))
print()
print(line_stolb_1("-"))
print('{:^20} | {:^20}'.format(ru_local.SPISOK_1,ru_local.SPISOK_2))
print(line_stolb_1("-"))
if resalt == ru_local.YES:
    print('{:^20} | {:^20}'.format(line_1,'--'))
else:
    print ('{:^20} | {:^20}'.format ('--', line_1))

if resalt_1 == ru_local.YES:
    print('{:^20} | {:^20}'.format(line_2,'--'))
else:
    print ('{:^20} | {:^20}'.format ('--', line_2))

if resalt_2 == ru_local.YES:
    print ('{:^20} | {:^20}'.format (line_3, '--'))
else:
    print ('{:^20} | {:^20}'.format ('--', line_3))

if resalt_3 == ru_local.YES:
    print ('{:^20} | {:^20}'.format (line_4, '--'))
else:
    print ('{:^20} | {:^20}'.format ('--', line_4))

if resalt_4 == ru_local.YES:
    print('{:^20} | {:^20}'.format(line_5,'--'))
else:
    print ('{:^20} | {:^20}'.format ('--', line_5))

print (line_stolb_1("-"))
