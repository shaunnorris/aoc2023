# aoc2023
- input files ommitted, tests inline
- co-pilot and GPT-4 used for syntax / hints
- TDD with some AI help in auto-completing, setting up test cases etc.

## Day1

### First used a crude solution
- started just finding all the digits, adding to a list, then taking the first and last element of list. (worked from fine for part1 which was fairly trivial)
- once part2 came along with spelled out digits, first tried this again, and thought i would replace each spelled instance with a digit (this breaks the 'dont mutate data rule' but it seemed ok at the time.
- this solution was finally bodged together enough to work by replacing the first letter of each spelled word, and then replacing that with it's equivalent digit, and then feeding that to the function from part1 to find first/last digit. 
- why crude? we only care about first and last... some strings very long and this approach both mutated the data, and checked a bunch of irrelevant data by finding every digit in order to get first/last. 
- can see first approach in _old functions

### Improved solution
- After a chat with Phil in the office, improved with 'read from the ends' strategy
- read in the string character by character, if you find a digit, return it... otherwise keep a LIFO stack of characters read, and once you have at least 3, start checking for spelled digits
- once you have 5 characters, need to pop oldest before adding a new one, this way stack never goes above 5 and is a sort of sliding window along the string. Use a lookup table mapping spelled digit to integer and return the integer once you find a spelled digit in the stack
- by having 2 lookup tables, one for forward and reverse spelling, we could use the same logic and just feed the string in reverse order to get the last digit. used a simple 'direction' switch to choose which lookup table to use. 

## Day2
- easier if you read the question properly. spent a while adding up all colours per game first, and then wondering why didn't work. This also let the test cases pass so was a mystery who final answer wasn't correct. After more caffeine, things were easier.
- basic strategy was parse each game into a dictionary, with a key for id, and each colour
- from there, two functions then can take a game string line, and find whether its possible or not, or compute its power from part2
- mostly tedious in setting up tests cases, but choices of data structure etc. were fairly straightforward