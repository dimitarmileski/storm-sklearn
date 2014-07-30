from __future__ import absolute_import, print_function, unicode_literals
from streamparse.bolt import Bolt

import os
import pickle

import numpy as np
from sklearn.externals import joblib


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        mmpath = '/Users/danielfrg/code/storm-sklearn/data/mmap.pickle'
        model_path = '/Users/danielfrg/code/storm-sklearn/data/model.pickle'

        if not os.path.exists(mmpath):
            f = open(model_path, 'r')
            clf = pickle.load(f)
            f.close()

            joblib.dump(clf, mmpath)

        self.clf = joblib.load(mmpath)


    def process(self, tup):
        row_s = tup.values[0]
        row = np.fromstring(row_s)
        prediction = self.clf.predict(row)
        self.emit([row_s, str(prediction)])
        self.log('%s: %d' % (row_s, str(prediction)))


if __name__ == '__main__':
    WordCounter().run()