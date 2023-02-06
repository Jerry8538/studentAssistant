#########################################################
# HOMEWORK HELPER

from datetime import datetime,timedelta
from IPython.display import clear_output

HW = '/home/yk/studentAssistant/files/homework'

def display(list):
    list.sort()
    for x in range(len(list)):
        print(x+1,end=' - ')
        for y in range(1,4):
            print(list[x][y],end='  ')
        print()

def initialize(list):
    for i in range(len(list)):
        list[i].insert(0,['VV-IMP','V-IMP','IMP'].index(list[i][2])*7)
        rank = str(datetime.strptime(mlist[i][2],'%d/%m/%Y')-datetime.now()).split(' ')[0] #Generates rank of hw based on date n importance
        if '.' in rank:
            list[i][0] += int(rank.split(':')[0])/24
        else:
            list[i][0] += int(rank)
    display(list)

def add_hw(hw,date,imp):
    try:
        #what does this do??
        #if datetime.strptime(date,'%d/%m/%Y') and ['VV-IMP','V-IMP','IMP'].index(imp):
            a = open(f"{HW}/homework", "a")
            a.write('~'.join((hw,date,imp,'\n')))
            a.close()
            print('HW has been added!')
    except:
        print('Please enter valid dates and/or choose value from given options')

def del_hw():
    try:
        toDel = int(input('Enter index of homework completed: '))
        del mlist[toDel-1]
        a = open(f"{HW}/homework", "w")
        for i in mlist:
            del i[0]
            a.write('~'.join(i)+'\n') #Encodes and enters hw in homework file
        a.close()
        print('HW has been deleted!')
    except:
        print('Please enter an index from the list of hw')
#########################################################

from pomodoroTimer import pomodoro
from notesFinder import notes

while True:
    mlist = []
    a = open(f"{HW}/homework","r")
    for i in a:
        mlist.append((i[:-1]).split('~'))
    a.close()

    print('Homework: (Title/DoS/Value)')

    if mlist != []:
        initialize(mlist)
    else:
        print('No Homework!')
    print()

    print('''Enter:
    '1' to add new HW
    '2' to remove old HW
    '3' to start Pomodoro Timer
    '4' to start Notes Helper''')
    opt = input('')

    if opt == '1':
        hw = date = imp = ''
        hw = input('Enter HW title: ')
        date = input('Enter date of submission dd/mm/yyyy: ')
        imp = input('Enter importance (VV-IMP/V-IMP/IMP): ').upper()
        add_hw(hw,date,imp)


    elif opt == '2':
        del_hw()


    elif opt == '3':
        clear_output()
        display(mlist)
        print()

        work=int(input('Enter study time (min): '))
        rest=int(input('Enter rest time (min): '))
        iterations=int(input('Enter number of iterations: '))

        pomodoro(work,rest,iterations)


    elif opt == '4':
        print()
        notes()
        print()

    else:
        print('Please enter a valid option: ')

    clear_output()
