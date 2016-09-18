from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split


class LocationPipeline():

    def __init__(self, clf=RandomForestClassifier(n_estimators=100)):
        self.clf = clf
        self.dv = DictVectorizer(sparse=False)

    def fit(self, X, y):
        tX = self.dv.fit_transform(X)
        tX[tX == 0] = -100
        self.clf.fit(tX, y)
        return self

    def predict(self, X):
        tX = self.dv.transform(X)
        tX[tX == 0] = -100
        return self.clf.predict(tX)

    def predict_proba(self, X):
        tX = self.dv.transform(X)
        tX[tX == 0] = -100
        return self.clf.predict_proba(tX)

    def crossval(self, X, y, n=100):
        means = []
        for _ in range(n):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            self.fit(X_train, y_train)
            means.append(np.mean(self.predict(X_test) == y_test))
        return np.mean(means)
