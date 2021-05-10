# make_project
TCM final project.

# Used dataset on Cryptocurrency from Kaggle
https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory

# Rubric
Team GitHub requirement: If team didnot use GitHub, subtract five points. (-5) Used GitHub but little group activity on project page, or did not **include a description of use /learning process**, subtract three points.(-3)

Clearly understand story of project and challenges along the way.

# Documentation of Make Project
Why did we choose this topic?
We were inspired by our discussion in class about 
Why did we choose this dataset?
How did it fit into using Jupyter Notebook, based on our discussion in class?
What did we hope to accomplish?
How did it do? WHat did we struggle with?
Reflection? How we applied what we learned or improve on?

# How did we select our topic?
We were inspired by our class discussion on cryptocurrency and Bitcoin. The Verge article and podcast episode that Professor Scott posted was helpful towards highlighting the debate about Bitcoin's viability as a virtual currency (a means of exchange, unit of account, or store of value) vs. its more speculative aspect as an investment/security. In class, our discussion on blockchain technology, the accessibility to buy Bitcoin, and its limited supply brought our attention to if we should seriously considered buying and trading Bitcoin. This led to our question:
1) should we as individuals buy Bitcoin, and more broadly cryptocurrency in general
2) if so, when and what should we buy?

# How did we determine which language and tool to use?
To approach this our questions, we decided to go on Kaggle and find a dataset that would best showcase the performance of cryptocurrencies over time so we could analyze potential trends, make forecasts, and draw conclusions on the data. Looking at historical data and making predictions about the future might be helpful for helping us formulate an answer on crypto's investment potential. We decided that the best tool to use would be Jupyter Notebook and Pandas given its ability to work with large Excel datasets. To make this more challenging, we installed libraries we didn't learn like Seaborns for plotting and Statsmodel for forecasting - these new libraries would allow us to challenge ourselves but also improve the quality of our observations.

# What did we hope to accomplish?
There's generally two sides to the discussion about Bitcoin and crypto. It is super volatile which could be good for capital gains, BUT really risky to demand shocks so you would probably lose a lot. At the end of our project, we hoped for the data to either indicate that the future market price of Bitcoin and relevant crypto would be great and we should invest, or that the future looks terrible (demand shocks, decreased or even negative growth) and we should short or not invest.

# How did the project go? What did we struggle on?
The first part was straight forwarded, we found the Kaggle dataset and implemented some of the functions we learned in class to import the csv files, clean up the data, and make sure we could set our tables for our analysis.  We ended up having to pip install new libraries: Seaborns and Stats. 

Challenges & Solutions:
- Different datatypes: needed to convert datatypes for better manipulation, checked using dtypes that conversion was done correctly
- Dataframe properties: Creating a dataframe named "bitcoin" and setting it equal to another called "bitcoin_q3" meant we created pointers (it pointed to the information), not buckets that contained the information. If we made changes to "bitcoin_q3", it would also affect "bitcoin". We ran into some issues when we modified the dataframe's index and other properities, so instead of 
- graphing problems, allocate axis and titles
- git hub challenges - reclone repository
- Forecast model understanding - changing index to the date, and updating frequency
 

# Post project experience
Takeaways: I learned to create separate functions and call them as the main program, instead of writing one long page of code as the program itself. I also learned to store json data into a dictionary and append that to a list, and call the variable using return. Lastly, I was able to practice using while loops, for-loops, and if-statements in my functions so that my program can be more efficient. 
Next steps and improvements: I would like to offer higher user-friendly options when it comes to searching for news. This means including the ability to search multiple topics, filter through multiple keywords, and offer the option to search historical data as well, not just the latest news. 
Going forward, I would probably build another function that uses other currents API endpoints and ask the user to define what his use case is first. Then, I would call the relevant function which will give the program more use cases.
I might also find a way to get the output without using return because it shows the list result from my output dictionary. This makes the terminal less messy for the user. 
As well, I might explore writing my results on a csv file such that the Excel columns correspond to categories of information. (ie. One column for title, one for URL, one for date, etc.) I would like to see if this improves the digestibility of information for the user. 

