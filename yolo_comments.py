#Imports
import praw
import datetime
import re
from bs4 import BeautifulSoup
from decouple import config


#Reddit login & choose subreddit
def access():
    """
    Access the Reddit API and configure which subreddit to focus on.
    """
    reddit = praw.Reddit(
        client_id= config('reddit_client_id'),
        client_secret= config('reddit_secrent'),
        password= config('reddit_pw'),
        user_agent= config('reddit_agent'),
        username= config('reddit_usn')
        )

    #Make sure connection is established
    #print(reddit.user.me())

    subreddit = reddit.subreddit('wallstreetbets')
    return subreddit


def yolo_data():
    """
        Collects comment data from the hot section posted during the last 24 hours for the yolo flair.

        Output format: [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]]

    """
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flair = "YOLO"
    
    #Create data list and add (date, flair) as element 0
    yolo_data = []
    yolo_data.append([date, flair, "---"])

    n_posts = 0
    n_comments = 0
    
    flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)

    for submission in flair_submissions:
        if submission.score > upvotes:
            #Save submission id, text and name line=submission.
            yolo_data.append([submission.id, submission.selftext, "Line=Submission"])
            while True:
                try:
                    submission.comments.replace_more()
                    break
                
                except PossibleExceptions:
                    print("Handling replace_more exception")
                    sleep(1)
           
            comments = submission.comments.list()

            for comment in comments:
                if comment.score > upvotes:
                    #Avoid markdown formatting with bs4.
                    comment_text=BeautifulSoup(comment.body_html, "html.parser").text                    
                    yolo_data.append([comment.id, comment_text, comment.parent_id])  
                    n_comments += 1

            n_posts += 1

    print('Flair: ', flair)
    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
    #print('Data: ', yolo_data)
    return yolo_data

    
def yolo_processing():
    """
        This function performs Regular expressions on the collected comment-data. 
        Given that sentences may vary a lot it might still be lacking in some aspects.
        
        Output format: [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]]        

    """
    #Load data and prepare new collection.
    preprocess_data = yolo_data()
    processed_data = []

    #Regex expressions and string identifications.                                                                         
    links = r"([\w+]+\:\/\/)?([\w\d-]+\.)*[\w-]+[\.\:]\w+([\/\?\=\&\#\.]?[\w-]+)*\/?"            #Matches any links.
    reddit_reply = r"((\/u\/+|u\/+)(?:\w*))"                                                     #Matches any replys to a user.
    bot_reply = r"((Im|I'm|I am)(?:\sa bot))"                                                    #Identify bot comment.
    trimmer = r"^\s+|\s+$|\s+(?=\s)"                                                             #Trims unneccessary whitespace.
    deleted = "[raderat]"                                                                        #Identify deleted comment.
    removed = '[borttagen]'                                                                      #Identify removed comment.
    newline = "\n"                                                                               #Matches (repeated) newlines.
    #Compile
    generic_re = re.compile("(%s|%s)" % (links, reddit_reply))
    bot_re = re.compile(bot_reply)
    trimmer_re = re.compile(trimmer)

    #Loop through data
    for sentence in preprocess_data:
        #Deal with deleted / bot reply comments.
        if sentence[1] == deleted or re.search(bot_re, sentence[1]) or sentence[1] == removed:
            continue
        
        #Deal with newlines and apply changes.
        if newline in sentence[1]:
            sentence[1] = sentence[1].replace(newline,"")
            sentence[1] = re.sub(generic_re, "", sentence[1])
            sentence[1] = re.sub(trimmer_re, "", sentence[1])

            #Append comment data unless empy string.
            if sentence[1] == "" or sentence[1] == '""':
                continue
            else:
                processed_data.append(sentence)

        #Simply apply changes. 
        else:
            sentence[1] = re.sub(generic_re, "", sentence[1])
            sentence[1] = re.sub(trimmer_re, "", sentence[1])
            
            #Append comment data unless empy string.      
            if sentence[1] == "" or sentence[1] == '""':
                continue
            else:
                processed_data.append(sentence)

    return processed_data

#Run functions
if __name__ == "__main__":
    access()
    yolo_data()
    yolo_processing()
