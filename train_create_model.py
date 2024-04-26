import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
import pickle
import json

from common_functions import clean_resume

# ======================= READ DATASET ======================
def read_dataset(file_with_path):
    df = pd.read_csv(file_with_path)
    return df

def plot_category_Count(df, bar=0, pie=0):
    # bar chart
    if bar:
        sns.countplot(x=df.Category)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
    
    # pie
    if pie:
        counts = df.Category.value_counts()
        labels = df.Category.unique()
        plt.pie(counts, labels=labels, autopct='%1.1f%%', shadow=True)
        plt.show()



def encode_category(df):
    le = LabelEncoder()
    df['category_value'] = df['Category']
    df['Category'] = le.fit_transform(df['Category'])

    
    # create json file for category mapping
    category_mapping = df.set_index('Category')['category_value'].to_dict()
    with open('category.json', 'w') as f:
        json.dump(category_mapping, f, indent=4)

    return df

def vectorized_resume(df):
    tfidf = TfidfVectorizer(stop_words='english', min_df=1)
    tfidf.fit(df['Resume'])
    vectorized_text = tfidf.transform(df['Resume'])
    pickle.dump(tfidf, open('vectorizer.pkl', 'wb'))
    return vectorized_text, tfidf

# Read dataset
df = pd.read_csv("UpdatedResumeDataSet.csv")
df = encode_category(df)
# Clean resumes
df['clean_resume'] = df.Resume.apply(lambda x: clean_resume(x))

# Split dataset into training and testing
x_train, x_test, y_train, y_test = train_test_split(df['clean_resume'], df['Category'], test_size=0.2, random_state=42)

# Initialize and fit vectorizer
vectorizer = TfidfVectorizer(stop_words='english', min_df=1)
vectorizer.fit(x_train)

# Vectorize training data
x_train_vec = vectorizer.transform(x_train)

# Train KNeighborsClassifier
cl_model = OneVsRestClassifier(KNeighborsClassifier())
cl_model.fit(x_train_vec, y_train)

# Save models
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
pickle.dump(cl_model, open('classifier.pkl', 'wb'))





