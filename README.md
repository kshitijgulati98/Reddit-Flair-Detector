This is a reddit flair detector for r/India posts.

Part 1 - Data Collection
This part is illustrated in the file 'Part 1 -  Data Collection.ipynb'. I have collected data using Reddit API via the praw library on python. I have collected about 200 posts per flair. 

Part 2 - Exploratory Data Analysis
After collecting the data, I have performed a detailed EDA to decide what features to use while building the model. This part is illustrated in the file 'Part 2 - EDA.ipynb'

Part 3 - Building a Classifier
his part is illustrated in the file "Part 3 - Flair Detector.ipynb".
After loading the dataset, I have performed text preprocessing on the textual data such as comments, title, text(body) to remove special characters and stopwords(from the nltk library). After that I have performed vectorisation followed by TFIDF on these 3 text based features and appended them to other features such as number of comments, score, upvote ratio, locked(T/F). This constitues our feature matrix. 
We then split the dataset into 67% train and 33% test and use the Random Forest, MLP and Naive Bayes Model. The Random forest model performs the best with 81.5 % accuracy. The classification report is as follows:

![classification report](https://drive.google.com/uc?export=view&id=1ALTIJw6wwIGgS2cAd8e-Vw7N93UtDg-p)
