data = ("John", "Doe", 53.44)
format_string = "Hello"

#Hello John Doe. Your current balance is $53.44.
#print(format_string % data)

print(format_string + " " +data[0]+" "+data[1]+ " Your current balance is %d"  %data[2])