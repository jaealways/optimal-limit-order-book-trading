import numpy as np

def dSt(mu,dt,vt,lam,eps):
    """
    get dSt using weiner and possion process
    dSt: differential of stock price S in infinitesimal increment time t
    eps: jump size
    """
    weiner_term=np.sqrt(vt)*wiener_process(dt)
    possion_term=eps*poisson_process(lam,dt)-eps*poisson_process(lam,dt)
    return mu*dt + weiner_term + possion_term

def dvt(k,dt,sig,vt,theta):
    """
    get dvt using weiner process
    dvt: differential of S in infinitesimal increment time t

    """
    weiner_term=sig*np.sqrt(vt)*wiener_process(dt)
    return k*(theta-vt)*dt+weiner_term

def poisson_process(lam,dt):
    """
    Get numpy array of poisson process, by dt and lamda
    """
    return np.random.poisson(lam * dt)

def wiener_process(dt):
    """
    get np array of weiner process by dt
    """
    nor = np.random.standard_normal()
    return np.cumsum(nor)*np.sqrt(dt)

def jump(jump_size,dN):
    return (np.exp(jump_size) - 1) * dN


if __name__ == '__main__':
    mu,k,theta,sigma,rho=0.05,3,0.02,0.2,0.5
    T,N,S0,v0=1.0,252,100,0.04
    dt=T/N
    lam_p,lam_n,jump_p,jump_n=1,1,0.05,0.05

    S,v=np.zeros(N+1),np.zeros(N+1)
    S[0],v[0]=S0,v0

    for i in range(1,N+1):
        

        S[i]=S[i-1]+dSt(mu,N,dt,v[i-1],sigma,rho)
        v[i]=dvt(k,N,dt,sigma,v[i-1],theta)

    