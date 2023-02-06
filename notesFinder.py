import shutil,os

FILES = ['textbook','exemplar']
SOURCE = '/home/yk/studentAssistant/files/notesFinder'
OUTPUT = '/home/yk/Desktop/study'

def moveFiles (subject,chapter):
    for f in FILES:
        shutil.copy(f'{SOURCE}/{subject}/{chapter}/{f}.pdf',
                    f'{OUTPUT}/{f}.pdf')

def removeFiles():
    for f in FILES:
        os.remove(OUTPUT + f'/{f}.pdf')

def notes():
    # goes until file moved
    while True:
        sub = input('Enter subject: ')
        chap = input('Enter chapter: ')
        try:
            moveFiles(sub,chap)
        except:
            print('Wrong subject/chapter')
            continue
        break

    # goes until done
    while True:
        if input('Done? ') == 'yes':
            try:
                removeFiles()
            except:
                print('failed to delete; do it manually')
            break
