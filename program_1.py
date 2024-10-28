# Author: Andrew Bittner
# Date: 10/25/2024

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(name_full):
    name_full = validate_inp(name_full, str, None, ' ')
    persons_initials = []
    for name in name_full:
        if not name.isalnum():
            continue
        ch = name[0] + '.'
        persons_initials.append(ch)
    persons_initials = ' '.join(persons_initials)
    return persons_initials


def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')


def validate_inp(inp, out_type, elem_ct=None, spl_ch=None, err_msg='Invalid input (was it formatted correctly?). ',
                 inp_msg='Please re-enter your answer: '):
    # Set the loop control variable.
    repeat_cnv = True
    while repeat_cnv:
        #  Set the loop control variable to False so that loop does not run again on default.
        repeat_cnv = False
        try:
            # Split the input into a list, if possible and desired.
            if spl_ch is not None and type(inp) == str:
                inp = inp.split(spl_ch)
            # If the input type is not already list or tuple, convert variable to list for processing.
            elif type(inp) != list and type(inp) != tuple:
                inp = [inp]
            # If elements in the input list do not meet desired element count, raise an error to execute re-input code.
            if elem_ct is not None and elem_ct != len(inp):
                raise ValueError
            # Select an individual element from the input to process.
            for elem in inp:
                # If the input element's type is not already the desired output type, execute the conversion code.
                while type(elem) != out_type:
                    if out_type == int or float:
                        # Select an individual character from the element to process.
                        for ch in elem:
                            # If the character is not a digit, remove it.
                            if not ch.isdigit():
                                elem = elem.replace(ch, '')
                    # Convert the element to desired type and append it to the input list.
                    elem = out_type(elem)
                    inp.append(elem)
            # Remove original, unconverted data left in input list.
            for elem in inp.copy():
                if type(elem) != out_type:
                    inp.remove(elem)
            # If input list contains only one item, break it out of the list.
            if len(inp) > 0 and not len(inp) > 1:
                inp = inp[0]
        # If bad data results in a failing operation, run error handler.
        except ValueError:
            # Ask the user to input new data.
            print(err_msg, end='')
            inp = input(inp_msg)
            repeat_cnv = True
        return inp


def main():
    initials = initials_generator(input('Enter the user\'s first, middle, and last name (separated by spaces): '))
    print(initials)
    exit_sequence()


if __name__ == '__main__':
    main()
