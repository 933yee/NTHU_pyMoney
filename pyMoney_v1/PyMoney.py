from os import remove
from time import sleep
from msvcrt import getch
import myFunctions as mF

def begin():
    mF.interval()
    print("""
__      __   _                    _         ___      __  __                   
\ \    / /__| |__ ___ _ __  ___  | |_ ___  | _ \_  _|  \/  |___ _ _  ___ _  _ 
 \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ |  _/ || | |\/| / _ \ ' \/ -_) || |
  \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ |_|  \_, |_|  |_\___/_||_\___|\_, |
                                                |__/                     |__/    
""") 
    tempMenu="    Press \"\033[0;33mEnter\033[0m\" to start.\n    Press \"\033[0;33mEsc\033[0m\"   to quit."
    for i in tempMenu:
        print(i, end='', flush=True)
        sleep(0.015)

    print("",end='')
    while True:
        tempChoice = getch()
        if tempChoice == b'\r' :
            mF.interval()
            break
        elif tempChoice == b'\x1b':
            print("Quit!\n")
            mF.interval()
            mF.thank()
            exit(1)
def operation(className):
    classNameSize = len(className)
    _operations = ["Add", "Delete", "Show"]
    _operationsSize = len(_operations)
    mF.orderPrint("""    What do you want to do?\n\n    [0] Quit\n""")
    for i in range(_operationsSize):
        mF.orderPrint(f"    [{i+1}] {_operations[i]}\n")
    mF.orderPrint("    >> ")
    while True:
        tempChoice = getch()
        if not tempChoice.isdigit():
            continue
        tempChoice = int(tempChoice.decode("utf-8"))
        if 0<=tempChoice<=3:
            if tempChoice == 0:
                print("Quit!")
                mF.interval()
                mF.thank()
                exit(1) 
            print(f"{_operations[tempChoice-1]}!")
            mF.interval()
            if tempChoice == 1 :
                Choice(className, "add")
                break
            elif tempChoice == 2:
                Choice(className, "delete")
                break
            elif tempChoice == 3:
                showList(className, "Next Page", className)
                break
def deleteClass(className):
    classNameSize = len(className)
    print("    [0] Back")
    with open("className.txt", "r") as file:
        data = file.readlines()
    for n, classtitle in enumerate(data):
        print(f"    [{n+1}] {classtitle}",end='')
    mF.orderPrint("\n    Please choose the classification you want to delete\n    >> ")
    while True:
        tempChoice = getch().decode("utf-8")
        if(not tempChoice.isdigit()):
            continue
        tempChoice = int(tempChoice)
        if 0<= tempChoice <= classNameSize:
            if(tempChoice == 0):
                print("Back!",end='')
                mF.interval()
                return None
            mF.interval()
            mF.beCareful()
            mF.orderPrint(f"""\
    You can't retrieve your file once you deleted it!
    Are you sure to delete (Class)"\033[0;33m{className[tempChoice-1]}\033[0m"?\n\n""")
            if mF.confirm():
                mF.interval()
                with open("className.txt", "r") as file:
                    data = file.readlines()
                with open("className.txt", "w") as file:
                    for n, i in enumerate(data):
                        if(n+1 != tempChoice):
                            file.write(i)
                remove(className[tempChoice-1]+".txt")
                mF.orderPrint("    Delete successfully!\n")
                del className[tempChoice-1]
                mF.understand()
                return None
            else:
                mF.interval()
                deleteClass(className)
                return None
