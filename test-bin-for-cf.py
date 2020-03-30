'''import datetime
import sys
datatime=str(datetime.datetime.now())
file2=open("Garbage-Dump.coldfusion","a")
file2.write("\nWrite Data Current Time -- ")
file2.write(datatime)
file2.close()
print(datatime)
yes=input("Works to quit?")
if(yes=="m"):
    sys.exit()
else:
    print(".......")'''
salary1=int(input("Integar:"))
salary2=str(salary1)
file2=open("Garbage-Dump.coldfusion","a")
file2.write("\n DATA GARBAGE:\n")
file2.write(salary2)

