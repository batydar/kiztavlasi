import random
from time import sleep
import os
from turtle import clear

class tavla():
    grup1=2
    grup2=2
    grup3=2
    grup4=1
    grup5=1
    grup6=1
    tur=1

siyaht=tavla()
beyazt=tavla()

a=1

def siyahzaratis():
    global siyaht, a
    zar=random.randint(1,6)
    zar1=zar
    if zar==1:
        if siyaht.grup1>0:    
            siyaht.grup1-=1
        else:
            siyaht.grup1-=0

    if zar==2:
        if siyaht.grup2>0:    
            siyaht.grup2-=1
        else:
            siyaht.grup2-=0

    if zar==3:
        if siyaht.grup3>0:
            siyaht.grup3-=1
        else:
            siyaht.grup3-=0

    if zar==4:
        if siyaht.grup4>0:
            siyaht.grup4-=1
        else:
            siyaht.grup4-=0

    if zar==5:
        if siyaht.grup5>0:
            siyaht.grup5-=1
        else:
            siyaht.grup5-=0

    if zar==6:
        if siyaht.grup6>0:
            siyaht.grup6-=1
        else:
            siyaht.grup6-=0

    zar=random.randint(1,6)
    zar2=zar
    if zar==1:
        if siyaht.grup1>0:    
            siyaht.grup1-=1
        else:
            siyaht.grup1-=0

    if zar==2:
        if siyaht.grup2>0:    
            siyaht.grup2-=1
        else:
            siyaht.grup2-=0

    if zar==3:
        if siyaht.grup3>0:
            siyaht.grup3-=1
        else:
            siyaht.grup3-=0

    if zar==4:
        if siyaht.grup4>0:
            siyaht.grup4-=1
        else:
            siyaht.grup4-=0

    if zar==5:
        if siyaht.grup5>0:
            siyaht.grup5-=1
        else:
            siyaht.grup5-=0

    if zar==6:
        if siyaht.grup6>0:
            siyaht.grup6-=1
        else:
            siyaht.grup6-=0

    if siyaht.grup1==0 and siyaht.grup2==0 and siyaht.grup3==0 and siyaht.grup4==0 and siyaht.grup5==0 and siyaht.grup6==0:
        if siyaht.tur==1:
            siyaht.grup1=3
            siyaht.grup2=3
            siyaht.grup3=3
            siyaht.grup4=2
            siyaht.grup5=2
            siyaht.grup6=2
            siyaht.tur-=1
        elif siyaht.tur==0:
            print("Siyah kazandı")
            a=0

    for i in range(0,10):
        fakezar1=random.randint(1,6)
        fakezar2=random.randint(1,6)
        print(f"{fakezar1},{fakezar2}")
        sleep(0.1)
        clearConsole()
    
    for i in range(0,10):
        fakezar2=random.randint(1,6)
        print(f"{zar1},{fakezar2}")
        sleep(0.1)
        clearConsole()
    
    print(f"{zar1},{zar2}")


def beyazzaratis():
    global beyazt, a
    zar=random.randint(1,6)
    zar1=zar
    if zar==1:
        if beyazt.grup1>0:    
            beyazt.grup1-=1
        else:
            beyazt.grup1-=0

    if zar==2:
        if beyazt.grup2>0:    
            beyazt.grup2-=1
        else:
            beyazt.grup2-=0

    if zar==3:
        if beyazt.grup3>0:
            beyazt.grup3-=1
        else:
            beyazt.grup3-=0

    if zar==4:
        if beyazt.grup4>0:
            beyazt.grup4-=1
        else:
            beyazt.grup4-=0

    if zar==5:
        if beyazt.grup5>0:
            beyazt.grup5-=1
        else:
            beyazt.grup5-=0

    if zar==6:
        if beyazt.grup6>0:
            beyazt.grup6-=1
        else:
            beyazt.grup6-=0    

    zar=random.randint(1,6)
    zar2=zar
    if zar==1:
        if beyazt.grup1>0:    
            beyazt.grup1-=1
        else:
            beyazt.grup1-=0

    if zar==2:
        if beyazt.grup2>0:    
            beyazt.grup2-=1
        else:
            beyazt.grup2-=0

    if zar==3:
        if beyazt.grup3>0:
            beyazt.grup3-=1
        else:
            beyazt.grup3-=0

    if zar==4:
        if beyazt.grup4>0:
            beyazt.grup4-=1
        else:
            beyazt.grup4-=0

    if zar==5:
        if beyazt.grup5>0:
            beyazt.grup5-=1
        else:
            beyazt.grup5-=0

    if zar==6:
        if beyazt.grup6>0:
            beyazt.grup6-=1
        else:
            beyazt.grup6-=0 

    if beyazt.grup1==0 and beyazt.grup2==0 and beyazt.grup3==0 and beyazt.grup4==0 and beyazt.grup5==0 and beyazt.grup6==0:
        if beyazt.tur==1:
            beyazt.grup1=3
            beyazt.grup2=3
            beyazt.grup3=3
            beyazt.grup4=2
            beyazt.grup5=2
            beyazt.grup6=2
            beyazt.tur-=1
        elif beyazt.tur==0:
            print("Beyazlar kazandı")
            a=0
    
    for i in range(0,10):
        fakezar1=random.randint(1,6)
        fakezar2=random.randint(1,6)
        print(f"{fakezar1},{fakezar2}")
        sleep(0.1)
        clearConsole()
    
    for i in range(0,10):
        fakezar2=random.randint(1,6)
        print(f"{zar1},{fakezar2}")
        sleep(0.1)
        clearConsole()
    
    print(f"{zar1},{zar2}")

def tahta():
    print("Beyaz")
    print(f"{beyazt.grup1}|{beyazt.grup2}|{beyazt.grup3}|{beyazt.grup4}|{beyazt.grup5}|{beyazt.grup6}")
    print()
    print()
    print(f"{siyaht.grup1}|{siyaht.grup2}|{siyaht.grup3}|{siyaht.grup4}|{siyaht.grup5}|{siyaht.grup6}")
    input("Siyah (Geçmek için 'enter')")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


while a==1:
    clearConsole()
    input("Beyaz zar atışı(Atmak için 'enter')")
    beyazzaratis()
    sleep(1)
    input("Siyah zar atışı(Atmak için 'enter')")
    siyahzaratis()
    sleep(1)
    clearConsole()
    tahta()
    sleep(1)

