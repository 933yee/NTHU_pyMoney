import msvcrt, time, os
def thank():
    print("""\
 _____  _                    _      __   __               _ 
|_   _|| |__    __ _  _ __  | | __  \ \ / /___   _   _   | |
  | |  | '_ \  / _` || '_ \ | |/ /   \ V // _ \ | | | |  | |
  | |  | | | || (_| || | | ||   <     | || (_) || |_| |  |_|
  |_|  |_| |_| \__,_||_| |_||_|\_\    |_| \___/  \__,_|  (_)
  """)
def interval():
    print("""\

====================================================================================================
====================================================================================================
""")
def warning():
    print("""\
\033[0;31m    __        __                   _                 _ 
    \ \      / /__ _  _ __  _ __  (_) _ __    __ _  | |
     \ \ /\ / // _` || '__|| '_ \ | || '_ \  / _` | | |
      \ V  V /| (_| || |   | | | || || | | || (_| | |_|
       \_/\_/  \__,_||_|   |_| |_||_||_| |_| \__, | (_)
                                             |___/     \033[0m""")
def confirm():
    orderPrint("""\
    [0] Confirm
    [1] Cancel
    >> """)
    while True:
        tempChoice = msvcrt.getch().decode("utf-8")
        if tempChoice == '0':
            print("Confirm!")
            return True
        elif tempChoice == '1':
            print("Cancel")
            return False
def beCareful():
    print("""\
\033[0;31m    ____            ____                __       _     _ 
    | __ )  ___     / ___|__ _ _ __ ___ / _|_   _| |   | |
    |  _ \ / _ \   | |   / _` | '__/ _ \ |_| | | | |   | |
    | |_) |  __/   | |__| (_| | | |  __/  _| |_| | |   |_|
    |____/ \___|    \____\__,_|_|  \___|_|  \__,_|_|   (_)\033[0m
""")
def understand():
    orderPrint("\n    [0] Confirm\n    >> ")
    while True:
        tempChoice = msvcrt.getch().decode("utf-8")
        if tempChoice == '0':
            break
    interval()
def orderPrint(src):
    for i in src:
        print(i, end='', flush=True)
        time.sleep(0.01)