# Docstrings
###### date: 4/10/2020
---

How to add self documenting capabilty to our own module.
API documentation in python3 uses a facility called docstrings

!!! note docstrings
- Literal strings which document functions, modules and classes.
- They must be the first statement in the block for these constructs
!!!


!!! note SphinX
Tool to create HTML documentation from Python docstrings.
!!!

```python
def fetch_words(url):
    """Fetch a list of words from a URL.

        Args:
            url: The URL of a UTF-8 text document.

        Returns:
            A list of string containing the words from the document.
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()  
        for word in line_words:
            story_words.append(word)
    story.close( ) 
    return story_words
```
and if we run 
```bash 
>> from words.py import *
>> help(fetch_words)
```
youll get:

Help on function fetch_words in module words:
```bash
fetch_words(url)
    Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    
    Returns:
        A list of string containing the words from the document.
(END)
```
---

!!! note PostScriptum
Module docstring should be at the beginning of any module
!!!

```python 
"""Retrive and print words from a URL.

Usage:

    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

        Args:
            url: The URL of a UTF-8 text document.

        Returns:
            A list of string containing the words from the document.
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()  
        for word in line_words:
            story_words.append(word)
    story.close( ) 
    return story_words

def print_items(items):
    """Print items of list one per line.

        Args:
            An iterable series of printable items.
    """
    for word in items:
        print(word)

def main(url):
    """Print each word from a text document from at a URL.

        Args:
            url: The URL of a UTF-8 text document.
   """
    words = fetch_words(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1])
  
```