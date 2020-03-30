##
'''Empty Space for Documentation'''
##
##
'''Empty Space for Importing Modules'''
# adding win32com.client for text to speech chatbot
import sys
import datetime
import random
import win32com.client
# global calling for speak client
speak=win32com.client.Dispatch("SAPI.SpVoice")
# test speech client here
'''while 1: 
    s=input("Enter the word you want to speak it out by computer or ""stop"" to stop.") 
    if (s=="stop"):
        break
    else:
        speaker.Speak(s)'''
##
'''Personal Details class to take personal info from user'''
class Personaldetails:
    def __init__(self,name,address,age,payment,employee):
        ##
        ##
'''Class Avanticars to traverse make for memory efficiency'''

class Avanticars:
    def __init__(self,model,make,price,company,color):
        ##
        ##
    def features(self):
        ##
    def price(self):
        ###
        ###
'''AI based module to take in personal details from user and STORE and be UI'''
def LifeisanAI:
    # There might be descrepency for variable calling, might not work BiDirectional
    def __init__ (self,name1,address1,age1,payment1,employee1,salary1,company1,color1,vipstatus,model1):
        ###
        self.name1=name1
        self.address1=address1
        self.age1=age1
        self.payment1=payment1
        self.employee1=employee1
        self.salary1=salary1
        self.company1=company1
        self.color1=color1
        self.vipstatus1=vipstatus1
        self.model1=model1
        ###
    def WorkshopAI(self):
        #### Project Start
        ainames=["Vicky","Qutupali","Farhan","Jamshed","Priya","Sammy","Shreyas","Bhavya"]
        file1=open("User-Data.transcript","a")
        ainameup=(random.choice(ainames))
        print("Hi! My name is ",ainameup,"\nHappy to Serve You, today.")
        print("\nWelcome to ColdFusion. \n Looks like you would like to buy a car. \n Don't worry, we are here to take care of everything while you relax and answer some simple question.\n Are you ready?")
        answer=input("(yes/no)--> ")
        if(answer=="yes"):
            ##
            ## Data Collection Bin Starts HERE!!
            age1=input(input("First we need to make sure, you are viable to buy a car. What's you age? --> "))
            if (age1>=18):
                self.name1=input("Let's start with your name...How should I address you? --> ")
                self.address1=input("Great! See that was easy, alright {0}, Where do you stay? --> ".format(name1))
                self.employee1=input("Awesome!! Now, where do you work? --> ")
                self.salary1=int(input("Whats you *Annual Income*, by this way we can determine what car is perfect for you? --> "))
                self.color1=input("There We GO! A simple small step! Favorite Color?! --> ")
                self.payment1=input("We are close now, {0}. How would you like to pay for your car?(cash/card/emi/others) --> ".format(name1))
                self.model1=input("Rhetorical Question TIME! \n\n If you had all the money in the world, which car will you buy, obviously you can only buy 1! -->")
                self.company1=input("Nice! If I had that kind of money to, I would buy the same car! \n Realistic Question Time, FAVORITE CAR COMPANY?")
                self.name1=self.name1.upper()
                self.payment1=payment1.upper()
                print("AMAZING!! We have all the details we need! Processing your INFO, and getting you the best deals and car!")
                ## FileWriteHERE!!
                datatime=str(datetime.datetime.now())
                file1.write("***************************************")
                file1.write("\nData Collection for -- ")
                file1.write(datatime)
                file1.write("\nName: ")  
                file1.write(self.name1)
                file1.write("\nAddress: ")
                file1.write(self.address1)
                file1.write("\nStatus: ")
                file1.write(self.employee1)
                #THIS MAY OR MAY NOT WORK!!
                salary2=str(self.salary1)
                file1.write("\nSalary: ")
                file1.write(salary2)
                file1.write("\nCOLOR: ")
                file1.write(self.color1)
                file1.write("\DreamCar: ")
                file1.write(self.model1)
                file1.write("\nCompany: ")
                file1.write(self.company1)
                file1.write("**************END OF COLLECTION\n\n")
                file1.close()
                ## FileWriteENDS!!
                ##
                # For SalaryVIPSTATUS
                if (salary>=200000 && salary<600000):
                    vipstatus="1"
                elif (salary>=600000 && salary<800000):
                    vipstatus="2"
                elif (salary>=800000 && salary<1200000):
                    vipstatus="3"
                elif (salary>=1200000 && salary<1900000):
                    vipstatus="4"
                elif (salary>=1900000):
                    vipstatus="5"
                else:
                    print("You are too poor to BUY even the lowest and cheapest possible car. \n You atlest need Annual Income of 2LAKHS to buy a car. \n If you think, you have entered wrong annual income.")
                    print("enter *okay* to restart or *quit*")
                    decision=input("(okay/quit)--> ")
                    if(decision=="okay"):
                        file1.close()
                        WorkshopAI(self):
                    else:
                        print("Money doesn't buy happiness, they said...")
                        file1.close()
                        sys.exit()
                if(vipstatus=="1"):
                    print("*\nHOW's Life treating you? It's difficult isn't.")
                    time.sleep(3)
                if(vipstatus=="5"):
                    print("*\nHEY! RICHIE RICH!\n*")
                    time.sleep(3)
                return self
            else:
                print("You should be atleast 18 years old to buy a car.\nIf you did this my mistake enter *okay* else enter *quit*")
                decision=input("(okay/quit)--> ")
                if(decision=="okay"):
                    file1.close()
                    WorkshopAI(self):
                else:
                    print("Age is just a number, they said...")
                    file1.close()
                    sys.exit()    
        else:
            print("Oops! No Problem, we can try next time, enter *okay* to try again \n OR \n *quit* to QUIT from the program.")
            decision=input("(okay/quit)--> ")
            if(decision=="okay"):
                file1.close()
                WorkshopAI(self):
            else:
                print("Sad to see you go and not buy anything...")
                file1.close()
                sys.exit()
######## END OF WORKSHOPAI########
#
#
#
# Global Variable Calling
myobj=LifeisanAI()
                
