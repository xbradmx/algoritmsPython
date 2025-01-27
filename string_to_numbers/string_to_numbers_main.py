import numpy as np


User_Input = input("Enter a string number: ")

Number_Dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
    "thirty": "30",
    "forty": "40",
    "fifty": "50",
    "sixty": "60",
    "seventy": "70",
    "eighty": "80",
    "ninety": "90",
    "hundred": "100",
    "thousand": "1000",
    "million": "1000000",
    "billion": "1000000000"
}

#splits the input into a list 
User_Input_Splitter = np.array(User_Input.split(" "))

print(User_Input_Splitter[0])


#while loop to check through all words in array individually 

# def loop_until_limit(limit):
#     count = 0
#     while count < limit:
#         count += 1

#this splits the words up
#Individual_Input = User_Input_Splitter[count]

###########
def loop_until_limit(limit):
    count = 0
    while count < limit:
        Individual_Input = User_Input_Splitter[count]
        if Individual_Input in Number_Dict:
          print(f"The value for '{Individual_Input}' is {Number_Dict[Individual_Input]}")
          Arr_of_Converted_numbers.append(Number_Dict[Individual_Input])
        else:
          print(f"'{Individual_Input}' is not a valid key in the dictionary.")
        count += 1



#############


Arr_of_Converted_numbers = []


#checking function
# def Check_Num_In_Dict():
#   if Individual_Input in Number_Dict:
#     print(f"The value for '{Individual_Input}' is {Number_Dict[Individual_Input]}")
#     Arr_of_Converted_numbers.append(Number_Dict[Individual_Input])
#   else:
#     print(f"'{Individual_Input}' is not a valid key in the dictionary.")

# Check_Num_In_Dict()



loop_until_limit(len(User_Input_Splitter))

print(Arr_of_Converted_numbers)



####### converting the array to integers 

int_array = [int(x) for x in Arr_of_Converted_numbers]
print(int_array)


#####

# function for turning the int_array into the original number
this_is_an_integer = []

def Dont_Make_Me_cry():
  if len(int_array) == 1:
    this_is_an_integer.append(int_array[0])
    One_Number_MF = this_is_an_integer[0]
    print(One_Number_MF)

  elif len(int_array) == 2 and int_array[0] < int_array[1]:
    this_is_an_integer.append(int_array[0] * int_array[1])
    One_Number_MF = this_is_an_integer[0]
    print(One_Number_MF)
  
  elif len(int_array) == 2 and int_array[0] > int_array[1]:
    this_is_an_integer.append(int_array[0] + int_array[1])
    One_Number_MF = this_is_an_integer[0]
    print(One_Number_MF)

  elif len(int_array) == 3:

    if int_array[1] < int_array[2]:
      this_is_an_integer.append(int_array[0] * int_array[1] * int_array[2])
      One_Number_MF = this_is_an_integer[0]
      print(One_Number_MF)

    else:
      this_is_an_integer.append(int_array[0] * int_array[1] + int_array[2])
      One_Number_MF = this_is_an_integer[0]
      print(One_Number_MF)

  elif len(int_array) == 4:

    if int_array[1] < int_array[2]:

      if int_array[2] < int_array[3]:
        this_is_an_integer.append((int_array[0] * int_array[1]) + ( int_array[2] * int_array[3]))
        One_Number_MF = this_is_an_integer[0]
        print(One_Number_MF)
      else:
        this_is_an_integer.append((int_array[0] * int_array[1]) + ( int_array[2] + int_array[3]))
        One_Number_MF = this_is_an_integer[0]
        print(One_Number_MF)

    else:
      this_is_an_integer.append(int_array[0] * int_array[1] + int_array[2])
      One_Number_MF = this_is_an_integer[0]
      print(One_Number_MF)


Dont_Make_Me_cry()


#0-9 dict
#10-19 dict
#10s multiplier dict
#100s multiplier dict
#1000s multiplier dict


#"five hundred"
#"five", "hundred"

#if five in 0-9 dict, and only 1 component 
#print 5 

#elif five in 0-9 dict and componenets >1;

#def twocomponents
    # if five in o-9 dict;
          # multiplier a = 5
    # if second component in multiplier components dicts
          #multiplier b = 100

    # print (sum of multiplier a * b)

#"five hundred fifty five"



#split by finding space
#userinput= (0).lower


#SPLITTING

#0-9 dict, and it first; first value



