from doctest import master
import tkinter as tk
from tkinter import ttk
import json
from tracemalloc import start

window = tk.Tk()
window.title("Rapid React Scouting")
window.configure(background='white')
window.geometry("1000x750")


def add_team():  # called when submit button pressed; adds new team object to json
    f = open('TeamData.json')
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
        teams[robotNumEntry.get()]["timeTaken"] = int(timeTakenEntry.get())
        teams[robotNumEntry.get()]["numDataPoints"] = 1
        teams[robotNumEntry.get()]["penalties"] = int(penaltiesEntry.get())
    with open("TeamData.json", "w") as f:
        json.dump(teams, f)

def find_teams():
    output1.delete(1.0, 'end')
    with open("TeamData.json", "r") as f:
        teams = json.load(f)
    #for team in teams:
        #if (teams[team]["startingSpot"] == startingSpotFilter.get()) and (
                #(teams[team]['autoBalls'] / teams[team]['numDataPoints']) >= int(autoBallsFilter.get())) and (
                #teams[team]['ballColor'] == ballColorFilter.get()) and (
                #teams[team]['floorBalls'] == floorBallsFilter.get()) and (
                #teams[team]['droppedBalls'] == droppedBallsFilter.get()) and (
                #(teams[team]['highBalls'] / teams[team]['numDataPoints']) >= int(highBallsFilter.get())) and (
                #(teams[team]['lowBalls'] / teams[team]['numDataPoints']) >= int(lowBallsFilter.get())) and (
                #(teams[team]['rungsClimbed'] / teams[team]['numDataPoints']) >= int(rungsClimbedFilter.get())):
            #output1.insert('end', team + "               num penalties:" + teams[team]["penalties"] + '\n')



def find_team_number():
    output2.delete(1.0, 'end')
    with open("TeamData.json", "r") as f:
        teams = json.load(f)
    for team in teams:
        if team == searchByTeamNumFilter.get():
            output2.insert('end', 'startingSpot: ' + teams[team]["startingSpot"] + '\n')
            output2.insert('end', 'Auto Balls:: ' + str(teams[team]["autoBalls"] / teams[team]["numDataPoints"]) + '\n')
            output2.insert('end', 'Ball Color: ' + str(teams[team]["ballColor"]) + '\n')
            output2.insert('end', 'Floor Balls: ' + str(teams[team]["floorBalls"]) + '\n')
            output2.insert('end', 'Balls Dropped in: ' + str(teams[team]["droppedBalls"]) + '\n')
            output2.insert('end',
                           'Balls in High: ' + str(teams[team]["highBalls"] / teams[team]["numDataPoints"]) + '\n')
            output2.insert('end', 'Balls in low: ' + str(teams[team]["lowBalls"] / teams[team]["numDataPoints"]) + '\n')
            output2.insert('end',
                           'Rungs Climbed: ' + str(teams[team]["rungsClimbed"] / teams[team]["numDataPoints"]) + '\n')
            output2.insert('end', 'Penalties: ' + str(teams[team]["penalties"] / teams[team]["numDataPoints"]) + '\n')


# Add in text for all questions
tk.Label(window, text='Auto', bg='white', fg='black', font='none 12 bold').place(x=115, y=30, width=70, height=20)
tk.Label(window, text='Auto', bg='white', fg='black', font='none 12 bold').place(x=115, y=405, width=70, height=20)
tk.Label(window, text='Balls', bg='white', fg='black', font='none 12 bold').place(x=415, y=30, width=70, height=20)
tk.Label(window, text='Balls', bg='white', fg='black', font='none 12 bold').place(x=415, y=405, width=70, height=20)
tk.Label(window, text='Climb', bg='white', fg='black', font='none 12 bold').place(x=115, y=187, width=70, height=20)
tk.Label(window, text='Climb', bg='white', fg='black', font='none 12 bold').place(x=115, y=562, width=70, height=20)
tk.Label(window, text='Robot Num', bg='white', fg='black', font='none 12 bold').place(x=230, y=10, width=70, height=20)
tk.Label(window, text='Start Pos', bg='white', fg='black', font='none 12 bold').place(x=80, y=90, width=70, height=20)
tk.Label(window, text='Balls Scored', bg='white', fg='black', font='none 12 bold').place(x=60, y=110, width=90,
                                                                                         height=20)
tk.Label(window, text='Detect Color?', bg='white', fg='black', font='none 12 bold').place(x=350, y=90, width=100,
                                                                                          height=20)
