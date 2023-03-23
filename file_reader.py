# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)
# print(contents.rstrip())

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

# pi_file = 'pi_million_digits.txt'

# with open(pi_file) as pi_million_digits:
#     pi_lines = pi_million_digits.readlines()

# pi = ''

# for line in pi_lines:
#     pi += line.strip()

# birthday = input('Enter your birthday, in the form mmddyy: ')
# if birthday in pi:
#     print('Your birthday is in the first million digits of pi!')
# else:
#     print('Your birthday doesn\'t appear in the first million digits of pi :(')

with open('learning_python.txt') as learned_stuff:
    learned = learned_stuff.read()

# print(learned)

with open('learning_python.txt') as learned_stuff:
    learned_lines = learned_stuff.readlines()
    
for line in learned_lines:
    print(line.strip())


