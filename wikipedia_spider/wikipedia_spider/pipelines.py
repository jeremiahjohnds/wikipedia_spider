# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from collections import defaultdict


class WikipediaSpiderPipeline:
    def process_item(self, item):

        adapter = ItemAdapter(item)
        if any(isinstance(v, dict) for v in adapter.values()):

            phyla = defaultdict(list)
            for webpage, data in adapter.items():
                for webpages, url in adapter.items():
                    phyla[webpages].append(url)

            phylum = {}
            for website, data in phyla.items():
                for webpage in data:
                    for url, classes in webpage.items():
                        phylum[str((website, url))] = classes

            return phylum

        return item
