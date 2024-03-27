import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def data_discription(data):
    """
    Calculate various statistics and descriptions for a given dataset.

    Parameters:
    - data (pd.DataFrame): Input dataset.

    Returns:
    - Stylishly formatted DataFrame with statistics and descriptions.
    """
    n = data.shape[0]
    add_desc_df = pd.DataFrame()
    add_desc_df['range'] = data.max() - data.min()
    add_desc_df['skew'] = data.skew()
    add_desc_df['kurt'] = data.kurt()
    add_desc_df['NaN'] = data.isnull().sum()
    add_desc_df['NaN (in %)'] = (add_desc_df['NaN']/n)*100
    add_desc_df['Duplicate'] = data.duplicated(keep=False).sum()
    add_desc_df['Duplicate (in %)'] = (add_desc_df['Duplicate']/n)*100
    
    desc_df = data.describe().T.drop(['count'], axis = 1)
    info_df = pd.concat([desc_df, add_desc_df], axis = 1).style.background_gradient(cmap = 'Reds', axis = 1).format(formatter = '{:,.2f}')
    
    return info_df
    
# Code Credit - RAVI RAMAKRISHNAN (https://www.kaggle.com/ravi20076)
def MakeContColPlots(train_df, test_df, cont_cols):
    """
    Generate distribution plots for continuous columns in both training and testing datasets.

    Parameters:
    - train_df (pd.DataFrame): Training dataset.
    - test_df (pd.DataFrame): Testing dataset.
    - cont_cols (list): List of continuous column names.
    - plot_colors (list): List of colors for plotting.

    Returns:
    - Displayed distribution plots.
    """
    grid_specs = {'visible': True, 'which': 'both', 'linestyle': '--', 
                  'color': 'lightgrey', 'linewidth': 0.75};
    title_specs = {'fontsize': 9, 'fontweight': 'bold', 'color': '#992600'};
    
    df = pd.concat([train_df[cont_cols].assign(Source = 'Train'), 
                    test_df[cont_cols].assign(Source = 'Test'),
                   ],
                   axis=0, ignore_index = True
                  )
    
    fig, axes = plt.subplots(len(cont_cols), 3 ,figsize = (16, len(cont_cols) * 4.2), 
                             gridspec_kw = {'hspace': 0.35, 
                                            'wspace': 0.3, 
                                            'width_ratios': [0.80, 0.20, 0.20]
                                           }
                            );

    for i,col in enumerate(cont_cols):
        ax = axes[i,0];
        sns.kdeplot(data = df[[col, 'Source']], x = col, hue = 'Source', 
                    palette = ['#0039e6', '#ff5500', '#00b300'], 
                    ax = ax, linewidth = 2.1
                   );
        ax.set_title(f"\n{col}", **title_specs);
        ax.grid(**grid_specs);
        ax.set(xlabel = '', ylabel = '');

        ax = axes[i,1];
        sns.boxplot(data = df.loc[df.Source == 'Train', [col]], y = col, width = 0.25,
                    color = '#0039e6', saturation = 0.90, linewidth = 0.90, 
                    fliersize= 2.25,
                    ax = ax)
        ax.set(xlabel = '', ylabel = '')
        ax.set_title(f"Train", **title_specs)

        ax = axes[i,2]
        sns.boxplot(data = df.loc[df.Source == 'Test', [col]], y = col, width = 0.25, fliersize= 2.25,
                    color = '#ff5500', saturation = 0.6, linewidth = 0.90, 
                    ax = ax)
        ax.set(xlabel = '', ylabel = '')
        ax.set_title(f"Test", **title_specs)

    plt.suptitle(f"\nDistribution Analysis - Continuous Columns\n", fontsize = 20, fontweight = 'bold', y = 0.89, x = 0.50)
    plt.tight_layout()
    plt.show()
