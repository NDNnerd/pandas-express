"""
ExpressDataFrame - A verbose, talkative pandas DataFrame extension

This module contains the ExpressDataFrame class that inherits from pandas DataFrame
and provides enhanced error handling and verbose feedback.
"""

import pandas as pd
import warnings
from typing import Any, Optional, Union, Dict


class ExpressDataFrame(pd.DataFrame):
    """
    A verbose, talkative extension of pandas DataFrame.
    
    ExpressDataFrame catches errors with verbose, helpful messages and provides
    enhanced feedback for common operations.
    
    This class inherits all functionality from pandas DataFrame while adding
    improved error handling and user feedback.
    """
    
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy=None):
        """
        Initialize ExpressDataFrame.
        
        Parameters are the same as pandas DataFrame constructor.
        """
        try:
            super().__init__(data=data, index=index, columns=columns, dtype=dtype, copy=copy)
            print(f"✅ ExpressDataFrame created successfully with shape {self.shape}")
            if len(self.columns) > 0:
                print(f"📊 Columns: {list(self.columns)}")
        except Exception as e:
            print(f"❌ Error creating ExpressDataFrame: {str(e)}")
            print("💡 Tip: Check your data format and ensure it's compatible with pandas DataFrame")
            raise
    
    def head(self, n: int = 5) -> 'ExpressDataFrame':
        """
        Return the first n rows with verbose feedback.
        """
        print(f"👀 Showing first {n} rows of {len(self)} total rows")
        result = super().head(n)
        return ExpressDataFrame(result)
    
    def tail(self, n: int = 5) -> 'ExpressDataFrame':
        """
        Return the last n rows with verbose feedback.
        """
        print(f"👀 Showing last {n} rows of {len(self)} total rows")
        result = super().tail(n)
        return ExpressDataFrame(result)
    
    def info(self, verbose: Optional[bool] = None, buf=None, max_cols: Optional[int] = None,
             memory_usage: Optional[Union[bool, str]] = None, show_counts: Optional[bool] = None) -> None:
        """
        Print a concise summary with enhanced verbose output.
        """
        print("📋 ExpressDataFrame Info:")
        print("=" * 50)
        super().info(verbose=verbose, buf=buf, max_cols=max_cols, 
                    memory_usage=memory_usage, show_counts=show_counts)
        print("=" * 50)
        print(f"💭 This DataFrame has {len(self)} rows and {len(self.columns)} columns")
        
        # Check for missing values
        missing_count = self.isnull().sum().sum()
        if missing_count > 0:
            print(f"⚠️  Warning: Found {missing_count} missing values")
        else:
            print("✅ No missing values detected")
    
    def describe(self, percentiles=None, include=None, exclude=None) -> 'ExpressDataFrame':
        """
        Generate descriptive statistics with verbose feedback.
        """
        print("📊 Generating descriptive statistics...")
        result = super().describe(percentiles=percentiles, include=include, exclude=exclude)
        print(f"📈 Statistics computed for {len(result.columns)} columns")
        return ExpressDataFrame(result)
    
    def dropna(self, **kwargs) -> 'ExpressDataFrame':
        """
        Remove missing values with verbose feedback.
        """
        original_length = len(self)
        missing_before = self.isnull().sum().sum()
        
        result = super().dropna(**kwargs)
        rows_dropped = original_length - len(result)
        
        print(f"🧹 Dropped {rows_dropped} rows containing missing values")
        print(f"📊 DataFrame size: {original_length} → {len(result)} rows")
        
        return ExpressDataFrame(result)
    
    def fillna(self, value=None, **kwargs) -> 'ExpressDataFrame':
        """
        Fill missing values with verbose feedback.
        """
        missing_before = self.isnull().sum().sum()
        result = super().fillna(value=value, **kwargs)
        missing_after = result.isnull().sum().sum()
        
        print(f"🔧 Filled {missing_before - missing_after} missing values")
        if missing_after > 0:
            print(f"⚠️  {missing_after} missing values remain")
        
        return ExpressDataFrame(result)
    
    def __getitem__(self, key):
        """
        Override item access to provide verbose feedback for column selection.
        """
        if isinstance(key, str) and key in self.columns:
            print(f"📍 Accessing column: '{key}'")
        elif isinstance(key, list):
            valid_cols = [col for col in key if col in self.columns]
            invalid_cols = [col for col in key if col not in self.columns]
            if invalid_cols:
                print(f"⚠️  Warning: Columns not found: {invalid_cols}")
            if valid_cols:
                print(f"📍 Accessing columns: {valid_cols}")
        
        result = super().__getitem__(key)
        
        # Return ExpressDataFrame if result is a DataFrame
        if isinstance(result, pd.DataFrame):
            return ExpressDataFrame(result)
        else:
            return result
    
    @property
    def _constructor(self):
        """
        Ensure that pandas operations return ExpressDataFrame objects.
        """
        return ExpressDataFrame
    
    def __str__(self) -> str:
        """
        String representation with helpful info.
        """
        base_str = super().__str__()
        return f"ExpressDataFrame[{self.shape[0]}x{self.shape[1]}]\n{base_str}"
    
    def __repr__(self) -> str:
        """
        Official string representation.
        """
        return f"ExpressDataFrame({super().__repr__()})"