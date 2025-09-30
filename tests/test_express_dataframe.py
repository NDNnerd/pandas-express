"""
Tests for the pandasExpress module and ExpressDataFrame class.
"""

import json
import os
import sys
import unittest
from io import StringIO

# Add the package to the path for testing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pandasExpress import ExpressDataFrame
import pandas as pd


class TestExpressDataFrame(unittest.TestCase):
    """Test cases for ExpressDataFrame class."""
    
    def setUp(self):
        """Set up test data."""
        self.sample_data = {
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [25, 30, 35],
            'city': ['New York', 'San Francisco', 'Chicago']
        }
        
        # Capture stdout for testing verbose output
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.held
    
    def test_create_express_dataframe(self):
        """Test creating an ExpressDataFrame."""
        df = ExpressDataFrame(self.sample_data)
        
        # Check that it's an instance of both ExpressDataFrame and DataFrame
        self.assertIsInstance(df, ExpressDataFrame)
        self.assertIsInstance(df, pd.DataFrame)
        
        # Check shape
        self.assertEqual(df.shape, (3, 3))
        
        # Check columns
        expected_columns = ['name', 'age', 'city']
        self.assertListEqual(list(df.columns), expected_columns)
    
    def test_inheritance_from_pandas(self):
        """Test that ExpressDataFrame properly inherits from pandas DataFrame."""
        df = ExpressDataFrame(self.sample_data)
        
        # Test that pandas methods work
        self.assertEqual(len(df), 3)
        self.assertTrue(hasattr(df, 'head'))
        self.assertTrue(hasattr(df, 'tail'))
        self.assertTrue(hasattr(df, 'info'))
        self.assertTrue(hasattr(df, 'describe'))
    
    def test_head_method(self):
        """Test the enhanced head method."""
        df = ExpressDataFrame(self.sample_data)
        result = df.head(2)
        
        # Should return ExpressDataFrame
        self.assertIsInstance(result, ExpressDataFrame)
        self.assertEqual(len(result), 2)
    
    def test_tail_method(self):
        """Test the enhanced tail method."""
        df = ExpressDataFrame(self.sample_data)
        result = df.tail(1)
        
        # Should return ExpressDataFrame
        self.assertIsInstance(result, ExpressDataFrame)
        self.assertEqual(len(result), 1)
    
    def test_column_access(self):
        """Test column access with verbose feedback."""
        df = ExpressDataFrame(self.sample_data)
        
        # Access single column
        name_column = df['name']
        self.assertEqual(len(name_column), 3)
        
        # Access multiple columns
        subset = df[['name', 'age']]
        self.assertIsInstance(subset, ExpressDataFrame)
        self.assertEqual(subset.shape, (3, 2))
    
    def test_constructor_property(self):
        """Test that operations return ExpressDataFrame objects."""
        df = ExpressDataFrame(self.sample_data)
        
        # Test that slicing returns ExpressDataFrame
        subset = df.iloc[0:2]
        self.assertIsInstance(subset, ExpressDataFrame)
    
    def test_empty_dataframe(self):
        """Test creating an empty ExpressDataFrame."""
        df = ExpressDataFrame()
        self.assertIsInstance(df, ExpressDataFrame)
        self.assertEqual(df.shape, (0, 0))


class TestWithSampleData(unittest.TestCase):
    """Test ExpressDataFrame with the included sample data."""
    
    def setUp(self):
        """Set up with sample data file."""
        # Capture stdout for testing verbose output
        self.held, sys.stdout = sys.stdout, StringIO()
        
        # Load sample data
        data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.json')
        if os.path.exists(data_path):
            with open(data_path, 'r') as f:
                self.sample_data = json.load(f)
        else:
            self.sample_data = {
                'name': ['Test User'],
                'age': [25],
                'city': ['Test City'],
                'salary': [50000],
                'department': ['Test Dept']
            }
    
    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.held
    
    def test_with_sample_data(self):
        """Test ExpressDataFrame with the sample data."""
        df = ExpressDataFrame(self.sample_data)
        
        self.assertIsInstance(df, ExpressDataFrame)
        self.assertGreater(len(df), 0)
        
        # Test that all expected columns are present
        expected_columns = ['name', 'age', 'city', 'salary', 'department']
        for col in expected_columns:
            if col in self.sample_data:
                self.assertIn(col, df.columns)


if __name__ == '__main__':
    unittest.main()