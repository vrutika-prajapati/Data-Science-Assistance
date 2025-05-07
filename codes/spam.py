Certainly! Below is an example of a simple spam detection model using the popular Naive Bayes algorithm from the `sklearn` library. We'll use the SMS Spam Collection Dataset, which is a common dataset for this task.

First, make sure you have the necessary libraries installed:
```bash
pip install pandas numpy scikit-learn
```

Here's the Python code for spam detection:

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# Map labels to binary values
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Convert the text data into a matrix of token counts
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Make predictions
y_pred = clf.predict(X_test_counts)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)
```

This code does the following:
1. Loads the SMS Spam Collection Dataset.
2. Maps the labels 'ham' and 'spam' to binary values 0 and 1, respectively.
3. Splits the data into training and testing sets.
4. Converts the text data into a matrix of token counts using `CountVectorizer`.
5. Trains a Naive Bayes classifier on the training data.
6. Makes predictions on the testing data.
7. Evaluates the model using accuracy and a classification report.

You can further improve this model by using more advanced techniques such as TF-IDF vectorization, hyperparameter tuning, or trying different algorithms like SVM or Random Forest.