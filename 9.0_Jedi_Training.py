#Sign your name:________________


#1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase():
    num = float(input("Enter a number: "))
    num+=1
    print("Your number has been increased to", num)
#increase()
                        
 


#2. Correct the following code to print 1-10:

def count_to_ten():
    x=0
    for i in range(10):
        x+=1
        print(x)
 
#count_to_ten()



#3.) Correct the following code to sum the list:

def sum_list():
    sum=0
    list = [45, 2, 10, -5, 100]
    for item in list:
        sum+=item
    print(sum)
#sum_list()




#4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = " "
    text_length = len(text)
    for i in range(1,len(text) + 1):
        result = result + text[i * -1]
    return result

text = str(input("Enter a sentence: "))
print(reverse(text))



#5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = str(input("Command: "))
        if command.lower() == "f" or command.lower() == "m" or command.lower() == "s" or command.lower() == "d" or command.lower() == "q":
            print("You entered:", command)
            return command
        else:
            print("Hey, that's not a command. Here are your options:" )
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")


#get_user_choice()



