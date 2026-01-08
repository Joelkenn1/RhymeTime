
import random
import sys
import pronouncing as retrieve
import mysql.connector
import tkinter as tk
from tkinter import *



'''mysql connector guide'''

# replace my info with your own and connect to your database 
# mydb = mysql.connector.connect(
#   host= "127.0.0.1",
#   user = "root",
#   password= "Ckenney1",
#   database = "RhymeDatabase"
  
# )

# auto commits every query
# mydb.autocommit = True

# # the cursor is used to execute queries 
# mycursor = mydb.cursor()


# query1 = "select SEC_TO_TIME(Time_Sum) from Users"

# mycursor.execute(query1)

# title = mycursor.fetchall()

# # print(title) outputs a tuple containing the title at the first index.  
# for i in title:
#     print(i[0])



# # query values must be contained in tuples to execute formatted queries 
# name = ("Jose",)
# query2 = "Select address from CE_Students where ce_name = %s"

# mycursor.execute(query2, name)

# address = mycursor.fetchone()

# print(address[0])



# values = ("104","Mike", "CE")
# query3 = "Update CE_Students set sid = %s where ce_name = %s and major = %s"

# #the table will update
# mycursor.execute(query3, values)





# '''Tkinter(GUI) Snippet'''

# # create the window
# window = tk.Tk()
# window.attributes('-fullscreen', True)
# window.title("Example")


# # Label is used for placing text in the GUI
# text1 = tk.Label(window, font=("Arial", 60))
# text2 = tk.Label(window, font=("Arial", 60))
# text3 = tk.Label(window, font=("Arial", 60))

# # create buttons for switching pages
# button1 = tk.Button(window, 
#                     text="Next Page", 
#                     font=("Times New Roman" ,25))

# button2 = tk.Button(window, 
#                         text="Previous Page", 
#                         font=("Times New Roman" ,25), 
#                         background="lightblue",
#                         activebackground="lightblue")

# # Time in Tkinter (check newPage())
# time_label = tk.Label(window, text = "Incrementing Time: ", font=("Arial", 40))
    
# time = tk.Label(window, text = "35", font=("Arial", 38))

# # ---Page Navigation---
# startObjs = []

# def startPage():

#     # place_forget is used to make elements from previous pages disappear 
#     button2.place_forget()
#     time_label.place_forget()
#     time.place_forget()
    
#     # place is used to display elements with exact location
#     text1.config(text="text1")
#     text1.place(x=530, y=245)

#     text2.config(text="text2")
#     text2.place(x=530, y=355)

#     text3.config(text="text3")
#     text3.place(x=530, y=455)
    
    
#     button1.place(x=555, y=600)
    
    
#     # Add the elements of the page that aren't in
#     # newPage() to be forgotten in newPage()
#     startObjs.append(text1)
#     startObjs.append(text2)
#     startObjs.append(button1)
    

    

# # You have to create a method for a button functionality
# def newPage():

#     # place_forget is used to make elements from previous pages disappear 
#     # Always forget unneccesary elements first
#     for i in startObjs:
#         i.place_forget()
        
#     # config is used to change an element's attributes
#     text3.config(text="Text 3 Remains", font=("Arial", 45))

#     button2.place(x=555, y=580)

#     # Time
#     time_label.place(x=530, y=255)
    
#     time.place(x=1030, y=260)


                                              
#     t = 0
#     while(t < 100):

#         # Increment the time value by one
#         t+=1

#         # Update the time display with each increment
#         time.config(text = str(t))

#         # window.after is a method to used to execute functions after x milliseconds
#         # In order to see the time change, the window must be updated. If you update the 
#         # window each second (1000), the game lags, so we have to use higher time values
#         # so the GUI and update with milliseconds.
#         window.after(180, window.update())


        
# # give the buttons functionality
# button1.config(command=newPage)
# button2.config(command=startPage)


# # call the startPage method
# startPage()

# # display the window
# window.mainloop()


# # Random Word Generation
random_words = ["add", "aid", "air", "age", "act", "aim", "axe", "art", "ace", "across", "admit", "ache", "annoy", "agent", "alarm",
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
                "juice","jumbo", "jump", "jar", "jive", "know", "kind", "kneel", "kin","keen", "keep", "kept", "kick", "knit", "knob",
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

# # # The index for the random word in the array
# num = random.randint(0, len(random_words))

# The value of the random word in the array
# word = random_words[num]

# Pronouncing has a 'rhymes' method for getting a list of rhymes for words.
rhymeList = retrieve.rhymes(sys.argv[1])

print("Words that rhyme with " + sys.argv[1] + ":")

# A for loop to print every word in the list of words
for rhyme in rhymeList: print(rhyme)





number =  round(5 % 1)
print(str(number))



''' Rhyme Accuracy/Avg Time Example

number = round(10/17, 3)
print(str(number * 100) + "%")

'''
