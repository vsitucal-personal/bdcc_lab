import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def thousands_formatter(x, pos):
    """Convert large numbers to thousands with 'K' suffix."""
    return f'{x * 1e-3:,.0f}K'


def millions_formatter(x, pos):
    """Convert large numbers to millions with 'M' suffix."""
    return f'{x * 1e-6:,.0f}M'


def billions_formatter(x, pos):
    """Convert large numbers to billions with 'B' suffix."""
    return f'{x * 1e-9:,.0f}B'


def trillions_formatter(x, pos):
    """Convert large numbers to trillions with 'T' suffix."""
    return f'{x * 1e-12:,.0f}T'


def plot_multiple_line_graphs2(
    x_list, y_list, x_labels=None, y_labels=None, titles=None,
    formatter=None, use_legend=None, show_grid=False, max_cols=3,
    start_figure_number=1, marker="o",  # New parameter for starting figure number
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
    formatter (list of callable): List of formatting functions for the y-axes
    use_legend (list of bool): Whether to show legend for each plot
    show_grid (bool): Whether to show grid on each plot
    start_figure_number (int): Starting number for figure annotations
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

    for i, (use_legend_, formatter_, x, y) in enumerate(zip(use_legend, formatter, x_list, y_list)):
        ax = axes[i]

        if y == []:
            ax.axis('off')
            continue
        
        # Check if x and y are lists or array-like
        if isinstance(x, (list, pd.Series)) and isinstance(y, (list, pd.Series)):
            for x_, y_ in zip(x, y):
                ax.plot(x_, y_[0], marker=marker, linestyle='-', color=y_[2], label=y_[1])
                if use_legend_:
                    ax.legend()
        else:
            ax.plot(x, y[0], marker=marker, linestyle='-', color=y[2], label=y[1])
            if use_legend_:
                ax.legend()

        # Labels and title
        ax.set_xlabel(x_labels[i] if x_labels else 'X-axis')
        ax.set_ylabel(y_labels[i] if y_labels else 'Y-axis')
        ax.set_title(titles[i] if titles else f'Graph {i + 1}')

        # Format the y-axis to show values in thousands
        if formatter_:
            ax.yaxis.set_major_formatter(FuncFormatter(formatter_))

        # Show grid
        ax.grid(show_grid)

    # Annotate figure number at the top of the figure
    fig.text(0.5, -0.015, f'Figure {start_figure_number}', ha='center', fontsize=13)

    # Hide any unused axes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def read_sql_file(path):
    with open(path, "r") as file:
        return_string = file.read()
    return return_string
