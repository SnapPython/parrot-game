import time
prompt = "\nTell me something and I will repeat it to you:"
prompt += "\nEnter quit to end the program.\n"
message=""
turns=0
turns=int(turns)
while message != "quit":
    if turns != 0:
        print("The program has been running for "+str(turns)+" time(s)")
    message=input(prompt)
    print("You messages are processing now!")
    time.sleep(1)
    
    print(message)
    turns += 1
print("You have played "+str(turns)+" time(s).")
print("Thanks for your playing!")
print("The program will shut in 5 seconds.")
time.sleep(5)
