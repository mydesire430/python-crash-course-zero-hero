#Write a script that returns a sentence with the words reversed
sentence = "we work everyday"
word_list = sentence.split()
reversed_list = word_list[:: -1]
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)

#Write a script that returns a sentence with the words reversed
sentence = "compaction test is the priority"
word_list = sentence.split()
reversed_list = reversed(word_list)
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)