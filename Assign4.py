
#Student's Marks
import os
P = "Sample.txt"

isFile = os.path.isfile(P)
if isFile==True:
    with open("Sample.txt") as file:
        print(file.read())

else:

    print("The file {} was not found".format(P))



#file_read_write
write_data = input("Enter text to write to the file: ")

filename = "output.text"
with open(filename, "w") as file:
    file.write(write_data)
    print("Data successfully written to ", filename)

append_data = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(append_data)
    print("Data appended successfully")

with open(filename) as file:
    print("final content of {} {}".format(filename, file.read()))