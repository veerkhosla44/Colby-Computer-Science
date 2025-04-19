import numpy as np
from adaline import Adaline

class AdalineLogistic(Adaline):
    def activation(self, net_in):
        return 1 / (1 + np.exp(-net_in))

    def predict(self, features):
        net_in = self.net_input(features)
        net_act = self.activation(net_in)
        return np.where(net_act >= 0.5, 1, 0)

    def loss(self, y, net_act):
        return -np.sum(y * np.log(net_act) + (1 - y) * np.log(1 - net_act))