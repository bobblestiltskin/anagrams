# this takes as input a text file and outputs any anagrams in the order found in the file

def is_anagram(s1, s2):
# returns True if the second string is an anagram of the first
  if len(s1) != len(s2):
    return False

  if s1 == s2:
    return False

  s1list = list(s1)
  s1list.sort()

  s2list = list(s2)
  s2list.sort()

  for i in range(0, len(s1list)):
    if s1list[i] != s2list[i]:
      return False

  return True

def check_words(word, testwords):
# checks a word against a list of words and returns 
# a set of all anagrams of the first word
# if there are anagrams of the first word in the list
  myset = set()
  for testword in testwords:
    if (is_anagram(word, testword)):
      myset.add(testword)
  if myset:
    myset.add(word)
  return myset

f = open("textfile.txt", "r")
words = f.read().split()

setlist = []
while (len(words) > 1):
  myset = check_words(words[0], words[1:])
  if myset:
# walk the list of words and find the first occurrence of each word
    mylist = []
    for word in words:
      if word in myset and word not in mylist:
          mylist.append(word)

# remove all the words in our set from the list of words
    for element in myset:
      for word in words:
        if word == element:
          words.remove(word)

    if mylist:
      setlist.append(mylist)
  else:
    del words[0]

if setlist:
  for s in setlist:
    for e in s:
      print(e, end =' ')
    print()
else:
  print("no anagrams found")
    
f.close
