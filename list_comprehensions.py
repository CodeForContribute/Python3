# A list comprehension generally consist of these parts :
#    Output expression,
#    input sequence,
#    a variable representing member of input sequence and
#    an optional predicate part.
if __name__ == '__main__':
    ######################## squaring numbers in a given range if number is odd ##################
    lst = [x ** 2 for x in range(1, 11) if x % 2 == 1]
    print(lst, end=" ")

    ############### Power of 2#################################################
    print("\n")
    power_2 = [2*x for x in range(1,9) if x %2 == 0] # if the given number is even or odd
    print(power_2, end=" ")
    print("\n")
    power_3 = [3 * x for x in range(1, 9) if x % 2 == 0]  # if the given number is even or odd
    print(power_3, end=" ") # similary we can find power of any number

    ######################### Loweirng the characters ######################################
    print("\n")
    print([x.lower() for x in 'ADFRTGGG'])
    a = [x.lower() for x in 'ADFRTGGG']
    stop_index = 4
    print(a[:stop_index:2]) # print the list form start_index = 0 to stop_index-1 in step of 2
    print(a[::-1]) # print the list in reverse order

    #######################################################################################
    print("\n")
    a = 5
    table = [[a, b, a*b] for b in range(a,9) if b %2 == 0]
    print(table, end=" ")

    ############## Use of Filter Functions ####################################################
    # filter(function=, iterable=)
    # So filter takes 2 arguments one is functions mostly-> lambda and second is iterables -> list
    print("\n")
    lst = list(filter(lambda x: x % 5 == 0,[x ** 2 for x in range(1, 11) if x % 2 == 1]))
    print(lst)

    ############ Multiplying a list with a given number ##########################################
    print("\n")
    lst = [1,3,2]
    print(lst * 2) # it justs populate list with a given number of times(2 in this case) within the same list

    ####################################################################################################
    list1 = [3, 4, 5]
    new_multiplied_list = [item * 2 for item in list1]
    print(new_multiplied_list)
    print("\n")
    listOfWords = ["this", "is", "python", "tutorial", "from", "intellipaat"]
    new_list = [word[0] for word in listOfWords]
    print(new_list)