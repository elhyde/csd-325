#Emeralde Hyde
#10/23/2025
#Distance Conversion, CSD205 Module 4.2


#The purpose of this program is to convert miles into kilometers.

def message():
    print("Distance Converter")
    print ('Hello')
    #call the conversion function
    conversion ()

def conversion():
#input initial distance
    miles = float(input('Please enter the enter the number of miles driven: '))

    #convert miles to kilometers
    kilometers = (miles * 1.61)

    print (f"{miles:.2f} miles equals around {kilometers:.2f} kilometers.")
#Call the message function
message()







