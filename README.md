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

## Day3
- slow going, this time due to some subtle errors 
- overall approach is not very optimised, lots of room for improvement
- parse data, find numbers, store a list of values, and the starting coordinate of each number, also store a separate list of every non. symbol encountered with its coordinates
- for each number in our number list, check all adjacent values for a symbol (against the symbol list with coords) (wildly inefficient, as it checks every symbol against every number, but it works through brute force)
- variation on this for part2, create a dict of * symbols, add to a list with the value of an adjacent number when found, look for all lists that are length2, and get product / sum etc. was fairly simple
- nothing terribly difficult, just kept making subtle errors and eventually had to fix test data and double-check coords by hand of test data which solved

## Day4
- easier today, a few minor issues with spacing etc. and removing multiple spaces
- let me play wtih sets / intersection which was easier way to find matches between lists
- part2 was tricky at first but breaking down wasn't that hard in the end

## Day5
- toughest so far
- solved part1 on my own
- had to consult the forums for part2
- best solution i found: https://topaz.github.io/paste/#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

##Day6
- quite challenging

##Day7
- solved part1 ok
- challenge with part2, used external solution from forum and fighting with it for a while

##Day8
- part1 fairly straightforward
- struggled with part2, eventually looked at forums.  Saw references to LCM and realized that the cycles must repeat
- with this info, used lcm function to calculate the lowest common multiple of the repeat time for each one
- GPT was essential on this one to help with syntax of math.lcm function etc. 

##Day9
- a really fun one, used a 'pyramid' data structure with a dict to store the reduced lists. 
- this let me do things like max(pyramid) to get the number of levels etc. 
- overall fun, straightforward and didn't require a lot of math

##Day10
- lots of fun with this one
- had to lookup the ray tracing algorithm in part2 (with GPT), once i had that, was fairly straightforward to write a function to check and position and determine if inside or outside the loop
- takes a few seconds to run but works. could be optimized a lot further

##Day11
- also really fun
- typical AOC challenge where naive solution in part1 does not help in part2
- resttarted with a substitution approach rather than just naively inserting empty rows
- calculated new coords based on nubmer of X's found in slice vertically and horizontally
- some 'off by one' fun but otherwise was nice puzzle