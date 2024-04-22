
# Program to apply naive bayes classifier on the iris dataset
'''
Source for theory
https://github.com/sixteenpython/Naive-Bayes/blob/master/machine-learning-with-iris-dataset.ipynb
'''


# Ceated on 22-03-2024 at 12:00pm
from sklearn import datasets, decomposition
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# Import the dataset
iris = datasets.load_iris()
# data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
X = iris.data
y = iris.target

# Split the data into training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

# Create an instance of classifier
model = GaussianNB()

# Fit the model to the training data 
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy rate
accuray = accuracy_score(y_pred, y_test)
print("Accuracy is : ", accuray)