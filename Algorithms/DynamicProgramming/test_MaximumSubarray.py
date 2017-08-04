import unittest
from MaximumSubarray import MaximumSubArraySum
class MaxiMumSubarrayTests(unittest.TestCase):
    
    def setUp(self):
        self.array = [1, 2, 4]
            
    def test_sum(self):
        self.assertEqual(MaximumSubArraySum( self.array, len(self.array) ), 7) 
        
if __name__ == '__main__':
    unittest.main()