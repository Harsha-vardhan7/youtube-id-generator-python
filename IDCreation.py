from pyyoutube import Api
import random
import re
import tkinter
import time

root = tkinter.Tk()
root.title('Youtube ID Genarating ')
root.geometry('600x300')

videoId = str()


validity = tkinter.Label(root, text='', font=('Courier', 20))
validity.place(x=55, y=120)

availability = tkinter.Label(root, text='', font=('Courier', 20))
availability.place(x=55, y=150)


def createId():
    validity.config(text='')
    availability.config(text='')
    tempId = str()
    for i in range(11):
        rand = random.randrange(0, 65)
        if(rand >= 0 and rand <= 9):
            tempId += str(rand)
        elif(rand >= 10 and rand <= 35):
            tempId += str(chr(rand+87))
        elif(rand >= 36 and rand < 62):
            tempId += str(chr(rand+29))
        elif rand == 62:
            tempId += '-'
        elif rand == 63:
            tempId += '_'
    videoId = 'LydzWx2ScT8'
    # videoId = 'G6F-0o3oLwE'
    # print(videoId)
    itrId = str()
    for i in videoId:
        itrId = itrId + i
        Tid.config(text=itrId, font=('Courier', 30))
        Tid.update()
        time.sleep(0.2)
    checkAvailability(videoId)
    checkValidity(videoId)


def getRegEx(val):
    reg = str()
    reg += '[0-9-_]*'
    for i in val:
        reg += i + '[0-9-_]*'
    return reg


def checkValidity(id):
    flag = True
    words = open('words.txt', 'r')
    wordList = words.readlines()
    for i in wordList:
        reg = getRegEx(i[0:-1])
        x = re.search(reg, id, re.IGNORECASE)
        if x:
            msg = id + ' is not Valid ID'
            validity.config(text=msg, fg='red')
            flag = False
            break
    if flag:
        msg = id + ' is Valid ID'
        validity.config(text=msg, fg='green')


def checkAvailability(id):
    api = Api(api_key='AIzaSyC6caNTk146yQamCj0IKT2J9yYjGghpm2c')
    video_by_id = api.get_video_by_id(video_id=id)
    count = video_by_id.items
    print(count)
    if len(count) == 0:
        availability.config(text=id+' is available ', fg='green')
    else:
        availability.config(text=id+' is not available ', fg='red')


button = tkinter.Button(root, text='Create ID', command=createId)
button.place(x=250, y=25)

Tid = tkinter.Label(root, text='')
Tid.place(x=100, y=60)


root.mainloop()
