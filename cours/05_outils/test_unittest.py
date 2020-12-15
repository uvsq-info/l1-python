import unittest

def is_even(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
    return nbr % 2 == 0


def is_prime(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
    for i in range(2,nbr):
        if nbr % i == 0:
            return False
    return True

class MyTest(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(1))
        
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(15))    

if __name__ == '__main__':
    unittest.main()
