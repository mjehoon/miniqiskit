import numpy as np
def Diagonalization(EJ,ECC,ng,N1,N2):
    N=N2-N1+1
    Hdash=np.zeros(N*N).reshape((N,N))
    Eav=ECC*ng*ng-ECC*ng+ECC/2
    
    for i in range(N):
        for j in range(N):
            if(i==j):
                Hdash[i,j]=ECC*(i+N1-ng)**2-Eav
            if(i==j+1):
                Hdash[i,j]=-EJ/2
            if(i==j-1):
                Hdash[i,j]=-EJ/2

    #return Hdash
    evalue,evector=np.linalg.eig(Hdash)
    idx=evalue.argsort()
    evalue=evalue[idx]
    evector=evector[:,idx]
    return evalue, np.transpose(evector)
