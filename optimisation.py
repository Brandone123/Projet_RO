from cvxopt import solvers, matrix, spdiag, log

def acent(A, b):
    m, n = A.size
    def F(x=None, z=None):
        if x is None:
            # l'algorithme fonctionne de manière itérative
            # il faut choisir un x initial, c'est ce qu'on fait ici
            return 0, matrix(1.0, (n,1))
        if min(x) <= 0.0:
            return None   # cas impossible

        # ici commence le code qui définit ce qu'est une itération
        f = -sum(log(x))
        Df = -(x**-1).T
        if z is None: return f, Df
        H = spdiag(z[0] * x**(-2))
        return f, Df, H

    return solvers.cp(F, A=A, b=b)['x']

A = matrix ( [[1.0,2.0]] ).T
b = matrix ( [[ 1.0 ]] )
print(acent(A,b))