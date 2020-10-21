
import datetime
g=datetime.datetime.now()

n=int(input("PRESS 1 TO START THE GAME"))
nam=input("Please enter a 5-8 digit username")
if len(nam)==5:
    
    nam=nam+"   "
if len(nam)==6:
    
    nam=nam+"  "
if len(nam)==7:
    
    nam=nam+" "
while(len(nam)>8 or len(nam)<5):
    print("Please enter a 5-8 digit username")
    k=input()
    nam=k

if len(nam)==7:
    nam=nam+" "
print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
print("|                                                                   |                         |                                                                  |")
print("|                                                                   |  WELCOME TO INTELLOQUIZ |                                                                  |")
print("|                                                                   |                         |                                                                  |")   
print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------|")
print("                                                                      The quiz for Intellects                     ")


while(n==1):
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    
    print()
    print()
    print()
    print("-->START QUIZ                  - PRESS 2")
    print("-->INSTRUCTIONS                - PRESS 3")
    print("-->PERSONAL IMPROVEMENT TABLE  - PRESS 4")
    print("-->QUIT                        - PRESS 5")
    n=int(input())
    while(n==3):
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("                                                                  INSTRUCTIONS                              ")
        print()
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("                      LEVEL 1                              ")
        print("                   .............                           ")
        print()
        print("This level consists of 5 questions")
        print("For every Right answer, you are awarded 2 points and you earn 0 points for not giving the right answer")
        print("PLEASE TYPE ALL YOUR ANSWERS IN SMALL LETTER")
        print()
        print()
        print("                      LEVEL 2                               ")
        print("                   .............                           ")
        print()
        print("This round consists of 6 MCQ Questions.")
        print("Each correct answer will fetch you 4 points and wrong answer leads to -1 point")
        
        print()
        print()
        print("                      LEVEL-3                                                                                                       ")
        print("                   .............                           ")
        print()
        print("This level consists of 3 questions each containing two parts.")
        print("If you answer the first part correct you get 5 points and a choice to play the next part or not")
        print("If you answer the second part correct,you win 10 points, But if you answer wrong, you get -10 points.")
        print()
        print()
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        n=1
        
    while(n==4):
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        print("                                  Through this table, we will show you how much your score has improved through all your games                                              ")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("IMPROVEMENT TABLE OF",nam)
        import mysql.connector
        db=mysql.connector.connect(host="localhost",user="root",password="1shanusurabhi1",database="surman1")
        cursor=db.cursor()
        q="select * from highscore where NAME='%s'" %(nam)
    
    
        cursor.execute(q)
        r=cursor.fetchall()
        
        print(".........................................................")
        print("NAME        L-1   L-2   L-3  TOTAL         DATE-TIME")
        print(".........................................................")
        for i in r:
            for k in i:
                str1=str(k)
                l=len(str1)
                if l==2:
                    print(k,end="    ")
                else:
                    print(k,end="     ")
                        
            
            print()
        print(".........................................................")
        n=1
                    
                
                       
        


    
    while(n==2):
        print(".................................................................................................................................................")
        print("                                                                             LEVEL-1                                                                                                                                                  ")
        print("                                                               This level consists of 5 questions")
        print("                                 For every Right answer, you are awarded 2 point and you earn 0 points for not giving the right answer")
        print("                                                                         Here you go!!!")
        print("                                                          PLEASE TYPE ALL YOUR ANSWERS IN SMALL LETTER")
        print()
        print()
        a=0
        score=0
        i=0
        import time
        import random
            
        print("questions coming in:")
        x=3
        while(x>0):
            print(x,end=" ")
            time.sleep(1)
            x=x-1
        print()
        while(i<5):
            #............................................................................
            while i==0:
                r=random.randint(1,4)
                if r==1:
                    print("Q1. How many players are there in a cricket team?")
                    ans=input()
                    if (ans=="11"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==2:
                    print("Q1.In which year did India gain independence from the British rule")
                    ans=input()
                    if (ans=="1947"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==3:
                    print("Q1.Which is the national aquatic animal of India?")
                    ans=input()
                    if (ans=="dolphin"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1

                if r==4:
                    print("Q1.In which year was Indian national congress formed?")
                    ans=input()
                    if (ans=="1885"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
            #......................................................................................................................
            while i==1:
                print()
                r=random.randint(1,4)
                if r==1:
                    print("Q2.Chandrayan 2 mission lander 'vikram' attempted to lamd on which pole of the moon?")
                    ans=input()
                    if (ans=="south"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==2:
                    print("Q2.PM Narendra Modi celebrated his __th birthday on 17 September 2019")
                    ans=input()
                    if (ans=="69"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        
                        i=i+1
                if r==3:
                    print("Q2.Name the man who founded rock garden")
                    ans=input()
                    if (ans=="nek chand")or(ans=="nekchand"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==4:
                    print("Q2.India’s first satellite- Aryabhata- was launched by India on 19th April 1975 from which country?")
                    ans=input()
                    if (ans=="russia"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                 #......................................................................................................................
            while i==2:
                print()
                r=random.randint(1,4)
                if r==1:
                    print("Q3.MC Mary Kom belongs to which state of India?")
                    ans=input()
                    if (ans=="Manipur")or(ans=="manipur"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==2:
                    print("Q3.Mahesh Bhupati is associated with which sport?")
                    ans=input()
                    if (ans=="tennis")or(ans=="lawn tennis"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==3:
                    print("Q3.Bhangra is to Punjab as Mohiniyattam is to_______?")
                    ans=input()
                    if (ans=="kerala"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==4:
                    print("Q3.Natya – Shastra:The main source of India's classical dances was written by?")
                    ans=input()
                    if (ans=="bharat muni")or(ans=="bharatmuni"):
                        print("Correct answer")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
            #......................................................................................................................
            while i==3:
                print()
                r=random.randint(1,4)
                if r==1:
                    print("Q4.which is the smallest planet in the solar system?")
                    ans=input()
                    if (ans=="mercury"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==2:
                    print("Q4.During which year did World War I begin?")
                    ans=input()
                    if (ans=="1914"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                        i=i+1
                if r==3:
                    print("Q4.India’s first railway university –The National Rail and Transportation Institute(NRTI)-is located in which state?")
                    ans=input()
                    if (ans=="gujrat"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                        i=i+1
                if r==4:
                    print("Q4.In which year did Mother Teresa win the Nobel Peace Prize?")
                    ans=input()
                    if (ans=="1979"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                
                
            #......................................................................................................................
            while i==4:
                print()
                r=random.randint(1,4)
                if r==1:
                    print("Q5.Which is the smallest state in India in terms of area?")
                    ans=input()
                    if (ans=="goa"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==2:
                    print("Q5.which is state has the largest population?")
                    ans=input()
                    if (ans=="uttar pradesh")or("uttarpradesh"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==3:
                    print("Q5.In which city of India is the Rock Garden located?")
                    ans=input()
                    if (ans=="chandigarh"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
                if r==4:
                    print("Q5.which is the largest planet in the solar system?")
                    ans=input()
                    if (ans=="jupiter"):
                        print("Correct")
                        score=score+2
                        i=i+1
                    else:
                        print("WRONG ANSWER")
                        i=i+1
        #................................................................................................................................
        print("YOUR SCORE AT THE END OF LEVEL-1 IS",score)
        if(score>=6):
            print()
            
            print()
            
            print("                                          Yay!congrats you have qualified to play the next level                                                ")
            print("                                                              Press 6 to play leveL-2                                                           ")
            n=int(input())
        else:
            
            s2=0
            s3=0
            ts=score+s2+s3
            import datetime
            g="             "+str(datetime.datetime.now())
            
            print()
            i=10
            n=1
            print("Sorry,Your score was not enough to let you qualify to the next round! ")
            import mysql.connector
            db=mysql.connector.connect(host="localhost",user="root",password="1shanusurabhi1",database="surman1")
            cursor=db.cursor()
            query="insert into highscore values(%s,%s,%s,%s,%s,%s)"
            data=(nam,score,s2,s3,ts,g)
            print("HIGHSCORE TABLE                                                                                             ")
            print()
            cursor.execute(query,data)
            db.commit()
            cursor.execute("select * from highscore order by total desc")
            result=cursor.fetchall()
            print(".........................................................")
            print("NAME        L-1   L-2   L-3  TOTAL       DATE-TIME")
            print(".........................................................")
            for i in result:
                for k in i:
                    str1=str(k)
                    l=len(str1)
                    if l==2:
                        print(k,end="    ")
                    else:
                        print(k,end="     ")
                        
                    
                print()
            print(".........................................................")
            
        while(n==6):
            s2=0
            s3=0
            print()
            print("                                                         WELCOME TO LEVEL-2                                 ")
            print("......................................................................................................................................")
            print("                 This round consists of 6 MCQ Questions.Each correct answer will fetch you 4 points and wrong answer leads to -1 point")                                                                             
            import time
            import random
            
            print("questions coming in:")
            x=3
            while(x>0):
                print(x,end=" ")
                time.sleep(1)
                x=x-1
            print()
            print("Q1.who in the following options is the current finanace minister of india?")
            print("..........................................................................")
            print("             options             ->           press       ")
            print("..........................................................................")
            print("1)Rajnath Singh                  ->            1          ")
            print("2)Amit Shah                      ->            2          ")
            print("3)G. Kishan Reddy                ->            3          ")
            print("4)Nirmila Sitharaman             ->            4          ")
            print("..........................................................................")
            k=int(input("ENTER OPTION"))

        
            if (k==4):
                s2=s2+4
                print("CORRECT")
            else:
                print('WRONG')
                s2=s2-1

            print()
            print("Q2.Chanakya is known by two other names.One is Kautilya.What is the other one?")
            print("..........................................................................")
            print("             options             ->           press       ")
            print("..........................................................................")
            print("1)Samudragupta                   ->            1          ")
            print("2)Amarsimha                      ->            2          ")
            print("3)Kumaragupta                    ->            3          ")
            print("4)Vishnugupta                    ->            4          ")
            print("..........................................................................")
            k=int(input("ENTER OPTION"))

        
            if (k==4):
                s2=s2+4
                print("CORRECT")
            else:
                print('WRONG')
                s2=s2-1

            print()
            print("In the ICC world cup 2019,India lost to New Zealand by how many runs?")
            print("..........................................................................")
            print("             options             ->           press       ")
            print("..........................................................................")
            print("1)15                             ->            1          ")
            print("2)18                             ->            2          ")
            print("3)19                             ->            3          ")
            print("4)21                             ->            4          ")
            print("..........................................................................")
            k=int(input("ENTER OPTION"))

        
            if (k==2):
                s2=s2+4
                print("CORRECT")
            else:
                print('WRONG')
                s2=s2-1

            print()
            print("Who is the chief architect of the Taj Mahal?")
            print("..........................................................................")
            print("             options             ->           press       ")
            print("..........................................................................")
            print("1)Mir Abdul Karim                ->            1          ")
            print("2)Ustad Isa                      ->            2          ")
            print("3)Ahmad Lahauri                  ->            3          ")
            print("4)Makramat Khan                  ->            4          ")
            print("..........................................................................")
            k=int(input("ENTER OPTION"))

        
            if (k==3):
                s2=s2+4
                print("CORRECT")
            else:
                print('WRONG')
                s2=s2-1
            print()
            print("what new program is to be launched relatedto education in India?")
            print(".........................................................................")
            print("             options             ->           press       ")
            print(".........................................................................")
            print("1)Study in India                 ->      1          ")
            print("2)Beti Bachao Beti Padhao        ->      2          ")
            print("3)Mid Day Meal scheme            ->      3          ")
            print("4)Operation Blackboard           ->      4          ")
            print(".........................................................................")
            n=int(input("ENTER OPTION"))
            if n==1:
                print("CORRECT")
                s2=s2+4
            else:
                print("WRONG")
                s2=s2-1

            print()
            print("who is the current governer of Haryana?")
            print(".........................................................................")
            print("             options             ->           press       ")
            print(".........................................................................")
            print("1)Satyadev Narayan Arya          ->      1          ")
            print("2)Lalji Tandon                   ->      2          ")
            print("3)Manhar Lal Khatter             ->      3          ")
            print("4)Ganga Prasad                   ->      4          ")
            print(".........................................................................")
            n=int(input("ENTER OPTION"))
            if n==1:
                print("CORRECT")
                s2=s2+4
            else:
                print("WRONG")
                s2=s2-1
            
            

            
        
            if (s2>=12): #condition for qualification
                print()
                print("YOUR SCORE AT THE END OF LEVEL-2 IS",score)
                print()
            
                print("Yay!congrats you have qualified to play the next level")
                print("Press 7 to play leveL-3")
                n=int(input())
            else:
                
                s3=0
                ts=score+s2+s3
                print()
                i=10
                n=1
                print("Sorry,Your score was not enough to let you qualify for the next round! ")
                import mysql.connector
                db=mysql.connector.connect(host="localhost",user="root",password="1shanusurabhi1",database="surman1")
                cursor=db.cursor()
                query="insert into highscore values(%s,%s,%s,%s,%s,%s)"
                data=(nam,score,s2,s3,ts,g)
                cursor.execute(query,data)
                db.commit()
                cursor.execute("select * from highscore order by total desc")
                result=cursor.fetchall()
                print("HIGHSCORE TABLE                                                                                             ")
                print()
                print(".........................................................")
                print("NAME        L-1   L-2   L-3  TOTAL   DATE-TIME")
                print(".........................................................")
                for i in result:
                    for k in i:
                        str1=str(k)
                        l=len(str1)
                        if l==2:
                            print(k,end="    ")
                        else:
                            print(k,end="     ")
                        
                    print()
                print(".........................................................")
            while(n==7):
                print("......................................................................................................................................")
                print("                                                                   LEVEL-3                                                                                                       ")
                print("RULE:This level consists of 3 questions each containing two parts. If you answer the first part correct you get 5 points and a choice to play the next part or not")
                print("                          If you answer the second part correct,you win 10 points, But if you answer wrong, you get -10 points.")
                print("                                                              PLAY MINDFULLY!                                                                                          ")
                print("questions coming in:")
                x=3
                while(x>0):
                    print(x,end=" ")
                    time.sleep(1)
                    x=x-1
                print()
                s3=0
                print("Q1.Which emporor constructed the Taj Mahal?")
                n=input()
                if(n=="shah jahan" or n=="shahjahan"):
                    s3=s3+5
                    print("CORRECT ANSWER!")
                    print("WOULD YOU LIKE TO ATTEMPT THE SECOND PART?n/y")
                    k=input()
                    if k=="y":
                        print("In which year,the construction of Taj Mahal got over?")
                        g=input()
                        if g=="1653":
                            
                            print("CORRECT ANSWER!")
                            s3=s3+10
                        else:
                            print("WRONG ANSWER!")
                            s3=s3-10
                    if(k=="n"):
                        print("OK")
                    
                        
                else:
                    print("WRONG ANSWER!")
                    print("You don't have the choice to attempt the next part of the question")
                print()
                print()
                print("Q2.Where is the oldest known monumental structure in the world located?")
                n=input()
                if(n=="giza" or n=="egypt"):
                    s3=s3+5
                    print("CORRECT ANSWER!")
                    print("WOULD YOU LIKE TO ATTEMPT THE SECOND PART?n/y")
                    k=input()
                    if k=="y":
                        print("The sphnix has the body of a/an ........ and the head of a Pharaoh ?")
                        g=input()
                        if g=="lion":
                            
                            print("CORRECT ANSWER!")
                            s3=s3+10
                        else:
                            print("WRONG ANSWER!")
                            s3=s3-10
                    if(k=="n"):
                        print("OK")
                    
                    
                        
                else:
                    print("WRONG ANSWER!")
                    print("You don't have the choice to attempt the next part of the question")
                print()
                print()
                print("Q3.Where are Northern Lights observed?")
                n=input()
                if(n=="artic circle")or(n=="articcircle"):
                    s3=s3+5
                    print("CORRECT ANSWER!")
                    print("WOULD YOU LIKE TO ATTEMPT THE SECOND PART?n/y")
                    k=input()
                    if k=="y":
                        print("What is the real name of this phenomenon?")
                        g=input()
                        if (g=="aurora borealis")or(g=="auroraborealis"):
                            
                            print("CORRECT ANSWER!")
                            s3=s3+10
                        else:
                            print("WRONG ANSWER!")
                            s3=s3-10
                    if(k=="n"):
                        print("OK")
                    
                    
                        
                else:
                    print("WRONG ANSWER!")
                    print("You don't have the choice to attempt the next part of the question")
                print("................................................................................................................................................")
                print("                                                                YOUR LEVEL-3 SCORE IS",s3)
                print()
                print("HIGHSCORE TABLE                                                                                             ")
                
                ts=score+s2+s3
                import datetime
                g=datetime.datetime.now()
                        
                print()
                i=10
                n=1
                
                import mysql.connector
                db=mysql.connector.connect(host="localhost",user="root",password="1shanusurabhi1",database="surman1")
                cursor=db.cursor()
                query="insert into highscore values(%s,%s,%s,%s,%s,%s)"
                data=(nam,score,s2,s3,ts,g)
                cursor.execute(query,data)
                db.commit()
                cursor.execute("select * from highscore order by TOTAL desc")
                result=cursor.fetchall()
                        
                print(".........................................................")
                print("NAME        L-1   L-2   L-3  TOTAL        DATE-TIME")
                print(".........................................................")
                for i in result:
                    for k in i:
                        str1=str(k)
                        l=len(str1)
                        if l==2:
                            print(k,end="    ")
                        else:
                            print(k,end="     ")
                        
                    print()
                print(".........................................................")
                print("WELL PLAYED!!!")
                print("THANKS FOR PLAYING!")
    while(n==5):
        print("THANKS FOR PLAYING")
        n=100
                
