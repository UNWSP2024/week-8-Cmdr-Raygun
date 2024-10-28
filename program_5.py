# Author: Andrew Bittner
# Date: 10/25/2024

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

def validate_inp(inp, func, err_msg ='Invalid input (was it formatted correctly?). ', inp_msg ='Please re-enter your '
                                                                                               'answer: '):
    # Set the loop control variable.
    repeat_cnv = True
    while repeat_cnv:
        #  Set the loop control variable to False so that loop does not run again on default.
        repeat_cnv = False
        try:
            # Execute input checker code.
            inp = func(inp)
        except ValueError:
            # Ask the user to input new data.
            print(err_msg, end='')
            inp = input(inp_msg)
            repeat_cnv = True
    return inp

def get_id():
    courses = {}
    print('Input course IDs to store in the program. Course IDs are comprised of three-digit prefixes followed by \n'
          'four-digit indexes (e.g., HIS1075). Alternatively, enter "end" to exit input sequence. ', end = '')
    while True:
        id = input('Enter a course ID: ')
        if id.lower() == 'end':
            break
        id = validate_inp(id, parse_id)
        if id[0] not in courses:
            courses[id[0]] = [id[1]]
        else:
            courses[id[0]].append(id[1])
    return courses

def parse_id(id):
    if not id.isalnum():
        id = id.replace(' ', '')
    if len(id) == 7 and id[0: 2].isalpha() and id[3: 6].isdigit():
        id = [id[0: 3], id[3: 7]]
        return id
    else:
        raise ValueError

def list_courses(courses):
    subject = input('Enter a subject ID (e.g., HIS for history) to retrieve course catalog: ')
    # subject = 'COS'
    print(f'Courses under subject {subject}: ', end = '')
    for ind in range(len(courses[subject])):
        print(subject + courses[subject][ind], end = '')
        if ind != range(len(courses[subject]))[-1]:
            print(', ', end = '')

def main():
    courses = get_id()
    # courses = {'HIS': ['1075', '2000'], 'COS': ['2005', '1969', '1229']}
    list_courses(courses)
    exit_sequence()

if __name__ == '__main__':
    main()