from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest

def train(X, y):
    knn = KNeighborsClassifier(n_neighbors=13, weights='distance', p=2)
    knn.fit(X, y)

    return knn

def feature_select(X, y):
    features = SelectKBest(k=4)
    features.fit(X, y)
    selected_idx = features.get_support(1)
    selected_features = list(X.columns[selected_idx])
    print('Selected features:', selected_features)

    return selected_features

def test(knn, test_data, attributes):
    predictions = knn.predict(test_data[attributes])
    prob = knn.predict_proba(test_data[attributes])

    return predictions, prob
