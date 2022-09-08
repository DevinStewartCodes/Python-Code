#Sys Random used here

import sys, random

#List of rude names - names added here will randomly appear in list
name = ('Ader Titsoff','Adolf Oliver Nipple','A. Nellsechs','A. Nelprober',
'A.S. Muncher','Amanda D. P. Throat','Amanda Hugginkiss','Amanda Hump',
'Amanda Lick','Amanda Mount','Amanda Poker','Andy Cornholder',
'Andy Feltherbush','Andy Felthersnatch','Anita B. Jainow','Anita Bath',
'Anita Dick','Anita Dickenme','Anita Dump','Anita Fartinghouse',
'Anita Hanjaab','Anita Hardcok','Anita Head','Anita Hoare','Anita Naylor',
'Annie Position','Anya Neeze','Annie Position','Banana Hammock','Bartolos Colonoscopy',
'Bea O’Problem','Ben Derhover','Ben Gurgen Hoffe','Ben N. Syder','Ben O. Verbich',
'Ben R. Over','Benoit Bawles','Berry McCaulkiner','Betty Drilzzer','Betty Humper',
'Betty Humpter','Betty Phuckzer','Bruce D. Cocque', 'Bo N. Herr','Brooke N. Rubbers','Bruce D. Cocque',
'Bruce D. Lipps','Buck Nekkid','Buster Cherry','Buster Himen','Clee Torres','C. Mike Rack',
'Cole Ostamie','Colin Forsecs','Connie Lingus','Craven Moorehead','Curley Pubes',
'Dang Lin-Wang','Daryl B. Payne','Dick Long','Dick Myaz','Dick Nose','Dick Pound',
'Dick Ramdass','Dick Raasch','Dill Doe','Dixie Normous','Dixie Rect',
'Dixon B. Tweenerlegs','Dixon Butts','Dixon Kuntz','Drew Peanoze','E. Norma Scock',
'E. Norma Stits','E. Normous Peter','E. Rex Sean','Eaton Beaver','Eileen Ulick',
'Eaton Beaver','Eileen Ulick','Fluffy Cookie','Gazzy Colon','Harry Azcrac','Harry Cox','Harry Johnson',
'Hairy Poppins','Heywood Japulmah Finga','I. C. Yadick','I. P. Freely','Ivana Tinkle','Jenny Tayla',
'Kenny Dewitt','Laffmy Titsoff','Kareem O’Weet','Lance Lyde','Lee Keyrear','Lee Nover','Leo Tarred',
'Lipin Jection','Lou Briccant','Lon Moore','Lou Sirr','Luke Atmyass','Madka Owdiseez',
'Martha Fokker','Marion Money','Mark Z. Spot','Mary Juana','Master Bates','May I. Tutchem',
'Maya Buttreeks','Max E. Mumm','Max E. Pad','Mel Keetehts','Michael Toris','Mike Rotchburns',
'Miya Buttreaks','Nadia Seymour','Nick O’ Teen','Oliver Closeoff','Ollie Tabooger','Pat Myaz',
'Patty Meltt','Phil Down','Peter Pantz','Pierre Pants','Phil Accio','Poppa Woody','Rhoda Hotte',
'Robin D. Craydle','Roch Myaz','Ron Chee','Rueben G. Spaut','Sal Ami','Semour Asscrack','Seymour Buttz',
'Sheeza Freak','Stella Virgin','Ura Snotball','Vye Agra','Vye Brator','Wayne Kerr','Willie B. Hardigan',
'Willie Eetmioutt','Willie Layer','Wilma Dickfit','Wilma Fingerdoo','Yuri Nator')

#Code starts here:
print("Welcome to the Ministry of Rude Names!\n")
while True:
    yes = input("Would you like a randomly selected Rude Name? ")
    if yes.lower() == "yes":
        yes = input("Are you sure? Some of these are pretty rude! ")
        if yes.lower() == "yes":
            rudeName = random.choice(name)
            print("\n")
            print("     ",rudeName,"     ")
            print("\n")
    yes = input("Would you like another? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
    yes = input("Would you like another? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
        break
while True:
    yes = input("Would you like another Daddy? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
    yes = input("Would you like another Daddy? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
    yes = input("Would you like another Daddy? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
        break
while True:    
    yes = input("Do you love me Senpai? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
    yes = input("Do you really love me Senpai? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
        break
while True:
    yes = input("Here is another rude name Senpai, okay? ")
    if yes.lower() == "yes":
        rudeName = random.choice(name)
        print("\n")
        print("     ",rudeName,"     ")
        print("\n")
    else:
        try_again = input("\nAre you sure? (Press Enter for another or yes to quit)\n")
        if try_again.lower() == "yes":
            break
input("Press Enter to Exit.")
