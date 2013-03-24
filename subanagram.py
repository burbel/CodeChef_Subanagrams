#! /usr/bin/env python

def main():    # Don't leave the code in the global namespace, it runs slower
    import sys

    N = int(raw_input())

    list_of_strings = []
    smallest_string_length = 101 
    smallest_string = ''
    temp_string = ''

    for count in xrange(N):
        temp_string = str(raw_input())
        list_of_strings.append(temp_string)
        if len(temp_string) < smallest_string_length:
            smallest_string = temp_string
            smallest_string_length = len(smallest_string)

    search_set = list(smallest_string)

    results = {}

    for x in search_set:
        if x in results:
            results[x] = results[x] + 1
        else:
            results[x] = 1

    for character in list(set(search_set)):
        for strings in list_of_strings:
            occurrences = strings.count(character)
            if occurrences < results[character]:
                results[character] = occurrences

    result_set = []
    for key in results:
        while results[key] > 0:
            result_set.append(key)
            results[key] -= 1

    result_set.sort()

    if len(result_set) == 0:
        print "no such string"
    else:
        for x in result_set:
            sys.stdout.write(x)
   
main()
