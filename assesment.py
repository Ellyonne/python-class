#sentences = ['no worries', 'time heal pain', 'black december', 'ladder of success']
#def longest_words(lst):
 #   longest = ' '
  #  for word in lst:
   #     if len(word.split(' ')) > len(longest.split(' ')):  
    #        longest  = word
    #return longest
#longest = longest_words(sentences)
#print(longest)




random_stuff = ['hello', '23', '3.4','night', 'welcome']

def get_on_string_with_characters(lst):
    return[value for value in lst if value.isalpha()]
print(get_on_string_with_characters(random_stuff))