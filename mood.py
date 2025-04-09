import json
from datetime import date
import matplotlib.pyplot as plt

FILENAME="mood.json"

def load_moods():
    try:
         with open(FILENAME,"r") as file:
            return json.load(file)
    except: 
        return{}
    




def show_mood_chart():
    data = load_moods
    if not data:
        print ("There is no data yet.")
        return
    
    dates= list(data.keys())
    moods = list(data.values())
    mood_levels= {
        "happy": 5,
        "okay": 4,
        "tired": 3,
        "angry": 2,
        "sad": 1,
    }
    yvalues= [mood_levels.get(mood,0)for mood in moods]


    plt.plot(dates,yvalues,marker="o")
    plt.title("Feelings Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mood Level")
    plt.yticks([1,2,3,4,5],["Sad","Tired","Happy","Angry","Okay"])