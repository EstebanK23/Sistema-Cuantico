def suma(t1,t2):
    res_r=t1[0]+t2[0]
    res_i=t1[1]+t2[1]
    fin=(res_r,res_i)
    return fin

def multiplicacion(t1,t2):
    res_r=t1[0]*t2[0]+((t1[1]*t2[1])*-1)
    res_i=t1[0]*t2[1]+t1[1]*t2[0]
    fin=(res_r,res_i)
    return fin

def multi_mat(vec,mat):
    mat_fin=[[(0,0)]*len(mat[0]) for x in range(len(vec))]
    aux=0
    if len(mat_fin)==1:
        aux=1
    for i in range(len(vec)):
        for j in range(len(mat[0])):
            for k in range(len(mat_fin)+aux):

                mat_fin[i][j]=suma(mat_fin[i][j],multiplicacion(vec[i][k],mat[k][j]))
    return mat_fin

def conjugado(t1):
    fin=(t1[0],t1[1]* -1)
    return fin

def norma_mat(mat):
    num1=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            x=mat[i][j]
            num1+=(x[0]**2+x[1]**2)
    res=num1**0.5
    return res

def mat_trans(mat):
    mat_fin=[[None]*len(mat) for x in range(len(mat[0]))]
    for i in range(len(mat_fin)):
        for j in range(len(mat_fin[0])):
            mat_fin[i][j]=mat[j][i]
    return mat_fin

def mat_conju(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j]=conjugado(mat[i][j])
    return mat

def mat_adjun(mat):
    res=mat_conju(mat_trans(mat))
    return res

def magnitud(vec):
    res=0
    for i in range(len(vec)):
        res+=abs((vec[i][0][0])**2+(vec[i][0][1])**2)
    res_fin=res**(0.5)
    return res_fin

def probabilidad(vec,posicion):
    var1=norma_mat(vec)
    lista=vec[posicion]
    res=lista[0][0]**2+lista[0][1]**2
    res_fin=res/(var1**2)
    return res_fin

def transicion(mat1,mat2):
    up = multi_mat(mat_adjun(mat2),mat1)
    down = norma_mat(mat1)*norma_mat(mat2)
    left = up[0][0][0] / down
    rigth = up[0][0][1] / down
    res_fin = left + rigth
    return res_fin
