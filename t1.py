'''1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны любому из чисел в диапазоне от 2 до 9.'''

numbers = [a for a in range(2,100)]
i = 0
b=[]

for a in numbers:
    if a%2==0 and a%3==0 and a%4==0 and a%5==0 and a%6==0 and a%7==0 and a%8==0 and a%9==0:
        b.append(a)
        i += 1
print('Таких чисел',i,'шт.')