# REDDIT FLAIR DETECTOR
This is a reddit flair detector for r/India posts.

## Part 1 - Data Collection
This part is illustrated in the file [Part 1 -  Data Collection.ipynb](https://github.com/kshitijgulati98/reddit-flair-detector/blob/master/Jupyter%20Notebooks/Part%201%20-%20%20Data%20Collection.ipynb). I have collected data using Reddit API via the praw library on python. I have collected about 200 posts per flair. The collected data is a csv file [reddit_data.csv](https://drive.google.com/file/d/1pgHtXP2qkEPZvcatJB2nrnbvSUGWjk_o/view?usp=sharing).

## Part 2 - Exploratory Data Analysis
After collecting the data, I have performed a detailed EDA to decide what features to use while building the model. This part is illustrated in the file [Part 2 - EDA.ipynb](https://github.com/kshitijgulati98/reddit-flair-detector/blob/master/Jupyter%20Notebooks/Part%202%20-%20EDA.ipynb)

## Part 3 - Building a Classifier
his part is illustrated in the file [Part 3 - Flair Detector.ipynb](https://github.com/kshitijgulati98/reddit-flair-detector/blob/master/Jupyter%20Notebooks/Part%203%20-%20Flair%20Detector.ipynb)
After loading the dataset, I have performed text preprocessing on the textual data such as comments, title, text(body) to remove special characters and stopwords(from the nltk library).The data after filtering and preprocessing the textual features is [cleandata.csv](https://github.com/kshitijgulati98/reddit-flair-detector/blob/master/cleandata.csv)
After that I have performed vectorisation followed by TFIDF on these 3 text based features and appended them to other features such as number of comments, score, upvote ratio, locked(T/F). This constitues our feature matrix. 
We then split the dataset into 67% train and 33% test and use the Random Forest, MLP and Naive Bayes Model. The Random forest model performs the best with 81.5 % accuracy. The classification report is as follows:

![classification report](https://drive.google.com/uc?export=view&id=1ALTIJw6wwIGgS2cAd8e-Vw7N93UtDg-p)

## Part 4 - Building a Web Application
I created a web application using Flask. 
- I have created two seperate web applications. 
  1. The first one for Flair detection by giving the input as a link : [Website- Flair Detector](https://github.com/kshitijgulati98/reddit-flair-detector/tree/master/Website-%20Flair%20Detector)
  2. The second for the automated checkpoint which takes the input as a .txt file with reddit links and outputs a json file        with the results :[Website - Automated_Checkpoint](https://github.com/kshitijgulati98/reddit-flair-detector/tree/master/Website%20-%20Automated_Checkpoint)
  
  The installation for boths apps is exactly the same.
  
  Installaation:-
  1) First download the pickle file for the random forest classifier from https://drive.google.com/file/d/18vIjbW96VATbpCL_6rmMdWCnfvhmnbzU/view?usp=sharing.
  Open the folder for either [Flair Detector](https://github.com/kshitijgulati98/reddit-flair-detector/tree/master/Website-%20Flair%20Detector).
  2) Clone the github repositroy
  3) After downloading the pickle file, put it in the folder 'Website- Flair Detector' of the repository
  4) Open the terminal and route it to the 'Website- Flair Detector'
  5) Next, Create a virtual environment.
  6) type ```pip install -r requirements.txt``` in the terminal
  7) This will install the required libraries
  8) Next, Type ```python app.py``` in the terminal and this will open the app on the browser

After finishing installation, give r/India post link to the flair detector and it will output the predicted flair
The flair detector also has a link to the **automated_checkpoint**
In the automated checkpoint, Give an input of reddit links as a .txt file for example: [reddit-links.txt](https://github.com/kshitijgulati98/reddit-flair-detector/blob/master/reddit-links.txt) and you will get an output in the form of a json file where the key is the link and the value is the predicted flair like this :

![JSON output](https://drive.google.com/uc?export=view&id=1pgHtXP2qkEPZvcatJB2nrnbvSUGWjk_o)



## Part 5 - Deploying the app on Heroku
We deploy the apps on heroku
1) The link for the flair detector is - https://reddit-flair-det.herokuapp.com/
2) The link for the automated_checkpoint is - https://reddit-automated-checkpoint.herokuapp.com/
