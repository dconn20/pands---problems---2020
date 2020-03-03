# Damien Connolly
# A program that reads in a text file and outputs 
# the number of e's it contains

fn = input("Enter file name: ")
l = input("Enter letter to be searched: ")
k = 0


with open(fn, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:",k,)

    


