import numpy as np
import pandas as pd


def interpretattion(norm_data, data, labels, centroids, norm):
    norm_data_matrix = norm_data.as_matrix()
    D = np.sum(norm_data_matrix * norm_data_matrix)  # data scatter
    me = np.mean(data[norm_data.columns].as_matrix(), axis=0)
    # range = np.max(data, 0) - np.min(data, 0)
    scac = 0  # proportion of data scatter taken into account by the "first" clusters
    mem = labels  # membership
    rc = norm.apply_reverse(data, norm_data, centroids)  # centers real scale
    sc = centroids  # centers standardised
    ak = np.max(mem)
    result = dict()
    for number in np.unique(labels):
        cluster = norm_data_matrix[labels == number]  # cluster data
        centr_real = rc[number]  # real center
        centr_norm = sc[number]  # center standardized
        # ----- getting differences from grand mean
        diff = centr_real - me
        on = (centr_real - me) / me
        ovn = np.round(100 * on)  # same, percent
        # -----------getting cluster's contribution
        clcon = np.dot(centr_norm, centr_norm)
        sccl = np.sum(clcon)
        scatcl = sccl * len(cluster) / D  # relative contribution of the cluster
        scac = scac + scatcl
        result[number] = {'centr_real': centr_real, 'diff': diff,
                          'ovn': ovn, 'centr_norm': centr_norm}
        result[number]['scatcl'] = scatcl
        result[number]['scac'] = scac
    return result


class Cluster(object):
    def __init__(self, label, centroid, power):
        self.centroid = centroid
        self.power = power
        self.label = label


class Report:
    report = None

    def __init__(self):
        self.alg = None
        self.data = None
        self.norm = None
        self.labels = None
        self.u_labels = None
        self.centroids = None
        self.apc = None
        self.norm_data = None
        self.clusters = dict()

    def set_alg(self, alg):
        self.alg = alg

    def set_norm_data(self, norm_data):
        self.norm_data = norm_data

    def set_data(self, data):
        self.data = pd.DataFrame()
        for column in data:
            col_data = data[column]
            try:
                pd.to_numeric(col_data)
                self.data[column] = col_data
            except ValueError:
                unique_values = col_data.unique()
                for uv in unique_values:
                    new_col = pd.Series(data=0, index=col_data.index)
                    new_col[col_data == uv] = 1
                    # self.data[column] = new_col
                    self.data[column + str('[' + uv + ']')] = new_col
                    # if len(unique_values) == 2:
                    #     break
                    # self.data = data

    def set_labels(self, labels):
        self.labels = labels
        self.u_labels = np.unique(self.labels)
        self.centroids = None

    def set_centroids(self, centroids):
        self.centroids = centroids

    def set_norm(self, norm):
        self.norm = norm

    def set_apc(self, apc):
        self.apc = apc

    def __str__(self):
        rprt = []
        if self.labels is None:
            return 'Clusters not derived. Empty report.'
        if self.centroids is None:
            features = self.norm_data.shape[1]
            self.centroids = np.empty((0, features))
            for l in self.u_labels:
                new_centroid = np.mean(self.norm_data[self.labels == l], axis=0)
                self.centroids = np.vstack((self.centroids, new_centroid))
        rprt.append('Intelligent K-Means resulted in ' + str(len(self.u_labels)) + ' clusters;')
        rprt.append('Algorithm used: ' + self.alg if self.alg is not None else 'N/A')
        if self.norm:
            rprt.append('Normalization:\n\t')
            rprt.append("\t" + str(self.norm.center_str()))
            rprt.append("\t" + str(self.norm.range_str()))
        else:
            rprt.append('Normalization: N/A')
        rprt.append('Anomalous pattern cardinality to discard: ' + str(self.apc if self.apc is not None else 'N/A'))
        rprt.append('Features involved:')
        for f_name in self.norm_data.columns:
            feature = self.norm_data[f_name]
            # import re
            # f_name_new = re.sub('\[.*\]', '', f_name)
            feature_real = self.data[f_name]
            try:
                rprt.append(
                    '\t' + str(f_name) + ': ' + ' mean = {:10.3};'.format(
                        feature_real.mean()) + ' std = {:10.3};'.format(
                        feature_real.std()))
            except:
                rprt.append(
                    '\t' + str(f_name) + ': ' + ' mean = Nominal;'
                    + ' std = Nominal;')
        interp = interpretattion(self.norm_data, self.data, self.labels, self.centroids, self.norm)
        rprt.append('Cluster-specific info:')
        for l in self.u_labels:
            rprt.append('Cluster #' + str(l) + ' [' + str(np.count_nonzero(self.labels == l)) + ' entities]:')
            rprt.append('\tcentroid (real): ' + str(['{0:.3f}'.format(x) for x in interp[l]['centr_real']]))
            rprt.append('\tcentroid (norm): ' + str(['{0:.3f}'.format(x) for x in interp[l]['centr_norm']]))
            rprt.append('\tcentroid (% over/under grand mean): ' + str(interp[l]['ovn']))
            rprt.append(
                '\tcontribution (proper and cumulative): {:10.2}'.format(interp[l]['scatcl']) + ',{:10.2}'.format(
                    interp[l]['scac']))
            nado, nido = [], []
            for f, f_name in enumerate(self.norm_data.columns):
                if interp[l]['ovn'][f] > 30:
                    nado.append(f_name)
                if -interp[l]['ovn'][f] > 30:
                    nido.append(f_name)
            rprt.append('\tfeatures significantly larger than average: ' + ("None" if nado == [] else ",".join(nado)))
            rprt.append('\tfeatures significantly smaller than average: ' + ("None" if nido == [] else ",".join(nido)))
            #     TODO CHANGE!!! !!!
            self.clusters[l] = Cluster(l, interp[l]['centr_real'], np.count_nonzero(self.labels == l))
        rprt = [x.replace("\n", "") for x in rprt]
        return '\n'.join(rprt)

    @staticmethod
    def get_report():
        if Report.report is None:
            Report.report = Report()
        return Report.report
