from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest

def train(X, y):
    knn = KNeighborsClassifier(weights='distance', p=1)
    knn.fit(X, y)

    return knn

def feature_select(X, y):
    features = SelectKBest(k=5)
    features.fit(X, y)
    selected_idx = features.get_support(1)

    return list(X.columns[selected_idx])

def test(knn, test_data, attributes):
    predictions = knn.predict(test_data[attributes])
    prob = knn.predict_proba(test_data[attributes])

    return predictions, prob
