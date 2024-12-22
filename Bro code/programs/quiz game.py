"""
way to add and remove questions and options
way to take the quiz 
score system 
"""
questions = [] 
options = []
while True : 
    question = input("Enter question: ")
    questions.append(question)
    
    for letter in ['A' , 'B' , 'C' , 'D']:
        opps = []
        opp = input(f"Enter options{letter} : ")
        opps.append

