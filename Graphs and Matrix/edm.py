import pprint as pp
# pprint: pretty-print is the application of any of various stylistic formatting conventions

cdm = [[0.05456876580630843, 1.9454312341936917, 1.1905457461711129],
       [0.503683956275738, 1.496316043724262, 1.9999909744230189],
       [1.3358817904110032, 0.6641182095889967, 0.016346185224920817],
       [0.3086753264636525, 1.6913246735363476, 1.9714040141558133],
       [1.4075447868503779, 0.5924552131496221, 0.005386007369691859]]


def eucmat(cdm1):
    """

    :param cdm1: provided correlation distance matrix
    :return: eucmat
    """
    edm = []    # initiating Euclidean distance matrix
    for i in range(len(cdm1)):
        list1 = cdm1[i]
        test = []
        for j in range(len(cdm1)):
            list2 = cdm1[j]
            squares = [(p - q) ** 2 for p, q in zip(list1, list2)]
            test.append(sum(squares) ** .5)
        edm.append(test)
    return edm   # edm: Euclidean Distance Matrix


pp.pprint(eucmat(cdm))
