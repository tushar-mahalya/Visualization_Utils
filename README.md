# Helper Functions for Data Analysis

This Python module, `helper_functions.py`, provides a set of utility functions designed to assist in data analysis tasks. It includes functions for generating descriptive statistics and creating distribution plots for continuous variables. 
Please be advised that the functions presented herein are tailored to suit my personal preferences and are not intended for widespread adoption. However, should any individuals find utility in their application, they are welcome to utilize them accordingly.

## Installation

To use these functions, you need to have Python installed along with the following libraries:

- pandas
- numpy
- matplotlib
- seaborn

You can install these libraries along with complete package using pip:

```bash
pip install git+https://github.com/tushar-mahalya/Visualization_Utils.git
```
## Functions
### `data_discription`
The data_discription function provides a comprehensive statistical summary of a given dataset. It calculates the range, skewness, kurtosis, and the number of NaN values and duplicates in each column.

Usage:
```python
from Visualization_Utils.helper_functions import data_discription

# Load your data
data = pd.read_csv('your_data.csv')

# Get the data description
data_discription(data)
```
### `MakeContColPlots`
The MakeContColPlots function generates distribution plots for continuous columns in both training and testing datasets. This is particularly useful for visualizing and comparing the distribution of variables in your training and testing sets.

Usage:
```python
from Visualization_Utils.helper_functions import MakeContColPlots

# Load your data
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

# Specify the continuous columns
cont_cols = ['col1', 'col2', 'col3']

# Generate the plots
MakeContColPlots(train_data, test_data, cont_cols)
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the terms of the MIT license.
