# Created by Jenny Trac
# Created on Oct 26 2017
# Program calculates a students final average
# learned how to do arrays from:
# http://www.i-programmer.info/programming/python/3942-arrays-in-python.html

import ui

# constants and variables
average = 0
marks_sum = 0
number_of_marks = 0

def calculate_touch_up_inside(sender):
    # calculates the average
    
    # constants and variables
    global average
    global marks_sum
    global number_of_marks
    
    # input
    mark = float(view['mark_textfield'].text)
    
    if mark >= -1 and mark <= 100:
        if mark >= 0 and mark <= 100:
            # process
            number_of_marks = number_of_marks + 1
            marks_sum = marks_sum + mark
            average = marks_sum / number_of_marks
            
        else:
            number_of_marks = number_of_marks
            marks_sum = marks_sum
            average = average
            
        view['average_label'].text = str(average) + "%"
    
    else:
        view['average_label'].text = "Not an option for marks."
    

view = ui.load_view()
view.present('sheet')
