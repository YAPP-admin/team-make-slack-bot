from doctest import OutputChecker
from pip import main
import properties
import dedenziBot
import divide

slack = dedenziBot.SlackAPI()

# LIMITED_NUMBER_OF_PEOPLE = 5 이라고 가정하고 진행.

def limit_minus_one_member():
    #given
    result = ["1", "2", "3", "4", "5"]
    
    #when
    output = divide.divid_member(result)
    
    #then
    if len(output) == 1:
        pass_print(output)
        
    else:
        print("fail")
        
def limit_plus_one_member():
    #given
    result = ["1", "2", "3", "4", "5", "6", "7"]
    
    #when
    output = divide.divid_member(result)
    
    #then
    if len(output) == 2:
        pass_print(output)
    else:
        print("fail")

def limit_member():
    #given
    result = ["1", "2", "3", "4", "5", "6"]
    
    #when
    output = divide.divid_member(result)
    
    #then
    if len(output) == 1:
        pass_print(output)
    else:
        print("fail")

def limit_double_minus_one_member():
    #given
    result = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    
    #when
    output = divide.divid_member(result)
    
    #then
    if len(output) == 2:
        pass_print(output)
    else:
        print("fail")

def limit_double_plus_one_member():
    #given
    result = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    
    #when
    output = divide.divid_member(result)
    
    #then
    if len(output) == 3:
        pass_print(output)
    else:
        print("fail")

def limit_double_member():
    #given
    result = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    
    #when
    output = divide.divid_member(result)
    
    #then
    if len(output) == 2:
        pass_print(output)
    else:
        print("fail")
        
def one_list_to_message_list():
    #given
    result = [['1', '4', '3', '5', '6', '2']]
    
    #when
    output = divide.member_lists_to_message_lists(result)
    
    #then
    if len(output) == 1:
        pass_print(output)
    else:
        print("fail")
        
def one_list_and_one_member_to_message_list():
    #given
    result = [['1', '4', '3', '5', '6', '2'], ['7']]
    
    #when
    output = divide.member_lists_to_message_lists(result)
    
    #then
    if len(output) == 2:
        pass_print(output)
    else:
        print("fail")

def many_list_to_message_list():
    #given
    result = [['9', '1', '4', '3', '5'], ['13', '6', '10', '2', '11'], ['12', '8', '7']]
    
    #when
    output = divide.member_lists_to_message_lists(result)
    
    #then
    if len(output) == 3:
        pass_print(output)
    else:
        print("fail")

def pass_print(output):
    print("pass")
    print("-------------result-------------")
    print(output)
    print("--------------end---------------\n\n")

def main():
    limit_minus_one_member()
    limit_plus_one_member()
    limit_member()
    limit_double_minus_one_member()
    limit_double_plus_one_member()
    limit_double_member()
    one_list_to_message_list()
    one_list_and_one_member_to_message_list()
    many_list_to_message_list()
    
if __name__ == "__main__":
	main()