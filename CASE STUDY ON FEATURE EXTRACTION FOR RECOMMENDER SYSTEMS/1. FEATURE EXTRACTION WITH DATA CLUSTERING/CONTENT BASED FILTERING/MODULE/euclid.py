import numpy as np

class EuclideanDistance:
    '''  This class computes the euclidean distance between each cluster
        and each data point available in the dataset.

        Returns a array of euclidean distance
    '''
    def __init__(self, data, cluster, centroid):
        self.data = data
        self.cluster = cluster
        self.centroid = centroid

    def compute(self):
        euc_dis = np.zeros((self.data.shape[0], self.cluster))
        for i in range(self.data.shape[0]):
            for k in range(self.cluster):
                dist = 0
                for j in range(self.data.shape[1]):
                    val = (self.data[i][j] - self.centroid[k][j])**2
                    dist = dist + val
                ed = np.sqrt(dist)
                euc_dis[i][k] = ed
        return euc_dis