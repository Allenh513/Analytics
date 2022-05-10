import joblib
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split



class ModelMethods:
    def __init__(self,models,params, features, labels, scoring):
        self.models = models
        self.params = params
        self.features = features
        self.labels = labels
        self.scoring = scoring

    def model_compare(self):
        '''

        :param models: list of model names
        :param params: list of dict model hyper-parameters
        :param features: multi-dimensional list from tfidf vectorizer
        :param labels:
        :param scoring:
        :return:
        '''
        CV = 5
        models_ = []
        for i,m in enumerate(self.models):
            models_.append(m.set_params(**self.params[i]))

        print(models_)
        entries = []
        col_names = ['model_name', 'fold_idx']
        col_names.append(s for s in self.scoring)

        for model in models_:
            model_name = model.__class__.__name__
            cv = cross_val_score(model, self.features, self.labels, scoring=self.scoring, cv=CV)
            for fold_idx, c in enumerate(cv):
                entries.append((model_name, fold_idx, c))
        return entries



