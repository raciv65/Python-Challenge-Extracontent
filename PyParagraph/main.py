import os
import re
import csv

Choose=input(f'''Wich paragraph do you want to analysis:
(1) paragraph_1.txt
(2) paragraph_2.txt
(3) paragraph_3.txt

''')

def avarange(numbers):
    n=len(numbers)
    total=0
    for x in numbers:
        total=total+x
    if n!=0:
        return total/n
    else:
        return 0

if Choose== "1" or Choose=="2" or Choose=="3":
    File=os.path.join("Resources","paragraph_"+str(Choose)+".txt")
    Paragraph=[x.rstrip() for x in open(File, "r", encoding="UTF-8")]
    Words=Paragraph[0].split(" ")

    LettersWord=[]
    WordsCount=0
    for word in Words:
        WordsCount=WordsCount+1
        LettersWord.append(len(word))

    Sentences=re.split("(?<=[.!?]) +",Paragraph[0])

    SentenceCount=0
    for sentence in Sentences:
        SentenceCount=SentenceCount+1


    print(f'''
    Paragraph Analysis
    ---------------------------------------------
    Approximate Word Count: {WordsCount:,}
    Approximate Sentence Count: {SentenceCount:,}
    Average Letter Count: {round(avarange(LettersWord),1):,}
    Average Sentence Length: {round((WordsCount/SentenceCount),2):,}
    ''')

    SaveFile=os.path.join("Analysis","Paragraph"+str(Choose)+".txt")
    with open(SaveFile, "w", newline='', encoding="UTF-8") as datafile:
        writer=csv.writer(datafile)
        writer.writerow(['Paragraph Analysis'])
        writer.writerow(['-------------------------------------------------'])
        writer.writerow(['Approximate Word Count: {:n}'.format(WordsCount)])
        writer.writerow(['Approximate Sentence Count: {:n}'.format(SentenceCount)])
        writer.writerow(['Averange Letter Count: {:n}'.format(round(avarange(LettersWord),1))])
        writer.writerow(['Averange Setence Length: {:n}'.format(round(WordsCount/SentenceCount,2))])
        
else:
    print(f''' Please, choose or write a number''')