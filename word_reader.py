class count:
    def __init__(self):
        self.lst = []
        with open('readfrom.txt','rt') as Read:
            self.text = Read.read()
            # Options to be implemented later...
        #with open('results.txt','wt') as Results:
        #    self.write = Results.write()
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
            if i != " ":                # if i doesn't equal a new sentence
                if i == "\\n":
                    i = ""
                    continue
                elif i == "?":
                    i = ""
                    continue
                elif i == ".":
                    i = ""
                    continue
                elif i == "!":
                    i = ""
                    continue
                elif i == ",":
                    i = ""
                    continue
                elif i == "\n":
                    i = ""
                    continue
                elif i == "\"":
                    i = ""
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
            p = print(f"Word: {word} --> Said:{num}")
 #           self.write(p)
c = count()
c.Count()