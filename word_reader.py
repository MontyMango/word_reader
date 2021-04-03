class count:
    def __init__(self):
        self.lst = []
        with open('readfrom.txt') as Read:
            self.text = Read.read()
        self.text.split()
        self.inn = ""
        self.lst = []
        self.dictionari = {}
        self.num = 1

    def Count(self):
        for i in self.text:
            if i != " ":                # if i doesn't equal a new sentence
                self.inn += i           # add the new letter to form the word again
            elif i == " ":                  # if there's a new sentence
                self.lst.append(self.inn)   # puts inn in list
                self.inn = ""               # resets inn
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
        #for x in self.dictionari:
        print(self.dictionari)
c = count()
c.Count()