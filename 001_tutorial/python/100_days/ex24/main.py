# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()


# with open('my_file.txt') as f:  # another options without  close file
#     contents = f.read()
#     print(contents)


# with open('my_file.txt', mode='a') as f:  # another options without  close file
#     f.write("\nnew text")


with open('new_file.txt', mode='w') as f:  # another options without  close file
    f.write("\nnew text")
