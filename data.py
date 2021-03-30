### This file is intended to collect user data.
# In order to circumvent Reddit API limits with 1000 calls per request there are separate functions for browsing each flair.
# Depending on the amount of comments on a post, the extraction limit might be enforced preventing full scraping of all the comments.
# This lead to not being able to loop the different flairs, instead every function is baseline the same apart from which flair it browses.

#Imports
import praw
import requests
import datetime
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


"""
def dd_data():
    
        OBS This function is not used.

        Collects comment data from the last 24 hours for the DD flair.
        
        Output format: [(date, flair), (comment id, comment)]

    
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flairs = ["DD", "Discussion", "YOLO", "News", "Earningsthread"]

    #Create data list and add date as element 0
    data = []
    n_posts = 0
    n_comments = 0
    
    comment_ids = []
    #Loop flairs and append (date, flair) as element 0
    for flair in flairs:
        data.append((date, flair))
    
        flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)
        n_flair_posts = 0

        for submission in flair_submissions:
            if submission.score > upvotes:
                
                submission.comments.replace_more(limit=None)
                comments = submission.comments.list()
                
                #Make sure comments does not get extracted twice. 
                #Is also be used to compare comments if a post is hot in regards to several flairs.
                for comment in comments:
                    if comment.score > upvotes:
                        if comment.id not in comment_ids:
                            #Appends a tuple (id, comment) to flair list
                            data.append((comment.id, comment.body))
                            comment_ids.append(comment.id)
                            n_comments += 1
                n_flair_posts +=1

        print('Flair: ', flair)
        print('flair posts: ', n_flair_posts)
        
        n_posts += 1

    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
   
    return data
"""

def dd_data():
    """
        Collects comment data from the hot section posted during the last 24 hours for the DD flair.

        Output format: [(date, flair), (comment id, comment)]

    """
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flair = "DD"

    #Create data list and add (date, flair) as element 0
    dd_data = []
    dd_data.append((date, flair))

    n_posts = 0
    n_comments = 0
    
    flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)

    for submission in flair_submissions:
        if submission.score > upvotes:
            
            submission.comments.replace_more(limit=None)
            comment_ids = []

            for comment in submission.comments.list():
                if comment.score > upvotes:
                    
                    #Make sure comments does not get extracted twice. 
                    #Will also be used to compare comments if a post is hot in regards to several flairs.
                    if comment.id not in comment_ids:
                        dd_data.append((comment.id, comment.body))
                        comment_ids.append(comment.id)
                        
                        n_comments += 1

            n_posts += 1

    print('Flair: ', flair)
    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
    
    return dd_data


def news_data():
    """
        Collects comment data from the hot section posted during the last 24 hours for the News flair.

        Output format: [(date, flair), (comment id, comment)]

    """
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flair = "News"

    #Create data list and add (date, flair) as element 0
    news_data = []
    news_data.append((date, flair))

    n_posts = 0
    n_comments = 0
    
    flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)

    for submission in flair_submissions:
        if submission.score > upvotes:
            
            submission.comments.replace_more(limit=None)
            comment_ids = []

            for comment in submission.comments.list():
                if comment.score > upvotes:
                    
                    #Make sure comments does not get extracted twice. 
                    #Will also be used to compare comments if a post is hot in regards to several flairs.
                    if comment.id not in comment_ids:
                        news_data.append((comment.id, comment.body))
                        comment_ids.append(comment.id)
                        
                        n_comments += 1

            n_posts += 1

    print('Flair: ', flair)
    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
    
    return news_data


def yolo_data():
    """
        Collects comment data from the hot section posted during the last 24 hours for the YOLO flair.

        Output format: [(date, flair), (comment id, comment)]

    """
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flair = "YOLO"

    #Create data list and add (date, flair) as element 0
    yolo_data = []
    yolo_data.append((date, flair))

    n_posts = 0
    n_comments = 0
    
    flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)

    for submission in flair_submissions:
        if submission.score > upvotes:
            
            submission.comments.replace_more(limit=None)
            comments = submission.comments.list()
            comment_ids = []

            for comment in comments:
                if comment.score > upvotes:
                    
                    #Make sure comments does not get extracted twice. 
                    #Will also be used to compare comments if a post is hot in regards to several flairs.
                    if comment.id not in comment_ids:
                        yolo_data.append((comment.id, comment.body))
                        comment_ids.append(comment.id)
                        
                        n_comments += 1

            n_posts += 1

    print('Flair: ', flair)
    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
    
    return yolo_data

