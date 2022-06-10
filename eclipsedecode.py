fname=input("Enter file name: ")
try:
    fh=open(fname)
except:
    print(f"File Name:{fname} could not be found!")
    quit()
sum=0
count=0
for line in fh:
    #if line.startswith("From "):
        #  Remove line change
        line = line.rstrip()
        #  Converts line in a list
        arguments = line.split()

    # Extract  second argument from the list created by split function
        print(arguments)
