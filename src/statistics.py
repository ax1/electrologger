'''
https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html
'''
import matplotlib.pyplot as plt
import numpy as np

# ------------- NORMAL DISTRIBUTION------------------------
mu, sigma = 10, 0.1
size = 100
normal = np.random.default_rng().normal(mu, sigma, size)

# get random val ()
#  when infinite values required on the same curve
print('')
for r in range(10):
    print(np.random.choice(normal))

# when finite values required, this is faster
print('')
for r in range(size):
    print(normal[r])


# walk over the curve
print('')
curve = np.sort(normal)
for r in range(size):
    print(curve[r])

# plot distribution
count, bins, ignored = plt.hist(normal, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)
         ** 2 / (2 * sigma**2)),         linewidth=2, color='r')
plt.show()

# ---------------GAMMA DISTRIBUTION-------------------------
dist_gamma = np.random.standard_gamma(2, 1)
shape, scale = 2., 1.  # mean and width
s = np.random.default_rng().standard_gamma(shape, 1000000)
