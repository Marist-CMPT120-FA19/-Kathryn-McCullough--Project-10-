#name: Kathryn McCullough
#email: kathryn.mccullough1@marist.edu
#description: This program references a file with words and a separate
#file with a phrase and censors those words from the first into a third file.


#goes through characters and replaces all letters with *
#plus censores word with comma will still have comma
def censor(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word=word[:i] + '*' + word [i+1:]
    return word



def main():
    file= input ("Enter the name of the file to censor: ")
    text= open(file, 'r')
    words_file= input ("Enter the name of the file containing the censord words: ")
    censored= open(words_file, 'r')
    censored_words= censored.read().split()

    censored_text= ""
    for line in text:
        words=line.split()

        #Checks if letters in one of the 'words' in line spells out censored word
        #If yes, replace with *
        for i in range(len(words)):
            word= ""
            for letter in words [i]:
                if letter.isalpha():
                    word+= letter
            if word in censored_words:
                words[i]= censor(words[i])
        censored_text += " ".join(words) + '\n'

        #close files 
        text.close()
        censored.close()
        
        #create and open final file to insert censoreed data and then close also
        newfile=open("censored:" + file, 'w')
        newfile.write(censored_text)
        newfile.close()
        
        

        

main()

            
