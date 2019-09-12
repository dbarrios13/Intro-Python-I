"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
open('foo.txt', 'r')

print("Do you bite your thumb at us, sir?")
print("I do bite my thumb, sir.")
print("Do you bite your thumb at us, sir?")
print("No, sir. I do not bite my thumb at you, sir, but I bite my thumb, sir.")
print("Do you quarrel, sir?")
print("Quarrel, sir? No, sir.")


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
open('bar.txt', 'w')