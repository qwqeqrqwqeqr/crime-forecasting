

def service(train_data):
    pass






# def run_kfold(clf):
#     kf = KFold(n_splits=10, random_state=42, shuffle=True)
#     outcomes = []
#     fold = 0
#     for train_index, val_index in kf.split(x_trainval):
#         fold += 1
#         Xtrain, Xval = x_trainval.values[train_index], x_trainval.values[val_index]
#         ytrain, yval = y_trainval.values[train_index], y_trainval.values[val_index]
#         clf.fit(Xtrain, ytrain)
#         predictions = clf.predict(Xval)
#         accuracy = accuracy_score(yval, predictions)
#         outcomes.append(accuracy)
#     mean_outcome = np.mean(outcomes)
#     print("Mean Validation Accuracy: {0}".format(mean_outcome))
