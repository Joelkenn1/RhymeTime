
import random
import pronouncing as retrieve
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
import re
import smtplib, ssl
from email.message import EmailMessage
from email.header import Header

# mydb = mysql.connector.connect(
#   host= "Your Hostname (Ex:111.0.0.1)",
#   user = "Your Username (Ex:root)",
#   password= "Your Password",
#   database = "RhymeDatabase"
  
# )

mydb = mysql.connector.connect(
  host= "127.0.0.1",
  user = "root",
  password= "Ckenney1",
  database = "RhymeDatabase"
  
)

# auto commits every query
mydb.autocommit = True

# the cursor is used to execute queries 
mycursor = mydb.cursor()


window = tk.Tk()
window.attributes('-fullscreen', True)
window.title("RhymeTime")
window.configure(bg="light blue")


# The fonts are subject to change
# The text variables can be reused across multiple methods
mainFrame = tk.Frame(window, background="alice blue", borderwidth=3)
mainHeader = tk.Label(mainFrame, bg="#00bfff")
mainHeader.pack(padx=1, pady=1)

mainText = tk.Label(window, font=("Arial", 28), bg="light blue", fg="#191970")
leaderText = tk.Label(window)


# The button variables can be reused across multiple methods
loginButton = tk.Button(window, text="Login", font=("Arial" ,25, "bold"), bg="#191970", fg="white")
logoutButton = tk.Button(window, text="Logout", font=("Arial" ,25, "bold"), bg="#191970", fg="white")
createButton = tk.Button(window, text="Create A RhymeTime Account", font=("Arial" ,25, "bold"), bg="#191970", fg="white")
startGameButton = tk.Button(window, text="Start Game", font=("Arial" ,25,"bold"), bg="#191970", fg="white")
replayGameButton = tk.Button(window, text="Replay Game", font=("Arial" ,25,"bold"), bg="#191970", fg="white")
startTimeButton = tk.Button(window, text="Start Time", font=("Arial" ,25,"bold"), bg="#191970", fg="white")
returnHomeButton = tk.Button(window, text="Return Home", font=("Arial" ,25,"bold"), bg="#191970", fg="white")
leadersButton = tk.Button(window, text="Leaderboard", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white",width=18, height=2)
quitButton = tk.Button(window, text="Quit Game", font=("Arial" ,25,"bold"), bg="#191970", fg="white")
updateLoginButton = tk.Button(window, text="Personal Information", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white",width=18, height=2)
changeUpdateButton = tk.Button(window, text="Next", font=("Arial" ,28,"bold"), bg="#191970", fg="white")
updateCheckButton = tk.Button(window, text="Confirm Update", font=("Arial" ,26,"bold"), bg="#191970", fg="white")
reportButton = tk.Button(window, text="Report An Issue", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white",width=18, height=2)
feedbackButton = tk.Button(window, text="Provide Feedback", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white", width=18, height=2)
reviewsButton = tk.Button(window, text="Ratings & Reviews", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white",width=18, height=2)
badgesButton = tk.Button(window, text="Badge Collection", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white",width=18, height=2)
statsButton = tk.Button(window, text="Personal Statistics", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white",width=18, height=2)
moreButton = tk.Button(window, text="More Options", font=("Arial" ,25,"bold"), bg="#191970", fg="white")
deleteButton = tk.Button(window, text="Delete My Account", font=("Arial" ,25,"bold"), bg="#191970", fg="white")



# The text input variables can be reused across multiple methods
fname = tk.StringVar()
lname = tk.StringVar()
email = tk.StringVar()
logname = tk.StringVar()
logpass = tk.StringVar()
rhyme_input = tk.StringVar()



# The text prompt variables can be reused across multiple methods
fname_Frame = tk.Frame(window, background="light blue")
fname_entry = tk.Entry(fname_Frame, textvariable = fname, font=("Arial", 17, "normal"), fg="#191970")  
fname_prompt = tk.Label(fname_Frame, text = "First Name: ", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
fname_prompt.pack(side = tk.LEFT)
fname_entry.pack(side = tk.RIGHT)


lname_Frame = tk.Frame(window, background="light blue")
lname_entry = tk.Entry(lname_Frame, textvariable = lname, font=("Arial", 17, "normal"), fg="#191970")
lname_prompt = tk.Label(lname_Frame, text = "Last Name: ", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
lname_prompt.pack(side = tk.LEFT)
lname_entry.pack(side = tk.RIGHT)


email_Frame = tk.Frame(window, background="light blue")
email_entry = tk.Entry(email_Frame, textvariable = email, font=("Arial", 17, "normal"), fg="#191970")
email_prompt = tk.Label(email_Frame, text = "Email Address: ", font=("Arial", 20,"bold"), bg = "light blue",fg="#191970")
email_prompt.pack(side = tk.LEFT)
email_entry.pack(side = tk.RIGHT)


username_Frame = tk.Frame(window, background="light blue")
username_entry = tk.Entry(username_Frame, textvariable = logname, font=("Arial", 17, "normal"), fg="#191970")    
username_prompt = tk.Label(username_Frame, text = "Username: ", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
username_prompt.pack(side = tk.LEFT)
username_entry.pack(side = tk.RIGHT)


password_Frame = tk.Frame(window, background="light blue")
hidePass = tk.Button(window, text="Show Password", font=("Arial" ,10,"bold"), bg="#191970", fg="white")
password_entry = tk.Entry(password_Frame, textvariable = logpass, font=("Arial", 17, "normal"), fg="#191970")    
password_prompt = tk.Label(password_Frame, text = "Password: ", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
password_prompt.pack(side = tk.LEFT)
password_entry.pack(side = tk.RIGHT)


score_Frame = tk.Frame(window, background="light blue")
score_display = tk.Label(score_Frame, text = "0", font=("Arial", 30, "bold"), bg = "light blue",fg="#191970")
score_prompt = tk.Label(score_Frame, text = "Score: ", font=("Arial", 30,"bold"), bg = "light blue",fg="#191970")
score_prompt.pack(side = tk.LEFT)
score_display.pack(side = tk.RIGHT)


time_Frame = tk.Frame(window, background="light blue")
time_prompt = tk.Label(time_Frame, text = "Time: ", font=("Arial", 25,"bold"), bg = "light blue",fg="#191970")
time_display = tk.Label(time_Frame, text = "50", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
time_prompt.pack(side = tk.LEFT)
time_display.pack(side = tk.RIGHT)


correct_Frame = tk.Frame(window, background="light blue")
correct_prompt = tk.Label(correct_Frame, text = "Correct Rhymes: ", font=("Arial", 25,"bold"), bg = "light blue",fg="#191970")
display_correct = tk.Label(correct_Frame, text = "None", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
correct_prompt.pack(side = tk.LEFT)
display_correct.pack(side = tk.RIGHT)

rhyme_Frame = tk.Frame(window, background="light blue")
rhyme_prompt = tk.Label(rhyme_Frame, text = "Rhyme: ", font=("Arial", 25,"bold"), bg = "light blue",fg="#191970")
rhyme_entry = tk.Entry(rhyme_Frame, textvariable = rhyme_input, font=("Arial", 17, "normal"), fg = "#191970")
rhyme_prompt.pack(side = tk.LEFT)
rhyme_entry.pack(side = tk.RIGHT)

# game conditions/variables
createFirst = []

user = [" "]
username_values = []
pass_ = [" "]
contact = [" "]
email_values = []
first = [" "]
last = [" "]

top_players = []
low_leader = [" "]


badges_earned = []

# get all game badges
game_badges = []
badge_query = "select * from Badges"
mycursor.execute(badge_query)
results = mycursor.fetchall()


for i in range(0, len(results)):
    game_badges.append([results[i][0], results[i][1]])



position = [" "]
logged = [False]
gameloop = [False]

totalTime = [0]
totalInputs = [0]
time = [0]

correct_rhymes = []
correct_streak = [0]
incorrect_count = [0]
rhymeList = []

score = [0]



random_words = ["add", "aid", "air", "age", "act", "aim", "axe", "art", "ace", "across", "admit", "ache", "annoy", "alarm",
                "arks", "able", "about", "abuse", "ago", "back", "bail", "bag", "bake","ball", "ban", "bad", "bald", "box", "bark", 
                "bar", "beat", "bench", "beg", "best", "blade", "bit", "blue", "buck", "but", "bush", "burn", "bunk", "bunch", 
                "boat","bug", "buy", "bowl", "cab", "cage", "crave", "call", "calm", "came", "can", "car", "care", "cat", "catch",
                "caught","chair", "cheap", "coat", "clean", "cream", "cheat", "chest","choose", "cruise", "climb", "crime", "cloud",
                "clip","churn", "cook", "cool", "cold", "crack", "cup", "curl", "cute", "dam", "dance", "dank", "dash", "dawn", 
                "day", "daze", "dead", "dear", "deed", "den", "dent", "die", "dig", "dill", "dime", "dine", "doe", "dog", "dirt", 
                "doll", "dome", "dot", "drain", "draw", "drill", "drum", "dry", "duck","earn", "east", "eat", "eight", "eye","ease",
                "ever", "each", "enough", "eggs","emit", "erie", "elect", "effect","eagle", "exalt", "exert", "explain", "erase", 
                "earth", "face", "fact", "fast", "fall", "field", "fire", "fly","float", "free", "flop", "fan","find", "flaw", 
                "fond", "font", "far", "fat", "fate", "feed", "fence", "foe", "fought", "feed", "gag", "gauge", "game", "gang",
                "group", "gel", "had", "germ","guess","grain","grit", "gland", "good", "grow", "goal", "gold", "grant", "grave", 
                "guy", "gum", "guest", "hail", "hall", "ham", "hare", "hay", "hate", "head", "hike", "hang", "horn", "host","hill",
                "hide", "hold", "hole", "home", "hook", "hope", "hug", "ice", "inch", "ink", "its", "itch", "isle", "inner", "ideal",
                "import", "impose","infect", "ignite", "inside", "intend", "invent", "insist", "insert", "include","inform", "ill",
                "jab", "jack", "jade", "jail", "jam", "jaunt", "jaw", "jeep", "jeer", "jeans", "jet", "jig", "job", "joke", "joy", 
                "juice","jumbo", "jump", "jar", "jive", "know", "kind", "kneel", "kin","keen", "keep", "kick", "knit", "knob",
                "key","kid", "king", "knew", "knock", "kiss", "kit", "kite", "knack","knight", "knot", "lamp", "leak", "lid", "loan",
                "loss", "lack","lace", "lad", "lamb", "land", "lane", "last", "led","learn", "lick", "lie", "log", "loot","lurk",  
                "link", "made", "mad", "main", "male", "map", "march", "meal", "melt", "muse", "miss", "mix", "mud", "much", "more",
                "mule", "mere", "mile", "moon", "meek", "maze","nerve", "news", "notes", "nurse", "nod", "nope", "none", "nab",    
                "nail", "name", "neat", "neck", "need", "net", "new", "nest", "nice", "niece", "now", "nest", "oak", "oats", "odd", 
                "occur", "one", "oppose", "ordeal", "over", "ozone", "omit", "ooze", "owl", "ode", "ounce", "oil", "old", "ouch",  
                "own", "out", "ought", "pack", "pad", "page", "paid", "paint", "pain", "pant", "park", "part", "pet", "peg", "pen",
                "pew", "pitch", "plant", "plate", "poll", "pool", "pound", "pour", "print", "prize", "quack", "quad", "quit", 
                "quake", "quail", "queen", "queue", "quest", "quick", "quote", "race", "rad", "rag", "rage", "raid", "raise", 
                "rake", "rear", "reed", "reef", "reap", "reign", "rose", "rally", "rise", "room", "rule", "rope", "ring","rats",
                "rail","ride", "right", "roam", "roast", "rob", "rock", "role", "row", "sack", "sag","said","same","sand","school", 
                "seal", "shade", "shark", "shed", "side", "slay", "slug", "snail", "smell", "snack", "son","sore", "spam",    
                "spread","still", "stone", "sword", "sewer", "sweat", "sweet", "swear", "tab", "tack", "tale", "talk","tall", 
                "tank", "tart","term", "thank", "thin", "time", "toad", "toast", "toy", "trade", "trail", "train", "treat","tree", 
                "try", "truth", "tune", "van", "vine", "vase",  "verge", "vein", "vest", "view", "vile", "vast", "vice", "veil",   
                "vow", "vouch", "vote", "vent", "viking", "very", "vape", "verse", "vet", "waist", "wall", "walk", "wine","won",  
                "weep", "weak", "white", "west", "wet", "wire", "wit", "wipe", "wins", "woe", "woke", "wakes", "wrote", "worn",  
                "wow", "yield", "yell", "yawn", "take", "yet", "yikes", "youth", "yuck", "yacht", "year","yearn", "young","yard",
                "yes", "your", "zip", "zoom", "zeal", "zone" ]


        






# A method for password inputs
def hide():
    if(hidePass["text"] == "Hide Password"):
        hidePass.config(text = "Show Password")
        password_entry.config(show = "*")

    elif(hidePass["text"] == "Show Password"):
        hidePass.config(text = "Hide Password")
        password_entry.config(show = "")
        
hidePass.config(command=hide)




def createAccountPage():
  
    for widget in window.winfo_children():
        widget.pack_forget()
        

    # Get all the usernames of players to prevent duplicates
    username_query = "select Username from Users"
    mycursor.execute(username_query)
    
    usernames = mycursor.fetchall()
    
    username_values.clear()
    for i in usernames:
        username_values.append(i[0])
    
    
    
    # Get all the emails of players to prevent duplicates
    email_query = "select Email from Users"
    mycursor.execute(email_query)
    
    emails = mycursor.fetchall()
    
    email_values.clear()
    for i in emails:
        email_values.append(i[0])

    returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)

    mainHeader.config(text="RhymeTime", font=("Arial", 65, "bold"))
    mainFrame.pack(pady=(13,8))
    
    mainText.config(text="A RhymeTime Account Is Required For Gameplay.", font=("Arial", 32, "bold"))
    mainText.pack(pady=(8,15))

    
    fname_Frame.pack(pady=(15,15))
    lname_Frame.pack(pady=(15,15))
    email_Frame.pack(pady=(15,15))
    username_Frame.pack(pady=(15,15))
    password_Frame.pack(pady=(15,0))

    hidePass.pack(pady=(6,0))
    
    loginButton.pack(pady=(27,0))
    loginButton.config(text="Create Account")

    

    createFirst.append(True)



def loginPage():
    
    """ Displays the Login Page """
    for widget in window.winfo_children():
        widget.pack_forget()


    # Get all the usernames of players to prevent duplicates
    username_query = "select Username from Users"
    mycursor.execute(username_query)
    
    usernames = mycursor.fetchall()
    
    username_values.clear()
    for i in usernames:
        username_values.append(i[0])
    
    
    
    # Get all the emails of players to prevent duplicates
    email_query = "select Email from Users"
    mycursor.execute(email_query)
    
    
    emails = mycursor.fetchall()
    
    email_values.clear()
    for i in emails:
        email_values.append(i[0])


    

    if(len(createFirst) > 0):
        
        username = logname.get()
        password = logpass.get()
        fn = fname.get()
        ln = lname.get()
        em = email.get()

        em_check = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        
        if(username_values.__contains__(username)):

            returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)
            mainFrame.pack(pady=(13,8))
    
            mainText.config(text="The Inserted Username Is Taken.", font=("Arial", 32, "bold"))
            mainText.pack(pady=(8,15))

            fname_Frame.pack(pady=(15,15))
            lname_Frame.pack(pady=(15,15))
            email_Frame.pack(pady=(15,15))
            username_Frame.pack(pady=(15,15))
            password_Frame.pack(pady=(15,0))
        
            hidePass.pack(pady=(6,0))
            
            loginButton.pack(pady=(27,0))
            loginButton.config(text="Create Account")


        elif(email_values.__contains__(em)):

            returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)
            mainFrame.pack(pady=(13,8))
    
            mainText.config(text="The Inserted Email Is Taken.", font=("Arial", 32, "bold"))
            mainText.pack(pady=(8,15))

            fname_Frame.pack(pady=(15,15))
            lname_Frame.pack(pady=(15,15))
            email_Frame.pack(pady=(15,15))
            username_Frame.pack(pady=(15,15))
            password_Frame.pack(pady=(15,0))
        
            hidePass.pack(pady=(6,0))
            
            loginButton.pack(pady=(30,0))
            loginButton.config(text="Create Account")

    
        elif(password == "" or  username == "" or fn == "" or ln == "" or em == ""):

            returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)
            mainFrame.pack(pady=(13,8))
    
            mainText.config(text="Please Fill In All Entries.", font=("Arial", 32, "bold"))
            mainText.pack(pady=(8,15))

            fname_Frame.pack(pady=(15,15))
            lname_Frame.pack(pady=(15,15))
            email_Frame.pack(pady=(15,15))
            username_Frame.pack(pady=(15,15))
            password_Frame.pack(pady=(15,0))
        
            hidePass.pack(pady=(6,0))
            
            loginButton.pack(pady=(30,0))
            loginButton.config(text="Create Account")

        
        elif(re.match(em_check, em) == None):

            returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)
            mainFrame.pack(pady=(13,8))
    
            mainText.config(text="Please Insert A Valid Email.", font=("Arial", 32, "bold"))
            mainText.pack(pady=(8,15))

            fname_Frame.pack(pady=(15,15))
            lname_Frame.pack(pady=(15,15))
            email_Frame.pack(pady=(15,15))
            username_Frame.pack(pady=(15,15))
            password_Frame.pack(pady=(15,0))
        
            hidePass.pack(pady=(6,0))
            
            loginButton.pack(pady=(30,0))
            loginButton.config(text="Create Account")

        
        else:
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            fname_entry.delete(0, tk.END)
            lname_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            
            info = (fn, ln, em, username, password, "0%")
            create_query = "insert into Users values(%s, %s, %s, %s, %s, 0, 1, 0, 0, 0, 0, 0, %s, 0)"
            mycursor.execute(create_query, info)

            info2 = (username, "False", "False", "False", "False")
            create2_query = "insert into Single_Game (Username, Learned, Well_Done, APTR, Master_Class) values(%s, %s, %s, %s, %s)"
            mycursor.execute(create2_query, info2)

            first[0] = fn
            last[0] = ln
            contact[0] = em
    
            username_values.append(username)
            email_values.append(em)

            returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)
            mainHeader.config(text="RhymeTime", font=("Arial", 90, "bold"))
            mainFrame.pack(pady=(90,8))
        
                
            mainText.config(text="Enter Your RhymeTime Credentials Below.", font=("Arial", 34,"bold"))
            mainText.pack(pady=(20,0))
        
            username_Frame.pack(pady=(15,15))
            password_Frame.pack(pady=(15,0))
            hidePass.pack(pady=(6,0))
        
            startGameButton.config(command=startGame)
            startGameButton.pack(pady=(17,0))
            

    else:
        returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)
        mainHeader.config(text="RhymeTime", font=("Arial", 90, "bold"))
        mainFrame.pack(pady=(90,8))
    
            
        mainText.config(text="Enter Your RhymeTime Credentials Below.", font=("Arial", 34, "bold"))
        mainText.pack(pady=(20,0))
    
        username_Frame.pack(pady=(15,15))
        password_Frame.pack(pady=(15,0))
        hidePass.pack(pady=(6,0))
        
        startGameButton.config(command=startGame)
        startGameButton.pack(pady=(17,0))


            

 
def login_verify():

    if(logged[0] == True):
        return
        
    else:
        createFirst.clear()
        username = logname.get()
        user[0] = username
        password = logpass.get()
        pass_[0] = password

        info = (username, )
        
        get_info = "select First_Name, Last_Name, Email from Users where Username = %s"
        mycursor.execute(get_info, info)
        set_info = mycursor.fetchall()
        
        if(username_values.__contains__(username)):
    
            password_query = "select Password_ from Users where Username = %s"
            mycursor.execute(password_query, info)
    
            password_verify = mycursor.fetchone()
    
            
            if(password == str(password_verify[0])):
                
                for i in window.winfo_children():
                    logged[0] = True
                    first[0] = set_info[0][0]
                    last[0] = set_info[0][1]
                    contact[0] = set_info[0][2]
    
            elif(password != str(password_verify[0])):
                password_entry.delete(0, tk.END)
                password_entry.insert(0, "Incorrect Password")
                loginPage()
    
        else:
            
            username_entry.delete(0, tk.END)
            username_entry.insert(0, "Unknown Player")
            loginPage()




def startGame():
    
  login_verify()

  if (logged[0] == True):
      
      for widget in window.winfo_children():
            widget.pack_forget()


      # Initially set the Leaderboard
      leaderboard_query = "select Username, High_Score from Users order by High_Score desc limit 5"
      mycursor.execute(leaderboard_query)
      leaders = mycursor.fetchall()

      top_players.clear()
      for i in leaders:
         top_players.append(i[0])

         if(i[0] == user[0]):
             position[0] = top_players.index(i[0]) + 1

      low_leader[0] = top_players[len(top_players) - 1]

      
      score[0] = 0
      totalInputs[0] = 0
      totalTime[0] = 0
      correct_streak[0] = 0
      incorrect_count[0] = 0
      
      rhyme_entry.delete(0, tk.END)

      score_display.config(text="0")
      score_Frame.pack(side = tk.TOP, anchor = tk.CENTER)
    
    
    
      mainText.config(text = "Time Is Moving Fast! Before It Runs Out, Can You Enter\n 3 Words That Rhyme With Each Randomly Generated Word? ", font = ("Arial", 32, "bold"))
        
    
      mainText.pack(pady=(160, 25))

      time_display.config(text="50")
      time_Frame.pack()
      startTimeButton.pack(pady=(40,0))

      returnHomeButton.pack(pady=(25,0))


def EndGame():
    
    gameloop[0] = False
    
    for i in window.winfo_children():
        i.pack_forget()


    mainHeader.config(text="Game Over!" ,font=("Arial", 130, "bold"))
    mainFrame.pack(pady=(120, 0))

    time_display.config(text = " ")

    
    name = (user[0],)
    
    # get/update high score
    score_query = "select High_Score from Users where Username = %s"
    mycursor.execute(score_query, name)
    current_high = mycursor.fetchone()

    if(score[0] > current_high[0]):
        mainText.config(text = "New High Score: " + str(score[0]), font=("Arial", 30, "bold"))
        mainText.pack(pady=10)

        high_info = (str(score[0]), user[0])
        high_query = "update Users set High_Score = %s where Username = %s"
        mycursor.execute(high_query, high_info)


    elif(score[0] <= current_high[0]):
        mainText.config(text = "Your Score: " + str(score[0]) + " | Your Highest Score: " + str(current_high[0]), font=("Arial", 30,"bold"), fg="#191970")
        mainText.pack(pady=(16,0))


    # get/update consecutive rhymes streak
    streak_query = "select Rhyme_Streak from Users where Username = %s"
    mycursor.execute(streak_query, name)
    current_streak = mycursor.fetchone()

    if(correct_streak[0] > current_streak[0]):
        info = (str(correct_streak[0]), user[0])
        newStreak = "update Users set Rhyme_Streak = %s where Username = %s"
        mycursor.execute(newStreak, info)

    
    # check/update single game badges
    singles_query = "select Learned, Well_Done, APTR, Master_Class from Single_Game where Username = %s"
    mycursor.execute(singles_query, name)
    singles = mycursor.fetchall()


    if(score[0] >= 20 and incorrect_count[0] <= 3 and singles[0][3] == "False"):
        query = "update Single_Game set Master_Class = 'True' where Username = %s"
        mycursor.execute(query, name)

    elif(score[0] >= 15 and incorrect_count[0] <= 3 and singles[0][2] == "False"):
        query = "update Single_Game set APTR = 'True' where Username = %s"
        mycursor.execute(query, name)

    elif(score[0] >= 10 and incorrect_count[0] <= 3 and singles[0][1] == "False"):
        query = "update Single_Game set Well_Done = 'True' where Username = %s"
        mycursor.execute(query, name)

    elif(score[0] >= 5 and incorrect_count[0] <= 3 and singles[0][0] == "False"):
        query = "update Single_Game set Learned = 'True' where Username = %s"
        mycursor.execute(query, name)



    # update total score in the database
    scoreSum_query = "select Score_Sum from Users where Username = %s"
    mycursor.execute(scoreSum_query, name)
    scoreSum = mycursor.fetchone()

    scoreTemp = scoreSum[0]
    scoreTemp += score[0]

    score_info = (str(scoreTemp), user[0])
    scoreSum_update = "update Users set Score_Sum = %s where Username = %s"
    mycursor.execute(scoreSum_update, score_info)

    
    # update total time in the database
    timeSum_query = "select Time_Sum from Users where Username = %s"
    mycursor.execute(timeSum_query, name)
    timeSum = mycursor.fetchone()

    timeTemp = timeSum[0]
    timeTemp += totalTime[0]

    time_info = (str(timeTemp), user[0])
    timeSum_update = "update Users set Time_Sum = %s where Username = %s"
    mycursor.execute(timeSum_update, time_info)

    
    # update total inputs in the database 
    inputs_query = "select Input_Count from Users where Username = %s"
    mycursor.execute(inputs_query, name)
    inputCount = mycursor.fetchone()

    inputTemp = inputCount[0]
    inputTemp += totalInputs[0]

    input_info = (str(inputTemp), user[0])
    inputCount_update = "update Users set Input_Count = %s where Username = %s"
    mycursor.execute(inputCount_update, input_info)

    # calculate rhyming accuracy
    if(scoreTemp == 0):
        accuracy_info = (str(0)+"%", user[0])
        accuracy_update = "update Users set Rhyming_Accuracy = %s where Username = %s"
        mycursor.execute(accuracy_update, accuracy_info)

    else:
        accuracy = round(scoreTemp / (inputTemp/3), 1)
        accuracy_info = (str(accuracy * 100)+"%", user[0])
        accuracy_update = "update Users set Rhyming_Accuracy = %s where Username = %s"
        mycursor.execute(accuracy_update, accuracy_info)

     # calculate average time per word
    if (scoreTemp == 0):
        avgtime_info = (str(8), user[0])
        avgtime_update = "update Users set Average_Time = %s where Username = %s"
        mycursor.execute(avgtime_update, avgtime_info)
        
    elif (timeTemp / (scoreTemp*3) > 8):
        avgtime_info = (str(8), user[0])
        avgtime_update = "update Users set Average_Time = %s where Username = %s"
        mycursor.execute(avgtime_update, avgtime_info)

    elif (timeTemp / (scoreTemp*3) < 8):
        temp = round(timeTemp / (scoreTemp*3), 1)
        avgtime_info = (str(temp), user[0])
        avgtime_update = "update Users set Average_Time = %s where Username = %s"
        mycursor.execute(avgtime_update, avgtime_info)


    
    # Update the Leaderboard
    leaderboard_query = "select Username, lvl, High_Score, Rhyme_Streak, Rhyming_Accuracy, Average_Time from Users order by High_Score desc limit 5"
    mycursor.execute(leaderboard_query)
    leaders = mycursor.fetchall()

    top_players.clear()
    for i in leaders:
        top_players.append(i[0])

        if(i[0] == user[0]):
            position[0] = top_players.index(i[0]) + 1

    low_leader[0] = top_players[len(top_players) - 1]

    # check if player is on the leaderboard
    if(user[0] in top_players):
        leaderText.config(text = "You Are Currently Ranked #" + str(position[0]) + " On The Leaderboard.", font=("Arial", 30, "bold"), bg = "light blue",fg="#191970")
        leaderText.pack(pady=10)

        

    replayGameButton.pack(pady=(40,15))
    returnHomeButton.pack()
    




#Sean: Function to award player XP, update XP, and Level up
def award_xp(score):
    xp_reward = score  #Change this value to fit system better
    return xp_reward

def update_xp(username, xp_awarded):
    # Get current XP and level
    query = "SELECT XP, lvl FROM Users WHERE Username = %s"
    mycursor.execute(query, (username,))
    result = mycursor.fetchone()
    current_xp, current_level = result

    # Update the XP
    new_xp = current_xp + xp_awarded
    level_up(new_xp, current_level, username)  # Check if player should level up

def level_up(new_xp, current_level, username):
    # Set the XP thresholds for leveling up
    level_thresholds = [25, 50, 100, 200]  # Example thresholds for levels 2, 3, 4, and 5
    
    # Find the player's new level based on the XP
    new_level = 1  # Start at level 1
    for threshold in level_thresholds:
        if new_xp >= threshold:
            new_level += 1
        else:
            break  # No need to check further if XP is below this threshold

    if new_level != current_level:
        print(f"Level up! {username} is now Level {new_level}")

    # Update the player's level and XP in the database
    query = "UPDATE Users SET XP = %s, lvl = %s WHERE Username = %s"
    mycursor.execute(query, (new_xp, new_level, username))

def get_user_level(username):
    # Retrieve the player's level from the database using the provided username
    query = "SELECT lvl FROM Users WHERE Username = %s"
    mycursor.execute(query, (username,))
    result = mycursor.fetchone()
    
    # If the player exists in the database, return their current level
    if result:
        return result[0]
    else:
        # If the player does not exist, return None or handle the case accordingly
        return None



def verifyRhyme(*args):
  
    if(gameloop[0] == False):
        rhyme_entry.delete(0, tk.END)
    
    else:
        # Get the rhyme input
        word_input = rhyme_entry.get()

        
        if(word_input.strip() in correct_rhymes or word_input.strip() not in rhymeList):
            totalInputs[0]+=1
            rhyme_entry.delete(0, tk.END)

            # clear the 'consecutive rhymes' streak for incorrect inputs. Increment incorrect rhyme count.
            correct_streak[0] = 0
            incorrect_count[0]+=1

        # if 3 correct rhymes are inputted
        elif(len(correct_rhymes) == 2 and word_input.strip() in rhymeList):

            # "Speed Round" badge check
            check_secs = round(time[0] * 0.14, 10)
            if(check_secs <= 3 and "Rapid Rhyming" not in badges_earned):
                badges_earned.append("Rapid Rhyming")
            if(check_secs <= 4 and "Speed Round" not in badges_earned):
                badges_earned.append("Speed Round")
            if(check_secs <= 5 and "Pace Posthaste" not in badges_earned):
                badges_earned.append("Pace Posthaste")


            # update consecutive rhyme count
            correct_streak[0]+= 1
            
            # update the total inputs value
            totalInputs[0]+=1

            # update the score/recall StartTime for new word/time
            score[0]+=1
            StartTime(score[0])
            rhyme_entry.delete(0, tk.END)

            xp_awarded = award_xp(score[0])
            update_xp(user[0], xp_awarded)
            
        # if a correct rhyme is inputted
        elif(len(correct_rhymes) < 2 and word_input.strip() in rhymeList):

            correct_rhymes.append(word_input.strip())
            display_correct.config(text = correct_rhymes)

            totalInputs[0]+=1

            correct_streak[0]+= 1
            
            rhyme_entry.delete(0, tk.END)
            window.update()

        
rhyme_entry.bind("<Return>", verifyRhyme)





def StartTime(current_score=0):

    gameloop[0] = True

    returnHomeButton.pack_forget()
    startTimeButton.pack_forget()
    correct_rhymes.clear()
    display_correct.config(text = " ")
    rhyme_entry.delete(0, tk.END)
    
    num = random.randint(0,len(random_words) - 1)

    word = random_words[num]
    
    for i in retrieve.rhymes(word):
        rhymeList.append(i)

    mainText.config(text=word,font=("Arial", 180, "bold"))
    mainText.pack(pady=(100,0))

    rhyme_Frame.pack(pady=(20,11))

    correct_Frame.pack()

    score_display.config(text=str(current_score))


    time[0] = 50
    while(time[0] >= -1):
      
        time[0]-=1

        if(time[0] == 0):
            EndGame()
            break
            

        elif(time[0] > 0):
        
            time_display.config(text = str(time[0]))
            
            time_display.pack_forget()
    
            time_display.pack()
            
            totalTime[0]+= round(1 * 0.14, 10)
    
            window.after(140, window.update())


    

    

# Variables For Update Methods: verifyUpdate, updateOption, updateLogin, hide2
new_fname = tk.StringVar()
new_lname = tk.StringVar()
new_email = tk.StringVar()
new_logname = tk.StringVar()
new_logpass = tk.StringVar()
curr_logpass = tk.StringVar()
confirm_logpass = tk.StringVar()
selected_update = tk.StringVar(window)

updates = ["First Name", "Last Name", "Email", "Username", "Password"]


prompt_Frame = tk.Frame(window, background="light blue")
prompt_entry = tk.Entry(prompt_Frame, font=("Arial", 17, "normal"),  fg="#191970") 
prompt = tk.Label(prompt_Frame, font=("Arial", 25, "bold"), bg="light blue", fg="#191970")
prompt.pack(side = tk.LEFT)
prompt_entry.pack(side = tk.RIGHT)

prompt2_Frame = tk.Frame(window, background="light blue")
prompt2_entry = tk.Entry(prompt2_Frame, font=("Arial", 17, "normal"),  fg="#191970") 
prompt2 = tk.Label(prompt2_Frame, font=("Arial", 25, "bold"), bg="light blue", fg="#191970")
prompt2.pack(side = tk.LEFT)
prompt2_entry.pack(side = tk.RIGHT)

prompt3_Frame = tk.Frame(window, background="light blue")
prompt3_entry = tk.Entry(prompt3_Frame, font=("Arial", 17, "normal"),  fg="#191970") 
prompt3 = tk.Label(prompt3_Frame, font=("Arial", 25, "bold"), bg="light blue", fg="#191970")
prompt3.pack(side = tk.LEFT)
prompt3_entry.pack(side = tk.RIGHT)


dropdown = tk.OptionMenu(window, selected_update, *updates)
dropdown.config(font=("Arial", 29, "bold"), bg="#191970", fg="white")
dropdown["menu"].config(font=("Arial", 29, "bold"), bg="#191970", fg="white")

hideUpdate = tk.Button(window, text="Show Passwords", font=("Arial" ,10,"bold"), bg="#191970", fg="white")

prompts = [prompt_Frame, prompt2_Frame, prompt3_Frame, hideUpdate, dropdown, changeUpdateButton]




def verifyUpdate():
    
    if(selected_update.get() == "First Name"):
           
        if(new_fname.get() == ""):
            mainText.config(text="Insert Your New First Name")

        else:
            info = (new_fname.get(), contact[0])
            update_fname = "update Users set First_Name = %s where Email = %s"
            mycursor.execute(update_fname, info)

            mainText.config(text="Your First Name Has Been Updated To " + new_fname.get())
            first[0] = new_fname.get()
            

    elif(selected_update.get() == "Last Name"):

        if(new_lname.get() == ""):
            mainText.config(text="Insert Your New Last Name")

        else:
            info = (new_lname.get(), contact[0])
            update_lname = "update Users set Last_Name = %s where Email = %s"
            mycursor.execute(update_lname, info)

            mainText.config(text="Your Last Name Has Been Updated To " + new_lname.get())
            last[0] = new_lname.get()
    

    elif(selected_update.get() == "Email"):

        em_check = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        if(new_email.get() == ""):
            mainText.config(text="Insert Your New Email")

        elif(re.match(em_check, new_email.get()) == None):
            mainText.config(text="Insert A Valid Email")

        elif(email_values.__contains__(new_email.get())):
            mainText.config(text="The Inserted Email Is Taken")
            
        else:
            info = (new_email.get(), user[0])
            update_email = "update Users set Email = %s where Username = %s"
            mycursor.execute(update_email, info)

            mainText.config(text="Your Email Has Been Updated To " + new_email.get())

            email_values.remove(contact[0])
            email_values.append(new_email.get())
            contact[0] = new_email.get()
            

    elif(selected_update.get() == "Username"):
        
        if(new_logname.get() == ""):
            mainText.config(text="Insert Your New Username")

        elif(username_values.__contains__(new_logname.get())):
            mainText.config(text="The Inserted Username Is Taken")
            
        else:
            info = (new_logname.get(), user[0])
            update1 = "update Users set Username = %s where Username = %s"
            mycursor.execute(update1, info)

            update2 = "update Single_Game set Username = %s where Username = %s"
            mycursor.execute(update2, info)

            update3 = "update Reports set Username = %s where Username = %s"
            mycursor.execute(update3, info)

            update4 = "update Reviews set Username = %s where Username = %s"
            mycursor.execute(update4, info)

            

            mainText.config(text="Your Username Has Been Updated To " + new_logname.get())
           
            if(user[0] in top_players):
                top_players.remove(user[0])
                top_players.append(new_logname.get())
            
            username_values.remove(user[0])
            username_values.append(new_logname.get())
            user[0] = new_logname.get()

    
    elif(selected_update.get() == "Password"):

        if(curr_logpass.get() == ""):
            mainText.config(text="Insert Your Current Password.")
            
        elif(new_logpass.get() == ""):
            mainText.config(text="Insert Your New Password.")

        elif(confirm_logpass.get() == ""):
            mainText.config(text="Confirm Your New Password.")

        elif(curr_logpass.get() != pass_[0]):
            mainText.config(text="The Current Password Is Incorrect.")

        elif(new_logpass.get() != confirm_logpass.get()):
            mainText.config(text="The Confirmed Password Doesn't Match.")
        
        else:
            info = (new_logpass.get(), contact[0])
            update_logpass = "update Users set Password_ = %s where Email = %s"
            mycursor.execute(update_logpass, info)

            mainText.config(text="Your Password Has Been Updated")
            pass_[0] = new_logpass.get()


def hide2():
    if(hideUpdate["text"] == "Hide Passwords"):
        hideUpdate.config(text = "Show Passwords")
        prompt_entry.config(show = "*")
        prompt2_entry.config(show = "*")
        prompt3_entry.config(show = "*")


    elif(hideUpdate["text"] == "Show Passwords"):
        hideUpdate.config(text = "Hide Passwords")
        prompt_entry.config(show = "")
        prompt2_entry.config(show = "")
        prompt3_entry.config(show = "")
                
hideUpdate.config(command=hide2)
        

def updateOption():

     if(selected_update.get() == "Select An Option"):
         mainText.config(text="Select An Update From The Menu.", font=("Arial", 34, "bold"))
         changeUpdateButton.pack(pady=8)
    
     else:
        for widget in prompts:
           widget.pack_forget()

     
     moreButton.config(text="Back", command=moreOptions)
     moreButton.pack(side = tk.TOP, anchor = tk.NW)

     if(selected_update.get() == "First Name"):
        mainText.config(text="Update Your First Name Below.", font=("Arial", 34, "bold"))
        prompt.config(text="New First Name: ")
        prompt_entry.config(textvariable=new_fname)

        prompt_Frame.pack(pady=(15,15))
        updateCheckButton.pack(pady=7)

     elif(selected_update.get() == "Last Name"):
        mainText.config(text="Update Your Last Name Below.", font=("Arial", 34, "bold"))
        prompt.config(text="New Last Name: ")
        prompt_entry.config(textvariable=new_lname)

        prompt_Frame.pack(pady=(15,15))
        updateCheckButton.pack(pady=7)
         
     elif(selected_update.get() == "Email"):
        mainText.config(text="Update Your Email Below.", font=("Arial", 34, "bold"))
        prompt.config(text="New Email: ")
        prompt_entry.config(textvariable=new_email)

        prompt_Frame.pack(pady=(15,15))
        updateCheckButton.pack(pady=7)

     elif(selected_update.get() == "Username"):
        mainText.config(text="Update Your Username Below.", font=("Arial", 34,"bold"))
        prompt.config(text="New Username: ")
        prompt_entry.config(textvariable=new_logname)

        prompt_Frame.pack(pady=(15,15))
        updateCheckButton.pack(pady=7)

     elif(selected_update.get() == "Password"):
        
        mainText.config(text="Update Your Password Below.", font=("Arial", 34, "bold"))
        prompt.config(text="Current Password: ")
        prompt_entry.config(textvariable=curr_logpass)

        prompt2.config(text="New Password: ")
        prompt2_entry.config(textvariable=new_logpass)

        prompt3.config(text="Confirm Password: ")
        prompt3_entry.config(textvariable=confirm_logpass)

        prompt_Frame.pack(pady=(15,0))
        prompt2_Frame.pack(pady=(15,0))
        prompt3_Frame.pack(pady=(15,10))
        hideUpdate.pack(pady=(6,0))

        prompt_entry.config(show = "*")
        prompt2_entry.config(show = "*")
        prompt3_entry.config(show = "*")

        updateCheckButton.pack(pady=15)

    
    

def updateLogin():

    for widget in window.winfo_children():
        widget.pack_forget()

    prompt_entry.delete(0, tk.END)
    prompt2_entry.delete(0, tk.END)
    prompt3_entry.delete(0, tk.END)

    hideUpdate.config(text="Show Passwords")
    updateLoginButton.config(text="Personal Information", font=("Arial" ,21,"bold"), bg="#00bfff", fg="white")
    
    moreButton.config(text="Back", command=moreOptions)
    moreButton.pack(side = tk.TOP, anchor = tk.NW)
    
    mainHeader.config(text="Credentials", font=("Arial", 90, "bold"))
    mainFrame.pack(pady=(35, 20))

    mainText.config(text="Update Your RhymeTime Credentials.", font=("Arial", 34, "bold"), fg="#191970")
    mainText.pack(pady=8)

    dropdown.pack(pady=8)
    selected_update.set("Select An Option")
    
    changeUpdateButton.pack(pady=8)

    cred_prompt = tk.Label(window, text="Your Current Credentials", font=("Arial", 27, "bold"), bg = "light blue",fg="#191970")
    cred_prompt.pack(pady=(35,0))


    credentials = ttk.Treeview(window, columns=("First Name", "Last Name", "Email", "Username"), show='headings', height = 2)

    credentials.column("#1", anchor=CENTER, width = 230)
    credentials.column("#2", anchor=CENTER, width = 230)
    credentials.column("#3", anchor=CENTER, width = 230)
    credentials.column("#4", anchor=CENTER, width = 230)
    
    credentials.heading("First Name", text="First Name")
    credentials.heading("Last Name", text="Last Name")
    credentials.heading("Email", text="Email")
    credentials.heading("Username", text="Username")
    credentials.pack(pady=(9,0))

    info = (user[0],)
    cred_query = "select First_Name, Last_Name, Email, Username from Users where Username = %s"
    mycursor.execute(cred_query, info)
    creds = mycursor.fetchall()
    
    for i in creds:
        credentials.insert("", "end", values=i)

    style = ttk.Style()

    style.configure("Treeview", font = ("Arial", 16), foreground = "#191970")
    style.configure("Treeview.Heading", foreground="white", background="#191970")
    
    
    prompt_entry.config(show = "")
    prompt2_entry.config(show = "")
    prompt3_entry.config(show = "")
    prompts.append(credentials)
    prompts.append(cred_prompt)
    prompts.append(deleteButton)

    deleteButton.pack(pady=(33,0))



def playerStats():
    
    for widget in window.winfo_children():
        widget.pack_forget()
        
    moreButton.config(text="Back")
    moreButton.pack(side = tk.TOP, anchor = tk.NW)

    mainHeader.config(text="Statistics & Badges", font=("Arial", 75, "bold"))
    mainFrame.pack(pady=(65, 0))

    stats_prompt = tk.Label(window, text="Your Statistics", font=("Arial", 27, "bold"), bg = "light blue",fg="#191970")
    stats_prompt.pack(pady=(25,0))

    personal = ttk.Treeview(window, columns=("All-Time Points", "High Score", "Longest Streak", "Rhyming Accuracy", "Average Seconds Per Word", "Total Playing Time"), show='headings', height = 2)

    personal.column("#1", anchor=CENTER, width = 150)
    personal.column("#2", anchor=CENTER, width = 150)
    personal.column("#3", anchor=CENTER, width = 150)
    personal.column("#4", anchor=CENTER, width = 150)
    personal.column("#5", anchor=CENTER, width = 300)
    personal.column("#6", anchor=CENTER, width = 200)
    
    personal.heading("All-Time Points", text="All-Time Points")
    personal.heading("High Score", text="High Score")
    personal.heading("Longest Streak", text="Longest Streak")
    personal.heading("Rhyming Accuracy", text="Rhyming Accuracy")
    personal.heading("Average Seconds Per Word", text="Average Seconds Per Word")
    personal.heading("Total Playing Time", text="Total Playing Time")
    personal.pack(pady=10)

    info = (user[0],)
    personal_query = "select Score_Sum, High_Score, Rhyme_Streak, Rhyming_Accuracy, Average_Time, SEC_TO_TIME(Time_Sum) from Users where Username = %s"
    mycursor.execute(personal_query, info)
    stats = mycursor.fetchall()
    
    for i in stats:
        personal.insert("", "end", values=i)

    style = ttk.Style()

    style.configure("Treeview", font = ("Arial", 16), foreground = "#191970")
    style.configure("Treeview.Heading", foreground="white", background="#191970")
    

    
    # personal badge section
    badges = tk.Label(window, text="Badges Earned", font=("Arial", 27, "bold"), bg = "light blue",fg="#191970")
    badges.pack(pady=(38,0))

    badge_Frame = tk.Frame(window)
    badges_entry = tk.Text(badge_Frame, font=("Arial", 14, "bold"), bg="#00bfff", fg="white", highlightthickness=8, highlightbackground = "white", highlightcolor= "white", width = 70, height = 7)
    badges_entry.pack()
    badge_Frame.pack(pady=20)

    def setBadges():

        badges_earned.clear()
        
        ### Create Queries & Variables ###
        info = (user[0],)
        
        stats_query = "select High_Score, Score_Sum, Rhyming_Accuracy, Average_Time, Time_Sum, lvl, Rhyme_Streak from Users where Username = %s"
        mycursor.execute(stats_query, info)
        stats = mycursor.fetchall()

        singles_query = "select Learned, Well_Done, APTR, Master_Class from Single_Game where Username = %s"
        mycursor.execute(singles_query, info)
        singles = mycursor.fetchall()

        # gets the player's accuracy value without %
        accuracy = stats[0][2][:-1]

        # Award badges based on the player's level
        player_level = stats[0][5]

        maxs_query = "select MAX(Score_Sum), MAX(Time_Sum), MAX(High_Score), MAX(lvl), MAX(Average_Time), MAX(Rhyming_Accuracy) from Users"
        mycursor.execute(maxs_query)
        maxs = mycursor.fetchall()



        ### Badge Attribution ###
        if(stats[0][1] == maxs[0][0]):
            badges_earned.append("All-Time Leading Scorer")

        if(top_players[0] == user[0]):
            badges_earned.append("One-Of-One")

        if(stats[0][3] <= 2):
            badges_earned.append("Flying")

        
        if(stats[0][0] >= 20):
            badges_earned.append("20+ Club")
        elif(stats[0][0] >= 15):
            badges_earned.append("15+ Club")
        elif(stats[0][0] >= 10):
            badges_earned.append("10+ Club")
        

        
        if(float(accuracy) >= 90):
            badges_earned.append("MC")
        elif(float(accuracy) >= 80):
            badges_earned.append("Rhymes Like Dimes")
        elif(float(accuracy) >= 60):
            badges_earned.append("Show It To A Poet")
        elif(float(accuracy) >= 40):
            badges_earned.append("It's Time To Rhyme")

        
        if(player_level) >= 5:
            badges_earned.append("Elite")
        elif(player_level) >= 4:
            badges_earned.append("Expert")
        elif(player_level) >= 3:
            badges_earned.append("Pro")
        elif(player_level) >= 2:
            badges_earned.append("Average Joe")
        elif(player_level) >= 1:
            badges_earned.append("Rookie")

        
        if(stats[0][4] == maxs[0][1]):
            badges_earned.append("All-Day Long")


        if(stats[0][6] >= 50):
            badges_earned.append("Legendary Rhymes")
        elif(stats[0][6] >= 40):
            badges_earned.append("Can't Stop, Won't Stop")
        elif(stats[0][6] >= 25):
            badges_earned.append("Nothing But Rhymes")
        elif(stats[0][6] >= 15):
            badges_earned.append("Efficiency")

        if(singles[0][3] == "True"):
            badges_earned.append("Master Class")
        elif(singles[0][2] == "True"):
            badges_earned.append("A Performance To Remember")
        elif(singles[0][1] == "True"):
            badges_earned.append("Well Done")
        elif(singles[0][0] == "True"):
            badges_earned.append("Learned")
    
            
            
    setBadges()

    # display all the player's badges in the second entry       
    for i in range(0, len(badges_earned)):
        if(i > 0):
            badges_entry.insert("1.0", badges_earned[i] + ", ")

        else:
            badges_entry.insert("1.0", badges_earned[i])

        
    badges_entry.config(state=tk.DISABLED)
    








def feedback():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    moreButton.config(text="Back")
    moreButton.pack(side = tk.TOP, anchor = tk.NW)

    mainHeader.config(text="Rate & Review RhymeTime", font=("Arial", 70, "bold"))
    mainFrame.pack(pady=(70, 0))

    review_prompt = tk.Label(window, text="Your Review Will Be Shown By Your Username: '" + user[0] +"'", font=("Arial", 23, "bold"), bg = "light blue",fg="#191970")
    review_prompt.pack(pady=(15,25))

    review_Frame = tk.Frame(window)
    review_entry = tk.Text(window, font=("Arial", 17, "normal"), bg="#00bfff", fg="white", highlightthickness=8, highlightbackground = "white", highlightcolor= "white", width = 50, height = 6)
    review_entry.pack()
    review_Frame.pack(pady=(20,0))


    star_select = tk.StringVar()
    
    starFrame = tk.Frame(window)
    one_star = tk.Radiobutton(starFrame, text="1 Star", font=("Arial", 17, "bold"), variable=star_select, value=1, fg="white", bg="#191970")
    two_stars = tk.Radiobutton(starFrame, text="2 Stars", font=("Arial", 17, "bold"), variable=star_select, value=2, fg="white", bg="#191970")
    three_stars = tk.Radiobutton(starFrame, text="3 Stars",font=("Arial", 17, "bold"), variable=star_select, value=3, fg="white", bg="#191970")
    four_stars = tk.Radiobutton(starFrame, text="4 Stars", font=("Arial", 17, "bold"), variable=star_select, value=4, fg="white", bg="#191970")
    five_stars = tk.Radiobutton(starFrame, text="5 Stars", font=("Arial", 17, "bold"), variable=star_select, value=5, fg="white", bg="#191970")

    one_star.pack(side=tk.LEFT, ipadx=17)
    five_stars.pack(side=tk.RIGHT, ipadx=17)
    four_stars.pack(side=tk.RIGHT, ipadx=17)
    three_stars.pack(side=tk.RIGHT, ipadx=17)
    two_stars.pack(side=tk.RIGHT, ipadx=17)

    starFrame.pack(pady=(20, 0))

    submit1Button = tk.Button(window, text = "Submit Rating & Review",  font=("Arial", 20, "bold"), bg="#191970", fg="white")
    submit1Button.pack(pady=(20, 0))


    stars = [one_star, two_stars, three_stars, four_stars, five_stars]
    
    def highlight():
        
        x = int(star_select.get())
        stars[x-1].config(fg="#FFD700")

        for i in stars:
            if(i["value"] != x):
                i.config(fg="white")


    for i in stars:
        i.config(command = highlight)
        

    def submit1():
        review = review_entry.get("1.0", END)
        rating = star_select.get()

        if review.isspace():
            review_prompt.config(text = "Type Your Review Below.", font=("Arial", 23, "bold"))
            
        elif(rating == ""):
            review_prompt.config(text = "Select A Rating From 1-5 Stars.", font=("Arial", 23, "bold"))

        elif(rating != "" and review != ""):
            info = (user[0], rating, review)
            review_query = "insert into Reviews (Username, Rating, Review) values (%s, %s, %s)"
            mycursor.execute(review_query, info)
            
    
            for widget in window.winfo_children():
                widget.pack_forget()
                widget.place_forget()
    
            moreButton.config(text="Back")
            moreButton.pack(side = tk.TOP, anchor = tk.NW)
        
            mainHeader.config(text="Feedback Submitted!", font=("Arial", 83, "bold"), fg="#191970")
            mainFrame.pack(pady=(140, 0))
    
            mainText.config(text = "Thanks For Your Feedback!", font=("Arial", 34,"bold"), fg="#191970")
            mainText.pack(pady=15)
            
            review_prompt.config(text="Your Review Can Now Be Seen On The 'Ratings & Reviews' Page")
            review_prompt.pack(pady=10)

    
    submit1Button.config(command=submit1)


    

def reviews():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    moreButton.config(text="Back")
    moreButton.pack(side = tk.TOP, anchor = tk.NW)

    mainHeader.config(text="Ratings & Reviews", font=("Arial", 90, "bold"))
    mainFrame.pack(pady=(70, 0))

    avg_query = "select AVG(Rating) from Reviews"
    mycursor.execute(avg_query)
    avg_rating = mycursor.fetchone()

    rating = avg_rating[0]

    if (rating == None):
        rating = 0
        
    rating_prompt = tk.Label(window, text="Current RhymeTime Rating: " + str(round(rating,1)) + " Stars", font=("Arial", 25, "bold"), bg = "light blue",fg="#191970")
    rating_prompt.pack(pady=(16,0))


    
    filterFrame = tk.Frame(window)
    filter_select = tk.StringVar()
    latest = tk.Radiobutton(filterFrame, text="Latest Reviews", font=("Arial", 14, "bold"), variable=filter_select, value="Latest Reviews", bg="#191970", fg="white")
    highest = tk.Radiobutton(filterFrame, text="Highest-Rated",  font=("Arial", 14, "bold"), variable=filter_select, value="Highest-Rated", bg="#191970", fg="white")
    lowest = tk.Radiobutton(filterFrame, text="Lowest-Rated", font=("Arial", 14, "bold"), variable=filter_select,value="Lowest-Rated", bg="#191970", fg="white")

    latest.pack(side=tk.LEFT, ipadx=22)
    lowest.pack(side=tk.RIGHT, ipadx=22)
    highest.pack(side=tk.RIGHT, ipadx=22)

    filterFrame.pack(pady=(10,0))
    

    reviewer_prompt = tk.Label(window, font=("Arial", 16, "bold"), bg="light blue", fg="#191970")
    reviewer_prompt.pack(pady=7)
    
    review_Frame = tk.Frame(window)
    review_entry = tk.Text(window, font=("Arial", 17, "normal"), bg="#00bfff", fg="white", highlightthickness=8, highlightbackground = "white", highlightcolor= "white", width = 50, height = 6)
    review_entry.pack()
    review_Frame.pack(pady=(20,0))

    


    load_review = [0]
    
    lowest_query = "select Username, Rating, Review from Reviews order by Rating asc"
    mycursor.execute(lowest_query)
    low_reviews = mycursor.fetchall()

    highest_query = "select Username, Rating, Review from Reviews order by Rating desc"
    mycursor.execute(highest_query)
    high_reviews = mycursor.fetchall()
    
    latest_query = "select Username, Rating, Review from Reviews order by ReviewID desc"
    mycursor.execute(latest_query)
    latest_reviews = mycursor.fetchall()

    normal_query = "select Username, Rating, Review from Reviews"
    mycursor.execute(normal_query)
    normal_reviews = mycursor.fetchall()


    navFrame = tk.Frame(window, background="light blue")
    previousButton = tk.Button(navFrame, text="Previous", font=("Arial" ,15,"bold"), bg="#191970", fg="white")
    review_num = tk.Label(navFrame, font=("Arial", 17, "bold"), bg="light blue",fg="#191970")
    nextButton = tk.Button(navFrame, text="Next", font=("Arial" ,15,"bold"), bg="#191970", fg="white")

    previousButton.pack(side=tk.LEFT, ipadx=15)
    nextButton.pack(side=tk.RIGHT, ipadx=15)
    review_num.pack(side=tk.LEFT, ipadx=15)

    navFrame.pack(pady=7)
    

    def normal():

        if(len(latest_reviews) == 0):
            reviewer_prompt.config(text="RhymeTime Currently Has No Ratings. Be The First To Rate RhymeTime!")

        else:
            User = normal_reviews[load_review[0]][0]
            Rating = normal_reviews[load_review[0]][1]
            Review = normal_reviews[load_review[0]][2]
        
            reviewer_prompt.config(text=User + " Gave A Rating Of " + str(Rating) + " Stars And Wrote:")
            review_entry.insert("1.0", Review)
            review_entry.config(state=DISABLED)
            review_num.config(text=str(load_review[0] + 1) + " of " + str(len(normal_reviews)))

    normal()

    def filter(current=0):

        load_review[0] = current
        
        if(len(latest_reviews) == 0):
            reviewer_prompt.config(text="RhymeTime Currently Has No Ratings. Be The First To Rate RhymeTime!")         
        
        
        elif(filter_select.get() == "Latest Reviews"):

            latest.config(fg="#FFD700")
            highest.config(fg="white")
            lowest.config(fg="white")

            User = latest_reviews[load_review[0]][0]
            Rating = latest_reviews[load_review[0]][1]
            Review = latest_reviews[load_review[0]][2]

            review_entry.config(state=tk.NORMAL)
            review_entry.delete("1.0", END)
            
            reviewer_prompt.config(text=User + " Gave A Rating Of " + str(Rating) + " Stars And Wrote:")
            review_entry.insert("1.0", Review)
            review_entry.config(state=DISABLED)
            
            review_num.config(text=str(load_review[0] + 1) + " of " + str(len(latest_reviews)))

        elif(filter_select.get() == "Highest-Rated"):

            highest.config(fg="#FFD700")
            latest.config(fg="white")
            lowest.config(fg="white")
            
            User = high_reviews[load_review[0]][0]
            Rating = high_reviews[load_review[0]][1]
            Review = high_reviews[load_review[0]][2]

            review_entry.config(state=tk.NORMAL)
            review_entry.delete("1.0", END)
            
            reviewer_prompt.config(text=User + " Gave A Rating Of " + str(Rating) + " Stars And Wrote:")
            review_entry.insert("1.0", Review)
            review_entry.config(state=DISABLED)
            
            review_num.config(text=str(load_review[0] + 1) + " of " + str(len(latest_reviews)))

        elif(filter_select.get() == "Lowest-Rated"):

            lowest.config(fg="#FFD700")
            highest.config(fg="white")
            latest.config(fg="white")
            
            User = low_reviews[load_review[0]][0]
            Rating = low_reviews[load_review[0]][1]
            Review = low_reviews[load_review[0]][2]

            review_entry.config(state=tk.NORMAL)
            review_entry.delete("1.0", END)
            
            reviewer_prompt.config(text=User + " Gave A Rating Of " + str(Rating) + " Stars And Wrote:")
            review_entry.insert("1.0", Review)
            review_entry.config(state=DISABLED)
            
            review_num.config(text=str(load_review[0] + 1) + " of " + str(len(latest_reviews)))

    
    
    def next():
        
        review_entry.config(state=NORMAL)
        review_entry.delete("1.0", END)        
            
        if(load_review[0] + 1 == len(latest_reviews) and filter_select.get() == ""):
            load_review[0] = 0
            normal()
            
        elif(filter_select.get() == ""):
            load_review[0]+=1
            normal()

        elif(load_review[0] + 1 == len(latest_reviews) and filter_select.get() != ""):
            load_review[0] = 0
            filter(load_review[0])
        
            
        elif(filter_select.get() != ""):
            load_review[0]+=1
            filter(load_review[0])
    

    def previous():

        review_entry.config(state=NORMAL)
        review_entry.delete("1.0", END)        
            
        if(load_review[0] + 1 == 1 and filter_select.get() == ""):
            load_review[0] = len(latest_reviews) - 1
            normal()
            
        elif(filter_select.get() == ""):
            load_review[0]-=1
            normal()

        elif(load_review[0] + 1 == 1 and filter_select.get() != ""):
            load_review[0] = len(latest_reviews) - 1
            filter(load_review[0])
        
            
        elif(filter_select.get() != ""):
            load_review[0]-=1
            filter(load_review[0])

    
    latest.config(command=filter)
    highest.config(command=filter)
    lowest.config(command=filter)

    nextButton.config(command=next)
    previousButton.config(command=previous)





def badges():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    moreButton.config(text="Back")
    moreButton.pack(side = tk.TOP, anchor = tk.NW)

    mainHeader.config(text="Badge Collection", font=("Arial", 70, "bold"))
    mainFrame.pack(pady=(90, 10))

    mainText.config(text = "Earn Badges Based On Your Rhyming Skills.", font=("Arial", 28, "bold"), fg="#191970")
    mainText.pack(pady=5)


    
    # all badges section
    load_badge = [0]
    Name = game_badges[load_badge[0]][0]
    Description = game_badges[load_badge[0]][1]
    
    badge_name = tk.Label(window, text="Badge: " + Name, font=("Arial", 25, "bold", "underline"), bg = "light blue",fg="#191970")
    badge_name.pack(pady=20)

    badge_Frame = tk.Frame(window)
    badge_entry = tk.Text(badge_Frame, font=("Arial", 14, "bold"), bg="#00bfff", fg="white",highlightthickness=8, highlightbackground = "white", highlightcolor= "white", width = 80, height = 7)
    badge_entry.insert("1.0", Description)
    badge_entry.config(state=DISABLED)
    badge_entry.pack()
    badge_Frame.pack(pady=(20,0))

    
    navFrame = tk.Frame(window, background="light blue")

    previousButton = tk.Button(navFrame, text="Previous", font=("Arial" ,15,"bold"), bg="#191970", fg="white")

    badge_num = tk.Label(navFrame, text=str(load_badge[0] + 1) + " of " + str(len(game_badges)), font=("Arial", 17, "bold"), bg="light blue", fg="#191970")

    nextButton = tk.Button(navFrame, text="Next", font=("Arial" ,15,"bold"), bg="#191970", fg="white")

    previousButton.pack(side = tk.LEFT, ipadx=15)
    nextButton.pack(side = tk.RIGHT, ipadx=15)
    badge_num.pack(side = tk.RIGHT,  ipadx=15)

    navFrame.pack(pady=7)

    
  
    def next():

        if load_badge[0] == len(game_badges) - 1:
            load_badge[0] = 0  # Go back to the first badge
        else:
            load_badge[0] += 1  # Otherwise, increment to the next badge

        Name = game_badges[load_badge[0]][0]
        Description = game_badges[load_badge[0]][1]

        badge_entry.config(state=tk.NORMAL)
        badge_entry.delete("1.0", tk.END)

        badge_entry.insert("1.0", Description)
        badge_entry.config(state=tk.DISABLED)

        badge_name.config(text="Badge: " + Name)

        badge_num.config(text=str(load_badge[0] + 1) + " of " + str(len(game_badges)))

    
    def previous():

        print("")

        if load_badge[0] == 0:
            load_badge[0] = len(game_badges) - 1
        else:
            load_badge[0] -= 1

        Name = game_badges[load_badge[0]][0]
        Description = game_badges[load_badge[0]][1]

        badge_entry.config(state=tk.NORMAL)
        badge_entry.delete("1.0", tk.END)

        badge_entry.insert("1.0", Description)
        badge_entry.config(state=tk.DISABLED)

        badge_name.config(text="Badge: " + Name)

        badge_num.config(text=str(load_badge[0] + 1) + " of " + str(len(game_badges)))


    nextButton.config(command=next)
    previousButton.config(command=previous)




def report():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    moreButton.config(text="Back")
    moreButton.pack(side = tk.TOP, anchor = tk.NW)


    mainHeader.config(text="Contact Us", font=("Arial", 90, "bold"))
    mainFrame.pack(pady=(30, 0))

    mainText.config(text = "Email The Developers About Any Issues Or Concerns In The Game.", font=("Arial", 25, "bold"), fg="#191970")
    mainText.pack(pady=15)

    email_prompt = tk.Label(window, text="Your Report Will Be Sent From: " + contact[0], font=("Arial", 20, "bold", "underline"), bg = "light blue",fg="#191970")
    email_prompt.pack(pady=10)

    report_Frame = tk.Frame(window)
    report_entry = tk.Text(report_Frame, font=("Arial", 17, "normal"), bg="#00bfff", fg="white",highlightthickness=8, highlightbackground = "white", highlightcolor= "white", width = 50, height = 6)
    report_entry.pack()
    report_Frame.pack(pady=20)

    submitButton = tk.Button(window, text = "Send Email",  font=("Arial", 23,"bold"), bg="#191970", fg="white")
    submitButton.pack()


    def email(sender, receiver, subject, message):

        # email server: gmail
        smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        # the server logs into this email to access "gmail" for sending emails. 
        # the second argument is our "mail specific" password
        smtp_obj.login('gsgreenteam02@gmail.com', 'gjzi stfc ygeg arrp')
        smtp_obj.set_debuglevel(1)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        msg.set_content(message)
        smtp_obj.send_message(msg)
        smtp_obj.quit()

        email_prompt.config(text="Your Email Has Been Sent. Your Report Will Be Addressed At Our Closest Convenience.")


    # Send email
    def submit():

        report = report_entry.get("1.0", END)
        
        if report.isspace():
            mainText.config(text = "Type Your Report Below.")

        else:
            get_contacts = "select Dev_Email from Contacts"
            mycursor.execute(get_contacts)
            dev_emails = mycursor.fetchall()

    
            for i in dev_emails:
                email(str(Header('RhymeTime Concern!')), i, first[0] + " " + last[0] + ": " + contact[0], report_entry.get("1.0", END))
            
    
            info = (user[0], contact[0],report_entry.get("1.0", END) )
            report_query = "insert into Reports (Username, Email, Report) values (%s, %s, %s)"
            mycursor.execute(report_query, info)

        

    submitButton.config(command=submit)


def logout():
    logged[0] = False
    home()
    



def moreOptions():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    
    returnHomeButton.pack(side = tk.TOP, anchor = tk.NW)

    badgesButton.pack(pady=(25,0))
    badgesButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")
    
    leadersButton.pack()
    leadersButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")
    
    reviewsButton.pack()
    reviewsButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")
    
    feedbackButton.pack()
    feedbackButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")
    
    statsButton.pack()
    statsButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")
    
    updateLoginButton.pack()
    updateLoginButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")
    
    reportButton.pack()
    reportButton.config(highlightthickness=4,highlightbackground = "white", highlightcolor= "white")






    
# Christian: Create the "Home" screen method and its contents
# X: Update Home when user logs in
def home():
  
  #clear any previous widgets placed
  for widget in window.winfo_children():
        widget.pack_forget()

  createFirst.clear()
  password_entry.config(show="*")
  hidePass.config(text="Show Password")
  loginButton.config(text="Login")
    
  if (logged[0] == True):

      quitButton.pack(side = tk.TOP, anchor = tk.NE)
      mainHeader.config(text="RhymeTime", font=("Arial", 80, "bold"))
      mainFrame.pack(pady=(90, 20))

       # Fetch user level from the database
      query = "SELECT XP, lvl FROM Users WHERE Username = %s"
      mycursor.execute(query, (user[0],))
      user_data = mycursor.fetchone()
      user_xp, user_level = user_data

      mainText.config(text = "Welcome Back " + first[0] + "!", font=("Arial", 30, "bold"), fg="#191970")
      mainText.pack(pady=10)

      # Define XP thresholds
      level_thresholds = [0, 25, 50, 100, 200]  # Level 1 starts at 0

      # Find current and next threshold
      if user_level < len(level_thresholds):
          next_threshold = level_thresholds[user_level]
      else:
          next_threshold = level_thresholds[-1] + (user_level - len(level_thresholds) + 1) * 100  # Optional: linear growth after last defined threshold

      xp_progress_text = f"{user_xp}/{next_threshold}"

      # Create a label for the user's level
      frame = tk.Frame(window, bg="#1e1e1e", padx=10, pady=10, bd=2, relief="ridge")
      frame.pack(pady=20)

      xpLabel = tk.Label(frame, text=f"XP: {xp_progress_text}", font=("Helvetica", 18), fg="#00FF00", bg="#1e1e1e")
      xpLabel.pack()

      levelLabel = tk.Label(frame, text=f"Level: {user_level}", font=("Helvetica", 22, "bold"), fg="#FFD700", bg="#1e1e1e")
      levelLabel.pack()

      startGameButton.pack(pady=10)

      moreButton.pack(pady=10)
      moreButton.config(text="More Options")

      logoutButton.pack(pady=10)

      username_entry.delete(0, tk.END)
      password_entry.delete(0, tk.END)
      fname_entry.delete(0, tk.END)
      lname_entry.delete(0, tk.END)
      email_entry.delete(0, tk.END)

  else:
    
      mainHeader.config(text="Welcome To RhymeTime!", font=("Arial", 70, "bold"))
      mainFrame.pack(pady=(170, 20))
    
      mainText.config(text="How Fast Can You Rhyme?", font=("Arial", 34, "bold"))
      mainText.pack(pady=(7,15))
    
      loginButton.config(command=loginPage)
      loginButton.pack(pady=10)
      
      createButton.config(command=createAccountPage)
      createButton.pack(pady=10)
    
      quitButton.config(command=quitGame)
      quitButton.pack(pady=10)
    
      username_entry.delete(0, tk.END)
      password_entry.delete(0, tk.END)
      fname_entry.delete(0, tk.END)
      lname_entry.delete(0, tk.END)
      email_entry.delete(0, tk.END)





def leaderBoard():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    
    moreButton.config(text="Back")
    moreButton.pack(side = tk.TOP, anchor = tk.NW)
    
    mainHeader.config(text="Top RhymeTime Players", font=("Arial", 65, "bold"))
    mainFrame.pack(pady=(25, 20))

    mainText.config(text="'The Best Rhymers'", font=("Arial", 34, "italic"), fg="white")
    mainText.pack(pady=(7,15))
    

    leaderboard = ttk.Treeview(window, columns=("Player", "Level", "High Score", "Longest Streak", "Rhyming Accuracy", "Average Seconds Per Word"), show='headings', height = 6)

    leaderboard.column("#1", anchor=CENTER, width = 150)
    leaderboard.column("#2", anchor=CENTER, width = 150)
    leaderboard.column("#3", anchor=CENTER, width = 150)
    leaderboard.column("#4", anchor=CENTER, width = 150)
    leaderboard.column("#5", anchor=CENTER, width = 150)
    leaderboard.column("#6", anchor=CENTER, width = 300)
    
    leaderboard.heading("Player", text="Player")
    leaderboard.heading("Level", text="Level")
    leaderboard.heading("High Score", text="High Score")
    leaderboard.heading("Longest Streak", text="Longest Streak")
    leaderboard.heading("Rhyming Accuracy", text="Rhyming Accuracy")
    leaderboard.heading("Average Seconds Per Word", text="Average Seconds Per Word")
    leaderboard.pack(pady=10)

    # Get top players
    leaderboard_query = "select Username, lvl, High_Score, Rhyme_Streak, Rhyming_Accuracy, Average_Time from Users order by High_Score desc limit 5"
    mycursor.execute(leaderboard_query)
    leaders = mycursor.fetchall()
    
    for leader in leaders:
        leaderboard.insert("", "end", values=leader)

    top_players.clear()
    for i in leaders:
        top_players.append(i[0])

        if(i[0] == user[0]):
            position[0] = top_players.index(i[0]) + 1

    low_leader[0] = top_players[len(top_players) - 1]

    if (user[0] in top_players):

        if(position[0] == 1):
            
            congrats = tk.Label(window, text="Congratulations " + first[0] + ", You Are Ranked " + str(position[0]) + "st Amongst All RhymeTime players!", font = ("Arial", 25, "bold"), bg = "light blue",fg="#191970")
            congrats.pack(pady=20)

        elif(position[0] == 2):
            
            congrats = tk.Label(window, text="Congratulations " + first[0] + ", You Are Ranked " + str(position[0]) + "nd Amongst All RhymeTime players!", font = ("Arial", 25, "bold"), bg = "light blue",fg="#191970")
            congrats.pack(pady=20)

        elif(position[0] == 3):
            
            congrats = tk.Label(window, text="Congratulations " + first[0] + ", You Are Ranked " + str(position[0]) + "rd Amongst All RhymeTime players!", font = ("Arial", 25, "bold"), bg = "light blue",fg="#191970")
            congrats.pack(pady=20)


        elif(position[0] == 4 or position[0] == 5):
            
            congrats = tk.Label(window, text="Congratulations " + first[0] + ", You Are Ranked " + str(position[0]) + "th Amongst All RhymeTime players!", font = ("Arial", 25, "bold"), bg = "light blue",fg="#191970")
            congrats.pack(pady=20)


    else:
        info=(low_leader[0],)
        last_query = "select High_Score from Users where Username = %s"
        mycursor.execute(last_query, info)
        lowest = mycursor.fetchone()

        info2=(user[0],)
        personal_query = "select High_Score from Users where Username = %s"
        mycursor.execute(personal_query, info2)
        player_score = mycursor.fetchone()


        points_needed = int(lowest[0]) - int(player_score[0])
        
        prompt = tk.Label(window, font = ("Arial", 21, "bold"), bg = "light blue",fg="#191970")

        if(points_needed == 1):
            prompt.config(text="Your High Score Needs To Be " + str(points_needed) + " Point Higher In Order To Reach The Leaderboard.")
        else:
            prompt.config(text="Your High Score Needs To Be " + str(points_needed) + " Points Higher In Order To Reach The Leaderboard.")
        prompt.pack(pady=20)
        

    style = ttk.Style()

    style.configure("Treeview", font = ("Arial", 16), rowheight = 27, foreground = "#191970")
    style.configure("Treeview.Heading", foreground="white", background="#191970")
    


def deleteAccount():
    
    for widget in window.winfo_children():
        widget.pack_forget()

    yes = tk.Button(window,text="Yes", font=("Arial" ,35,"bold"), bg="#191970", fg="white")
    no = tk.Button(window,text="No", font=("Arial" ,37,"bold"), bg="#191970", fg="white")
    back = tk.Button(window, text="Back", font=("Arial" ,25,"bold"), bg="#191970", fg="white")


    
    back.pack(side = tk.TOP, anchor = tk.NW)
    back.config(command=updateLogin)
    
    mainHeader.config(text="Delete Your Account", font=("Arial", 60, "bold"))
    mainFrame.pack(pady=(120, 0))

    question = tk.Label(window, text="Are You Sure You Would Like To Delete Your RhymeTime Account?", font=("Arial", 23, "bold"), bg = "light blue",fg="#191970")
    question.pack(pady=(35,0))

    def selectYes():
        
        for widget in window.winfo_children():
            widget.pack_forget()

        info = (user[0],)
        delete = "delete from Users where Username = %s"
        mycursor.execute(delete, info)

        logged[0] = False

        mainHeader.config(text="RhymeTime", font=("Arial", 70, "bold"))
        mainFrame.pack(pady=(110, 0))

        confirm = tk.Label(window, text="Your Account Has Been Removed.", font=("Arial", 29, "bold"), bg = "light blue",fg="#191970")
        confirm.pack(pady=(35,0))
        returnHomeButton.pack(pady=30)

    def selectNo():
        updateLogin()


    yes.pack(pady=(20,0))
    yes.config(command=selectYes)
    
    no.pack(pady=(10,0))
    no.config(command=selectNo)



def quitGame():
  window.destroy()




# animate meain header text
def animate_text():
    colors = ["red", "#191970", "green", "purple", "orange"]
    mainHeader.config(fg=random.choice(colors))  
    window.after(500, animate_text)  # Change color every 500ms


def on_enter(e, button):
    button.config(font=("Arial", 30, 'bold','underline'), fg="#191970", cursor="hand2")


def on_leave(e, button):
    button.config(font=("Arial", 25,'bold'), fg="white")


# set button commands
returnHomeButton.config(command=home)
loginButton.bind("<Enter>", lambda e: on_enter(e, loginButton)) 
loginButton.bind("<Leave>", lambda e: on_leave(e, loginButton)) 
createButton.bind("<Enter>", lambda e: on_enter(e, createButton)) 
createButton.bind("<Leave>", lambda e: on_leave(e, createButton)) 
quitButton.bind("<Enter>", lambda e: on_enter(e, quitButton)) 
quitButton.bind("<Leave>", lambda e: on_leave(e, quitButton)) 
returnHomeButton.bind("<Enter>", lambda e: on_enter(e, returnHomeButton)) 
returnHomeButton.bind("<Leave>", lambda e: on_leave(e, returnHomeButton))
startGameButton.bind("<Enter>", lambda e: on_enter(e, startGameButton)) 
startGameButton.bind("<Leave>", lambda e: on_leave(e, startGameButton)) 
logoutButton.bind("<Enter>", lambda e: on_enter(e, logoutButton)) 
logoutButton.bind("<Leave>", lambda e: on_leave(e, logoutButton)) 
moreButton.bind("<Enter>", lambda e: on_enter(e, moreButton)) 
moreButton.bind("<Leave>", lambda e: on_leave(e, moreButton)) 
startTimeButton.bind("<Enter>", lambda e: on_enter(e, startTimeButton)) 
startTimeButton.bind("<Leave>", lambda e: on_leave(e, startTimeButton)) 
replayGameButton.bind("<Enter>", lambda e: on_enter(e, replayGameButton)) 
replayGameButton.bind("<Leave>", lambda e: on_leave(e, replayGameButton)) 
animate_text()




# Button Configurations
returnHomeButton.config(command=home)
startTimeButton.config(command=StartTime)
replayGameButton.config(command=startGame)
logoutButton.config(command=logout)
leadersButton.config(command=leaderBoard)
moreButton.config(command = moreOptions)
updateLoginButton.config(command=updateLogin)
changeUpdateButton.config(command=updateOption)
updateCheckButton.config(command=verifyUpdate)
badgesButton.config(command=badges)
feedbackButton.config(command=feedback)
reviewsButton.config(command=reviews)
reportButton.config(command=report)
statsButton.config(command=playerStats)
deleteButton.config(command=deleteAccount)



# call home function to display the home screen
home()





# display the window
window.mainloop()