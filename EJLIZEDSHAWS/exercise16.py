from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line = input("line : ")
line = input("line : ")
line = input("line : ")

print("I'm going to write these to the file.")

target.write(line)
target.write("\n")
target.write(line)
target.write("\n")
target.write(line)
target.write("\n")

print("And finally, we close it.")
target.close()
