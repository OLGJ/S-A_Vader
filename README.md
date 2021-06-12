# S-A_Vader
Semantic analysis on wallstreetbets.

The comment-data for this project was scraped from Reddits subforum "Wallstreetbets" between 06/04/21 and 15/04/21.
The stock data was gathered from yahoo finance feed from the same timeperiod.

Comments were cleaned using regular expressions, which were also used for identifying potential stock mentions.
Comments mentioning stocks were analyzed with VADER.

The data was then analyzed with a LMER model which allowed for random intercept and slope. 

The result indicated that comments on Wallstreetbets regarding the most discussed stocks reflects the traded volume in the stock market.


------------------------- Disclaimer -------------------------


All data are not provided as this is a bachelor thesis. 
If you wish to gain access, @me.
