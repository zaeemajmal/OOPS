class flashcards:
    def __init__(self,w,m):
        self.w = w
        self.m = m
    def __str__(self):
        return(self.w  + "(" + self.m + ")")

flashcard = []
while True:
    word = input("Enter name you want add to your flashcard:- ")    
    meaning = input("Enter meaning of that word:- ")
    ob = flashcards(word,meaning)
    flashcard.append(ob)
    c = input("Enter 0 if u want to continue else enter 1:-")
    if c=="0":
        pass        
    elif c == "1":
        break
    else:
        print("invalid input")
for i in flashcard:
    print("--> " , i)        
    