import sqlite3
import  matplotlib.pyplot as plt

con = sqlite3.connect('survey.sqlite3')

cur = con.cursor()

mQuestions = []
fQuestions = []

mQsorted = []
fQsorted = []

def SortQuestions(items):
    sorted = []
    output = []
    x = 2
    while x <= 16:
        sorted = []
        for item in items:
            sorted.append(item[x])
        x+=1
        sorted.sort()
        output.append(sorted)
    return output
def Show(list, name):
    for i, q in  enumerate(list):
        plt.hist(q, bins=10, align='mid')
        plt.xlabel('Letter')
        plt.ylabel('Number')
        plt.title(f'Question {i}, {name}')
        plt.show()
def main():
    for row in cur.execute('SELECT * FROM questions WHERE gender="male"'):
        mQuestions.append(row)
    for row in cur.execute('SELECT * FROM questions WHERE gender="female"'):
        fQuestions.append(row)
    
    mQsorted = SortQuestions(mQuestions)
    fQsorted = SortQuestions(fQuestions)
    
    Show(mQsorted, "Male")
    Show(fQsorted, "Female")
    

    con.close()

if __name__ == '__main__':
    main()


