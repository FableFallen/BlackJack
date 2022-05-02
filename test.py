def choosecheck():
  a=input("Choose bathroom, bedroom, Tyrell, Chang, or living room:" )
  choice=a.lower()
  if choice=="bathroom":
    print ("You begin to enter the bathroom and BAM! The smell is too \noverwhelming, you start to lose conciousness, God?\nRoberto: はははは、あなたは私の幻術にいます....今すぐ悪臭を逃れてみてください！ Translation: Ha ha ha, you are in my\n genjutsu.... \nTry escaping the stench now!\nYou died:/")
  elif choice=="bedroom":
    print()
    print ("You have found Roberto's math homework! On the back of the \npaper it says solve if you want to get out... Where/who do you \nwant to visit to solve this correctly?")
    choice2=input("Choose bathroom, bedroom, Tyrell, Chang, or living room:" )
    choose2(choice2)
  elif choice=="tyrell":
    print()
    print("Tyrell: Yo! You return to the to the beginning confused, why is this man in Roberto's house?")
    choosecheck()
  elif choice=="chang":
    print()
    print("Hello for you, $5 off! Who is this man and what is he selling? You return to where you started confused. ")
    choosecheck()
  elif choice=="living room":
    print()
    print("You look around and it's bare. You here Roberto rumbling he sounds like he needs help from his sudden groans. Instead you \ndecide to head back to the front of the house quietly. ")
    choosecheck()
    



def choose2(b):
  if b==("Tyrell"):
    print("Tyrell: I'm sorry I don't know how to solve this.\\nYou return to the bedroom in shame")
  choosecheck()


print("Welcome to Hide and... welp just hide basically! ")
print("Your hiding from Roberto watch out or he'll make you code,\noh no!\nRemember Reburto always starts in the bathroom first becuase\nof his difficult diet he has to maintain.")
choosecheck()