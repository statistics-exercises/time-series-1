import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_lam(self) :
        for j in range(1,100) : 
           lam,mean=j*20,0
           for i in range(100) : mean = mean + exponential(lam)
           mean = mean / 100

           bar = np.sqrt(1/(lam*lam)/100)*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean - 1/lam )<bar, "your function for generating exponential random variables does not appear to be working correctly" )
