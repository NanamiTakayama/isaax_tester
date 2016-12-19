from updater import Updater
import time
repeat = 0
time = Updater("app.py")

for count in range(0,1):  
    test = Updater(1,1)
    test.modify()
    print("modifyed")
    test.commit()
    print("commited")
    test.push()
    print("___finish___")
    break
