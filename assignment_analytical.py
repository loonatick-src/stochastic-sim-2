import numpy as np
import random
from math import factorial

def MM1_sojourn_time(λ, μ):
    return 1.0 / (μ - λ)

def MM1_waiting_time(λ, μ):
    return MM1_sojourn_time(λ, μ) - 1/μ

def MM1_sojourn_waiting_times(λ, μ):
    sjn_time = MM1_sojourn_time(λ, μ)
    wt_time = sjn_time - 1/μ 
    return sjn_time, wtime

def MMn_utilization(λ, μ, n):
    """
    Mean server utilization for M/M/n system.
    ρ = λ / (μ * n)
    """
    ρ = λ / (μ * n)
    return ρ

    
def MMn_p0(λ, μ, n):
    ρ = MMn_utilization(λ, μ, n)
    assert 0 < ρ < 1, "ρ not in (0,1)"
    n_factorial = factorial(n)
    series_term = lambda k: np.power(n*ρ, k) / n_factorial
    series_sum = np.sum(series_term(range(n)))
    
    p0_inv = series_sum + series_term(n) * ρ/(1-ρ)
    p0 = 1/p0_inv
    return p0
    
    
def MMn_pk(λ, μ, n, k):
    ρ = MMn_utilization(λ, μ, n)
    assert 0 < ρ < 1, "ρ not in (0,1)"
    l = min(n, k)
    p0 = MMn_p0(λ, μ, n)
    pk = p0 * np.power(ρ, k) * np.power(n, l)/factorial(l)
    return pk
    
    
def MMn_mean_customer_count(λ, μ, n):
    """
    Asymptotic mean customer count for M/M/n queue
    """
    raise NotImplementedError
    ρ = MMn_utilization(λ, μ, n)
    assert 0 < ρ < 1, "ρ not in (0,1)"
    
def MMn_queueing_prob(λ, μ, n):
    ρ = MMn_utilization(λ, μ, n)
    pn = MMn_pk(λ, μ, n, n)
    P_Q = pn / (1-ρ)
    return P_Q

def MMn_mean_queue_length(λ, μ, n):
    ρ = MMn_utilization(λ, μ, n)
    P_Q = MMn_queueing_prob(λ, μ, n)
    N_q = P_Q * ρ / (1 - ρ)
    return N_q
    
def MMn_mean_waiting_time(λ, μ, n):
    ρ = MMn_utilization(λ, μ, n)
    P_Q = MMn_queueing_prob(λ, μ, n)
    N_q = MMn_mean_queue_length(λ, μ, n)
    T_q = N_q / λ
    return T_q
