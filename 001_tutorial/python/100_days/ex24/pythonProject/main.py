#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('./Input/Letters/starting_letter.txt', mode='r') as f:
    letter = f.read()

with open('./Input/Names/invited_names.txt', mode='r') as f:
    names = (f.read()).splitlines()

for i in range(len(names)):
    new_letter = letter.replace("[name]", f"{names[i]}")
    file_name = f"mailTo{names[i]}.txt"
    with open(f"./Output/ReadyToSend/{file_name}", mode="w") as f:
        f.write(new_letter)
