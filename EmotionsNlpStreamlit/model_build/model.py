from sklearn.svm import LinearSVC
import data_prep
from sklearn.model_selection import  train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from datetime import datetime
import joblib

data = data_prep.data_formatter()

train_features = data['FEATURES_TRAIN']
train_class = data['CLASS_TRAIN']
val_features = data['FEATURES_VAL']
val_class = data['CLASS_VAL']

#svc was best model from testing (see Jupyter Notebook for EDA and model testing)
svc = LinearSVC()

X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(train_features,
                                                                                 train_class,
                                                                                 data['TRAIN_DF'].index,
                                                                                 test_size=0.25,
                                                                                 random_state=1)
svc.fit(X_train, y_train.ravel())
y_pred = svc.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred,
                           target_names=data['TRAIN_DF']['CLASS'].unique())


joblib.dump(svc, '../models/{}.pkl'.format(svc.__class__.__name__))