def deleteItem(deleteItemClass):
    print("    0.    Back")
    with open(f"{deleteItemClass}.txt", "r") as file:
        data = file.readlines()
    n = 1 
    tmpInterval = 0
    for k, i in enumerate(data):
        i = i.strip('\n')
        if k%2 == 0:
            print(f"    {n}.", end='')
            for p in range(5-len(str(n))):
                print(" ", end='')
            print(f"{i}", end='')
            tmpInterval += (10+len(i))
            n+=1
        else:
            for q in range(30-tmpInterval):
                print("-", end='')
            print(f"{i}$")
            tmpInterval = 0
    mF.orderPrint("\n    Input the item you want to delete\n    >> ")
    while True:
        number = input()
        mF.interval()
        if not number.isdigit() or int(number)<0 or int(number)>len(data)/2:
            print("    0.    Back")
            n = 1 
            tmpInterval = 0
            for k, i in enumerate(data):
                i = i.strip('\n')
                if k%2 == 0:
                    print(f"    {n}.", end='')
                    for p in range(5-len(str(n))):
                        print(" ", end='')
                    print(f"{i}", end='')
                    tmpInterval += (10+len(i))
                    n+=1
                else:
                    for q in range(30-tmpInterval):
                        print("-", end='')
                    print(f"{i}$")
                    tmpInterval = 0
            mF.orderPrint("\n    The item does not exist!\n")
            mF.orderPrint("    Please try it again!\n")
            print("    >> ",end='')
        elif int(number)==0:
            return None
        elif 0 < int(number) <= len(data)/2:
            number = int(number)
            break
            
    mF.beCareful()
    tmp = data[number*2-2].strip('\n')
    print(f"""\
    You can't retrieve your file once you deleted it!
    Are you sure to delete (Item)\"\033[0;33m{tmp}\033[0m\"?\n""")
    if mF.confirm():
        mF.interval()
        with open(f"{deleteItemClass}.txt", "w") as file:
            for n, i in enumerate(data):
                if((n+1)!=(number*2) and (n+1)!=(number*2-1)):
                    file.write(i)
        mF.orderPrint("    Delete successfully!\n")
        mF.understand()
    else:
        mF.interval()
        deleteItem(deleteItemClass)
        return None
def showList(className, page, rec):
    listInterval = "______________________________________________________"
    tempSumWidth = 18
    sum = 0
    print(f"     {listInterval} ")
    if page == 'Next Page':
        key=31
        key2='-'
    else:
        key=32
        key2='+'
    for num,i in enumerate(className):
        tempSum = 0
        #class
        print(f"    ‖{i}:", end='')
        for l in range(len(listInterval)-1-len(i)):
            print(" ", end='')
        print("‖")
        with open(f"{i}.txt", "r") as file:
            data = file.readlines()
        tempItem = ""
        tempDot  = ""
        tempCost = ""
        print("    ‖",end='')
        for l in range(len(listInterval)):
            print(" ",end='')
        print("‖")
        #name, price
        for j, k in enumerate(data):
            k = k.strip('\n')
            if j%2==0:
                tempItem+=f"     {k}"
                for p in range(25-len(tempItem)):
                    tempDot+="."
            else:
                sum+=int(k)
                tempSum+=int(k)
                tempCost+=f"{key2}{k} $"
                tempLenth=len(tempItem)+len(tempCost)+len(tempDot)
                print("    ‖",end='')
                print(f"\033[0;34m{tempItem}\033[0m{tempDot}\033[0;{key}m{tempCost}\033[0m", end='')
                for l in range(len(listInterval)+1-tempLenth-1):
                    print(" ", end='')
                print("‖")
                tempItem=""  
                tempCost=""  
                tempDot=""  
        print("    ‖",end='')
        for l in range(len(listInterval)-tempSumWidth):
            print(" ",end='')
        print(f"total:{tempSum} $", end='')
        for l in range(tempSumWidth-len(str(tempSum))-8):
            print(" ", end='')
        print("‖")
        print(f"    ‖{listInterval}‖\n")
        if(num != len(className)-1):
            print(f"     {listInterval} ")
    if page == 'Next Page':
        mF.orderPrint(f"    Total Expenditure: \033[0;{key}m{sum}\033[0m $\n")
    else:
        mF.orderPrint(f"    Total Income: \033[0;{key}m{sum}\033[0m $\n")
    calc(rec)
    mF.orderPrint(f"""
    [0] Back
    [1] {page}
    >> """)
    while True:
        a = getch()
        if a==b'0':
            print("Back!")
            break
        elif a==b'1':
            if page == 'Next Page':
                print("Next Page!")
                mF.interval()
                showList(["Income"], "Last Page", className)
                return None
            else:
                print("Last Page!")
                mF.interval()
                showList(rec, "Next Page", rec)
                return None
    mF.interval()
def addItem(inputClass, key):
    #input
    mF.orderPrint("    Input the item's name:\n    >> ")
    name = input().lower()
    mF.interval()
    mF.orderPrint("    Input the item's price:\n    >> ")
    price = input()
    while(not price.isdigit()):
        mF.interval()
        mF.warning()
        mF.orderPrint("    INVALID PRICE!\n    Please try it again\n    >> ")
        price = input()
    name = name.strip()
    price = price.strip()
    mF.interval()
    #confirm 
    print(f"""\
        State      : Add {key}     
    Classification : {inputClass}
         Name      : {name} 
        Price      : {price} $\n\n""", end='')
    if mF.confirm():
        pass
    else:
        mF.interval()
        return None
    mF.interval()
    with open(f"{inputClass}.txt", "a+") as file:
        file.write(f"{name}\n{price}\n")
    mF.orderPrint("    Add successfully!\n")
    mF.understand()
