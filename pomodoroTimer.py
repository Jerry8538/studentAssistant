# POMODORO TIMER
import time

def countdown(t,status):
    #t is in seconds
    while t:
        min,sec=divmod(t,60)
        print('',end='\r')

        #updates value of timer every sec
        #flushes buffer because we are printing on same line
        print(f"{status}- {min:02d}m:{sec:02d}s",end="",flush=True)
        t-=1
        time.sleep(1)

def pomodoro(work,rest,iterations):
    #work and rest is in minutes
    w=work*60
    r=rest*60
    for i in range(iterations):

        countdown(w,'Study Time')
        #winsound.PlaySound(r'C:\Windows\Media\Alarm03.wav', winsound.SND_ALIAS) #plays music after each time period, repeats for 4 pomodoros
        print('\nbeep beep, study over')

        countdown(r,'Rest Time')
        #winsound.PlaySound(r'C:\Windows\Media\Alarm01.wav', winsound.SND_ALIAS)
        print('beep beep, rest over')
