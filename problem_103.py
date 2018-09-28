


#Given a string and a set of characters, return the shortest substring containing all the characters in the set.
#For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

#
#Make a histogram of the second string's characters (key operation is hist2[ s2[i] ]++).
#Make a cumulative histogram of the first string's characters until that histogram contains every character that the second string's histogram contains (which I will call "the histogram condition").
#Then move forwards on the first string, subtracting from the histogram, until it fails to meet the histogram condition. Mark that bit of the first string (before the final move) as your tentative substring.
#Move the front of the substring forwards again until you meet the histogram condition again. Move the end forwards until it fails again. If this is a shorter substring than the first, mark that as your tentative substring.
#Repeat until you've passed through the entire first string.
#The marked substring is your answer.


def checkString(aStr, mStr):
    if len(aStr) < 0 or len(aStr) < len(mStr):
        return [], False
    
    my_dict = {}


def newShortest(subString, string):
  myChars = set(subString)
  smallest = ""
  current={}
  for i, char in enumerate(string):
    if char in myChars:
      current[char] = i
      if len(current) == len(myChars):
        temp = string[current[min(current,key=current.get)]:current[max(current,key=current.get)]+1]
        if len(temp) < len(smallest) or len(smallest) == 0:
          smallest = temp
  print(smallest)
  print(current)
  return smallest



print(newShortest("figehaeci", 'aei'))



