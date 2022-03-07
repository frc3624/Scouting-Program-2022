from doctest import master
import tkinter as tk
import json
from tracemalloc import start

window = tk.Tk()
window.title("Rapid React Scouting")
window.configure(background='white')

def addTeam(): #called when submit button pressed; adds new team object to json
    with open("TeamData.json", "r") as f:
        teams = json.load(f)
    if str(robotNumEntry.get()) in teams:
        teams[robotNumEntry.get()]["highBalls"] += int(highBallsEntry.get())
        teams[robotNumEntry.get()]["lowBalls"] += int(lowBallsEntry.get())
        teams[robotNumEntry.get()]["autoBalls"] += int(autoBallsEntry.get())
        teams[robotNumEntry.get()]["rungsClimbed"] += int(rungsClimbed.get())
        teams[robotNumEntry.get()]["numDataPoints"] += 1
        teams[robotNumEntry.get()]["penalties"] += int(penaltiesEntry.get())

    else:
        teams[robotNumEntry.get()] = {}
        teams[robotNumEntry.get()]["startingSpot"] = startingSpot.get()
        teams[robotNumEntry.get()]["autoBalls"] = int(autoBallsEntry.get())
        teams[robotNumEntry.get()]["ballColor"] = ballColor.get()
        teams[robotNumEntry.get()]["floorBalls"] = floorBalls.get()
        teams[robotNumEntry.get()]["droppedBalls"] = droppedBalls.get()
        teams[robotNumEntry.get()]["highBalls"] = int(highBallsEntry.get())
        teams[robotNumEntry.get()]["lowBalls"] = int(lowBallsEntry.get())
        teams[robotNumEntry.get()]["rungsClimbed"] = int(rungsClimbed.get())
        teams[robotNumEntry.get()]["numDataPoints"] = 1
        teams[robotNumEntry.get()]["penalties"] = int(penaltiesEntry.get())
    with open("TeamData.json", "w") as f:
        json.dump(teams, f)

def findTeams():
    output.delete(1.0, 'end')
    with open("TeamData.json", "r") as f:
        teams = json.load(f)
    for team in teams:
        #print(team)
        if (teams[team]["startingSpot"] == startingSpotFilter.get()) and ((teams[team]['autoBalls'] / teams[team]['numDataPoints']) >= int(autoBallsFilter.get())) and (teams[team]['ballColor'] == ballColorFilter.get()) and (teams[team]['floorBalls'] == floorBallsFilter.get()) and (teams[team]['droppedBalls'] == droppedBallsFilter.get()) and  ((teams[team]['highBalls'] / teams[team]['numDataPoints']) >= int(highBallsFilter.get())) and ((teams[team]['lowBalls'] / teams[team]['numDataPoints']) >= int(lowBallsFilter.get())) and ((teams[team]['rungsClimbed'] / teams[team]['numDataPoints']) >= int(rungsClimbedFilter.get())):
            output.insert('end', team +"               num penalties:"+teams[team]["penalties"]+'\n')

#Add in text for all questions
tk.Label(window, text='Robot Num', bg='white', fg='black', font='none 12 bold').grid(row=0, column=0, sticky='W') 
tk.Label(window, text='Starting Spot', bg='white', fg='black', font='none 12 bold').grid(row=1, column=0, sticky='W')
tk.Label(window, text='Auto Balls', bg='white', fg='black', font='none 12 bold').grid(row=2, column=0, sticky='W')
tk.Label(window, text='Detect Ball Color?', bg='white', fg='black', font='none 12 bold').grid(row=3, column=0, sticky='W')
tk.Label(window, text='Pick up balls from floor?', bg='white', fg='black', font='none 12 bold').grid(row=4, column=0, sticky='W')
tk.Label(window, text='Have balls dropped in?', bg='white', fg='black', font='none 12 bold').grid(row=5, column=0, sticky='W')
tk.Label(window, text='Balls scored in high goal', bg='white', fg='black', font='none 12 bold').grid(row=6, column=0, sticky='W')
tk.Label(window, text='Balls scored in low goal', bg='white', fg='black', font='none 12 bold').grid(row=7, column=0, sticky='W')
tk.Label(window, text='Rungs Climbed', bg='white', fg='black', font='none 12 bold').grid(row=8, column=0, sticky='W')
tk.Label(window, text='Num of Penalties', bg='white', fg='black', font='none 12 bold').grid(row=0, column=2, sticky='W')


#Make input objects for each data point
robotNumEntry = tk.Entry(window, width=20, bg='white')
robotNumEntry.grid(row=0, column=1, sticky='W') 

penaltiesEntry = tk.Entry(window, width=20, bg='white')
penaltiesEntry.grid(row=0, column=3, sticky='W') 

startingSpot = tk.StringVar(master)
startingSpot.set("1") # default value
startingSpotDropdown = tk.OptionMenu(master, startingSpot, "1", "2", "3")
startingSpotDropdown.grid(row=1, column=1, sticky='W') 

