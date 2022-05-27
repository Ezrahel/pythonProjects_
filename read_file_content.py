# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    filename=open("story.txt")
    filename=filename.read()
    return filename

def count_word():
    word=read_file_content("./story.txt")
    dictKey={}
    count=word.split()
    for i in count:
        dictKey[i]=count.count(i)
    return dictKey
print(count_word())
