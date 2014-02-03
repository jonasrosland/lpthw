name = 'Jonas Rosland'
age = 32
height = 6.336
weight = 210
eyes = 'Green'
teeth = 'White'
hair = 'Blondish'

height_in_cm = height / 0.0328083989501
weight_in_kg = weight / 2.20462262185
print "Let's talk about %s." % name
print "He's %r feet tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." %(age, height, weight, age + height + weight)
print "He's %d cm tall" % height_in_cm
print "He's %d kg heavy" % weight_in_kg