tk.Label(window, text='Ground Intake?', bg='white', fg='black', font='none 12 bold').place(x=350, y=110, width=100,
                                                                                           height=20)
tk.Label(window, text='Driver Intake?', bg='white', fg='black', font='none 12 bold').place(x=350, y=130, width=100,
                                                                                           height=20)
tk.Label(window, text='Balls in high goal', bg='white', fg='black', font='none 12 bold').place(x=350, y=150, width=100,
                                                                                               height=20)
tk.Label(window, text='Balls in low goal', bg='white', fg='black', font='none 12 bold').place(x=350, y=170, width=100,
                                                                                              height=20)
tk.Label(window, text='Rungs Climbed', bg='white', fg='black', font='none 12 bold').place(x=50, y=267, width=100,
                                                                                          height=20)
tk.Label(window, text='Time Taken', bg='white', fg='black', font='none 12 bold').place(x=80, y=287, width=70, height=20)
tk.Label(window, text='Team List', bg='white', fg='black', font='none 12 bold').place(x=765, y=10, width=70, height=20)
tk.Label(window, text='Specific Team Info', bg='white', fg='black', font='none 12 bold').place(x=725, y=385, width=150,
                                                                                               height=20)
tk.Label(window, text='Penalties', bg='white', fg='black', font='none 12 bold').place(x=350, y=190, width=100,
                                                                                      height=20)

# Make input objects for each data point
robotNumEntry = tk.Entry(window, width=20, bg='white')
robotNumEntry.place(x=300, y=10, width=70, height=20)

penaltiesEntry = tk.Entry(window, width=20, bg='white')
penaltiesEntry.place(x=450, y=190, width=100, height=20)

startingSpot = tk.StringVar(master)
startingSpot.set("1")  # default value
startingSpotDropdown = tk.OptionMenu(master, startingSpot, "1", "2", "3")
startingSpotDropdown.place(x=150, y=90, width=70, height=20)

autoBallsEntry = tk.Entry(window, width=90, bg='white')
autoBallsEntry.place(x=150, y=110, width=90, height=20)

ballColor = tk.BooleanVar(value=False)
ballColorBox = tk.Checkbutton(window, variable=ballColor, onvalue=True, offvalue=False)
ballColorBox.place(x=450, y=90, width=100, height=20)

floorBalls = tk.BooleanVar(value=False)
floorBallsBox = tk.Checkbutton(window, variable=floorBalls, onvalue=True, offvalue=False)
floorBallsBox.place(x=450, y=110, width=100, height=20)

droppedBalls = tk.BooleanVar(value=False)
droppedBallsBox = tk.Checkbutton(window, variable=droppedBalls, onvalue=True, offvalue=False)
droppedBallsBox.place(x=450, y=130, width=100, height=20)

highBallsEntry = tk.Entry(window, width=70, bg='white')
highBallsEntry.place(x=450, y=150, width=70, height=20)

lowBallsEntry = tk.Entry(window, width=70, bg='white')
lowBallsEntry.place(x=450, y=170, width=70, height=20)

rungsClimbed = tk.StringVar(master)
rungsClimbed.set("1")  # default value
rungsClimbedDropdown = tk.OptionMenu(master, rungsClimbed, "1", "2", "3", "4")
rungsClimbedDropdown.place(x=150, y=267, width=100, height=20)

timeTakenEntry = tk.Entry(window, width=20, bg='white')
timeTakenEntry.place(x=150, y=287, width=70, height=20)

tk.Button(window, text='Add Team', width=20, command=add_team).place(x=260, y=350, width=80, height=20)

# spacer
tk.Label(window, text='', bg='white', fg='black', font='none 12 bold').grid(row=10, column=0, sticky='W')

# Add text for filters
tk.Label(window, text='Start Pos', bg='white', fg='black', font='none 12 bold').place(x=80, y=465, width=70, height=20)
tk.Label(window, text='Min Balls Scored', bg='white', fg='black', font='none 12 bold').place(x=50, y=485, width=100,
                                                                                             height=20)
tk.Label(window, text='Detect Color?', bg='white', fg='black', font='none 12 bold').place(x=350, y=465, width=100,
                                                                                          height=20)
tk.Label(window, text='Ground Intake?', bg='white', fg='black', font='none 12 bold').place(x=350, y=485, width=100,
                                                                                           height=20)
tk.Label(window, text='Driver Intake?', bg='white', fg='black', font='none 12 bold').place(x=350, y=505, width=100,
                                                                                           height=20)
