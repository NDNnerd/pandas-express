# pandas-express

Catch errors with a verbose, talkative python pandas.

A Python module that creates `ExpressDataFrame`, a class that inherits from pandas DataFrame and provides enhanced error handling with verbose, helpful feedback.

## Installation

```bash
pip install pandas-express
```

## Features

- **Verbose Feedback**: Get helpful messages for every operation
- **Enhanced Error Handling**: Better error messages with tips for common issues
- **Full pandas Compatibility**: Inherits all pandas DataFrame functionality
- **Easy to Use**: Drop-in replacement for pandas DataFrame

## Usage

```python
import pandasExpress as px
from pandasExpress import ExpressDataFrame

# Create an ExpressDataFrame from various data sources
df = ExpressDataFrame(data)

# Or load from the included sample data
import json
with open('data.json', 'r') as f:
    sample_data = json.load(f)

df = ExpressDataFrame(sample_data)
```

## Example

```python
import pandasExpress as px
from pandasExpress import ExpressDataFrame
import json

# Load sample data
with open('data.json', 'r') as f:
    data = json.load(f)

# Create ExpressDataFrame
df = ExpressDataFrame(data)
# ✅ ExpressDataFrame created successfully with shape (5, 5)
# 📊 Columns: ['name', 'age', 'city', 'salary', 'department']

# Get basic info with verbose output
df.info()
# 📋 ExpressDataFrame Info:
# ==================================================
# <class 'pandasExpress.express_dataframe.ExpressDataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 5 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   name        5 non-null      object
#  1   age         5 non-null      int64 
#  2   city        5 non-null      object
#  3   salary      5 non-null      int64 
#  4   department  5 non-null      object
# dtypes: int64(2), object(3)
# memory usage: 328.0+ bytes
# ==================================================
# 💭 This DataFrame has 5 rows and 5 columns
# ✅ No missing values detected

# Access columns with feedback
engineering_staff = df[df['department'] == 'Engineering']
# 📍 Accessing column: 'department'

# View data with helpful messages
df.head(3)
# 👀 Showing first 3 rows of 5 total rows
```

## API Reference

### ExpressDataFrame

A verbose extension of pandas DataFrame that provides enhanced feedback and error handling.

#### Methods

All pandas DataFrame methods are available, plus enhanced versions of:

- `head(n=5)`: Show first n rows with verbose feedback
- `tail(n=5)`: Show last n rows with verbose feedback  
- `info()`: Enhanced info display with helpful summaries
- `describe()`: Generate statistics with progress feedback
- `dropna()`: Remove missing values with detailed reporting
- `fillna()`: Fill missing values with progress tracking

#### Properties

- Maintains all pandas DataFrame properties
- Enhanced string representation with shape information

## Requirements

- Python 3.8+
- pandas >= 1.3.0

## Development

```bash
# Clone the repository
git clone https://github.com/NDNnerd/pandas-express.git
cd pandas-express

# Install in development mode
pip install -e .[dev]

# Run tests
pytest

# Format code
black pandasExpress/
isort pandasExpress/
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
