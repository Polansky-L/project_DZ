# coding: utf8
import random
pptk = 0
num = random.randint(1,10)
uzer_num = 0
while uzer_num != num:
    uzer_num = int(input("������� ����� 1 - 10 "))
    pptk+=1

    if uzer_num > num:
        print("�������")
    elif (uzer_num < num):
        print("�������")
    else:
        print(f"������! ����� ������� - {pptk}")