tk.Label(window, text='Min Balls in High', bg='white', fg='black', font='none 12 bold').place(x=350, y=525, width=100,
                                                                                              height=20)
tk.Label(window, text='Min Balls in Low', bg='white', fg='black', font='none 12 bold').place(x=350, y=545, width=100,
                                                                                             height=20)
tk.Label(window, text='Min Rungs Climbed', bg='white', fg='black', font='none 12 bold').place(x=30, y=642, width=120,
                                                                                              height=20)
tk.Label(window, text='Time to Finish', bg='white', fg='black', font='none 12 bold').place(x=30, y=662, width=120,
                                                                                           height=20)
tk.Label(window, text='Penalties', bg='white', fg='black', font='none 12 bold').place(x=350, y=565, width=100,
                                                                                      height=20)

# Input objects to filter data
startingSpotFilter = tk.StringVar(master)
startingSpotFilter.set("1")  # default value
startingSpotDropdownFilter = tk.OptionMenu(master, startingSpotFilter, "1", "2", "3")
startingSpotDropdownFilter.place(x=150, y=465, width=70, height=20)

autoBallsFilter = tk.Entry(window, width=20, bg='white')
autoBallsFilter.place(x=150, y=485, width=100, height=20)

ballColorFilter = tk.BooleanVar(value=False)
ballColorBoxFilter = tk.Checkbutton(window, variable=ballColorFilter, onvalue=True, offvalue=False)
ballColorBoxFilter.place(x=450, y=465, width=100, height=20)

floorBallsFilter = tk.BooleanVar(value=False)
floorBallsBoxFilter = tk.Checkbutton(window, variable=floorBallsFilter, onvalue=True, offvalue=False)
floorBallsBoxFilter.place(x=450, y=485, width=100, height=20)

droppedBallsFilter = tk.BooleanVar(value=False)
droppedBallsBoxFilter = tk.Checkbutton(window, variable=droppedBallsFilter, onvalue=True, offvalue=False)
droppedBallsBoxFilter.place(x=450, y=505, width=100, height=20)

highBallsFilter = tk.Entry(window, width=20, bg='white')
highBallsFilter.place(x=450, y=525, width=100, height=20)

lowBallsFilter = tk.Entry(window, width=20, bg='white')
lowBallsFilter.place(x=450, y=545, width=100, height=20)

rungsClimbedFilter = tk.StringVar(master)
rungsClimbedFilter.set("1")  # default value
rungsClimbedDropdownFilter = tk.OptionMenu(master, rungsClimbedFilter, "1", "2", "3", "4")
rungsClimbedDropdownFilter.place(x=150, y=642, width=120, height=20)

penaltiesFilter = tk.Entry(window, width=20, bg='white')
penaltiesFilter.place(x=450, y=565, width=100, height=20)

timeToFinishFilter = tk.Entry(window, width=20, bg='white')
timeToFinishFilter.place(x=150, y=662, width=120, height=20)

searchByTeamNumFilter = tk.Entry(window, width=20, bg='white')
searchByTeamNumFilter.place(x=300, y=380, width=200, height=20)

tk.Button(window, text='Search by Team Number', width=20, command=find_team_number).place(x=100, y=380, width=200,
                                                                                          height=20)
tk.Button(window, text='Find Teams', width=20, command=find_teams).place(x=260, y=725, width=80, height=20)

output1 = tk.Text(window, width=50, height=20, wrap='word', background='white')
output1.place(x=610, y=30, width=380, height=335)

output2 = tk.Text(window, width=50, height=20, wrap='word', background='white')
output2.place(x=610, y=405, width=380, height=335)

# add dividers (separator widgets)
yaxis = tk.ttk.Separator(window, orient='vertical')
yaxis.place(x=600, width=2, height=750)

xaxis = tk.ttk.Separator(window, orient='horizontal')
xaxis.place(y=375, width=1000, height=2)

q2v = tk.ttk.Separator(window, orient='vertical')
q2v.place(x=300, y=30, width=2, height=320)

q2h = tk.ttk.Separator(window, orient='horizontal')
q2h.place(x=0, y=187, width=300, height=2)

q3h = tk.ttk.Separator(window, orient='horizontal')
q3h.place(x=0, y=562, width=300, height=2)

q3v = tk.ttk.Separator(window, orient='vertical')
q3v.place(x=300, y=400, width=2, height=320)

window.mainloop()
