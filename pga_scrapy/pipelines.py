# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import re


def get_valid_filename(s):
    """A little helper function to strip out illegal characters for filenames"""
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)


class PgaScrapyPipeline:
    """Scrapy Pipeline class to handle the parsed stat pages"""

    def process_item(self, item, spider):
        PATH = ""
        df = pd.read_html(str(item.pop("table")))[0]
        filename = get_valid_filename(item.pop("name"))

        df.to_csv(PATH+filename+'.csv', index=False)
