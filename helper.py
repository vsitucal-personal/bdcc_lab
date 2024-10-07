import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def thousands_formatter(x, pos):
    """Convert large numbers to thousands with 'K' suffix."""
    return f'{x * 1e-3:,.0f}K'


def plot_multiple_line_graphs2(
    x_list, y_list, x_labels=None, y_labels=None, titles=None,
    use_k=None, use_legend=None, show_grid=False, max_cols=3,
):
    """
    Plots multiple line graphs in subplots and formats the y-axis in thousands.
    Dynamically sets the layout to a maximum of 3 columns.

    Parameters:
    x_list (list of pd.Series or array-like): List of data for the X-axes
    y_list (list of pd.Series or array-like): List of data for the Y-axes
    x_labels (list of str): List of labels for the X-axes
    y_labels (list of str): List of labels for the Y-axes
    titles (list of str): List of titles for each subplot
    use_k (bool): Whether to format the y-axis in thousands
    show_grid (bool): Whether to show grid on each plot
    """
    n_plots = len(x_list)
    n_cols = min(n_plots, max_cols)
    n_rows = math.ceil(n_plots / max_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(8 * n_cols, 6 * n_rows))

    # Ensure axes is iterable, even for single plots
    if n_rows == 1 and n_cols == 1:
        axes = [[axes]]
    elif n_rows == 1:
        axes = [axes]
    elif n_cols == 1:
        axes = [[ax] for ax in axes]

    # Flatten axes for easy indexing
    axes = [ax for sublist in axes for ax in sublist]

    for i, (use_legend_, use_k_, x, y) in enumerate(zip(use_legend, use_k, x_list, y_list)):
        ax = axes[i]

        if y == []:
            ax.axis('off')
            continue
        
        # Check if x and y are lists or array-like
        if isinstance(x, (list, pd.Series)) and isinstance(y, (list, pd.Series)):
            for x_, y_ in zip(x, y):
                ax.plot(x_, y_[0], marker='o', linestyle='-', color=y_[2], label=y_[1])
                if use_legend_:
                    ax.legend()
        else:
            ax.plot(x, y[0], marker='o', linestyle='-', color=y[2], label=y[1])
            if use_legend_:
                    ax.legend()

        # Labels and title
        ax.set_xlabel(x_labels[i] if x_labels else 'X-axis')
        ax.set_ylabel(y_labels[i] if y_labels else 'Y-axis')
        ax.set_title(titles[i] if titles else f'Graph {i+1}')

        # Format the y-axis to show values in thousands
        if use_k_:
            ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        # Show grid
        ax.grid(show_grid)

    # Hide any unused axes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_multiple_line_graphs(
    x_list, y_list, x_labels=None, y_labels=None, titles=None,
    use_k=None, show_grid=False
):
    """
    Plots multiple line graphs in subplots and formats the y-axis in thousands.
    Dynamically sets the layout to a maximum of 3 columns.

    Parameters:
    x_list (list of pd.Series or array-like): List of data for the X-axes
    y_list (list of pd.Series or array-like): List of data for the Y-axes
    x_labels (list of str): List of labels for the X-axes
    y_labels (list of str): List of labels for the Y-axes
    titles (list of str): List of titles for each subplot
    use_k (bool): Whether to format the y-axis in thousands
    show_grid (bool): Whether to show grid on each plot
    """
    n_plots = len(x_list)
    max_cols = 3
    n_cols = min(n_plots, max_cols)
    n_rows = math.ceil(n_plots / max_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(8 * n_cols, 6 * n_rows))

    # Ensure axes is iterable, even for single plots
    if n_rows == 1 and n_cols == 1:
        axes = [[axes]]
    elif n_rows == 1:
        axes = [axes]
    elif n_cols == 1:
        axes = [[ax] for ax in axes]

    # Flatten axes for easy indexing
    axes = [ax for sublist in axes for ax in sublist]

    for i, (use_k_, x, y) in enumerate(zip(use_k, x_list, y_list)):
        ax = axes[i]
        ax.plot(x, y, marker='o', linestyle='-', color='b')

        # Labels and title
        ax.set_xlabel(x_labels[i] if x_labels else 'X-axis')
        ax.set_ylabel(y_labels[i] if y_labels else 'Y-axis')
        ax.set_title(titles[i] if titles else f'Graph {i+1}')

        # Format the y-axis to show values in thousands
        if use_k_:
            ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        # Show grid
        ax.grid(show_grid)

    # Hide any unused axes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout
    plt.tight_layout()
    plt.show()

def cache_spark_df(df):
    df.cache()
    df.count()


def read_sql_file(path):
    with open(path, "r") as file:
        return_string = file.read()
    return return_string
