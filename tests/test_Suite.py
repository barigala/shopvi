import os
import  unittest
from tests.shopTEST import ShopTest

shop_tests = unittest.TestLoader().loadTestsFromTestCase(ShopTest)

sanityTest = unittest.TestSuite([shop_tests])

unittest.TextTestRunner(verbosity=1).run(sanityTest)
