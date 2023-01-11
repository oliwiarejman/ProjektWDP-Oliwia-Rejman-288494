import random
from sprawdzanie import checkans

questionslist=[]
def questions(source):
    with open(source, 'r') as file:
        read=file.readlines()
        for i in read:
            i=i.strip()
            questionslist.append(i.split(";"))
questions('pytania.txt')

def randomizer():
    a=random.choice(questionslist)
    questionslist.remove(a)
    qst=a[0]
    ans=a[1:5]
    print(qst,ans)
    return answers(ans,qst)

def answers(ans,qst):
    list=[]
    i=random.sample(range(1,5),4)
    correct=ans[3]
    for j in range(len(ans)):
        list.insert(j,ans[i[j]-1])
    print(list)

    if checkans(correct,list):
        return True
    else:
        return False


randomizer()


