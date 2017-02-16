def filter_string(a):
  new_s=""
  for i in a:
    if i >= "a" and i <= "z":
      new_s+=i
    else:
      new_s+=" "
  return(new_s)



def main():
  # open book
  book = open("hard_times.txt","r")

  # create a dictionary for word count
  word_dict={}

  # total numerof words
  total_words=0

  # read book line by line
  for line in book:
  # remove leading and trailing space
    line=line.strip()

    # lower case
    line line.lower()

    # filter the line
    line =filter_string(line)

    # get the words in the line
    word_list=line.split()

    # add words to the dictionary
    for word in word_list:
      total_words+=1
      if words in word_dict:
        word_dict[word]=word_dict[word]+1
      else:
        word_dict[word]=1

    # close
    book.close()

    print(total_words)

    # print unique word
    num_unique=len(word_dict)
    print(num_unique)


    # retio of unique to total words
    ratio=num_unique/total_words

    # word frequency
    all_words=list(word_dict.keys())
    all_words.sort()
    for word in all_words:
      print(word+str(word_dict[word]))

    freq_dict={}
    for word in word_dict:
      freq=word_dict[word]
      if freq in freq_list:
        (freq_dict(freq)).append(word)
      else:
        new_list=[]
        new_list.append(word)
        freq_dict[freq]=new_list

    # print according to frequency
    all_freq=list(freq_dict.keys())
    all_freq.sort()
    all_freq.reverse()
    for freq in all_freq:
      print(str(freq)+":"+freq_dict[freq])
