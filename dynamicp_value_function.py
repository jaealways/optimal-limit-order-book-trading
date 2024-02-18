import numpy as np

# Quadratic Utility Function

def utility_function(X_T, S_T, q_T, alpha):
    eta_qT = -alpha * q_T**2
    return X_T + q_T * S_T + eta_qT

def value_function(X_T, q_T, S_T, sigma, v, alpha, T, delta_strategy):
    """

    """
    time_steps = np.linspace(0, T, num=len(delta_strategy))
    inventory_penalty = -v**2 * np.trapz(q_T**2, time_steps)
    
    values = [utility_function(X_T, S_T, q_T, alpha) + inventory_penalty for q_T in delta_strategy]
    return max(values)


if __name__=="__main__":
    alpha,v,sigma = 0.1,0.05,0.2
    T,X_T,S_T = 1.0,100,50
    q_T = np.array([10, 20, 30])

    delta_strategy = [np.array([0, 0.1, -0.1])] * len(q_T)

    value = value_function(X_T, q_T, S_T, sigma, v, alpha, T, delta_strategy)
    print("Value function:", value)





