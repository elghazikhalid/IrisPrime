# test_irisprime.py
"""
Tests for IrisPrime module.
"""

import unittest
from irisprime import IrisPrime

class TestIrisPrime(unittest.TestCase):
    """Test cases for IrisPrime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IrisPrime()
        self.assertIsInstance(instance, IrisPrime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IrisPrime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
