import datetime
print ("Welcome to Notes! Try help for more information")
command = "true"
print("hello shit!")
id = 1
while command != "exit" and command != "ex":    
    command = input("Once again: ")
    if command == "help":
        print("___________INFO_________\n#add - add new note\n#read * - to read note with article *\n#show - to see all note's articles\n#edit * - edit note with article *\n#del * - delete note with article *\n#show_sort - to see articles sorted by date")
        print("________________________")
    elif command == "add":
        print("adding...")
        data = open('Notes.txt','a')
        data.close

        data = open('Notes.txt', 'r')            
        for line in data:
            if "id" in line:
                id = id+1
        data.close

        data = open('Notes.txt','a')
        data.write("_________id: "+str(id) + "\n")
        data.write("datetime: " + str(datetime.datetime.now())+ "\n")
        message = input("Note's article: ")
        data.write("article: " + message+ "\n")
        message = input("Note's body: ")
        data.write("body: " + message+ "\n")
        data.close
    elif command == "show":
        data = open ('Notes.txt', 'r')
        for line in data:
            if "id" in line:
                print ("_______________")
            else:
                print(line, end="")
        data.close
    elif "read" in command:
        print("reading...")
        list_command = command.split()
        data = open('Notes.txt', 'r')
        conteins = data.readlines()
        for line in range(len(conteins)):
            if list_command[1] in conteins[line] and "article" in conteins[line]:
                print(conteins[line], end = "")
                print(conteins[line+1], end = "")  
        data.close
    elif command == "show_sort":
        print("showing sort...")

    elif "edit" in command:
        list_command = command.split()
        data = open('Notes.txt', 'r')       
        conteins = data.readlines()
        for line in range(len(conteins)):
            if list_command[1] in conteins[line] and "article" in conteins[line]:
                old_note_body = conteins[line+1]
                print(old_note_body, end = "")
        data.close


        with open ('Notes.txt', 'r') as data:
            old_data = data.read()
        new_data = old_data.replace(old_note_body, "body: " + input("text new note's body: ") + "\n")
        with open ('Notes.txt', 'w') as f:
            f.write(new_data)

    elif "del" in command:
        list_command = command.split()
        data = open('Notes.txt', 'r')       
        conteins = data.readlines()
        for line in range(len(conteins)):
            if list_command[1] in conteins[line] and "article" in conteins[line]:
                old_note_body = conteins[line+1]
                old_note_datetime = conteins[line-1]
                old_note_article  = conteins[line]
                old_note_id = conteins[line-2]
        data.close


        with open ('Notes.txt', 'r') as data:
            old_data = data.read()
        new_data = old_data.replace(old_note_body, "").replace(old_note_article,"").replace(old_note_datetime,"").replace(old_note_id,"")
        with open ('Notes.txt', 'w') as f:
            f.write(new_data)

    else:
        print("!Command is not available. Try again")


