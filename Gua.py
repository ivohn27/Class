#CONDITIONAL!!
#john_age = 14
#alex_age = 15
#if john_age > 1 and john_age <= 5:
#	print("John age is " + str(john_age) )
#	if alex_age > 1 and alex_age <= 5:
#		print("Alex age is " + str(alex_age) )
#elif john_age > 5 and john_age <= 10:
#	print("John age is range 5 - 10 " + str(john_age) )
#	if alex_age > 5 and alex_age <= 10:
#		print("Alex age is" + str(alex_age) )
#elif john_age > 10 and john_age <= 15:
#	print("Johnage is range 10 - 15 " + str(john_age) )
#	if alex_age > 10 and alex_age <= 15:
#		print("Alex age is " + str(alex_age) )
#else:
#	print("John and Alex aged 15 and above")




#LOOPS!
#function range()
# items = range(0, 10)
# year3_students = ['alex', 'john','airel','joy', 'lopez', 'karl']
# year4_students = ['kevin', 'mayang','jason', 'biol', 'christian']
# it_year_lvl = {
# 	'3rd year':year3_students,
# 	'4th_year':year4_students
# }
# for item in items:
# 	print(item)

# for student in students:
# 	print(student)


# DISPLAY EVEN AND ODD USING LOOP AND CONDITIONING STATEMENT

# for x in range(0,100):
# 	if x % 2 == 0:
# 		print("even "+str(x))
# 	else:
# 		print("odd "+str(x))


import random

name = input("Enter name: ")
rand = random.randint(1,20)
flag = True

while flag:
	print(rand)
	ask = input("Guess what im thinking? ")
	ask = int(ask)
	if ask == rand:
		print(name+". Congrats! You're correct!")
		
	else:
		print(name+". You are incorrect! Guess again.")
	