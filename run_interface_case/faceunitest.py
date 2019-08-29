import unittest

from Publicmethod.read_config import read_ini

from business_interface.facecase import Run_class


class Run_case(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01case(self):
        run_test_case = Run_class()
        read_con = read_ini()
        readagin = read_con.Read_ini_loading()
        secs = readagin.sections()#加载ini值
        Selecttheusecase1 = readagin.getint('Selecttheusecase', 'Selecttheusecase')
        if Selecttheusecase1 == 1:
            run_test = run_test_case.test_02_Basic_double_coverage()
            run_test_sui = run_test_case.test_03_Basic_double_coverage()




if __name__ == '__main__':
    unittest.main()
