import random
import numpy as np

def exp_factory(λ):
    return lambda: random.expovariate(λ)


def hyperexp_factory(λ_values, ps, seed = None):
    # within machine epsilon
    assert np.abs(np.sum(ps) - 1.0) == 0

    exp_distributions = [exp_factory(λ) for λ in λ_values]

    def _hyperexp():
        psum = 0
        rand_n = random.uniform(0,1)
        for i, p in enumerate(ps):
            psum += p
            if rand_n < psum:
                return exp_distributions[i]()

    return _hyperexp


def deterministic_factory(mean):
    def _f():
        return mean
    
    return _f


def rolling_average(data, window_size):
    """
    Calculates rolling average of array using kernel of specified size.
    """
    kernel = np.ones(window_size) / kernel_size
    smooth_data = np.convolve(data, kernel, mode='same')
    return smooth_data

def sample_mean_variance(data):
    """returns (sample mean, sample variance) of given 1D data"""
    n = len(data)
    assert n > 1
    smean = np.mean(data)
    svar = np.sum(np.power(data - smean, 2)) / (n-1)
    return smean, svar

def hyperexp_mean_var(λs, ps):
    ps = np.array(ps)
    λs = np.array(λs)
    mean = np.sum(ps / λs)
    expval_xsq = 2*np.sum(ps/ np.power(λs,2))
    var = expval_xsq - np.power(mean, 2)
    return mean, var
