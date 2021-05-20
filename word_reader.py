import os
from time import sleep

class count:
    def __init__(self):
        self.lst = []
        print("Read from readfrom.txt file?")
        a = input("[y or n]: ")
        if a == 'y':
            try:
                with open('readfrom.txt','rt') as Read:
                    self.text = Read.read()
                self.a = open('results.txt','wt')
                self.rite = 1
            except:
                self.rite = 0
                print("\n\n\n\n\nCouldn't find file...\n\nPlease input anything for the program to read it.\n")
                self.text = input()
        elif a == 'n':
            self.rite = 0
            print("Input anything below to be analysed and read by the program.\n")
            self.text = input()
        #with open('options.txt', 'rt') as Options:
        #    self.optionsw = Options.write()
        self.inn = ""
        self.lst = []
        self.dictionari = {}
        self.num = 1

        # Option to be implemented later
   # def Options(self):
   #     print("Ready to analysis the text word by word? Or do you need to change something?")
   #     inp = input("> ")
   #     if inp == "change":
   #         print("What would you like to change?\n1. Ignore newline \"\\n\""\n2. Ignore ?'s\n3. Ignore .'s\n",
    #               "4. Ignore !")
    def Count(self):
        for i in self.text:
            i = i.lower()
            if i != " ":                # if i doesn't equal a new sentence
                if i == "\\n":
                    i = None
                elif i == "?":
                    i = None
                elif i == ".":
                    i = None
                elif i == "!":
                    i = None
                elif i == ",":
                    i = None
                elif i == "\n":
                    i = None
                elif i == "\"":
                    i = None
                elif i == "-":
                    i = None
                if i == None:
                    self.lst.append(self.inn)  # puts inn in list
                    self.inn = ""  # resets inn
                elif i != "":
                    self.inn += i           # add the new letter to form the word again
            elif i == " ":                  # if there's a new sentence
                self.lst.append(self.inn)   # puts inn in list
                self.inn = ""               # resets inn
                i = ""
        self.lst.append(self.inn)           # catches the last word and puts it in the list
        self.lst.sort()
        self.Countup()

    def Countup(self):
        for i in self.lst:
            if i not in self.dictionari:
                self.num = 1
                self.dictionari[i] = self.num
            elif i in self.dictionari:
                self.num+=1
                self.dictionari[i] = self.num
        self.Display()

    def Display(self):
        for word,num in self.dictionari.items():
            a = str(f"Word: {word} --> Said:{num}\n")
            print(a,end='')
            if self.rite == 1:
                self.a.write(a)
        print("\n\nResults have been printed to the results.txt file too.\n")
        sleep(2)
        print("Thanks for using word_reader!")
        sleep(1)
        if self.rite == 1:
            self.a.close()

c = count()
c.Count()