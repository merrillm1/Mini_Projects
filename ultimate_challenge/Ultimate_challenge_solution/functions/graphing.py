import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_pct_class_by_category(df, category, class_col):
    '''This function will output the percentage of classified values for the 
        categories in a given categorical variable'''
    
    retained = df.groupby([category, class_col]).agg({class_col: 'count'})
    retained_pct = retained.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
    
    return retained_pct
    

def get_bar_labels(df, category, class_col):
    
    '''This function will output the percentage of classified values as a label for graphing'''
    
    pct_classified = get_pct_class_by_category(df, category, class_col)
    
    percentages = []
    for i in range(0, len(pct_classified[class_col])):
        if i % 2 != 0:
            percentages.append(pct_classified[class_col].iloc[i])
                
    bar_labels = []
    for i in range(len(percentages)):
        bar_labels.append("{}% retained".format(round(percentages[i], 1)))
    
    return bar_labels



def overlayed_labeled_bar_graph(df, category, class_col):
    '''This function will plot a bar graph with percent labels above each bar indicating the percentage of
        values in the labeled class'''
    
    bar_labels = get_bar_labels(df, category, class_col)
    
    y1 = df.groupby(category)[class_col].count()
    y2 = df.groupby(category)[class_col].sum()
    x = sorted(list(df[category].unique()))
    
    style = dict(size=15, color='grey')
    ax = plt.figure(figsize=(15, 6)).add_subplot(111)
    
    plt.bar(x, y1)
    plt.bar(x, y2)
    
    plt.title("{} retention rates by category".format(category), size=16)
    
    # specific for this project
    plt.legend(['Not retained', 'Retained'])
    
    for i, title, label in zip(range(len(x)), x, bar_labels):
        ax.text(title, y1[i], label, ha="center", **style)


def timeseries_frequency_plot(title, df, timeseries_col, y_col, dStart, dEnd, sample_by='D', xtick_freq ='W', axvline=[np.nan]):
    
    '''This function will aggregate a dataframe by count given two columns, the datetime column and any column used to 
    determine frequency'''
    
    timeseries_vs_y = df[[timeseries_col, y_col]]
    plot_df = timeseries_vs_y.set_index(timeseries_col).resample(sample_by)[y_col].count()
    df = plot_df[(dStart <= plot_df.index) & (plot_df.index <= dEnd)]

    ax = plt.figure(figsize=(20, 6)).add_subplot(111)   
    xticks = pd.date_range(start=dStart, end=dEnd, freq=xtick_freq)

    df.plot(ax = ax, xticks=xticks)
    
    ax.set_title(title, fontsize=16)
    ax.set_xticklabels([x.strftime('%h%d\n%a\n%-I%p\n%Y') for x in xticks])
    
    for axv in axvline:
        ax.axvline(axv, color='r', linestyle='--', lw=2)
    
    ax.tick_params(axis='x', which='major', pad=15)
    plt.setp(ax.xaxis.get_majorticklabels(), ha='right')
    
    plt.show()
    

def plot_coefficients(classifier, feature_names, top_features=5):
    '''This function will plot the significant coefficients of themachine learning features'''
    coef = classifier.coef_.ravel()
    top_coefficients = np.argsort(coef)
    # create plot
    plt.figure(figsize=(10, 5))
    colors = ['red' if c < 0 else 'blue' for c in coef[top_coefficients]]
    plt.bar(np.arange(top_features), coef[top_coefficients], color=colors)
    feature_names = np.array(feature_names)
    plt.xticks(np.arange(0, top_features), feature_names[top_coefficients], rotation=60, ha='right')
    plt.title('Feature Importance', size = 15)
    plt.show()
    
    

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1) / n
    return x, y
    

def hist_ecdf_pair_plot(df, col, class_col, title, bin_size = 20):
    
    retained = df[col].loc[df[class_col] == 1]
    not_retained = df[col].loc[df[class_col] == 0]
    
    x_active, y_active = ecdf(retained)
    x_inactive, y_inactive = ecdf(not_retained)
    
    plt.figure(figsize=(12, 4))
    plt.title(title, size=15)
    plt.hist(df[df[class_col] == 0][col], bins=bin_size)
    plt.hist(df[df[class_col] == 1][col], bins=bin_size)
    plt.ylabel('Frequency')
    plt.legend(['not retained', 'retained'])
    
    plt.figure(figsize=(12, 4))
    plt.plot(x_inactive, y_inactive, marker='.', linestyle='none')
    plt.plot(x_active, y_active, marker='.', linestyle='none')
    plt.xlabel(col)
    plt.ylabel('ECDF')
    plt.legend(['not retained', 'retained'])
    
    plt.show()