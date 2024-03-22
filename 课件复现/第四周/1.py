from sklearn.datasets import load_iris

data = load_iris()

# print(data.data[0])
#
# print(data.target[0])
#
# print(data.target[[10, 25, 50]])
#
# print(data.target_names)


###########################
# load dataset
iris = data
X = iris.data[:, :]
y = iris.target
    # print(X)

# split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# svm classification
from sklearn import svm
from sklearn import metrics

# 召回率也叫查全率，FN / (TP + FN)
clf = svm.SVC(kernel = 'poly', gamma=0.7, C = 1.0).fit(X_train, y_train)
y_predicted = clf.predict(X_test)
print("---------------poly-------------------")
print("Classification report for %s" % clf)
print(metrics.classification_report(y_test, y_predicted))
print(metrics.confusion_matrix(y_test, y_predicted))

clf = svm.SVC(kernel = 'rbf', gamma=0.7, C = 1.0).fit(X_train, y_train)
y_predicted = clf.predict(X_test)
print("---------------rbf-------------------")
print("Classification report for %s" % clf)
print(metrics.classification_report(y_test, y_predicted))
print(metrics.confusion_matrix(y_test, y_predicted))

print("macro avg precision（宏观平均精确率）：先算出每个类别的精确率在求平均值")
print("micro ave precision（微观平均精确率）：把类别们视为一个直接计算他们的精确率，如TP_1 + TP_2 / (TP_1 + FP_1 + TP_2 + FP_2)")

print("准确率：该分类器能够正确分类的概率，和精确率不同（分类为正的样本里实际为正的概率），准确率是在所有分类中分类正确的概率（不单单考虑正例，其它也算是）")

###############

print("ROC曲线：横坐标为假正例率（所有负例被预测为正的概率），纵坐标为真正例率（所有正例被预测为真的概率，这不就是准确率！！）")

print("假正例率：FTR，真正例率：TTR")

print("完美的分类器，TPR = 1，即召回率超级高，您给定的数据集正例我都成功预测为正了，有没有把负误判为正我不管。")

print("完美的分类器，FTR = 0，您给的负例我都没有预测为正，那不就是负例都预测为负吗？")

print("两者完美结合，正预测为正，负预测为负，就十分美好。所以ROC曲线的面积越大越好，越偏离45度对角线越好。")

