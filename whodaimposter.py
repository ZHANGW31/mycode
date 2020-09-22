import random

print("You are the Captain of the space ship NotSus, in command of 10 crewmates.")
input()
print("After a long expedition on the planet Mars, you are finally on the voyage home.")
input()
print("However, when you are just 48 hours away from home, one of your crewmates found what looked like human remains stuffed in the ship's garbage disposal 5000.")
input()
print("You call an emergency meeting to account for everyone... however to your suprise... everyone was accounted for and there.")
input()
print("This could only mean one thing!... There is an imposter among us!")
input()
print("There are tasks that needs to be completed on the ship and you have to rely on your crewmates for the ship the remain operational to make it home. At the same time, you can't afford to allow an alien being onto your home planet...")
input()
print("Everyone in your ships crew wears a different color space suit - the colors are: [red] [blue] [green] [pink] [orange] [yellow] [black] [white] [purple] [cyan] [lime]")
input()
print("As the Captain, you have the authority to send people out the airlock. You must exercise that ability carefully...")
input()

def imposter_kills(crew_list, imposter) :
    imposter_index = crew_list.index(imposter)
    victom_index = 0
    victom = ""
    
    if imposter_index < len(crew_list) - 1 :
        victom_index = imposter_index + 1
        victom = crew_list[victom_index]
        crew_list.pop(victom_index)
        
    elif imposter_index >= len(crew_list) - 1 :
        victom_index = imposter_index - 1
        victom = crew_list[victom_index]
        crew_list.pop(victom_index)
        
    print("Oh no! Looks someone was murdered! " + victom + " was found dead!")
    print("You pull up the ship crew roster...")
    
    
    
    
def send_it(crew_list, imposter, current_crew_count, imposter_found) :

    print("who do you vote off?")
    user_input = input("Choose a color: ")
    user_input.lower()
    if user_input in crew_list :
        crew_list.remove(user_input)
        print(user_input + " was sent out the airlock... and everyone goes back to working on tasks")
        current_crew_count -= 1
        if user_input == imposter :
            imposter_found = True
            print("You see a pair of tentacles burst out of " + user_input + "'s spacesuit visor! You got the imposter!")
    else :
        print("Ummm... are you the imposter? " + user_input + " is not a valid crewmate...")
        send_it(crew_list, imposter, current_crew_count, imposter_found)



def start() :

    crew_list = ["red", "blue", "green", "pink", "orange", "yellow", "black", "white", "purple", "cyan", "lime"]
    imposter = crew_list[random.randint(0,9)]

    user_input = ""
    current_crew_count = len(crew_list)
    imposter_found = False

    while current_crew_count > 2 or imposter_found == True :
        send_it(crew_list,imposter, current_crew_count, imposter_found)
        if imposter_found == True :
            break
        imposter_kills(crew_list, imposter)
        print(crew_list)
    if current_crew_count <= 2 :
        print("You hear alien noises behind you..." + imposter + " slices your neck open")

    


start()

        








