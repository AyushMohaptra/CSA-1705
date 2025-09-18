import numpy as np

class FNN:
    def __init__(self, i, h, o):
        self.W1, self.b1 = np.random.randn(i, h), np.zeros(h)
        self.W2, self.b2 = np.random.randn(h, o), np.zeros(o)

    def sig(self, x): return 1 / (1 + np.exp(-x))
    def sig_d(self, x): return x * (1 - x)

    def forward(self, X):
        self.h_in = np.dot(X, self.W1) + self.b1
        self.h_out = self.sig(self.h_in)
        self.p_in = np.dot(self.h_out, self.W2) + self.b2
        self.p_out = self.sig(self.p_in)
        return self.p_out

    def train(self, X, y, e, lr):
        for _ in range(e):
            p_out = self.forward(X)
            e_out = y - p_out
            d_p_out = e_out * self.sig_d(p_out)
            e_h = np.dot(d_p_out, self.W2.T)
            d_h = e_h * self.sig_d(self.h_out)
            self.W2 += np.dot(self.h_out.T, d_p_out) * lr
            self.b2 += np.sum(d_p_out, axis=0) * lr
            self.W1 += np.dot(X.T, d_h) * lr
            self.b1 += np.sum(d_h, axis=0) * lr

X, y = np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[0],[1],[1],[0]])
nn = FNN(2, 2, 1)
nn.train(X, y, 10000, 0.1)

print(nn.forward(X))
