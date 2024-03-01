""""Sevseg, by AI sweigart modified by Agbolade Elijah
A seven segmemt number display module, used by the countdown and Digital Clock Programs.
Tags: short, module"""

"""A labelled seven-segment display, with each segment lablelled A to G:

 _A_
|   |   Each digit in a seven segment_display:
F   B     _         _
|_G_|   |   |   |   _|
|   |   | _ |   |  |_ 
|   |    
E   C
|_D_|
"""

def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The returned string will be padded with zeros if it is smaller them minwidth."""
    number = str(number).zfill(minWidth)
    
    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.': # Render the decimal point.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue # skip the space in between digits
        elif numeral == '-': # Render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0': # Render the 0
            rows[0] += ' __ '    
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1': # Render the 1
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2': # Render the 2
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == "3": # Render the 3
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == "4": # Render the 4
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == "5": # Render the 5
            rows[0] += ' __ ' 
            rows[1] += '|__ ' 
            rows[2] += ' __|'  
        elif numeral == "6": # Render the 6
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|' 
        elif numeral == '7': # Render the 7
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8': # Render the 8
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9': # Render the 9
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
            
        # Add a space ( for the space in between the numerals) if this 
        # isn't the last numeral:
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
        
    return '\n'.join(rows)

# if this program isn't being imported, display the numbers 00 to 99.
if __name__ == '__main__':
    print('This module is meant to be imported rather them run.') 
    print('For example, this code: ')
    print('     import sevseg')  
    print('     nyNumber = seg.getSevSegStr(42, 3)')
    print('     print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __')           
    print('|  | |__|  __|')  
    print('|__|    | |__')
        
            
                
            