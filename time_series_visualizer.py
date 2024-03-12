import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
mask_low_page_views = df['value'] >= df['value'].quantile(0.025)
mask_high_page_views = df['value'] <= df['value'].quantile(0.975)
df = df.loc[mask_low_page_views & mask_high_page_views]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year.rename('year'), df.index.month.rename('month')]).mean()
    df_bar = df_bar.unstack()
    # print(df_bar.head().to_string())

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 7))

    df_bar.plot(ax=ax, kind='bar', xlabel='Years', ylabel='Average Page Views')
    ax.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14.4, 5.4))

    sns.boxplot(ax=ax_left, data=df_box, x='year', y='value')
    ax_left.set_title('Year-wise Box Plot (Trend)')
    ax_left.set_xlabel('Year')
    ax_left.set_ylabel('Page Views')

    sns.boxplot(ax=ax_right, data=df_box, x='month', y='value', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax_right.set_title('Month-wise Box Plot (Seasonality)')
    ax_right.set_xlabel('Month')
    ax_right.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