autoBallsEntry = tk.Entry(window, width=20, bg='white')
autoBallsEntry.grid(row=2, column=1, sticky='W') 

ballColor = tk.BooleanVar(value=False)
ballColorBox = tk.Checkbutton(window,variable=ballColor, onvalue=True, offvalue=False)
ballColorBox.grid(row=3, column=1, sticky='W') 

floorBalls = tk.BooleanVar(value=False)
floorBallsBox = tk.Checkbutton(window,variable=floorBalls, onvalue=True, offvalue=False)
floorBallsBox.grid(row=4, column=1, sticky='W') 

droppedBalls = tk.BooleanVar(value=False)
droppedBallsBox = tk.Checkbutton(window,variable=droppedBalls, onvalue=True, offvalue=False)
droppedBallsBox.grid(row=5, column=1, sticky='W') 

highBallsEntry = tk.Entry(window, width=20, bg='white')
highBallsEntry.grid(row=6, column=1, sticky='W') 

lowBallsEntry = tk.Entry(window, width=20, bg='white')
lowBallsEntry.grid(row=7, column=1, sticky='W') 

rungsClimbed = tk.StringVar(master)
rungsClimbed.set("1") # default value
rungsClimbedDropdown = tk.OptionMenu(master, rungsClimbed, "1", "2", "3","4")
rungsClimbedDropdown.grid(row=8, column=1, sticky='W') 

tk.Button(window, text='Add Team', width=20, command=addTeam).grid(row=9, column=0, sticky='W')

#spacer
tk.Label(window, text='', bg='white', fg='black', font='none 12 bold').grid(row=10, column=0, sticky='W')

#Add text for filters
tk.Label(window, text='Starting Spot', bg='white', fg='black', font='none 12 bold').grid(row=11, column=0, sticky='W')
tk.Label(window, text='Min Auto Balls', bg='white', fg='black', font='none 12 bold').grid(row=11, column=1, sticky='W')
tk.Label(window, text='Detect Ball Color?', bg='white', fg='black', font='none 12 bold').grid(row=11, column=2, sticky='W')
tk.Label(window, text='Pick up balls from floor?', bg='white', fg='black', font='none 12 bold').grid(row=11, column=3, sticky='W')
tk.Label(window, text='Have balls dropped in?', bg='white', fg='black', font='none 12 bold').grid(row=11, column=4, sticky='W')
tk.Label(window, text='Min Balls scored in high goal', bg='white', fg='black', font='none 12 bold').grid(row=11, column=5, sticky='W')
tk.Label(window, text='Min Balls scored in low goal', bg='white', fg='black', font='none 12 bold').grid(row=11, column=6, sticky='W')
tk.Label(window, text='Min Rungs Climbed', bg='white', fg='black', font='none 12 bold').grid(row=11, column=7, sticky='W')

#Input objects to filter data
startingSpotFilter = tk.StringVar(master)
startingSpotFilter.set("1") # default value
startingSpotDropdownFilter = tk.OptionMenu(master, startingSpotFilter, "1", "2", "3")
startingSpotDropdownFilter.grid(row=12, column=0, sticky='W') 

autoBallsFilter = tk.Entry(window, width=20, bg='white')
autoBallsFilter.grid(row=12, column=1, sticky='W') 

ballColorFilter = tk.BooleanVar(value=False)
ballColorBoxFilter = tk.Checkbutton(window,variable=ballColorFilter, onvalue=True, offvalue=False)
ballColorBoxFilter.grid(row=12, column=2, sticky='W') 

floorBallsFilter = tk.BooleanVar(value=False)
floorBallsBoxFilter = tk.Checkbutton(window,variable=floorBallsFilter, onvalue=True, offvalue=False)
floorBallsBoxFilter.grid(row=12, column=3, sticky='W') 

droppedBallsFilter = tk.BooleanVar(value=False)
droppedBallsBoxFilter = tk.Checkbutton(window,variable=droppedBallsFilter, onvalue=True, offvalue=False)
droppedBallsBoxFilter.grid(row=12, column=4, sticky='W') 

highBallsFilter = tk.Entry(window, width=20, bg='white')
highBallsFilter.grid(row=12, column=5, sticky='W') 

lowBallsFilter = tk.Entry(window, width=20, bg='white')
lowBallsFilter.grid(row=12, column=6, sticky='W') 

rungsClimbedFilter = tk.StringVar(master)
rungsClimbedFilter.set("1") # default value
rungsClimbedDropdownFilter = tk.OptionMenu(master, rungsClimbedFilter, "1", "2", "3","4")
rungsClimbedDropdownFilter.grid(row=12, column=7, sticky='W')

tk.Button(window, text='Find Teams', width=20, command=findTeams).grid(row=13, column=0, sticky='W')

output = tk.Text(window, width=50, height=20, wrap='word', background='white')
output.grid(row=14,column=0,columnspan=2,sticky='W')
window.mainloop()