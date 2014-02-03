# Define a variable with a string and a call to a variable
x = "There are %d types of people." % 10
# Define a variable with the value of binary
binary = "binary"
# Define a variable with the value of don't
do_not = "don't"
# Define a variable with a string and calls to the above variables
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the value of variable x
print x
# Print the value of variable y
print y

# Print a string with the value of variable x
print "I said: %r." % x
# Print a string with the value of variable y
print "I also said: '%s'." % y

# Define a variable with the value of False
hilarious = False
# Define a variable with a string and a call to a repr variable
joke_evaluation = "Isn't this joke so funny?! %r"

# Print the value of the variable joke_evaluation calling the value of variable hilarious
print joke_evaluation % hilarious

# Define a variable with a string
w = "This is the left side of..."
# Define a variable with a string
e = "a string with a right side."

# Print the value of variables w and e
print w + e
# Print the value of variables w and e with a space in between them
print w, e