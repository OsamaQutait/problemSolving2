if __name__ == '__main__':
    # Python program to convert a list
    # to string using join() function

    # Function to convert
    def listToString(s):
        # initialize an empty string
        str1 = " "

        # return string
        return (str1.join(s))


    # Driver code
    s = ['Geeks', 'for', 'Geeks']
    print(listToString(s))
