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
    series_term = lambda k: np.power(n*ρ, k) / factorial(k)
    sequence = np.array([series_term(k) for k in range(n)])
    series_sum = np.sum(sequence)
    
    p0_inv = series_sum + series_term(n)/(1-ρ)
    p0 = 1/p0_inv
    return p0
    
    
def MMn_pk(λ, μ, n, k):
    ρ = MMn_utilization(λ, μ, n)
    assert 0 < ρ < 1, "ρ not in (0,1)"
    l = min(n, k)
    p0 = MMn_p0(λ, μ, n)
    pk = p0 * np.power(ρ, k) * np.power(n, l)/factorial(l)
    return pk
    
    
def MMn_mean_queue_length(λ, μ, n):
    """
    Asymptotic mean customer count for M/M/n queue
    """
    ρ = MMn_utilization(λ, μ, n)
    p0 = MMn_p0(λ, μ, n)
    nρ = n * ρ
    L_Q = np.power(nρ, n+1) * p0/(n * factorial(n) * np.power(1 - ρ, 2))
    return L_Q
    
    
def MMn_queueing_prob(λ, μ, n):
    ρ = MMn_utilization(λ, μ, n)
    pn = MMn_pk(λ, μ, n, n)
    P_Q = pn / (1-ρ)
    return P_Q

    
def MMn_mean_waiting_time(λ, μ, n):
    L_Q = MMn_mean_queue_length(λ, μ, n)
    T_Q = L_Q / λ
    return T_Q

def MH1_soujorn_time(λ, μs, ps):
    μ_inv = np.sum(ps/μs)
    μ = 1/μ_inv
    ρ = λ*μ_inv
    var = 2*np.sum(ps/np.power(μs, 2)) - μ_inv**2 
    L = ρ + (ρ**2 * (1 + var * μ**2))/(2*(1 - ρ))
    return L/λ

def MH1_waiting_time(λ, μs, ps):
    μ_inv = np.sum(ps/μs)
    return MM1_sojourn_time(λ, μs, ps) - μ_inv

def MD1_soujorn_time(λ, μ):
    ρ = λ/μ
    L = ρ + ρ**2/(2*(1 - ρ))
    return L/λ

def MD1_waiting_time(λ, μ):
    return MD1_soujorn_time(λ, μ) - 1/μ
