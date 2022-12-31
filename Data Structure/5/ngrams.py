#
# Dissociated Press
#


# 16102275 Park Hyun Woo 16102284 Lee sung Ho

import random

# Read a text file and return a list of words
def read_text(fname):
  fd = open(fname, "r",encoding='UTF8')
  wl = [ "." ]
  for s in fd.readlines():
    line = s.rstrip()
    words = line.split()
    for w in words:
      word = w.rstrip(",.':;?!-_\"").lstrip('\'"_').lower()
      wl.append(word)
      if w[-1] == "." and w.lower() != "dr.":
        wl.append(".")
  return wl

# take a list of words, and return set of all n-grams
def find_ngrams(wl, n):
  if n>len(wl):
      raise "Error"
  ngrams=[]
  
  for i in range(0,len(wl)-n+1):
      B=[]
      for k in range(0,n):
          B.append(wl[i+k])
      B=tuple(B)
      ngrams.append(B)
  

  return ngrams

# given a set of ngrams, return a list of ngrams whose first word is "."
def find_starters(ngrams):
    
    ngrams=list(ngrams)
    starters = []
    for i in range(0,len(ngrams)):
        if(ngrams[i][0]=="."):
            starters.append(ngrams[i])
    
    ngrams=set(ngrams)
    return starters
    

# take set of n-grams, and return a map that maps (n-1)-grams
# to the set of all possible last words
def make_ngram_map(ngrams):
  length = len(ngrams[0])
  ngram_map={}
  
  for i in range(0,len(ngrams)):
      Value=set()
      Value.add(ngrams[i][length-1])
      for k in range(0,len(ngrams)):
          if ngrams[i][0:length-1]==ngrams[k][0:length-1]:
              Value.add(ngrams[k][length-1])
              
      ngram_map[ngrams[i][0:length-1]]=Value
  return ngram_map  
  
def print_word(w):
  if w != ".":
    print(" ", end="")
  print(w, end="")

#
# Generate and print a text consisting of count words,
# 
def dissociated_press(fname, n, count):
  words = read_text(fname)
  ngrams = find_ngrams(words, n)
  ngmap = make_ngram_map(ngrams)
  # start with a random n-gram that starts with a "period"
  starters = find_starters(ngrams)
  current = random.choice(starters)
  # skip period at the beginning and print first word without leading space
  print(current[1], end="")
  for w in current[2:]:   
    print_word(w)
  wcount = n
  while wcount < count:
    head = current[1:]                # take last n-1 words printed so far
    choices = ngmap.get(head)         # find n-grams starting with head
    if choices is None:
      print()
      return                          # cannot continue
    w = random.choice(list(choices))  # pick a random word 
    current = head + (w,)
    print_word(w)
    wcount += 1
  print()

if __name__ == "__main__":
  dissociated_press("seoultech.txt", 2, 100)
  print()
  dissociated_press("independence.txt", 3, 100)
  print()
  dissociated_press("president.txt", 3, 100)
  print()
  dissociated_press("alice.txt", 4, 200)
