def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handCopy = hand.copy()
    for i in word:
        handCopy[i] -= 1    
    return handCopy

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handCopy = hand.copy()
    wordDic = {}
    for i in word:
        wordDic[i] = wordDic.get(i, 0) + 1
    count = 0
    for j in word:
        count += wordDic[j] <= handCopy.get(j, 0)
    return count == len(word) and word in wordList

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total = 0
    handNew = hand.copy()
    while calculateHandlen(handNew) >= 0:
        if calculateHandlen(handNew) == 0:
            print 'Run out of letters. Total score:', total, 'points.'
            break
        print 'Current Hand:', displayHand(handNew)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            print 'Goodbye! Total score:', total, 'points.'
            break
        elif not isValidWord(word, handNew, wordList):
            print 'Invalid word, please try again.'
            print
        else:
            total += getWordScore(word, n)
            print str(word), 'earned', getWordScore(word, n), 'points.', 'Total:', total, 'points'
            print
            handNew = updateHand(handNew, word)

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    while True:
        user = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user == 'n':
            n = HAND_SIZE
            hand = dealHand(n)
            playHand(hand, wordList, n)
        elif user == 'e':
            break
        elif user == 'r':
            try:
                playHand(hand, wordList, n)
            except:
                print 'You have not played a hand yet. Please play a new hand first!'
        else:
            print 'Invalid command.'  

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    score = {}
    try:
        for word in wordList:
            if isValidWord(word, hand, wordList):
                score[word] = score.get(word, 0) + getWordScore(word, n)
        return max(score, key = score.get)    
    except:
        return None

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0
    handNew = hand.copy()
    while True:
        print 'Current Hand:', 
        displayHand(handNew)
        compWord = compChooseWord(handNew, wordList, n)
        if compWord != None:
            total += getWordScore(compWord, n)
            print '"'+ str(compWord) + '"', 'earned', getWordScore(compWord, n), 'points.', 'Total:', total, 'points'
            handNew = updateHand(handNew, compWord)
            if calculateHandlen(handNew) == 0:
                print 'Total score:', total, 'points.'
                break
        else:
            print 'Total score:', total, 'points.'
            break

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)"""
    

    while True:
        user = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user == 'n':
	   while True:
	       user_n = raw_input('Enter u to have yourself play, c to have the computer play: ')
	       n = HAND_SIZE
	       hand = dealHand(n)
	       if user_n == 'u':
	           playHand(hand, wordList, n)
	           break
	       elif user_n == 'c':
	           compPlayHand(hand, wordList, n)
	           break
	       else:
	           print 'Invalid command.'
        elif user == 'r':
            while True:
                try:
                    len(hand) > 0
                    user_r = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if user_r == 'u':
                        playHand(hand, wordList, n)
                        break
                    elif user_r == 'c':
                        compPlayHand(hand, wordList, n)
                        break
                    else:
                        print 'Invalid command.'  
                except:
                    print 'You have not played a hand yet. Please play a new hand first!'
                    break         
        elif user == 'e':
            break
        else:
            print 'Invalid command.'

