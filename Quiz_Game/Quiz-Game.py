########### MODULES #################
import warnings                     #
from datetime import datetime       #
import sys                          #   
try:                                #
    import pandas as pd             #
    import pyfiglet as pf           #
    import time                     #
    import random                   #
    import os                       #
#####################################

########### BANNER #############################
    pf = pf.figlet_format("Quiz Game")         #
    print(pf,"\n version 2.0")                 #
    print()                                    #
    warnings.filterwarnings('ignore')          #
################################################

###################### MAIN CODE ###########################################################
    data=pd.read_csv("quiz_questions.csv")
    df=data.to_string()
    #print("DATASET:\n",df)
    print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
    print("------------------------------------------------------- :INSTRUCTIONS: ----------------------------------------------------------------------------------")
    print()
    print('''[?]General Instructions:
   ********************

(1) For Every Correct Answer you will be Awarded (+4) points.

(2) For every Incorrect (-1) will be deducted.

(3) For Not Attempted (0) marks.

(4) For Wrong Question And Answer (+1) marks.

(5) The Question answers are of True/False.

(6) press ctrl+c to quit.

''')
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    inp=input("[+]Enter <Start> to Start or <Exit> to Stop: ")
    print()
    if inp=="Start" or inp=="start":
        pass
    else:
        print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
        print()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        sys.exit()
    name = input("Enter Your Name: ").strip().title()
    if name == "":
        name = "Player001"
    print()
    random=data.sample(n=5).reset_index(drop=True)
    lst=[]
    n=0
########### To Print Ramdom Values from Dataframe ###########################################
    while n<5:
        print("---------------------------------------------------------- :QUESTION: -----------------------------------------------------------------------------------")
        print()
        print("[?] Type: ",str(random.loc[n,'Type']).upper())
        print()
        if random.loc[n,'Difficulty']=='easy':
            print("[?] Category: ",random.loc[n,'Category'])
            print("[?] Difficulty: ",random.loc[n,'Difficulty'])
            print()
            print()
            print("[>>] System Question: ",random.loc[n,'Question'])
            print()
            res=str(input("[+] Enter Your Answer: "))
            print()
            print()
            print("------------------------------------------------------------ :RESULT: -----------------------------------------------------------------------------------")
            print()
            if res.lower()==str(random.loc[n,'Answer']).lower():
                print("[*] Your Answer:",res)
                print()
                print("[=>] System Answer: ",random.loc[n,'Answer'])
                print()
                print("[>>>] Answer Is Correct!")
                print()
                print("[+] Your Point: +4")
                print()
                lst.append(4)
            elif res=="":
                print("[*] Your Answer is null")
                print()
                print("[=>] System Answer: ",random.loc[n,'Answer'])
                print()
                print("[>>>] Not Attempted!")
                print()
                print("[+] Your Point: 0")
                print()
                lst.append(0)
            elif res.lower()!=str(random.loc[n,'Answer']).lower():
                print("[*] Your Answer:",res)
                print()
                print("[>>>] Answer Is Incorrect!")
                print()
                print("[=>] Correct Answer: ",random.loc[n,'Answer'])
                print()
                print("[-] Your Point: -1")
                print()
                lst.append(-1)
        else:
            print("Random Question:", random.loc[n,'Question'])
            print("[?] Difficulty: ",random.loc[n,'Difficulty'])
            print()
            res=str(input("[+] Enter Your Answer: "))
            print()
            print("------------------------------------------------------------ :ANSWER: -----------------------------------------------------------------------------------")
            print()
            print("[*] Your Answer:",res)
            print()
            print("[=>] System Answer: ",random.loc[n,'Answer'])
            print()
            print("[>>>] Question Level is Invalid!")
            print()
            print("[+] Your Bonus Point: +1")
            lst.append(1)

        n += 1
        print()

########################## SCORE SUMMARY ##################################
    print("------------------------------------------------------ :SCORE SUMMARY: ----------------------------------------------------------------------------------")
    print()
    print("[+] Generating your score...")
    print()
    time.sleep(3)
    total_score = sum(lst)
    print("[*] YOUR TOTAL SCORE:", total_score, "out of 20")
    print()
    if total_score >= 18:
        print("[🏆] Excellent! You are a quiz master!")
    elif total_score >= 14:
        print("[✔] Great job! You know your stuff.")
    elif total_score >= 8:
        print("[~] Good effort! Keep practicing.")
    else:
        print("[!] Needs improvement. Try again!")
    print()
    print("[-] Completed at:", datetime.now().strftime("%I:%M %p"), "On", datetime.now().strftime("%d %B %Y, %A"))
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    inpu=input("[+]Enter <CONTINUE> to continue or <EXIT> to Stop: ")
    print()
    if inp=="Continue" or inp=="continue":
        time.sleep(1)
        exec(open(__file__).read())
    else:
        ########### SAVE SCORE #####################
        score_data = pd.DataFrame([[name, total_score]], columns=["Name", "Score"])

        if os.path.exists("quiz_scores.csv"):
            existing = pd.read_csv("quiz_scores.csv")
            updated = pd.concat([existing, score_data], ignore_index=True)
            updated.to_csv("quiz_scores.csv", index=False)
        else:
            score_data.to_csv("quiz_scores.csv", index=False)

        print("[💾] Your score has been saved to 'quiz_scores.csv'.")
        print()

    ########### SCOREBOARD #####################
        print("------------------------------------------------------- :SCOREBOARD: -------------------------------------------------------------------------------------")
        scoreboard = pd.read_csv("quiz_scores.csv")
        scoreboard = scoreboard.sort_values(by=["Name", "Score"], ascending=[False, False]).reset_index(drop=True)
        top5 = scoreboard.head(5)
        print()
        print("[$] Your ScoreBoard:\n")
        print(top5.to_string(index=False))
        print()
        print()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
        print()
        sys.exit()

except KeyboardInterrupt or Exception:
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("[-] Something Went Wrong!")
    print("[-] Exited at:", datetime.now().strftime("%I:%M %p"), "On", datetime.now().strftime("%d %B %Y, %A"))
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    sys.exit()