def discussion_data():
    """
        Collects comment data from the hot section posted during the last 24 hours for the Discussion flair.

        Output format: [(date, flair), (comment id, comment)]

    """
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flair = "Discussion"

    #Create data list and add (date, flair) as element 0
    discussion_data = []
    discussion_data.append((date, flair))

    n_posts = 0
    n_comments = 0
    
    flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)

    for submission in flair_submissions:
        if submission.score > upvotes:
            
            submission.comments.replace_more(limit=None)
            comments = submission.comments.list()
            comment_ids = []

            for comment in comments:
                if comment.score > upvotes:
                    
                    #Make sure comments does not get extracted twice. 
                    #Will also be used to compare comments if a post is hot in regards to several flairs.
                    if comment.id not in comment_ids:
                        discussion_data.append((comment.id, comment.body))
                        comment_ids.append(comment.id)
                        
                        n_comments += 1

            n_posts += 1

    print('Flair: ', flair)
    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
    
    return discussion_data

def earningsthread_data():
    """
        Collects comment data from the hot section posted during the last 24 hours for the Earningsthread flair.

        Output format: [(date, flair), (comment id, comment)]

    """
    #Select subreddit
    subreddit = access()

    #Parameters
    upvotes = 2
    date = datetime.datetime.now().strftime("%x")
    flair = "Earningsthread"

    #Create data list and add (date, flair) as element 0
    earningsthread_data = []
    earningsthread_data.append((date, flair))

    n_posts = 0
    n_comments = 0
    
    flair_submissions = subreddit.search('flair:'+flair, 'sort:"hot"', 'syntax:"lucene"', time_filter = "day", limit = 25)

    for submission in flair_submissions:
        if submission.score > upvotes:
            
            submission.comments.replace_more(limit=None)
            comments = submission.comments.list()
            comment_ids = []

            for comment in comments:
                if comment.score > upvotes:
                    
                    #Make sure comments does not get extracted twice. 
                    #Will also be used to compare comments if a post is hot in regards to several flairs.
                    if comment.id not in comment_ids:
                        earningsthread_data.append((comment.id, comment.body))
                        comment_ids.append(comment.id)
                        
                        n_comments += 1

            n_posts += 1

    print('Flair: ', flair)
    print('Examined posts:', n_posts)
    print('Examined comments:', n_comments)
    
    return earningsthread_data






def run_datacollection():
    resp = requests.dd_data()
    return resp

def test_string():
    datan = [('03/30/21', 'News'), ('gsokoh0', 'The SEC doing fine work as usual??'), 
    ('gsojjcf', "Guys, I think the market might be.....controlled, altered in some way to benefit a select group of people. There's a word for it but, as a retail investor my brain is too smooth to remember it."),  
    ('gsosv4c', '“Much of the leverage was provided by the banks through swaps, according to people with direct knowledge of the deals. That meant that Archegos didn’t have to disclose its holdings in regulatory filings, since the positions were on the banks’ balance sheets.”\n\nSource: www.aljazeera.com/amp/economy/2021/3/29/bb-tiger-cubs-stumble-leaves-banks-with-giant-trading-losses'), 
    ('gsp2j6s', 'Hard to believe you can deal with that much cash and only have less than 15 clients.'), 
    ('gsolnlb', "It's all proprietary. Kevin is in the broom closet with a crystal ball.")]

    en_tv = ['gsp2j6s', 'b', 'c', 'd', 'e', 'f']
    new_list = []
    for letter in en_tv:
        
        check = [i[0] for i in datan]
        if letter not in check:
            new_list.append(letter)
        #if letter != x for x in [i[0] for i in datan]
         #   new_list.append(en_tv)
    
    print(new_list)
   

#Run functions
if __name__ == "__main__":
    access()
    dd_data()
    #news_data()
    #yolo_data()
    #discussion_data()
    #earningsthread_data()
    #run_datacollection()
    #test_string()
