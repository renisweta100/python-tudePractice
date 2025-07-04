
#Student's Marks
student_data = {"toddy":24,"ami":67,"yana":90}
ask = input("Enter student's name: ")
if ask in student_data.keys():
    print("{} mark's :{}".format(ask,student_data[ask]))
else:
    print("Student not found.")





#reverse list
l = [1,2,3,4,5,6,7,8,9,10]
size = int(len(l)/2)
new_list=[]

for i in range(size):
    new_list.append(l[i])


print("Original list: ",l)
print("Extracted first five items: ",new_list)
print("Reversed extracted elements: ",new_list[::-1])
