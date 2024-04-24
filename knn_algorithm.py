import numpy as np

class KNN:
    def __init__(self, k=3):
        self.k=k

    def fit(self,X_train, y_train):
        self.X_train=X_train
        self.y_train=y_train

    def predict(self, X_test):
        predictions=[]
        for sample in X_test:
            distances=[]
            for train_sample, label in zip(self.X_train, self.y_train):
                dist= np.linalg.norm(sample-train_sample)
                distances.append((dist,label))

            distances.sort(key=lambda x: x[0])
            k_nearest= distances[:self.k]
            k_nearest_labels = [label for _, label in k_nearest]
            prediction = max(set(k_nearest_labels), key=k_nearest_labels.count)
            predictions.append(prediction)

        return predictions
    

X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([2, 2,0, 0, 0])
X_test = np.array([[2.5, 3.5]])

model=KNN(k=3) 
model.fit(X_train,y_train)

predictions=model.predict(X_test)
print("Tahminler:" , predictions)