my_name = "Brian"
new_name = ""
for letters in my_name:
    if letters == "i":
        new_name = new_name + "y"
    else:
        new_name = new_name + letters

print(new_name)
