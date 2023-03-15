import random
import math
# zadanie 1
# A=[1-x for x in range(1,10)]
# B=[4**x for x in range(0,7)]
# C=[B[x] for x in range(0,len(B)) if B[x]%2==0]
# print(A)
# print(B)
# print(C)
# zadanie 2
# listy=[]
# for x in range(0,10):
#     listy.append(random.randint(-400,100000))
# implementacja=[listy[x] for x in range(0,10) if listy[x]%2==0]
# print(listy)
# print(implementacja)
# zadanie 3
# wolnosc={}
# liberty = {'crossaint': 'sztuka', 'woda': 'butelka', 'sól': 'kilogram', 'cebula':'kilogram','majonez':'sztuka'}
# wolnosc=[x for x in liberty if liberty[x]=='sztuka']
# print(liberty)
# print(wolnosc)
# zadanie 4
# def prostokatny(a,b,c):
#     if (a*a)+(b*b)==(c*c):
#         print('jest prostokatny')
#     elif (a*a)+(c*c)==(b*b):
#         print('jest prostokatny')
#     elif (c*c)+(b*b)==(a*a):
#         print('jest prostokatny')
#     else: print('nie jest prostokatny :(')
#     return 0
# h=int(input())
# w=int(input())
# d=int(input())
# prostokatny(h, w, d)
# zadanie 5
# def poletrapezu(podstawa=0, wysokosc=10, podstawa2=0):
#     pole=(((podstawa+podstawa2)*wysokosc)/2)
#     print(pole)
# a=int(input('a= '))
# b=int(input('b= '))
# h=int(input('h= '))
# poletrapezu(a,h,b)
# zadanie 6
# def iloczyn(a=1,b=4,ile=10):
#     koniec = a
#     koniec *= b**(ile-1)
#     return koniec
# print(iloczyn())
# zadanie 7
# def iloczyn(a=1,b=4,ile=10):
#     koniec = a
#     koniec *= b**(ile-1)
#     return koniec
# print(iloczyn())
# zadanie 8
# def ilosc_wartosc(**lista):
#     hajs = sum(lista.values())
#     suma = len(lista)
#     return hajs, suma
# lista = {'cebule': 5, 'kabanosy': 123, 'skarpety': 69}
# hajs, suma = ilosc_wartosc(**lista)
# print('kosztuja ',hajs)
# print('jest ich ',suma)

# zadanie 9
# x = int(input('podaj dodatnia wartosc= '))
# try:
#     sqrt = math.sqrt(x)
# except ValueError:
#     print('blad, podales liczbe ujemna')
#     exit()
#
# print(sqrt)
#
# print(x)
