#Just a file for trying regex.

import re

def a_function():

    datan = [['gsokoh0', 'The \nSEC doing Im a bot fine work as usual??'], 
    ['gsojjcf', "\nGuys, I think the market might be.....controlled, altered in some way to benefit a select group of people. There's a word for it but, as a retail investor my brain is too smooth to remember it."],  
    ['gsolnlb', "It's all u/JakTravis_u_SOB proprietary. \nKevin is in the broom I'm a bot closet with a crystal ball."],
    ['abskala', '[raderat]'],
    ['gsolnaa', "It's all http://www.example.com proprietary."],
    ['gaasaa', '-\n2200\n checking in\n']]
    return datan


def a_new_function():
    old_data = a_function()
    clean_data = []
#Regex expressions and string identifications.                                                                         
    links = r"([\w+]+\:\/\/)?([\w\d-]+\.)*[\w-]+[\.\:]\w+([\/\?\=\&\#\.]?[\w-]+)*\/?"            #Matches any links.
    reddit_reply = r"((\/u\/+|u\/+)(?:\w*))"                                                     #Matches any replys to a user.
    bot_reply = r"((Im|I'm|I am)(?:\sa bot))"                                                    #Identify bot comment.
    trimmer = r"^\s+|\s+$|\s+(?=\s)"                                                             #Trims unneccessary whitespace.
    deleted = "[raderat]"                                                                        #Identify deleted comment.
    newline = "\n"                                                                               #Matches (repeated) newlines.
    #Compile
    generic_re = re.compile("(%s|%s)" % (links, reddit_reply))
    bot_re = re.compile(bot_reply)
    trimmer_re = re.compile(trimmer)

    #Loop through data
    for sentence in old_data:
        #Deal with deleted / bot reply comments.
        if sentence[1] == deleted or re.search(bot_re, sentence[1]):
            continue
        
        #Deal with newlines and apply changes.
        if newline in sentence[1]:
            sentence[1] = sentence[1].replace(newline,"")
            sentence[1] = re.sub(generic_re, "", sentence[1])
            sentence[1] = re.sub(trimmer_re, "", sentence[1])
            clean_data.append(sentence)

        #Simply apply changes. 
        else:
            sentence[1] = re.sub(generic_re, "", sentence[1])
            sentence[1] = re.sub(trimmer_re, "", sentence[1])
            clean_data.append(sentence)

    print(clean_data)


if __name__ == "__main__":
    #a_function()
    a_new_function()
