from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn.svm import SVC
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize
from sklearn.cross_validation import cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score, make_scorer
import score

data = np.array([ [ float(x) for x in line.split(',') ] for line in open('ML-contest-training/completedData.csv') ])

normdata = normalize(data[:,:-1])

# prj = PCA(n_components = 100)
# prj = LDA(n_components = 100)
# newdata = prj.fit_transform(normdata,data[:,-1])
newdata = normdata
# for i in range(5):
# 	print newdata[i]
print len(newdata)
print len(newdata[0])
print np.shape(newdata)
print "data done"
print "logistic initialized"
# clf.fit(data[:,:-1], data[:,-1])
print "fitted data"
skf = StratifiedKFold(data[:,-1], n_folds=10, shuffle=True)
output =[]
for train, test in skf:
	clf = BaggingClassifier(n_estimators = 100)
	clf = clf.fit([ newdata[i][:] for i in train ], [ data[i][-1] for i in train ])
	prediction = clf.predict([ newdata[i][:] for i in test ])
	# pred = []
	# for i in prediction:
	# 	if(i > 1.5):
	# 		pred.append(2)
	# 	else:
	# 		pred.append(1)
	print(score.get_score(prediction,[ data[i][-1] for i in test ]))
	print "done"
# score = cross_val_score(clf, newdata[:,:], data[:,-1], cv = 5, scoring = 'get_score')
# print "in scores"
# for i in score:
# 	print i

# print "out of score"
# for i in output:
# 	print i
