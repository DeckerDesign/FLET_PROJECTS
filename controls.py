# in this file, we create a few line of code to map and keep note
#of the the class instances allowinf easy acces to each instance

global control_reference
control_reference = {}

def add_to_control_reference(key, value):
    #this funciton will be called before making any
    #instances of a class. ti takes in two argument a key and a value
    #which will be paired in the global diect

    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

#function to return the dict

def return_control_reference():
    global control_reference
    return control_reference
    