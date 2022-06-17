import os.path
import random

    
# functions
def newStudy():#user inputs words and definition
    word = input('Enter word here: ')
    print()
    definition = input('Type definition here: ')
    newDef = word + '-' + definition + '\n'
    print()
    return newDef


def tempDict(open_file): # create dictionary for quiz
    # Stack Overflow w/ edits - https://stackoverflow.com/questions/
    # 35516096/reading-a-file-and-storing-contents-into-a-dictionary-python
    temp_dict = {}
    with open(open_file) as vocab:
        for line in vocab:
            line = line.strip()
            words = line.split('-')

            temp_dict[words[0]] = words[1]
    return temp_dict


def studyQuiz(studyDict):
    word = random.choice(list(studyDict.keys())) #pulls word and definition out and stores in seperate vars 
   

    meaning = studyDict.get(word) #store key's value in meaning 

    print("What is the word for this definition: " ,meaning )#pulls definition  

    answer = input("Enter word: ")

    if answer.lower() == word: #users input converted to lowercase 
        print("Correct!")
        print()
        
    else:
        print("Wrong answer. CORRECT ANSWER: ", word)
        print()


menu_list = ['--- VOCAB STUDY MENU ---', "\n"
             '1. Create New Study List',
             '2. View Study List',
             '3. Add to Study List',
             '4. Quiz',
             '5. Exit']


o = True

while o:
    
    print()
    for i in menu_list:
        print(i)
    print()

    user_input = int(input('Enter menu option number: '))
    # Option set up

    print()
    ''' 1. Create New File - option to create new text file to hold new words with meanings'''
    if user_input == 1:
        file_name = input("Give file a name: ")
        file_name += '.txt'
        file = open(file_name, 'w')
        print()

        x = True
        while x:
            userInput = input('Add new words? y/n ')
            if userInput == 'y':
                file.write(newStudy())

            if userInput == 'n':
                print('File created and stored')
                x = False
        file.close()
        print()

    ''' 2. View txt. file made '''
    if user_input == 2:
        searchFile = input('Enter name of file to open: ')
        searchFile += '.txt'
        print()

        txt_path = os.path.exists(searchFile)
        if txt_path:
            with open(searchFile, 'r') as openFile:
                content = openFile.read().split('\n')
                for i in content:
                    print(i,"\n")
        else:
            print('File not found')
            print()

    ''' 3. Add to previous file '''
    if user_input == 3:

        open_file = input('Type name of file to open: ')
        open_file += '.txt'
        print()

        # to search and make sure file is there.
        txt_path = os.path.exists(open_file)

        if txt_path:
            # appending to file - 'a'
            addFile = open(open_file, 'a')

            x = True
            while x:
                u_input = input('Ready to add your word? y/n: ')
                

                if u_input == 'y':
                    addFile.write(newStudy())

                if u_input == 'n':
                    addFile.close()
                    print('Word(s) added.')
                    x = False
        else:
            print('File not found.')

        print()

    ''' 4. Quiz - reading from txt file and creating quiz.'''
    if user_input == 4:
        open_file = input('Type name of file to open: ')
        open_file += '.txt'
        print()

        # to search and make sure file is there.
        txt_path = os.path.exists(open_file)

        if txt_path:
            # turning info to dictionary
            studyDict = tempDict(open_file)

            # Quiz based on dictionary
            print()
            #------Quiz----- 
            print("---Quiz---","\n")
            
            #Referenced code from GeeksforGeeks
            yn_option = True

            while yn_option:
                
                studyQuiz(studyDict)
                
                try: 
                    #question to continue
                    option = input("Do you want to continue? Enter 'y' or 'n': ")
                    print()
                    if option == "y":
                        yn_option = True
                    elif option == 'n':
                        yn_option = False
                except ValueError:
                    print("Enter only 'y' or 'n':")
                    print()



    ''' 5. To exit program. '''
    if user_input == 5:
        print("Goodbye." "\n")
        break
