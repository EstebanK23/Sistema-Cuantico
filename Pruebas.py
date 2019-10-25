import unittest
import ProbTrans

class MytestCase(unittest.TestCase):
    def test_Probabilidad(self):
        vec=[[(-3,-1)],[(0,-2)],[(0,1)],[(2,0)]]
        posicion=2
        res=0.05263157894736841
        resultado=ProbTrans.probabilidad(vec,posicion)
        self.assertEqual(res,resultado)

    def test_Transicion(self):
        mat1=[[(1,0)],[(0,-1)]]
        mat2=[[(0,1)],[(1,0)]]
        res=-0.9999999999999998
        resultado=ProbTrans.transicion(mat1,mat2)
        self.assertEqual(res,resultado)

if __name__ == '__main__':
    unittest.main()
        
        
