import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==101, "The number of plotted data points is incorrect" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i-50-this_x[i])<1e-7, "One or more of your x values are not correct" )
            self.assertTrue( np.abs(0.1*(i-50)-this_y[i])<1e-7, "One or more of your y values are not correct" )
