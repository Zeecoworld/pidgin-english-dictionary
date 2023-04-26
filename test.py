
from __init__ import getMeaning

typed_desired_word = input("enter yr desired word here")

meaning = getMeaning(typed_desired_word)
print(meaning)

#printing meaning of the word in console
# if type(meaning) == list:
#     for item in meaning:
#         print(item)
# else:
#     print(meaning)