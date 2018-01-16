import os
import numpy as np
print('numpy: %s' % np.__version__)
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
import matplotlib.pyplot as plt
import pandas as pd
print('pandas: %s' % pd.__version__)
import datetime as dt
import pickle
from matplotlib.ticker import FuncFormatter

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    dt_pd_baseline_a = pd.read_pickle('dt_pd_aggregated_baseline_a.pickle')

    # subsetting date range for plot
    # start_date = '1/1/2016'
    # end_date = '1/1/2018'
    # mask = (dt_pd_vol.index > start_date) & (dt_pd_vol.index <= end_date)
    # dt_pd_aggr = dt_pd_vol[mask]

    matplotlib.rcParams.update({'font.size': 16})

    dt_pd_baseline_a.index.name = ''

    dt_pd_baseline_a['price'] = 100 * dt_pd_baseline_a['price'] / \
                                dt_pd_baseline_a.iloc[0]['price']

    dt_pd_baseline_a['google'] = 100 * dt_pd_baseline_a['google'] / \
                                 dt_pd_baseline_a.iloc[0]['google']

    dt_pd_baseline_a['tweets'] = 100 * dt_pd_baseline_a['tweets'] / \
                                 dt_pd_baseline_a.iloc[0]['tweets']

    dt_pd_baseline_a['new_users'] = 100 * dt_pd_baseline_a['new_users'] / \
                                 dt_pd_baseline_a.iloc[0]['new_users']

    dt_pd_baseline_a['wikipedia'] = 100 * dt_pd_baseline_a['wikipedia'] / \
                                dt_pd_baseline_a.iloc[0]['wikipedia']

    dt_pd_baseline_a['new_topics'] = 100 * dt_pd_baseline_a['new_topics'] / \
                                dt_pd_baseline_a.iloc[0]['new_topics']

    dt_pd_baseline_a['new_posts'] = 100 * dt_pd_baseline_a['new_posts'] / \
                                     dt_pd_baseline_a.iloc[0]['new_posts']

    dt_pd_baseline_a['new_topics'] = 100 * dt_pd_baseline_a['new_topics'] / \
                                    dt_pd_baseline_a.iloc[0]['new_topics']

    dt_pd_baseline_a['new_members'] = 100 * dt_pd_baseline_a['new_members'] / \
                                     dt_pd_baseline_a.iloc[0]['new_members']

    f, (ax1) = plt.subplots(1, 1, sharex=True, sharey=True)
    ax1.plot(dt_pd_baseline_a[['price']], color='blue', label='Price', alpha = 0.9)
    ax1.plot(dt_pd_baseline_a[['google']], color='red', label='Google', alpha = 0.9)
    ax1.plot(dt_pd_baseline_a[['tweets']], color='green', label='Tweets', alpha = 0.9)
    ax1.plot(dt_pd_baseline_a[['new_users']], color='orange', label='New Users', alpha = 0.9)
    # ax1.plot(dt_pd_baseline_a[['wikipedia']], color='magenta', label='Wikipedia', alpha=0.9)
    # ax1.plot(dt_pd_baseline_a[['new_posts']], color='black', label='New Posts', alpha=0.9)
    ax1.legend(loc='upper left')

    # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

    # set size of overall figure not needed here
    plt.gcf().set_size_inches(15, 8)
    # auto-format of x-axis labels & rotation
    f.autofmt_xdate()

    os.chdir('..')
    os.chdir(os.path.abspath(os.curdir) + sl + "F_Figs" + sl)
    f.tight_layout(pad=0.01)
    plt.savefig('pt_baseline_a.pdf')

    # plt.show()

    print(os.path.basename(__file__), 'executed')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")