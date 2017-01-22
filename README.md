# Calculator
#Calc.py
    calc1.py is a simple calculator that takes input a string of adding and differencing numbers. It tokenize the input string and parse them into a binary tree to do the calculation. For example, 4+3+5-2 would be parsed into
                                     '-'
                                   /     \
                                 '+'      2
                               /     \       
                             '+'      5
                           /    \
                          4      3
                          
                          
#calc2.py
    calc2.py utilize Tkinter to create GUI to make a calculator interface, and use eval() to directly get the answer
    
    
#Thing to improve:
    calc1 lacks the ability to multiply and divide. Even though there are functions such as eval() to get the answer, it would be a good practice to try to implement it myself. 
    In addition, both calculator are not able to take the previous result as a new input, and we would have to clear everything and re-enter the previous answer and the new function, I will try to imporve that in the future
