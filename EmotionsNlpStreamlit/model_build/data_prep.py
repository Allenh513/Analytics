import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import json


#global variables
DATA_SRC_TRAIN = '../data/train.txt'
DATA_SRC_TEST = '../data/test.txt'
DATA_SRC_VAL = '../data/val.txt'
COLUMNS = ['TEXT','CLASS']

def data_formatter():
    df_train = pd.read_csv(DATA_SRC_TRAIN, sep=';',header=None)
    df_test = pd.read_csv(DATA_SRC_TEST, sep=';',header=None)
    df_val = pd.read_csv(DATA_SRC_VAL, sep=';',header=None)

    #combine train and test files. We will split later but this simplifies the vectorization process
    df_train = pd.concat([df_train,df_test])

    #rename columns
    df_train.columns = COLUMNS
    df_val.columns = COLUMNS

    #init vectorizer for train
    tfidf_train = TfidfVectorizer(stop_words = 'english')

    #init vectorizer for validation
    tfidf_val = TfidfVectorizer(stop_words='english')

    #convert classes to numeric and create some mapping dict for later use
    df_train['CLASS_ID'] = df_train['CLASS'].factorize()[0]
    class_train_df = df_train[['CLASS','CLASS_ID']].drop_duplicates()

    df_val['CLASS_ID'] = df_val['CLASS'].factorize()[0]
    class_val_df = df_val[['CLASS','CLASS_ID']].drop_duplicates()

    class_class_id_dict = dict(class_train_df.values)
    class_id_class_dict = dict(class_train_df[['CLASS_ID','CLASS']].values)
    with open('../data/emotions.json','w') as j:
        json.dump(class_id_class_dict,j)


    #fit the tdfidf to transform each TEXT into a vector
    train_features = tfidf_train.fit_transform(df_train['TEXT']).toarray()
    val_features = tfidf_val.fit_transform(df_val['TEXT']).toarray()
    #serialize Vectorizer for use in app
    pickle.dump(tfidf_train,open('../models/vectorizer.pkl','wb'))

    train_class = df_train.CLASS_ID
    val_class = df_val.CLASS_ID

    return {
        'FEATURES_TRAIN':train_features,
        'CLASS_TRAIN':train_class,
        'FEATURES_VAL':val_features,
        'CLASS_VAL':val_class,
        'TRAIN_DF':df_train,
        'VAL_DF':df_val
    }
