from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def evaluationModel(x_train: list, y_train: list):
    # Here we will evaluate 2 models Logistic Regression and Decision Tree
    models = []
    models.append(('LogisticRegression', LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(("Decision Tree Classifier", DecisionTreeClassifier()))

    results = []
    names = []
    for name, model in models:
        kfold = StratifiedKFold(n_splits=20)
        cv_results = cross_val_score(model, x_train, y_train, cv=kfold,
                                     scoring='accuracy')  # evaluation the model by cross validation function
        results.append(cv_results)
        names.append(name)
    return results, names
