"""
pandas-express: A verbose, talkative pandas DataFrame extension

This module provides ExpressDataFrame, a class that inherits from pandas DataFrame
and adds enhanced error handling and verbose feedback.
"""

import pandas as pd
from .express_dataframe import ExpressDataFrame

__version__ = "0.1.0"
__author__ = "NDNnerd"
__email__ = ""

# Make ExpressDataFrame available at package level
__all__ = ["ExpressDataFrame"]