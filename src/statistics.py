'''
https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html
'''
import matplotlib.pyplot as plt
import numpy as np

# NORMAL DISTRIBUTION
mu, sigma = 0, 0.1
dist_normal = np.random.default_rng().normal(mu, sigma, 1000)
dist_gamma = np.random.standard_gamma(2, 1)
count, bins, ignored = plt.hist(dist_normal, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)
         ** 2 / (2 * sigma**2)),         linewidth=2, color='r')
plt.show()

# GAMMA DISTRIBUTION
shape, scale = 2., 1.  # mean and width
s = np.random.default_rng().standard_gamma(shape, 1000000)
