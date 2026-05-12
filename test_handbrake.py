# test_handbrake.py
"""
Tests for HandBrake module.
"""

import unittest
from handbrake import HandBrake

class TestHandBrake(unittest.TestCase):
    """Test cases for HandBrake class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HandBrake()
        self.assertIsInstance(instance, HandBrake)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HandBrake()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
