#! /usr/bin/env python

def main():             # Don't leave code in the global namespace - it runs slower
    import sys

    N = int(raw_input())

    list_of_strings = []
    smallest_string_length = 101 
    smallest_string = ''
    next_input_string = ''

    for count in xrange(N):
        next_input_string = str(raw_input())
        list_of_strings.append(next_input_string)
        if len(next_input_string) < smallest_string_length:
            smallest_string = next_input_string
            smallest_string_length = len(smallest_string)

    possibles_list = list(smallest_string)

    possibles_dict = {}

    for x in possibles_list:
        if x in possibles_dict:
            possibles_dict[x] = possibles_dict[x] + 1
        else:
            possibles_dict[x] = 1

    for character in list(set(possibles_list)):
        for a_string in list_of_strings:
            occurrences = a_string.count(character)
            if occurrences < possibles_dict[character]:
                possibles_dict[character] = occurrences

    results = []

    for key in possibles_dict:
        while possibles_dict[key] > 0:
            results.append(key)
            possibles_dict[key] -= 1

    results.sort()

    if len(results) == 0:
        print "no such string"
    else:
        for x in results:
            sys.stdout.write(x)
   
main()
