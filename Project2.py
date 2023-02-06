import math
print("This is a program to calculate the lift force of an object. The lift is a force that makes an airplane fly. It matches or exceeds the gravitional pull to create a tendency to rise into the air")
# Introduce the operation of the code 
print("Plese enter the area value in meters")
area_wing= float(input())
#Ask the user to enter a area value for use it to calculate the lift force 
print("Plese enter the angle in degrees")
angle_degrees=float(input())
#Ask the user to enter the anglee of the object for use it to calculate the lift force 
print("Please enter the air density ")
air_density= float(input())
#Ask the user to enter the air density value for use it to calculate the lift force 
print("Please enter the velocity in meters per second")
velocity=float(input())
#Ask the user to enter a velocity value for use it to calculate the lift force 
# Having all the inputs, the code can start to calculating 
angle_radians= math.radians(angle_degrees)
#Convert the angle to radians
coefficient= 2*math.pi*angle_radians
#Calculate the coefficient of lift force
lift= (coefficient * air_density * pow(velocity,2) * area_wing)/2
#Calculate with the lift equation, the lift force of those conditions the user entered 
lift_round= round(lift,2)
#Round the result to 2 decimal places ]]
print("The lift force of that object under those conditions is aprox: "+str(lift_round))
#Print the result in the screen 
print("Thank you for use this program :)")
#Say bye to the user 