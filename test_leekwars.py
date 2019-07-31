import unittest
import random
import leek_wars
import function_essential
import garden
import time

class leekwars_test(unittest.TestCase):
    def test_choice(self):
        """Test already true to see if unittest works"""
        self.assertEqual(True, True)

    def test_readCredential(self):
        start_time=time.time()
        credential = function_essential.readCredential("credential.txt","id")
        end_time = time.time()
        execution_time = end_time - start_time
        print("execution_time = " + str(execution_time))
        # test if function execution time less than 1 second
        self.assertEqual(execution_time < 1, True)
        print(type(credential))
        self.assertEqual(str(type(credential)), "<class 'str'>")

    def test_garden_getGardenForLeek(self):
        start_time=time.time()
        data_out_garden_getGardenForLeek = garden.getGardenForLeek(leek_wars.leek_id,leek_wars.token_global)
        end_time = time.time()
        execution_time = end_time - start_time
        print("execution_time = " + str(execution_time))
        # test if function execution time less than 2 second, 1 sec seems to be too short for this function
        self.assertEqual(execution_time < 2, True)
        self.assertNotEqual(str(type(data_out_garden_getGardenForLeek)), "<class 'disct'>")
        self.assertEqual(str(type(data_out_garden_getGardenForLeek)), "<class 'dict'>")


    def test_getFarmerOpponents(self):
        start_time=time.time()
        data_out_test_getFarmerOpponents=garden.getFarmerOpponents(leek_wars.token_global)
        end_time=time.time()
        execution_time=end_time-start_time
        print("execution_time = "+str(execution_time))
        #test if function execution time less than 1 second
        self.assertEqual(execution_time < 1,True)

        #test if class return is correct
        self.assertEqual(str(type(data_out_test_getFarmerOpponents)), "<class 'dict'>")



if __name__ == '__main__':
    unittest.main()


