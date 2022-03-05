from doctest import master
import tkinter as tk
import json

window = tk.Tk()
window.title("Rapid React Scouting ")
window.configure(background='white')

def addTeam(): #called when submit button pressed; adds new team object to json
    with open("TeamData.json", "r") as f:
        teams = json.load(f)
    if str(robotNumEntry.get()) in teams:
        teams[robotNumEntry.get()]["highBalls"] += int(highBallsEntry.get())
        teams[robotNumEntry.get()]["lowBalls"] += int(lowBallsEntry.get())
        teams[robotNumEntry.get()]["rungsClimbed"] += int(rungsClimbed.get())
        teams[robotNumEntry.get()]["numDataPoints"] += 1
    else:
        teams[robotNumEntry.get()] = {}
        teams[robotNumEntry.get()]["startingSpot"] = startingSpot.get()
        teams[robotNumEntry.get()]["autoBalls"] = autoBallsEntry.get()
        teams[robotNumEntry.get()]["ballColor"] = ballColor.get()
        teams[robotNumEntry.get()]["floorBalls"] = floorBalls.get()
        teams[robotNumEntry.get()]["droppedBalls"] = droppedBalls.get()
        teams[robotNumEntry.get()]["highBalls"] = int(highBallsEntry.get())
        teams[robotNumEntry.get()]["lowBalls"] = int(lowBallsEntry.get())
        teams[robotNumEntry.get()]["rungsClimbed"] = int(rungsClimbed.get())
        teams[robotNumEntry.get()]["numDataPoints"] = 0

    with open("TeamData.json", "w") as f:
        json.dump(teams, f)

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

#Make input objects for each data point
robotNumEntry = tk.Entry(window, width=20, bg='white')
robotNumEntry.grid(row=0, column=1, sticky='W') 

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


window.mainloop()