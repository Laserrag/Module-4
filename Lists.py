# Assignment 1
empty_list = []
print()

numbers = [1,2,3,4,5]
print(numbers)

# reverse the given list

a_list = [1,2,3,4,5]
a_list = a_list[::-1]#Rember this 😀
print(a_list)

# Assignment 2:First and last character of words match

def match_words(words):
    ctr = 0
    lts = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lts.append(word)

    return ctr


count = match_words(['abc', 'xyz', 'aba', '1221'])
print(count)


#Assignment 3

l = [4,5,1,2,9,7,10,8]
print("Original list:", l)
ctr = 0 
for i in l:
    ctr += i

print("Sum of all elements in given list:", ctr)
avg = ctr / len(l)
print("Average of all elements in given list:", avg)

l.sort()
print("Sorted list:", l)

print("The first element is", l[0])
print("The last element is", l[-1])

#Assignment 4

marks = [78, 90, 45, 67, 89]
No_of_students = len(marks)
print("No. of students is ", No_of_students)
print(marks[1:4])

for mark in marks:
    print(mark)