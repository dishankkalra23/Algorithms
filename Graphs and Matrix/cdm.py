import numpy as np
from statistics import variance as var

# using numpy.array
# : to give two dimensional array representation

# using statistics module
# : to import variance

x = np.array([[0.0347, 0.0897, 0.0912, -73.3024, 6.2152],
              [0.0814, 0.2727, 0.0857, -62.5844, 3.1832],
              [0.0115, 0.2736, 0.0844, -65.2353, 2.7950]])

# print(x)

y = np.array([[0, 1, 1],
              [1, 0, 0],
              [0, 1, 0]])


# print(y)


def cdm(x, y, z):
    """
    # Multilabel Data
    :param x: features
    :param y: labels
    :param z:
    :return: correlation distance matrix
    """
    cdm = []  # cdm : final correlation distance matrix
    for i in range(len(x[0])):
        fea = x[:, i]   # fea : features

        meanf = sum(fea) / len(fea)
        # meanf : mean of features

        corr = []  # corr : storing correlation
        for j in range(len(y[0])):
            lab = y[:, j]
            # lab: Labels
            print()

            meanl = sum(lab) / len(lab)
            # meanl : mean length of labels

            varx = (var(fea, meanf) * var(lab, meanl)) ** 0.5
            # varx : variance of feature
            print(varx)

            covx = np.cov(fea, lab)[0, 1]
            # covx : covariance feature and labels

            corr.append((1 - (covx / varx)))
            # formula : "1 - (covx / varx)" for finding correlation using covariance and variance

        cdm.append(corr)  # Adding correlation into cdm

    return cdm
