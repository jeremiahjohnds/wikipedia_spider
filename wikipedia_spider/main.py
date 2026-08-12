import os
import runpy
import shutil
import sys


def cache_deletion(path=os.getcwd()):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))


if __name__ == "__main__":
    cache_deletion()
    runpy.run_module("wikipedia_spider.spiders.wikipedia", run_name="__main__")
    sys.exit()

# https://en.wikipedia.org/wiki/Alone_for_Christmas, https://en.wikipedia.org/wiki/Alpha_(2018_film), https://en.wikipedia.org/wiki/Anaconda_(2025_film)
