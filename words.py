'''Retrieve and print words from a URL

Usage:

    python 3 words.py <url>
'''

import sys
from urllib.request import urlopen

def fetch_words(url):
    '''Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 document.

    Returns:
        A list of strings containing the words from the document.
    '''
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split() # .decode('utf-8') will decode bytes to string.
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    '''Prints items one per line

    Args:
        An iterable series of printable items.
    '''
    for item in items:
        print(item)

def main(url): # We defined this so as to be able to test from the REBL.
    '''Print each word from a text document from a URL

    Args:
        url: The URL of a UTF-8 document.
    '''
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
    # sys.argv is a list in Python, which contains the command-line arguments passed to the terminal.

 #http://sixty-north.com/c/t.txt

# In REPL __name__ is words. 