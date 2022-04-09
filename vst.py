# ===================================================================


from psychopy import core, visual, event
import numpy as np
import random
import pandas as pd
import circle 
import arrow

id = input("Select 1: circleA 2. circleB 3: orientation")
name = input("Enter your name")

# window
mywin = visual.Window([800, 650], monitor="stanleyMac", units="deg")
    
# position of objects for each trial
if id == "1" or id == "2":
    xCord = np.arange(-4, 4.1, 2)
    yCord = np.arange(-3, 3.1, 1.5)
    h = -2
    cls = circle
    obj = circle.Circle
    if id == "1": 
        target = [162, 0, 255]
    else:
        target = [0, 255, 0]
else:
    xCord = np.arange(-8, 8.1, 4)
    yCord = np.arange(-7, 7.1, 3.5)
    h = -3
    cls = arrow
    obj = arrow.Arrow
    target = 0

# data table
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
columns = [[], col1, col2, col3, col4, col5, col6]

e1 = []
e2 = []
e3 = []
e4 = []
e5 = []
e6 = []
stimE =[[], e1, e2, e3, e4, e5, e6] 

# pause between trials
def pause():

    message = visual.TextStim(mywin, text="Next task\n Below is the target", 
                                alignText = 'center', height = 0.5)
    message.draw()

    obj([0, h], target).instantiate(mywin).draw()
    mywin.update()
    core.wait(1.5)
    mywin.flip()

# order each trial is presented randomized
presentationOrder = [1, 1, 1, 1, 1, 1, 1,
                    2, 2, 2, 2, 2, 2, 2,
                    3, 3, 3, 3, 3, 3, 3,
                    4, 4, 4, 4, 4, 4, 4, 
                    5, 5, 5, 5, 5, 5, 5,
                    6, 6, 6, 6, 6, 6, 6]
random.shuffle(presentationOrder)



if id == "2":
    stimulus = [[], circle.Stim1, circle.Stim2, circle.Stim3, circle.Stim4, circle.Stim5, circle.Stim6]
else:
    stimulus = [[], cls.stim1, cls.stim2, cls.stim3, cls.stim4, cls.stim5, cls.stim6]

# accuracy detection
counter = [0, 2, 2, 2, 2, 2, 2]
result = [0, 7, 7, 7, 7, 7, 7]

def createFrame(stim, num):
    # location of target
    x1, y1 = np.random.choice(xCord), np.random.choice(yCord)
    # create stimuli
    for x in xCord:
        for y in yCord:
            if x != x1 or y != y1:
                obj([x, y], stim[random.randint(0, len(stim) - 1)]).instantiate(mywin).draw()
    
    if counter[num] > 0:
        exist = random.randint(0, 1)

        if exist == 1:
            obj([x1,y1], target).instantiate(mywin).draw()
        else:
            obj([x1,y1], stim[random.randint(0, len(stim) - 1)]).instantiate(mywin).draw()
            counter[num] -= 1
    else:
        exist = 1
        obj([x1,y1], target).instantiate(mywin).draw()
    mywin.update()

    # stimulus response time
    clock = core.Clock()

    key = event.getKeys(keyList = ["m", "z"])

    while clock.getTime() < 10.0:
        key = event.getKeys(keyList = ["m", "z"])
        if "m" in key:
            time = round(clock.getTime(), 4)
            if exist == 0:
                result[num] -= 1
                columns[num].append(0)
            else:
                columns[num].append(time)
            break
        elif "z" in key:
            time = round(clock.getTime(), 4)
            if  exist == 1:
                result[num] -= 1
                columns[num].append(0)
            else:
                columns[num].append(time)
            break

    if ("z" not in key) and ("m" not in key):
        result[num] -= 1
        columns[num].append(0)
    
    stimE[num].append(exist)

    mywin.clearBuffer()
    quit = event.getKeys()
    return quit

message = visual.TextStim(mywin, text='Welcome to the visual search task!\n Enter the space bar to start.', alignText = 'center', height = 0.6)
message.draw() 
mywin.update()
event.waitKeys(keyList = ["space"])

message = visual.TextStim(mywin, text="Your objective is to look for a target surrounded by similar objects.\n If the target exists, press 'm'. Otherwise, press the key 'z'.\n Try to respond as fast as you can with acccuracy. Do not guess!\n Press space to continue.",
                             height = 0.3)
message.draw()
mywin.update()
event.waitKeys(keyList = ["space"])

message = visual.TextStim(mywin, text="Below is the target.\n Press space to continue.", 
                            alignText = 'center', height = 0.5)
message.draw()

obj([0, h], target).instantiate(mywin).draw()
mywin.update()
event.waitKeys(keyList = ["space"])

for i in presentationOrder:
    pause()
    ret = createFrame(stimulus[i], i)
    if 'q' in ret:
        break
    

if 'q' not in ret:
    accuracy = list(map(lambda x: x / 7, result))
    # accuracy = accuracy[1:]

    print(stimE)
    print(columns)
    print(e6)
    print(col6)

    df = pd.DataFrame(
        {
            "col1": col1,
            "e1": e1,
            "col2": col2,
            "e2": e2,
            "col3": col3,
            "e3": e3,
            "col4": col4,
            "e4": e4,
            "col5": col5,
            "e5": e5,
            "col6": col6,
            "e6": e6,
            "accuracy": accuracy
        }
    )

    with pd.ExcelWriter('/Users/stan.park712/Desktop/Neuro378/indptProject/neuro378indptProject/vstData.xlsx', mode = 'a') as writer:
        df.to_excel(writer, sheet_name = name)


