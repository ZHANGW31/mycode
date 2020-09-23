
#Counter
room = ["ham and cheese", "mcdonald's chicken", "sausage", "dirty old buttermilk"]

for biscuit in room:
    print("There's a " + biscuit + " biscuit in your room!" + " CRACK!")

#Delete
laundry = ["red sock", "red sock inside out", "green sock", "blue sock inside out"]

print("In the laundry basket you currently have: " + str(laundry))

for sock in laundry:
    if "inside out" in sock:
        print("Grandma: I found a " + sock + " it is going in the trash!")
        laundry.remove(sock)
    
print("The remaining socks are: " + str(laundry))

#Add

report_card = ["a", "b", "c", "a", "b", "f", "f", "f", "a", "f", "d"]
snakes_in_bed = []

print("You've received your report card... here are the grades: " + str(report_card))

for grade in report_card:
    if grade == "f":
        snakes_in_bed.append("snake")
        print("Grandma puts a snake inside your bed.")
    elif grade == "d" :
        print("hmmmm looks like you got a " + grade + " getting close to an F, you better be careful.")
    elif grade == "c" :
        print("hmmmm looks like you got a " + grade + " getting close to an F, you know better.")
    elif grade == "b" :
        print("hmmmm looks like you got a " + grade + " meh still not an A.")
    elif grade == "a" :
        print("hmmmm looks like you got a " + grade + " it must've been a fluke!")

print("Looks like you got: " + str(len(snakes_in_bed)) + " snakes in your bed!")
