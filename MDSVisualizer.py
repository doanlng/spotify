import matplotlib.pyplot as plt
from sklearn.manifold import MDS


class MDSVisualizer:
    '''visualizing the multidimensional data with mds scaling using different distance metrics'''

    def __init__(self, df, labels):
        self.data = df
        self.labels = labels
        pass

    def mds(self):

        mds_sklearn = MDS(n_components=5)
        reduced = mds_sklearn.fit_transform(self.data)

        plt.figure(figsize=(10, 6))
        plt.scatter(reduced[:, 0], reduced[:, 1])
        plt.title('MDS with Sklearn')
        for label, x, y in zip(self.labels, reduced[:, 0], reduced[:, 1]):
            plt.annotate(
                label,
                xy=(x, y),
                xytext=(-10, 10),
                textcoords='offset points'
            )
        plt.show()
        print(mds_sklearn.stress_)
