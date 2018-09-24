# Finding the percentage between male and female in a class
# 23 September 2018
# CTI-110 P2HW2 - Male Female Percentage
# Marcell Gill
# Input the number of Male and Female students registering for class
# Display the percentage of Male and Female in a class

males = int( input( "Enter the number of males in the class: ") )
females = int( input( "Enter the number of females in the class: ") )
classTotal = males + females
 
malePercentage = ( males / classTotal ) * 100

femalePercentage = ( females / classTotal ) * 100

print( "Male percentage: " + str( malePercentage ) )
print( "Female percentage: " + str( femalePercentage ) )
      
