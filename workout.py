""" Sum mark """
def poisk_third_krit(first_krit, second_krit):
    return first_krit + second_krit
""" Dividing line """
def line_stolb(simvol):
    return simvol*64
" Test "
def ocenivanie(resalt):
    if third_krit >= 90:
        return resalt == 5
    elif third_krit >= 70 and third_krit < 90:
        return resalt == 4
    elif third_krit < 70 and third_krit >= 50:
        return resalt == 3
    else:
        return resalt == 2

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
resalt = ocenivanie(third_krit)

first_krit_1 = int(input(ru_local.SEMESTR))
second_krit_1 = int(input(ru_local.EXZAMEN))
third_krit_1 = poisk_third_krit(first_krit_1, second_krit_1)
resalt_1 = third_krit_1
resalt_1 = ocenivanie(third_krit_1)

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