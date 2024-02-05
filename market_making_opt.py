import numpy as np


def dSt(mu,dt,vt,db1,lam_p,lam_n,jump_p,jump_n):
    """
    get dSt using weiner and possion process
    dSt: differential of stock price S in infinitesimal increment time t
    """
    weiner_term=np.sqrt(vt)*db1
    possion_term=jump_p*poisson_process(lam_p,dt)-jump_n*poisson_process(lam_n,dt)
    return mu*dt + weiner_term + possion_term

def dvt(k,dt,sig,db2,vt,theta):
    """
    get dvt using weiner process
    dvt: differential of S in infinitesimal increment time t

    """
    weiner_term=sig*np.sqrt(vt)*db2
    return k*(theta-vt)*dt+weiner_term

def poisson_process(lam,dt):
    """
    Get numpy array of poisson process, by dt and lamda
    """
    return np.random.poisson(lam * dt)

def wiener_process(dt,N):
    """
    get np array of weiner process by dt
    """
    dB1 = np.sqrt(dt) * np.random.randn(N)
    dB2 = rho * dB1 + np.sqrt(1 - rho**2) * np.sqrt(dt) * np.random.randn(N)
    return dB1,dB2

def jump(jump_size,dN):
    return (np.exp(jump_size) - 1) * dN


if __name__ == '__main__':
    mu,k,theta,sigma,rho=0.05,3,0.02,0.2,0.5
    T,N,S0,v0=1.0,252,100,0.04
    dt=T/N
    lam_p,lam_n,jump_p,jump_n=1,1,0.05,0.05

    S,v=np.zeros(N+1),np.zeros(N+1)
    S[0],v[0]=S0,v0

    dB1,dB2=wiener_process(dt,N)
    
    for i in range(1,N+1):
        # check for the negative value or extremly close to zero
        # dvt = vt * ~ -> How to make equation
        v[i]=v[i-1]+dvt(k,dt,sig,dB2[i-1],vt,theta)        
        S[i]=S[i-1]+dSt(mu,dt,v[i],dB1[i-1],lam_p,lam_n,jump_p,jump_n)
    print(v,S)
    