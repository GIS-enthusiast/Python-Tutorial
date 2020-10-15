import sys
from urllib.request import urlopen

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split() #.decode('utf-8') will decode bytes to string.
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url): #We defined this so as to be able to test from the REBL.
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1]) #sys.argv is a list in Python, which contains the command-line arguments passed to the script.

 

