# TCM final MAKE project: welcome to our README page that documents our journey through the MAKE project.

# How did we select our topic?
We were inspired by our class discussion on cryptocurrency and Bitcoin. The Verge article and podcast episode that Professor Scott posted was helpful towards highlighting the debate about Bitcoin's viability as a virtual currency (a means of exchange, unit of account, or store of value) vs. its more speculative aspect as an investment/security. In class, our discussion on blockchain technology, the accessibility to buy Bitcoin, and its limited supply brought our attention to if we should seriously considered buying and trading Bitcoin. This led to our question:
1) Should we as individuals buy Bitcoin, and more broadly cryptocurrency in general.
2) If so, when and what should we buy?

# How did we determine which language and tool to use?
To approach this our questions, we decided to go on Kaggle and find a dataset that would best showcase the performance of cryptocurrencies over time so we could analyze potential trends, make forecasts, and draw conclusions on the data. Looking at historical data and making predictions about the future might be helpful for helping us formulate an answer on crypto's investment potential. We decided that the best tool to use would be Jupyter Notebook and Pandas given its ability to work with large Excel datasets. To make this more challenging, we installed libraries we didn't learn like Seaborns for plotting and Statsmodel for forecasting - these new libraries would allow us to challenge ourselves but also improve the quality of our observations. 

Used dataset on Cryptocurrency from Kaggle: https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory

# What did we hope to accomplish?
There's generally two sides to the discussion about Bitcoin and crypto. It is super volatile which could be good for capital gains, BUT really risky to demand shocks so you would probably lose a lot. At the end of our project, we hoped for the data to either indicate that the future market price of Bitcoin and relevant crypto would be great and we should invest, or that the future looks terrible (demand shocks, decreased or even negative growth) and we should short or not invest.

# How did the project go? What did we struggle on?
The first part was straight forwarded, we found the Kaggle dataset and implemented some of the functions we learned in class to import the csv files, clean up the data, and make sure we could set our tables for our analysis. We ended up having to pip install new libraries: Seaborns and Stats. 

Challenges & their Respective Solutions:

1. The imported datasets had columns that were different datatypes and we couldn't use functions like adding or subtracting. To address this, we did a .dtypes to look at which were integers, floats, and strings. Then we converted the datatypes so that we can manipulate them, and checked .dtypes again to see if we converted corrrectly.

2. We wanted to keep of a copy of a pandas data frame, so that we can modify it while saving the original. However, we realized that modifying the copy changes the original dataframe too. The problem here was that creating a dataframe named "bitcoin" and setting it equal to another called "bitcoin_q3" meant we created pointers (it pointed to the information), not buckets that contained the information. If we made changes to "bitcoin_q3", it would also affect "bitcoin". We ran into some issues when we modified the dataframe's index and other properities, so instead of setting it equal, we used the .copy() function.

3. We could not assign graph titles and plot graphs next to each other. To solve this, we created multiple axes, essentially a 2x2 empty frame and assigned each graph to its respect location on the axis. An example would be (0,0) (1,0) (0,1) (1,1). We also added graph titles using ax.set_title which was a good addition to our knowledge on using Seaborns for plotting.

4. Git hub challenges: Heather had some issues where if she forgot to "git pull" before working on the Jupyter notebook, she had to figure out a way to resolve conflicts before the merge could occur. In the end, there was once where she had to delete the cloned library in her personal files and reclone it.

5. The forecasting model using the Statsmodel libraries was much more complex than at first anticipated. Diving further into the function for exponential smoothing, we found out that we also had to first change the index to the "Date" column, and update the frequency, whether it was 15 days or 3 months - these arguments changed the framing of our forecasts. 
 
# Post project experience

Takeaways: 
Heather: GitHub is a usedful tool for collaboration. I learned a lot more about the Seaborns library - specific details you can add like text to graphs, how to make specific plots, and what functions to use.

Allen: I learned to make a complex set of data very readable and presentable through Jupyter notebook. It was helpful to create graphs and write comments so that when the read scrolls through, they can understand the code and the outputs from code, this is quite different than VSCode where we just see an output in terminal.


Next steps and improvements: potentially looking into more coins, maybe in the next couple of months, we can look back and compare actual market performance of the coins we analyzed and see how accurate our predictions were. We can also explore other potential forecasting models that are more fitting - ex: maybe a regression.
