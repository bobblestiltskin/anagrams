Exercise: Anagram Finder

Specification
You are developing software for a crossword website and have been asked to write an anagram finder.
The anagram finder, given a text file as input, must print any anagrams it detects to standard output. That is, for each
anagram word found in the supplied file, a line should be printed to standard output containing all anagrams of that
word found in the same file. If there are no anagrams in the file, print no anagrams found to standard output. Any
anagrams which are found should be output in the order they are found within the file.

Notes
You are not given a dictionary of anagrams as input. Think of the input file as a self contained collection of words, in
which you are looking for anagram sets.
You do not need to find combinations of words which are anagrams of other combinations of words.

Examples

| Input                   | Output           |
|--------------------------------------------|
| the quick brown fox     | no anagrams found|
|--------------------------------------------|
| eat my tea              | eat tea          |
|--------------------------------------------|
| do or door no no        | no anagrams found|
|--------------------------------------------|
| pots stop pots spot stop| pots stop spot   |
|--------------------------------------------|
| on pots no stop eat     | on no            |
| ate pots spot stop tea  | pots stop spot   |
|                         | eat ate tea      |
|--------------------------------------------|
