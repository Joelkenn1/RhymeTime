-- CREATE DATABASE RhymeDatabase;
CREATE TABLE Users (
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Email VARCHAR(100) unique,
	Username VARCHAR(100),
    Password_ VARCHAR(100),
    XP INT default 0,
    lvl INT DEFAULT 1,
    Time_Sum Integer,
    Score_Sum Integer,
    Input_Count Integer, 
    High_Score Integer DEFAULT 0,
    Average_Time Integer,
    Rhyming_Accuracy VARCHAR(100),
    Rhyme_Streak Integer,
    
    primary key (Username, Email)
);

CREATE TABLE Badges (
	Name VARCHAR(100),
    Description VARCHAR(2000),

    primary key (Name)
);

CREATE TABLE Reviews (
    reviewID int AUTO_INCREMENT,
    Username VARCHAR(100),
	Rating Integer,
    Review VARCHAR(4000),

    primary key (reviewID)
);

CREATE TABLE Reports (
    reportID int AUTO_INCREMENT,
    Username VARCHAR(100),
    Email VARCHAR(100),
    Report VARCHAR(4000),
    
    primary key (reportID)
);

CREATE TABLE Contacts (
	Dev_Name VARCHAR(100),
	Dev_Email VARCHAR(100),
    
    primary key (Dev_Name)
);

CREATE TABLE Single_Game(
    singleID int AUTO_INCREMENT,
    Username VARCHAR(100),
    Learned VARCHAR(100),
    Well_Done VARCHAR(100),
    APTR VARCHAR(100),
    Master_Class VARCHAR(100),

    primary key (singleID)
    
);

insert into Contacts values("Caleb Kenney", "c.joel45@icloud.com");
insert into Contacts values("Christian Ramsey", "camram007@icloud.com");
insert into Contacts values("Sean Michals", "michalsfamily3@icloud.com");



insert into Badges values("All-Time Leading Scorer", "Your All-Time Points Must Be The Greatest Among All Players.");
insert into Badges values("All-Day Long", "Your Total Play Time Must Be The Greatest Among All Players.");
insert into Badges values("It's Time To Rhyme", "Your Rhyming Accuracy Must Be Greater Than Or Equal To 40.");
insert into Badges values("Show It To A Poet", "Your Rhyming Accuracy Must Be Greater Than Or Equal To 60.");
insert into Badges values("Rhymes Like Dimes", "Your Rhyming Accuracy Must Be Greater Than Or Equal To 80.");
insert into Badges values("MC", "Your Rhyming Accuracy Must Be Greater Than Or Equal To 90.");
insert into Badges values("Flying", "Your Average Time Per Word Must Be Less Than Or Equal To 2.");
insert into Badges values("Elite", "Your Level Must Be Greater Than Or Equal To 5.");
insert into Badges values("Expert", "Your Level Must Be Greater Than Or Equal To 4.");
insert into Badges values("Pro", "Your Level Must Be Greater Than Or Equal To 3.");
insert into Badges values("Average Joe", "Your Level Must Be Greater Than Or Equal To 2.");
insert into Badges values("Rookie", "Your Level Must Be Greater Than Or Equal To 1.");
insert into Badges values("10+ Club", "Obtain A High Score Of 10 Or More Points.");
insert into Badges values("15+ Club", "Obtain A High Score Of 15 Or More Points.");
insert into Badges values("20+ Club", "Obtain A High Score Of 20 Or More Points.");
insert into Badges values("One-Of-One", "Reach The Top Of The Leaderboard.");



-- Single Game Badges
insert into Badges values("Efficiency", "Enter 15 Consecutive Correct Rhymes.");
insert into Badges values("Nothing But Rhymes", "Enter 25 Consecutive Correct Rhymes.");
insert into Badges values("Can't Stop, Won't Stop", "Enter 40 Consecutive Correct Rhymes.");
insert into Badges values("Legendary Rhymes", "Enter 50 Consecutive Correct Rhymes.");
insert into Badges values("Learned", "Obtain A Score Of 5 Or More Points With 3 Or Less Incorrect Rhyme Inputs.");
insert into Badges values("Well Done", "Obtain A Score Of 10 Or More Points With 3 Or Less Incorrect Rhyme Inputs.");
insert into Badges values("A Performance To Remember", "Obtain A Score Of 15 Or More Points With 3 Or Less Incorrect Rhyme Inputs.");
insert into Badges values("Master Class", "Obtain A Score Of 20 Or More Points With 3 Or Less Incorrect Rhyme Inputs.");
insert into Badges values("Rapid Rhyming", "Enter 3 Correct Rhymes In 3 Seconds Or Less");
insert into Badges values("Speed Round", "Enter 3 Correct Rhymes In 4 Seconds Or Less");
insert into Badges values("Pace Posthaste", "Enter 3 Correct Rhymes In 5 Seconds Or Less");