def addClass(className):
    classNameSize = len(className)
    if(classNameSize==9):
        mF.warning()
        mF.orderPrint("    There are too many classifications!\n")
        mF.orderPrint("    Please delete some of them!\n")
        mF.understand()
        Choice(className, "add")   
        return None
    mF.orderPrint("    Input the new classification\n    >> ")
    newClass = input().title()
    #check if it already exists
    with open("className.txt", "r") as file:
        data = file.readlines()
    for i in data:
        i=i.strip('\n')
        if(i.lower() == newClass.lower()):
            mF.interval()
            mF.warning()
            mF.orderPrint("    The classification already exists!\n")
            mF.orderPrint("    Please try it again!\n")
            mF.understand()
            Choice(className, "add")   
            return None
    mF.interval()
    mF.orderPrint(f"    Are you sure to add (Class)\"\033[0;33m{newClass}\033[0m\"?\n\n")
    if not mF.confirm():
        mF.interval()
        Choice(className, "add")
        return None
    mF.interval()
    with open(newClass+".txt", "w") as file:
        pass
    with open("className.txt", "a") as file:
        file.write(newClass+'\n')
    mF.orderPrint("    New classification successfully added!\n")
    mF.understand()
    className +=[newClass]
def Choice(className, key):
    mF.orderPrint(f"""\
    What do you want to {key}?\n
    [0] Back
    [1] Expenditure
    [2] Income
    [3] Classification
    >> """)
    while True:
        tempChoice = getch()
        if not tempChoice.isdigit():
            continue
        tempChoice = int(tempChoice.decode("utf-8"))
        if tempChoice == 0:
            print("Back!")
            mF.interval()
            return None
        elif  tempChoice == 1:
            print("Expenditure!")
            mF.interval()
            if(key == "add"):
                ClassOfItem(className, key)
            elif(key == "delete"):
                ClassOfItem(className, key)
            break
        elif  tempChoice == 2:
            print("Income")
            mF.interval()
            if(key == "add"):
                addItem("Income", "Income")
            elif(key == "delete"):
                deleteItem("Income")
            break
        elif tempChoice == 3:
            print("Classsfication!") 
            mF.interval()
            if(key == "add"):
                addClass(className)
            elif(key == "delete"):
                deleteClass(className)
            break
def ClassOfItem(className, key):
    classNameSize = len(className)
    #menu
    mF.orderPrint(f"""\
    What's the classification of the item which you want to {key}?
    \n""")
    mF.orderPrint(f"    [0] Back\n")
    for i in range(1,classNameSize+1):
        mF.orderPrint(f"    [{i}] {className[i-1]}\n")
    mF.orderPrint("    >> ")
    #choice
    while True:
        tempChoice = getch()
        if not tempChoice.isdigit():
            continue
        tempChoice = int(tempChoice.decode("utf-8"))
        if 0 <= tempChoice <= classNameSize:
            if tempChoice == 0:
                mF.interval()
                Choice(className, key)
                return None
            print(f"{className[tempChoice-1]}!")
            mF.interval()
            if(key == "add"):
                addItem(className[tempChoice-1], "Expenditure")
            elif(key == "delete"):
                deleteItem(className[tempChoice-1])
            break
def calc(className):
    sum = 0
    for i in className:
        with open(f"{i}.txt", "r") as file:
            data = file.readlines()
            for j in data:
                j = j.strip('\n')
                if j.isdigit():
                    sum-=int(j)
    with open("Income.txt", "r") as file:
        data = file.readlines()
        for j in data:
            j = j.strip('\n')
            if j.isdigit():
                sum+=int(j)
    if sum>0:
        mF.orderPrint(f"    Net Income : \033[0;32m{sum}\033[0m $\n")
    elif sum<0:
        mF.orderPrint(f"    Net Income : \033[0;31m{sum}\033[0m $\n")
    else:
        mF.orderPrint(f"    Net Income : \033[0;34m{sum}\033[0m $\n")
#init
className = []
with open("className.txt", "r") as file:
    data = file.readlines()
for n, i in enumerate(data):
    className += [""]
    className[n] += i.strip('\n')
begin()
while True:
    operation(className)
        


