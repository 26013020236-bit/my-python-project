import random
import time
print('=== JOB INTERVIEW PRACTICE ===')
print('Practice like a real HR interview')
name = input('Enter your name: ')
post = input('Which job you want - Developer, Designer, Manager: ')
print('Hello ' + name + '! Interview for ' + post + ' starts now...')
time.sleep(1)
score = 0
questions = ['Tell me about yourself?', 'Why should we hire you?', 'What is your biggest weakness?', 'Where do you see yourself in 5 years?', 'Why do you want this job?']
tips = ['Speak confidently, smile!', 'Give short and clear answer!', 'Show your skills, not just marks!', 'Be honest, HR catches lie!', 'Keep eye contact!']
for i in range(5):
    print(' ')
    print('HR Question ' + str(i + 1) + ' : ' + questions[i])
    ans = input('Your Answer: ')
    print('HR is thinking...')
    time.sleep(1)
    if len(ans) < 10:
        print('HR: Too short! Explain more!')
        print('Tip: ' + tips[i])
    elif len(ans) < 30:
        print('HR: Good, but you can do better!')
        score = score + 5
    else:
        print('HR: Excellent Answer! Very Impressive!')
        score = score + 10
    print('Your Score: ' + str(score) + '/50')
print(' ')
print('=== INTERVIEW RESULT ===')
print('Candidate: ' + name)
print('Post: ' + post)
print('Final Score: ' + str(score) + '/50')
if score >= 40:
    print('Result: SELECTED! Offer Letter Coming Soon!')
    print('Package: 8 LPA!')
elif score >= 25:
    print('Result: WAITLISTED! Second round pending!')
else:
    print('Result: REJECTED! But dont give up!')
    print('Practice more and come again!')
print('Interview Over! Best of Luck ' + name + '!')
