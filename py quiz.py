print('Welcome to the quiz')
score = 0
print("Question 1: How old is Nivaan?")

print('A. 9 B. 10 C. 4 D. 8')

answer=input('Enter your answer here(A/B/C/D): ')
if answer=='A':
     print ('Correct')
     score = score + 10
else:
     print ('Incorrect')
     score = score -5
print ('Question.2 What is the capital of the UAE') 

print ("A. Sharjah /B. Umm Al Quain /C. Abu Dhabi /D. Dubai")
answer=input('Enter your answer here (A/B/C/D): ')
if answer =='C':
     print ('Correct') 
     score = score +10

else:
     print ('Incorrect')
     score = score -5

print("your score is : ",score)