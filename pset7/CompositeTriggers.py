class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):
        newtext = text.lower()
        L = list(newtext)
        for count in range(len(L)):
            for punct in string.punctuation:
                if L[count] == punct:
                    L[count] = ' '
        string1 = ''.join(L)
        L2 = string1.split()
        return self.word.lower() in L2
        
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.getTitle()
        return self.isWordIn(text)

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)
    
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
    

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
