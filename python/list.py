# code your own list

subjects = ["Science", "Math", "Language Arts", "History"]
favnums = [9,1,2,3,5,7]
family = ["Hyeran", "Andrew", "Hyunsu", "Christine", "Brian"]
print(len(subjects), "Major subjects in my school include " + ', '.join(subjects) + ".")
print("My family consists of " + ', '.join(family) + ". " + "I have", len(family), "members in my family.")
print(family[0], "is my name.")
print("Science" in subjects)
print()
print(family[1:4])
print(subjects.insert())
for fam in family:
    print(fam)
print()
for i in range(len(subjects)):
    print(subjects[i])
print()
name = "Hyeran"
print("There are", len(name), "letters in my name.")
print("ran" in name)
print(name[0])

for letter in name:
    print(letter)

subjects.sort()
favnums.sort()
print(subjects.index("Science"))
print(subjects)
print(favnums)
