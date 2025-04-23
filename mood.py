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
    

def save_moods(data):
    with open (FILENAME,"w") as file:
        json.dump(data,file,indent= 4)

def log_todays_mood():
    mood = input("How do feel today? e.g sad,angry,tired,okay,happy,excited,bored,suprised").strip().lower()
    today = str(date.today())

    data = load_moods()
    data[today]=mood
    save_moods(data)

    print("\nLogged Mood for {today}:{mood}")


def show_mood_chart():
    data = load_moods()
    if not data:
        print ("There is no data yet.")
        return
    
    dates= list(data.keys())
    moods = list(data.values())
    mood_levels= {
        "surprised":8,
        "bored":7,
        "excited":6,
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
    plt.yticks([1,2,3,4,5,6,7,8],["Sad","Tired","Happy","Angry","Okay","Surprised","Excited", "Bored"])
    plt.xticks(rotation= 45)
    plt.tight_layout()
    plt.savefig("mood_chart.png")
    print("Chart saved as:mood_chart.png")

# MAIN:
while True:
    print("\nWelcome to the Mood Tracker!")
    print("1. Log today's Mood")
    print("2. Show Mood Chart")
    print("3.Exit")

    choice = input("Choose an option between (1-3)")

    if choice == "1":
        log_todays_mood()
    elif choice == "2":
        show_mood_chart()
    elif choice =="3":
        print("Goodbye take care")
        break
    else:
        print ("Invaild choice Pick (1-3)") 
