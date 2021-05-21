import random
from datetime import datetime
test1=1
test2=2
verotv=0
pr1, pr11 = (random.randrange(50, 120)), (random.randrange(50, 120))
dop1, dop11 = (random.randrange(-120, -50)), (random.randrange(-120, -50))
pr2 = random.randrange(0, 65000)
dop2 = random.randrange(-32000, 32000)
pr31, pr32 = (random.randrange(50, 220)), (random.randrange(50, 220)) 
dop31, dop32 = (random.randrange(50, 150)), (random.randrange(50, 150))
pr41, pr42 = (random.randrange(30000, 35000)), (random.randrange(30000, 35000))
dop41, dop42 = (random.randrange(19000, 22000)), (random.randrange(10000, 14000))
voprosi=[
f"0.Запишите натуральное число {pr1} в 8-битную ячейку памяти в 2-ной системе счисления в прямом коде.",
f"1.Запишите натуральное число {pr2} в 16-битную ячейку памяти в 2-ной системе счисления в прямом коде.",
f"2.Сложите числа {pr31} и {pr32} в 8-битной арифметике и запишите их в 2-ной системе счисления в прямом коде.",
f"3.Сложите числа {pr41} и {pr42} в 16-битной арифметике и запишите их в 2-ной системе счисления в прямом коде.",
f"4.Запишите натуральное число {pr11} в 8-битную ячейку памяти в 2-ной системе счисления в прямом коде.",
#доп код
f"5.Запишите натуральное число {dop1} в 8-битную ячейку памяти в 2-ной системе счисления в дополнительном коде.",
f"6.Запишите натуральное число {dop2} в 16-битную ячейку памяти в 2-ной системе счисления в дополнительном коде.",
f"7.Сложите числа {dop31} и {dop32} в 8-битной арифметике и запишите их в 2-ной системе счисления в дополнительном коде.",
f"8.Сложите числа {dop41} и {dop42} в 16-битной арифметике и запишите их в 2-ной системе счисления в дополнительном коде.",
f"9.Запишите натуральное число {dop11} в 8-битную ячейку памяти в 2-ной системе счисления в дополнительном коде."
]
def per10_2(n):
    c=''
    if n>0:
        k=''
    else:
        k='-'
        n=abs(n)
    while n>0:
        c=str(n%2)+c
        n//=2
    return k+c

otveti=[]
username=input("Введите ваше имя: ")
print("Здравствуйте ",username,"!")
test=int(input("Выбор режима.  (1-Тренировочный 2-Контрольный): "))
#Тренировочный режим
if (test==test1):
    print("Вы выбрали Тренировочный режим, желаем вам удачи!")
    datetime1=datetime.now().time()
    print("Время начала тестирования:",datetime1)
    a=int(input("Выберете количество вопросов(от 1 до 10): "))
    if a in range(1,11):
        for i in range(a):
            question=random.choice(voprosi)
            print(question[2:])
            voprosi.remove(question)
            uchotvet=str(input("Введите ответ: ")) 
            if int(question[0]) in [0,1,2,3,4,5,6,7,8,9]:
                if int(question[0])==0:
                    ss=pr1
                elif int(question[0])==1:
                    ss=pr2
                elif int(question[0])==2:
                    ss=pr31+pr32
                elif int(question[0])==3:
                    ss=pr41+pr42
                elif int(question[0])==4:
                    ss=pr11
                elif int(question[0])==5:
                    ss=dop1
                elif int(question[0])==6:
                    ss=dop2
                elif int(question[0])==7:
                    ss=dop31+dop32
                elif int(question[0])==8:
                    ss=dop41+dop42
                elif int(question[0])==9:
                    ss=dop11
                otveti.append([uchotvet, per10_2(ss)])
                if uchotvet==per10_2(ss):
                    print('Вы дали верный ответ!')
                    verotv += 1
                else:
                    print('Вы дали не верный ответ!') 
    elif a==0:
        print('Ты гений...')
    else:
        print('Введите число строго от 1 до 10!')
    datetime2=datetime.now().time()
    ll=verotv*100/a
    print("Время конца тестирования:",datetime2)
    print("Количество правильных ответов:",verotv," из ", a,", а это ",ll,"% из 100%!")
    result = []

#Контрольный режим
    
elif (test==test2):
    print("Вы выбрали Контрольный режим, желаем вам удачи!")
    datetime1=datetime.now().time()
    print("Время начала тестирования:",datetime1)
    a=10
    if a in range(1,11):
        for i in range(a):
            question=random.choice(voprosi)
            print(question[2:])
            voprosi.remove(question)
            uchotvet=str(input("Введите ответ: ")) 
            if int(question[0]) in [0,1,2,3,4,5,6,7,8,9]:
                if int(question[0])==0:
                    ss=pr1
                elif int(question[0])==1:
                    ss=pr2
                elif int(question[0])==2:
                    ss=pr31+pr32
                elif int(question[0])==3:
                    ss=pr41+pr42
                elif int(question[0])==4:
                    ss=pr11
                elif int(question[0])==5:
                    ss=dop1
                elif int(question[0])==6:
                    ss=dop2
                elif int(question[0])==7:
                    ss=dop31+dop32
                elif int(question[0])==8:
                    ss=dop41+dop42
                elif int(question[0])==9:
                    ss=dop11
                otveti.append([uchotvet, per10_2(ss)])
                if uchotvet==per10_2(ss):
                    verotv += 1 
    datetime2=datetime.now().time()
    ll=verotv*100/a
    print("Время конца тестирования:",datetime2)
    print("Количество правильных ответов:",verotv," из ", a,", а это ",ll,"% из 100%!")
else:
    print("Выбрать режим можно только поставив цифру 1-Тренировочный или 2-Контрольный")

