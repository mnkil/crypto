# https://pypi.python.org/pypi/mwviews
# https://github.com/Commonists/pageview-api
# https://wikimedia.org/api/rest_v1/#!/Pageviews_data/get_metrics_pageviews_per_article_project_access_agent_article_granularity_start_end
# actual (not legacy) https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/bitcoin/daily/2010071800/20181124

# https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/bitcoin/daily/2010071800/20181124
# https://wikitech.wikimedia.org/wiki/Analytics/Pageviews
# https://wikitech.wikimedia.org/wiki/Analytics/Systems/Dashiki
# https://github.com/abelsson/stats.grok.se/blob/master/backend/getstats.py
# https://dumps.wikimedia.org/other/pagecounts-raw/
# https://dumps.wikimedia.org/other/pagecounts-ez/

import gzip
import os
# from tkinter import Tk
import scipy
import datetime as dt
print('scipy: %s' % scipy.__version__)
import numpy as np
print('numpy: %s' % np.__version__)
import pandas as pd
import hashlib
print('pandas: %s' % pd.__version__)

print(os.getcwd())

def main():
    print("First Module's Name: {}".format(__name__))

    if os.name == 'posix':
        sl = '/'
    elif os.name == 'nt':
        sl = '\\'

    # All Files to be read in current cycle of scraping
    files = [
        'pagecounts-20120801-000001.gz',
        'pagecounts-20120801-010000.gz',
        'pagecounts-20120801-020000.gz',
        'pagecounts-20120801-030000.gz',
        'pagecounts-20120801-040000.gz',
        'pagecounts-20120801-050000.gz',
        'pagecounts-20120801-060000.gz',
        'pagecounts-20120801-070000.gz',
        'pagecounts-20120801-080000.gz',
        'pagecounts-20120801-090000.gz',
        'pagecounts-20120801-100000.gz',
        'pagecounts-20120801-110000.gz',
        'pagecounts-20120801-120000.gz',
        'pagecounts-20120801-130000.gz',
        'pagecounts-20120801-140001.gz',
        'pagecounts-20120801-150000.gz',
        'pagecounts-20120801-160000.gz',
        'pagecounts-20120801-170000.gz',
        'pagecounts-20120801-180000.gz',
        'pagecounts-20120801-190000.gz',
        'pagecounts-20120801-200000.gz',
        'pagecounts-20120801-210000.gz',
        'pagecounts-20120801-220000.gz',
        'pagecounts-20120801-230000.gz',
        'pagecounts-20120802-000000.gz',
        'pagecounts-20120802-010000.gz',
        'pagecounts-20120802-020000.gz',
        'pagecounts-20120802-030001.gz',
        'pagecounts-20120802-040000.gz',
        'pagecounts-20120802-050000.gz',
        'pagecounts-20120802-060000.gz',
        'pagecounts-20120802-070000.gz',
        'pagecounts-20120802-080000.gz',
        'pagecounts-20120802-090000.gz',
        'pagecounts-20120802-100000.gz',
        'pagecounts-20120802-110000.gz',
        'pagecounts-20120802-120000.gz',
        'pagecounts-20120802-130000.gz',
        'pagecounts-20120802-140000.gz',
        'pagecounts-20120802-150000.gz',
        'pagecounts-20120802-160000.gz',
        'pagecounts-20120802-170001.gz',
        'pagecounts-20120802-180000.gz',
        'pagecounts-20120802-190000.gz',
        'pagecounts-20120802-200000.gz',
        'pagecounts-20120802-210000.gz',
        'pagecounts-20120802-220000.gz',
        'pagecounts-20120802-230000.gz',
        'pagecounts-20120803-000000.gz',
        'pagecounts-20120803-010000.gz',
        'pagecounts-20120803-020000.gz',
        'pagecounts-20120803-030000.gz',
        'pagecounts-20120803-040000.gz',
        'pagecounts-20120803-050000.gz',
        'pagecounts-20120803-060001.gz',
        'pagecounts-20120803-070000.gz',
        'pagecounts-20120803-080000.gz',
        'pagecounts-20120803-090000.gz',
        'pagecounts-20120803-100000.gz',
        'pagecounts-20120803-110000.gz',
        'pagecounts-20120803-120000.gz',
        'pagecounts-20120803-130000.gz',
        'pagecounts-20120803-140000.gz',
        'pagecounts-20120803-150000.gz',
        'pagecounts-20120803-160000.gz',
        'pagecounts-20120803-170000.gz',
        'pagecounts-20120803-180000.gz',
        'pagecounts-20120803-190001.gz',
        'pagecounts-20120803-200000.gz',
        'pagecounts-20120803-210000.gz',
        'pagecounts-20120803-220000.gz',
        'pagecounts-20120803-230000.gz',
        'pagecounts-20120804-000000.gz',
        'pagecounts-20120804-010000.gz',
        'pagecounts-20120804-020000.gz',
        'pagecounts-20120804-030000.gz',
        'pagecounts-20120804-040000.gz',
        'pagecounts-20120804-050000.gz',
        'pagecounts-20120804-060000.gz',
        'pagecounts-20120804-070000.gz',
        'pagecounts-20120804-080000.gz',
        'pagecounts-20120804-090001.gz',
        'pagecounts-20120804-100000.gz',
        'pagecounts-20120804-110000.gz',
        'pagecounts-20120804-120000.gz',
        'pagecounts-20120804-130000.gz',
        'pagecounts-20120804-140000.gz',
        'pagecounts-20120804-150000.gz',
        'pagecounts-20120804-160000.gz',
        'pagecounts-20120804-170000.gz',
        'pagecounts-20120804-180000.gz',
        'pagecounts-20120804-190000.gz',
        'pagecounts-20120804-200000.gz',
        'pagecounts-20120804-210000.gz',
        'pagecounts-20120804-220000.gz',
        'pagecounts-20120804-230001.gz',
        'pagecounts-20120805-000000.gz',
        'pagecounts-20120805-010000.gz',
        'pagecounts-20120805-020000.gz',
        'pagecounts-20120805-030000.gz',
        'pagecounts-20120805-040000.gz',
        'pagecounts-20120805-050000.gz',
        'pagecounts-20120805-060000.gz',
        'pagecounts-20120805-070000.gz',
        'pagecounts-20120805-080000.gz',
        'pagecounts-20120805-090000.gz',
        'pagecounts-20120805-100000.gz',
        'pagecounts-20120805-110000.gz',
        'pagecounts-20120805-120000.gz',
        'pagecounts-20120805-130001.gz',
        'pagecounts-20120805-140000.gz',
        'pagecounts-20120805-150000.gz',
        'pagecounts-20120805-160000.gz',
        'pagecounts-20120805-170000.gz',
        'pagecounts-20120805-180000.gz',
        'pagecounts-20120805-190000.gz',
        'pagecounts-20120805-200000.gz',
        'pagecounts-20120805-210000.gz',
        'pagecounts-20120805-220000.gz',
        'pagecounts-20120805-230000.gz',
        'pagecounts-20120806-000000.gz',
        'pagecounts-20120806-010000.gz',
        'pagecounts-20120806-020001.gz',
        'pagecounts-20120806-030000.gz',
        'pagecounts-20120806-040000.gz',
        'pagecounts-20120806-050000.gz',
        'pagecounts-20120806-060000.gz',
        'pagecounts-20120806-070000.gz',
        'pagecounts-20120806-080000.gz',
        'pagecounts-20120806-090000.gz',
        'pagecounts-20120806-100000.gz',
        'pagecounts-20120806-110000.gz',
        'pagecounts-20120806-120000.gz',
        'pagecounts-20120806-130000.gz',
        'pagecounts-20120806-140000.gz',
        'pagecounts-20120806-150001.gz',
        'pagecounts-20120806-160000.gz',
        'pagecounts-20120806-170000.gz',
        'pagecounts-20120806-180000.gz',
        'pagecounts-20120806-190000.gz',
        'pagecounts-20120806-200000.gz',
        'pagecounts-20120806-210000.gz',
        'pagecounts-20120806-220000.gz',
        'pagecounts-20120806-230000.gz',
        'pagecounts-20120807-000000.gz',
        'pagecounts-20120807-010000.gz',
        'pagecounts-20120807-020000.gz',
        'pagecounts-20120807-030000.gz',
        'pagecounts-20120807-040000.gz',
        'pagecounts-20120807-050001.gz',
        'pagecounts-20120807-060000.gz',
        'pagecounts-20120807-070000.gz',
        'pagecounts-20120807-080000.gz',
        'pagecounts-20120807-090000.gz',
        'pagecounts-20120807-100000.gz',
        'pagecounts-20120807-110000.gz',
        'pagecounts-20120807-120000.gz',
        'pagecounts-20120807-130000.gz',
        'pagecounts-20120807-140000.gz',
        'pagecounts-20120807-150000.gz',
        'pagecounts-20120807-160000.gz',
        'pagecounts-20120807-170000.gz',
        'pagecounts-20120807-180001.gz',
        'pagecounts-20120807-190000.gz',
        'pagecounts-20120807-200000.gz',
        'pagecounts-20120807-210000.gz',
        'pagecounts-20120807-220000.gz',
        'pagecounts-20120807-230000.gz',
        'pagecounts-20120808-000000.gz',
        'pagecounts-20120808-010000.gz',
        'pagecounts-20120808-020000.gz',
        'pagecounts-20120808-030000.gz',
        'pagecounts-20120808-040000.gz',
        'pagecounts-20120808-050000.gz',
        'pagecounts-20120808-060000.gz',
        'pagecounts-20120808-070000.gz',
        'pagecounts-20120808-080001.gz',
        'pagecounts-20120808-090000.gz',
        'pagecounts-20120808-100000.gz',
        'pagecounts-20120808-110000.gz',
        'pagecounts-20120808-120000.gz',
        'pagecounts-20120808-130000.gz',
        'pagecounts-20120808-140000.gz',
        'pagecounts-20120808-150000.gz',
        'pagecounts-20120808-160000.gz',
        'pagecounts-20120808-170000.gz',
        'pagecounts-20120808-180000.gz',
        'pagecounts-20120808-190000.gz',
        'pagecounts-20120808-200000.gz',
        'pagecounts-20120808-210000.gz',
        'pagecounts-20120808-220001.gz',
        'pagecounts-20120808-230000.gz',
        'pagecounts-20120809-000000.gz',
        'pagecounts-20120809-010000.gz',
        'pagecounts-20120809-020000.gz',
        'pagecounts-20120809-030000.gz',
        'pagecounts-20120809-040000.gz',
        'pagecounts-20120809-050000.gz',
        'pagecounts-20120809-060000.gz',
        'pagecounts-20120809-070000.gz',
        'pagecounts-20120809-080000.gz',
        'pagecounts-20120809-090000.gz',
        'pagecounts-20120809-100000.gz',
        'pagecounts-20120809-110000.gz',
        'pagecounts-20120809-120000.gz',
        'pagecounts-20120809-130000.gz',
        'pagecounts-20120809-140001.gz',
        'pagecounts-20120809-150000.gz',
        'pagecounts-20120809-160000.gz',
        'pagecounts-20120809-170000.gz',
        'pagecounts-20120809-180000.gz',
        'pagecounts-20120809-190000.gz',
        'pagecounts-20120809-200000.gz',
        'pagecounts-20120809-210000.gz',
        'pagecounts-20120809-220000.gz',
        'pagecounts-20120809-230000.gz',
        'pagecounts-20120810-000000.gz',
        'pagecounts-20120810-010000.gz',
        'pagecounts-20120810-020000.gz',
        'pagecounts-20120810-030000.gz',
        'pagecounts-20120810-040001.gz',
        'pagecounts-20120810-050000.gz',
        'pagecounts-20120810-060000.gz',
        'pagecounts-20120810-070000.gz',
        'pagecounts-20120810-080000.gz',
        'pagecounts-20120810-090000.gz',
        'pagecounts-20120810-100000.gz',
        'pagecounts-20120810-110000.gz',
        'pagecounts-20120810-120000.gz',
        'pagecounts-20120810-130000.gz',
        'pagecounts-20120810-140000.gz',
        'pagecounts-20120810-150000.gz',
        'pagecounts-20120810-160000.gz',
        'pagecounts-20120810-170000.gz',
        'pagecounts-20120810-180001.gz',
        'pagecounts-20120810-190000.gz',
        'pagecounts-20120810-200000.gz',
        'pagecounts-20120810-210000.gz',
        'pagecounts-20120810-220000.gz',
        'pagecounts-20120810-230000.gz',
        'pagecounts-20120811-000000.gz',
        'pagecounts-20120811-010000.gz',
        'pagecounts-20120811-020000.gz',
        'pagecounts-20120811-030000.gz',
        'pagecounts-20120811-040000.gz',
        'pagecounts-20120811-050000.gz',
        'pagecounts-20120811-060000.gz',
        'pagecounts-20120811-070000.gz',
        'pagecounts-20120811-080001.gz',
        'pagecounts-20120811-090000.gz',
        'pagecounts-20120811-100000.gz',
        'pagecounts-20120811-110000.gz',
        'pagecounts-20120811-120000.gz',
        'pagecounts-20120811-130000.gz',
        'pagecounts-20120811-140000.gz',
        'pagecounts-20120811-150000.gz',
        'pagecounts-20120811-160000.gz',
        'pagecounts-20120811-170000.gz',
        'pagecounts-20120811-180000.gz',
        'pagecounts-20120811-190000.gz',
        'pagecounts-20120811-200000.gz',
        'pagecounts-20120811-210000.gz',
        'pagecounts-20120811-220000.gz',
        'pagecounts-20120811-230001.gz',
        'pagecounts-20120812-000000.gz',
        'pagecounts-20120812-010000.gz',
        'pagecounts-20120812-020000.gz',
        'pagecounts-20120812-030000.gz',
        'pagecounts-20120812-040000.gz',
        'pagecounts-20120812-050000.gz',
        'pagecounts-20120812-060000.gz',
        'pagecounts-20120812-070000.gz',
        'pagecounts-20120812-080000.gz',
        'pagecounts-20120812-090000.gz',
        'pagecounts-20120812-100000.gz',
        'pagecounts-20120812-110000.gz',
        'pagecounts-20120812-120000.gz',
        'pagecounts-20120812-130001.gz',
        'pagecounts-20120812-140000.gz',
        'pagecounts-20120812-150000.gz',
        'pagecounts-20120812-160000.gz',
        'pagecounts-20120812-170000.gz',
        'pagecounts-20120812-180000.gz',
        'pagecounts-20120812-190000.gz',
        'pagecounts-20120812-200000.gz',
        'pagecounts-20120812-210000.gz',
        'pagecounts-20120812-220000.gz',
        'pagecounts-20120812-230000.gz',
        'pagecounts-20120813-000000.gz',
        'pagecounts-20120813-010000.gz',
        'pagecounts-20120813-020000.gz',
        'pagecounts-20120813-030001.gz',
        'pagecounts-20120813-040000.gz',
        'pagecounts-20120813-050000.gz',
        'pagecounts-20120813-060000.gz',
        'pagecounts-20120813-070000.gz',
        'pagecounts-20120813-080000.gz',
        'pagecounts-20120813-090000.gz',
        'pagecounts-20120813-100000.gz',
        'pagecounts-20120813-110000.gz',
        'pagecounts-20120813-120000.gz',
        'pagecounts-20120813-130000.gz',
        'pagecounts-20120813-140000.gz',
        'pagecounts-20120813-150000.gz',
        'pagecounts-20120813-160000.gz',
        'pagecounts-20120813-170000.gz',
        'pagecounts-20120813-180001.gz',
        'pagecounts-20120813-190000.gz',
        'pagecounts-20120813-200000.gz',
        'pagecounts-20120813-210000.gz',
        'pagecounts-20120813-220000.gz',
        'pagecounts-20120813-230000.gz',
        'pagecounts-20120814-000000.gz',
        'pagecounts-20120814-010000.gz',
        'pagecounts-20120814-020000.gz',
        'pagecounts-20120814-030000.gz',
        'pagecounts-20120814-040000.gz',
        'pagecounts-20120814-050000.gz',
        'pagecounts-20120814-060000.gz',
        'pagecounts-20120814-070000.gz',
        'pagecounts-20120814-080001.gz',
        'pagecounts-20120814-090000.gz',
        'pagecounts-20120814-100000.gz',
        'pagecounts-20120814-110000.gz',
        'pagecounts-20120814-120000.gz',
        'pagecounts-20120814-130000.gz',
        'pagecounts-20120814-140000.gz',
        'pagecounts-20120814-150000.gz',
        'pagecounts-20120814-160000.gz',
        'pagecounts-20120814-170000.gz',
        'pagecounts-20120814-180000.gz',
        'pagecounts-20120814-190000.gz',
        'pagecounts-20120814-200000.gz',
        'pagecounts-20120814-210000.gz',
        'pagecounts-20120814-220001.gz',
        'pagecounts-20120814-230000.gz',
        'pagecounts-20120815-000000.gz',
        'pagecounts-20120815-010000.gz',
        'pagecounts-20120815-020000.gz',
        'pagecounts-20120815-030000.gz',
        'pagecounts-20120815-040000.gz',
        'pagecounts-20120815-050000.gz',
        'pagecounts-20120815-060000.gz',
        'pagecounts-20120815-070000.gz',
        'pagecounts-20120815-080000.gz',
        'pagecounts-20120815-090000.gz',
        'pagecounts-20120815-100000.gz',
        'pagecounts-20120815-110000.gz',
        'pagecounts-20120815-120001.gz',
        'pagecounts-20120815-130000.gz',
        'pagecounts-20120815-140000.gz',
        'pagecounts-20120815-150000.gz',
        'pagecounts-20120815-160000.gz',
        'pagecounts-20120815-170000.gz',
        'pagecounts-20120815-180000.gz',
        'pagecounts-20120815-190000.gz',
        'pagecounts-20120815-200000.gz',
        'pagecounts-20120815-210000.gz',
        'pagecounts-20120815-220000.gz',
        'pagecounts-20120815-230000.gz',
        'pagecounts-20120816-000000.gz',
        'pagecounts-20120816-010000.gz',
        'pagecounts-20120816-020000.gz',
        'pagecounts-20120816-030001.gz',
        'pagecounts-20120816-040000.gz',
        'pagecounts-20120816-050000.gz',
        'pagecounts-20120816-060000.gz',
        'pagecounts-20120816-070000.gz',
        'pagecounts-20120816-080000.gz',
        'pagecounts-20120816-090000.gz',
        'pagecounts-20120816-100000.gz',
        'pagecounts-20120816-110000.gz',
        'pagecounts-20120816-120000.gz',
        'pagecounts-20120816-130000.gz',
        'pagecounts-20120816-140000.gz',
        'pagecounts-20120816-150000.gz',
        'pagecounts-20120816-160000.gz',
        'pagecounts-20120816-170001.gz',
        'pagecounts-20120816-180000.gz',
        'pagecounts-20120816-190000.gz',
        'pagecounts-20120816-200000.gz',
        'pagecounts-20120816-210000.gz',
        'pagecounts-20120816-220000.gz',
        'pagecounts-20120816-230000.gz',
        'pagecounts-20120817-000000.gz',
        'pagecounts-20120817-010000.gz',
        'pagecounts-20120817-020000.gz',
        'pagecounts-20120817-030000.gz',
        'pagecounts-20120817-040000.gz',
        'pagecounts-20120817-050000.gz',
        'pagecounts-20120817-060000.gz',
        'pagecounts-20120817-070001.gz',
        'pagecounts-20120817-080000.gz',
        'pagecounts-20120817-090000.gz',
        'pagecounts-20120817-100000.gz',
        'pagecounts-20120817-110000.gz',
        'pagecounts-20120817-120000.gz',
        'pagecounts-20120817-130000.gz',
        'pagecounts-20120817-140000.gz',
        'pagecounts-20120817-150000.gz',
        'pagecounts-20120817-160000.gz',
        'pagecounts-20120817-170000.gz',
        'pagecounts-20120817-180000.gz',
        'pagecounts-20120817-190000.gz',
        'pagecounts-20120817-200000.gz',
        'pagecounts-20120817-210000.gz',
        'pagecounts-20120817-220001.gz',
        'pagecounts-20120817-230000.gz',
        'pagecounts-20120818-000000.gz',
        'pagecounts-20120818-010000.gz',
        'pagecounts-20120818-020000.gz',
        'pagecounts-20120818-030000.gz',
        'pagecounts-20120818-040000.gz',
        'pagecounts-20120818-050000.gz',
        'pagecounts-20120818-060000.gz',
        'pagecounts-20120818-070000.gz',
        'pagecounts-20120818-080000.gz',
        'pagecounts-20120818-090000.gz',
        'pagecounts-20120818-100000.gz',
        'pagecounts-20120818-110000.gz',
        'pagecounts-20120818-120001.gz',
        'pagecounts-20120818-130000.gz',
        'pagecounts-20120818-140000.gz',
        'pagecounts-20120818-150000.gz',
        'pagecounts-20120818-160000.gz',
        'pagecounts-20120818-170000.gz',
        'pagecounts-20120818-180000.gz',
        'pagecounts-20120818-190000.gz',
        'pagecounts-20120818-200000.gz',
        'pagecounts-20120818-210000.gz',
        'pagecounts-20120818-220000.gz',
        'pagecounts-20120818-230000.gz',
        'pagecounts-20120819-000000.gz',
        'pagecounts-20120819-010000.gz',
        'pagecounts-20120819-020001.gz',
        'pagecounts-20120819-030000.gz',
        'pagecounts-20120819-040000.gz',
        'pagecounts-20120819-050000.gz',
        'pagecounts-20120819-060000.gz',
        'pagecounts-20120819-070000.gz',
        'pagecounts-20120819-080000.gz',
        'pagecounts-20120819-090000.gz',
        'pagecounts-20120819-100000.gz',
        'pagecounts-20120819-110000.gz',
        'pagecounts-20120819-120000.gz',
        'pagecounts-20120819-130000.gz',
        'pagecounts-20120819-140000.gz',
        'pagecounts-20120819-150000.gz',
        'pagecounts-20120819-160001.gz',
        'pagecounts-20120819-170000.gz',
        'pagecounts-20120819-180000.gz',
        'pagecounts-20120819-190000.gz',
        'pagecounts-20120819-200000.gz',
        'pagecounts-20120819-210000.gz',
        'pagecounts-20120819-220000.gz',
        'pagecounts-20120819-230000.gz',
        'pagecounts-20120820-000000.gz',
        'pagecounts-20120820-010000.gz',
        'pagecounts-20120820-020000.gz',
        'pagecounts-20120820-030000.gz',
        'pagecounts-20120820-040000.gz',
        'pagecounts-20120820-050000.gz',
        'pagecounts-20120820-060001.gz',
        'pagecounts-20120820-070000.gz',
        'pagecounts-20120820-080000.gz',
        'pagecounts-20120820-090000.gz',
        'pagecounts-20120820-100000.gz',
        'pagecounts-20120820-110000.gz',
        'pagecounts-20120820-120000.gz',
        'pagecounts-20120820-130000.gz',
        'pagecounts-20120820-140000.gz',
        'pagecounts-20120820-150000.gz',
        'pagecounts-20120820-160000.gz',
        'pagecounts-20120820-170000.gz',
        'pagecounts-20120820-180000.gz',
        'pagecounts-20120820-190001.gz',
        'pagecounts-20120820-200000.gz',
        'pagecounts-20120820-210000.gz',
        'pagecounts-20120820-220000.gz',
        'pagecounts-20120820-230000.gz',
        'pagecounts-20120821-000000.gz',
        'pagecounts-20120821-010000.gz',
        'pagecounts-20120821-020000.gz',
        'pagecounts-20120821-030000.gz',
        'pagecounts-20120821-040000.gz',
        'pagecounts-20120821-050000.gz',
        'pagecounts-20120821-060000.gz',
        'pagecounts-20120821-070000.gz',
        'pagecounts-20120821-080001.gz',
        'pagecounts-20120821-090000.gz',
        'pagecounts-20120821-100000.gz',
        'pagecounts-20120821-110000.gz',
        'pagecounts-20120821-120000.gz',
        'pagecounts-20120821-130000.gz',
        'pagecounts-20120821-140000.gz',
        'pagecounts-20120821-150000.gz',
        'pagecounts-20120821-160000.gz',
        'pagecounts-20120821-170000.gz',
        'pagecounts-20120821-180000.gz',
        'pagecounts-20120821-190000.gz',
        'pagecounts-20120821-200000.gz',
        'pagecounts-20120821-210000.gz',
        'pagecounts-20120821-220001.gz',
        'pagecounts-20120821-230000.gz',
        'pagecounts-20120822-000000.gz',
        'pagecounts-20120822-010000.gz',
        'pagecounts-20120822-020000.gz',
        'pagecounts-20120822-030000.gz',
        'pagecounts-20120822-040000.gz',
        'pagecounts-20120822-050000.gz',
        'pagecounts-20120822-060000.gz',
        'pagecounts-20120822-070000.gz',
        'pagecounts-20120822-080000.gz',
        'pagecounts-20120822-090000.gz',
        'pagecounts-20120822-100000.gz',
        'pagecounts-20120822-110000.gz',
        'pagecounts-20120822-120001.gz',
        'pagecounts-20120822-130000.gz',
        'pagecounts-20120822-140000.gz',
        'pagecounts-20120822-150000.gz',
        'pagecounts-20120822-160000.gz',
        'pagecounts-20120822-170000.gz',
        'pagecounts-20120822-180000.gz',
        'pagecounts-20120822-190000.gz',
        'pagecounts-20120822-200000.gz',
        'pagecounts-20120822-210000.gz',
        'pagecounts-20120822-220000.gz',
        'pagecounts-20120822-230000.gz',
        'pagecounts-20120823-000000.gz',
        'pagecounts-20120823-010000.gz',
        'pagecounts-20120823-020000.gz',
        'pagecounts-20120823-030001.gz',
        'pagecounts-20120823-040000.gz',
        'pagecounts-20120823-050000.gz',
        'pagecounts-20120823-060000.gz',
        'pagecounts-20120823-070000.gz',
        'pagecounts-20120823-080000.gz',
        'pagecounts-20120823-090000.gz',
        'pagecounts-20120823-100000.gz',
        'pagecounts-20120823-110000.gz',
        'pagecounts-20120823-120000.gz',
        'pagecounts-20120823-130000.gz',
        'pagecounts-20120823-140000.gz',
        'pagecounts-20120823-150000.gz',
        'pagecounts-20120823-160000.gz',
        'pagecounts-20120823-170001.gz',
        'pagecounts-20120823-180000.gz',
        'pagecounts-20120823-190000.gz',
        'pagecounts-20120823-200000.gz',
        'pagecounts-20120823-210000.gz',
        'pagecounts-20120823-220000.gz',
        'pagecounts-20120823-230000.gz',
        'pagecounts-20120824-000000.gz',
        'pagecounts-20120824-010000.gz',
        'pagecounts-20120824-020000.gz',
        'pagecounts-20120824-030000.gz',
        'pagecounts-20120824-040000.gz',
        'pagecounts-20120824-050000.gz',
        'pagecounts-20120824-060001.gz',
        'pagecounts-20120824-070000.gz',
        'pagecounts-20120824-080000.gz',
        'pagecounts-20120824-090000.gz',
        'pagecounts-20120824-100000.gz',
        'pagecounts-20120824-110000.gz',
        'pagecounts-20120824-120000.gz',
        'pagecounts-20120824-130000.gz',
        'pagecounts-20120824-140000.gz',
        'pagecounts-20120824-150000.gz',
        'pagecounts-20120824-160000.gz',
        'pagecounts-20120824-170000.gz',
        'pagecounts-20120824-180000.gz',
        'pagecounts-20120824-190001.gz',
        'pagecounts-20120824-200000.gz',
        'pagecounts-20120824-210000.gz',
        'pagecounts-20120824-220000.gz',
        'pagecounts-20120824-230000.gz',
        'pagecounts-20120825-000000.gz',
        'pagecounts-20120825-010000.gz',
        'pagecounts-20120825-020000.gz',
        'pagecounts-20120825-030000.gz',
        'pagecounts-20120825-040000.gz',
        'pagecounts-20120825-050000.gz',
        'pagecounts-20120825-060000.gz',
        'pagecounts-20120825-070000.gz',
        'pagecounts-20120825-080001.gz',
        'pagecounts-20120825-090000.gz',
        'pagecounts-20120825-100000.gz',
        'pagecounts-20120825-110000.gz',
        'pagecounts-20120825-120000.gz',
        'pagecounts-20120825-130000.gz',
        'pagecounts-20120825-140000.gz',
        'pagecounts-20120825-150000.gz',
        'pagecounts-20120825-160000.gz',
        'pagecounts-20120825-170000.gz',
        'pagecounts-20120825-180000.gz',
        'pagecounts-20120825-190000.gz',
        'pagecounts-20120825-200000.gz',
        'pagecounts-20120825-210000.gz',
        'pagecounts-20120825-220001.gz',
        'pagecounts-20120825-230000.gz',
        'pagecounts-20120826-000000.gz',
        'pagecounts-20120826-010000.gz',
        'pagecounts-20120826-020000.gz',
        'pagecounts-20120826-030000.gz',
        'pagecounts-20120826-040000.gz',
        'pagecounts-20120826-050000.gz',
        'pagecounts-20120826-060000.gz',
        'pagecounts-20120826-070000.gz',
        'pagecounts-20120826-080000.gz',
        'pagecounts-20120826-090000.gz',
        'pagecounts-20120826-100000.gz',
        'pagecounts-20120826-110000.gz',
        'pagecounts-20120826-120000.gz',
        'pagecounts-20120826-130001.gz',
        'pagecounts-20120826-140000.gz',
        'pagecounts-20120826-150000.gz',
        'pagecounts-20120826-160000.gz',
        'pagecounts-20120826-170000.gz',
        'pagecounts-20120826-180000.gz',
        'pagecounts-20120826-190000.gz',
        'pagecounts-20120826-200000.gz',
        'pagecounts-20120826-210000.gz',
        'pagecounts-20120826-220000.gz',
        'pagecounts-20120826-230000.gz',
        'pagecounts-20120827-000000.gz',
        'pagecounts-20120827-010000.gz',
        'pagecounts-20120827-020000.gz',
        'pagecounts-20120827-030001.gz',
        'pagecounts-20120827-040000.gz',
        'pagecounts-20120827-050000.gz',
        'pagecounts-20120827-060000.gz',
        'pagecounts-20120827-070000.gz',
        'pagecounts-20120827-080000.gz',
        'pagecounts-20120827-090000.gz',
        'pagecounts-20120827-100000.gz',
        'pagecounts-20120827-110000.gz',
        'pagecounts-20120827-120000.gz',
        'pagecounts-20120827-130000.gz',
        'pagecounts-20120827-140000.gz',
        'pagecounts-20120827-150000.gz',
        'pagecounts-20120827-160000.gz',
        'pagecounts-20120827-170000.gz',
        'pagecounts-20120827-180001.gz',
        'pagecounts-20120827-190000.gz',
        'pagecounts-20120827-200000.gz',
        'pagecounts-20120827-210000.gz',
        'pagecounts-20120827-220000.gz',
        'pagecounts-20120827-230000.gz',
        'pagecounts-20120828-000000.gz',
        'pagecounts-20120828-010000.gz',
        'pagecounts-20120828-020000.gz',
        'pagecounts-20120828-030000.gz',
        'pagecounts-20120828-040000.gz',
        'pagecounts-20120828-050000.gz',
        'pagecounts-20120828-060000.gz',
        'pagecounts-20120828-070000.gz',
        'pagecounts-20120828-080001.gz',
        'pagecounts-20120828-090000.gz',
        'pagecounts-20120828-100000.gz',
        'pagecounts-20120828-110000.gz',
        'pagecounts-20120828-120000.gz',
        'pagecounts-20120828-130000.gz',
        'pagecounts-20120828-140000.gz',
        'pagecounts-20120828-150000.gz',
        'pagecounts-20120828-160000.gz',
        'pagecounts-20120828-170000.gz',
        'pagecounts-20120828-180000.gz',
        'pagecounts-20120828-190000.gz',
        'pagecounts-20120828-200000.gz',
        'pagecounts-20120828-210001.gz',
        'pagecounts-20120828-220000.gz',
        'pagecounts-20120828-230000.gz',
        'pagecounts-20120829-000000.gz',
        'pagecounts-20120829-010000.gz',
        'pagecounts-20120829-020000.gz',
        'pagecounts-20120829-030000.gz',
        'pagecounts-20120829-040000.gz',
        'pagecounts-20120829-050000.gz',
        'pagecounts-20120829-060000.gz',
        'pagecounts-20120829-070000.gz',
        'pagecounts-20120829-080000.gz',
        'pagecounts-20120829-090000.gz',
        'pagecounts-20120829-100000.gz',
        'pagecounts-20120829-110001.gz',
        'pagecounts-20120829-120000.gz',
        'pagecounts-20120829-130000.gz',
        'pagecounts-20120829-140000.gz',
        'pagecounts-20120829-150000.gz',
        'pagecounts-20120829-160000.gz',
        'pagecounts-20120829-170000.gz',
        'pagecounts-20120829-180000.gz',
        'pagecounts-20120829-190000.gz',
        'pagecounts-20120829-200000.gz',
        'pagecounts-20120829-210000.gz',
        'pagecounts-20120829-220000.gz',
        'pagecounts-20120829-230000.gz',
        'pagecounts-20120830-000000.gz',
        'pagecounts-20120830-010001.gz',
        'pagecounts-20120830-020000.gz',
        'pagecounts-20120830-030000.gz',
        'pagecounts-20120830-040000.gz',
        'pagecounts-20120830-050000.gz',
        'pagecounts-20120830-060000.gz',
        'pagecounts-20120830-070000.gz',
        'pagecounts-20120830-080000.gz',
        'pagecounts-20120830-090000.gz',
        'pagecounts-20120830-100000.gz',
        'pagecounts-20120830-110000.gz',
        'pagecounts-20120830-120000.gz',
        'pagecounts-20120830-130000.gz',
        'pagecounts-20120830-140000.gz',
        'pagecounts-20120830-150001.gz',
        'pagecounts-20120830-160000.gz',
        'pagecounts-20120830-170000.gz',
        'pagecounts-20120830-180000.gz',
        'pagecounts-20120830-190000.gz',
        'pagecounts-20120830-200000.gz',
        'pagecounts-20120830-210000.gz',
        'pagecounts-20120830-220000.gz',
        'pagecounts-20120830-230000.gz',
        'pagecounts-20120831-000000.gz',
        'pagecounts-20120831-010000.gz',
        'pagecounts-20120831-020000.gz',
        'pagecounts-20120831-030000.gz',
        'pagecounts-20120831-040000.gz',
        'pagecounts-20120831-050000.gz',
        'pagecounts-20120831-060001.gz',
        'pagecounts-20120831-070000.gz',
        'pagecounts-20120831-080000.gz',
        'pagecounts-20120831-090000.gz',
        'pagecounts-20120831-100000.gz',
        'pagecounts-20120831-110000.gz',
        'pagecounts-20120831-120000.gz',
        'pagecounts-20120831-130000.gz',
        'pagecounts-20120831-140000.gz',
        'pagecounts-20120831-150000.gz',
        'pagecounts-20120831-160000.gz',
        'pagecounts-20120831-170000.gz',
        'pagecounts-20120831-180001.gz',
        'pagecounts-20120831-190000.gz',
        'pagecounts-20120831-200000.gz',
        'pagecounts-20120831-210000.gz',
        'pagecounts-20120831-220000.gz',
        'pagecounts-20120831-230000.gz'
    ]

    # md5 checksum hashes to python
    dt_md5 = 'md5sums.txt'
    dt_pd_md5 = pd.read_table(os.path.dirname(os.path.realpath(__file__)) + sl + dt_md5, delim_whitespace=True,
                              header=None, names=['md5', 'fname'], index_col=1)
    t = 0
    for x in files:
        if hashlib.md5(open(x, 'rb').read()).hexdigest() == dt_pd_md5.loc[x]['md5']:
            print('md5 match', x)
        else:
            print('md5 error in', x)

    # dt_pd_wiki_legacy['tstamp'] = pd.to_datetime(dt_pd_wiki_legacy['tstamp'])

    print('md5 check done')

if __name__ == '__main__':
    main()
else:
    print("Run From Import")