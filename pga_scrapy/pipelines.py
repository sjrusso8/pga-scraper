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
        PATH = "C:/Users/sjrus/Documents/code/projects/pga-scraper/pga_scrapy/output/"

        foldername = get_valid_filename(item.pop("stat_group"))
        filename = get_valid_filename(item.pop("stat_name"))
        df = pd.read_html(str(item.pop("stat_table")))[0]

        saved_file_name = PATH+foldername+"_"+filename+'.csv'

        df.to_csv(saved_file_name, index=False)
