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
        
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.getSubject()
        return self.isWordIn(text)
    
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.getSummary()
        return self.isWordIn(text)
        
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase
    
    def evaluate(self,story):
        return self.phrase in story.getTitle() or self.phrase in story.getSummary() or self.phrase in story.getSubject()

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    newStories = []
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story):
                newStories.append(story)

    return newStories
