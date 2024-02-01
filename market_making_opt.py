import numpy as np

def dSt(mu,n,dt,vt,lam,eps):
    """
    get dSt using weiner and possion process

    Args:
        eps: jump size
    """
    weiner_term=np.sqrt(vt)*wiener(n,dt)
    possion_term=eps*poisson(lam,dt)-eps*poisson(lam,dt)
    return mu*dt + weiner_term + possion_term

def dvt(k,n,dt,sig,vt,theta):
    """
    
    """
    weiner_term=sig*np.sqrt(vt)*wiener(n,dt)
    return k*(theta-vt)+weiner_term

def poisson(lam,n,dt):
    """
    Get numpy array of poisson process with n times, dt and lamda
    """
    np.random.poisson(lam * dt)
    return 

def wiener(n,dt):
    """
    get np array of weiner process with n times and dt
    """
    nor = np.random.standard_normal(size=n)
    wp = np.cumsum(nor)*np.sqrt(dt)
    return wp

