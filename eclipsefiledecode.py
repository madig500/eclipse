import base64
import re

fname=input("Enter file name: ")
try:
    fh=open(fname)
except:
    print(f"File Name:{fname} could not be found!")
    quit()

for line in fh:
        #print("The type on INPUT : ", type(line))
        base64_bytes = line.encode('utf-8')
        #print("The type transformed to bytes : ", type(sample_string_bytes))

        # USE THIS LINE IN CASE String comes already on  Bytes

        # THIS LINE MIGHT NOT BE REQUIRED SINCE STRING MAY COME ALREADY ENCODE ON TYPE STR
        #message_bytes = base64.b64decode(base64_bytes)
        message_bytes = base64.decodebytes(base64_bytes)
        #message = message_bytes.decode('utf-8')


        new_data = message_bytes.decode("ascii")

        depurar=repr(new_data)

        depurar=depurar.replace("03","03 ")
        depurar=depurar.replace("\\x","  \\x")

        #print(depurar)
        lista=depurar.split()
        nuevalista=list()
        #print(lista)
        i=int()
        i=0
        for kkk in lista:
            #print(kkk)
            if "\\x" in kkk :
                #print(kkk)
                if  kkk.endswith("03") and lista[i+1].isalpha()  :
                    #print(kkk)
                    nuevalista.append("\n")
                #print(kkk)
                i=i+1
                continue

            kkk=kkk.replace("\\","")
            #print(kkk)
            nuevalista.append(kkk)
            i=i+1


        print(*nuevalista,sep=" ")

        #base64_string = sample_string_bytes.decode("ascii")
        #print(base64_string)



        #print(f"Encoded string: {base64_string}")


        #  Remove line change
        line = line.rstrip()

        #  Converts line in a list
        arguments = line.split()

    # Extract  second argument from the list created by split function
        #print(arguments)









#  EXAMPLE  DECODING  BASE 64
#base64_string ="SGVsbG8gV29ybGQh"
#base64_bytes = base64_string.encode("ascii")


# base64bytes contains polled strings


#decoded_frameset = base64.b64decode(base64_bytes)
#sample_string = decoded_frameset.decode("ascii")

#print(f"Decoded string: {sample_string}")
