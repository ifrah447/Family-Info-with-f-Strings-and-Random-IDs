
# string formatting is used for formatting the string
import random
father_name = str(input("enter your father name: "))
mother_name = str(input("enter your mother name: "))
letter = "hey your father name is {} and your mother is {}"
print(letter.format(father_name, mother_name))
print("here is your family members enquiry details")
for i in range(1, 11):
  name = str(input(f"enter name of {i} member of your family: "))
  country = str(input(f"enter country where {name} lives: "))
  age = int(input(f"enter age of {name} "))
  print(
    f"full name of a {i} member of {father_name}'s family is {name}{father_name} \n he/she belongs to {country} \n age of {name} is {age}"
  )
  # Generate a 13-digit random number
  cnic_number = ''.join([str(random.randint(0, 9)) for z in range(13)])
  # Print the random CNIC number
  print(f"the cnic of {name} is {cnic_number}")
  passport_number ="".join([str(random.randint(0,9)) for m in range(5)])
  if name == "ifrah":
    print("you are a good girl")
  # we can use fstrings to print the string in a better way
