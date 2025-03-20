#Задача2

a=int(input('Введите целое число:'))
b=int (a+1)
c=int (a-1)
print ("Следующее за числом", a ,"число", b)
print ("Для числа", a ,"предыдущее число:", c)

#Задача 3

time = int (input ('Время в минутах:')
Hour = int (time) // 60
min = int (time) % 60
print (f' {time} мин-это {Hour} час. {min} минут')

#Задача 4
xxx=int (input ('Введите 3-х значное число:'))
x1= xxx//100
x2= (xxx-x1*100)//10
x3= xxx-x1*100-x2*10

summ=x1+x2+x3

proiz=x1*x2*x3

print (f" Сумма цифр = {summ} {'\n'} Произведение цифр {proiz}")


# Задача 5
mille=int (input ('Введите целое число миль:'))
yard = int (input ('Введите число после запятой:'))
a= mille+yard/10*1,61
b= int (a)
km=round (a,1)
print (f'{mille}.{yard} миль = {km} км')