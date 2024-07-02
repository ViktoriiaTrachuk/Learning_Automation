def shifter(st):
    shifter_chars = ('HINOSXZMW')

    words = st.split()

    unique_shifters = set()

    for word in words:
        if all(char in shifter_chars for char in word):
            unique_shifters.add(word)
    return len(unique_shifters)

shifter_count = shifter("WHO IS SHIFTER AND WHO IS NO")
print(shifter_count)

#print(len(shifter))
#shifter("WHO IS SHIFTER AND WHO IS NO")# your code here
    #pass