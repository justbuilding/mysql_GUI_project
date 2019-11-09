# -*- coding:utf-8 -*-
# Author: Jay-Q
class DataManagement:
    goods = []

    def insert_db(self, goodinfo):
        self.goods = self.load()
        for good in self.goods:
            if good["isbn"] == goodinfo["isbn"]:
                return -1
        else:
            self.goods.append(goodinfo)
            with codecs.open("good.dat", "wb") as f:
                pickle.dump(self.goods, f)
            return 1

    def save_db(self, goodinfoes):
        with codecs.open("good.dat", "wb") as f:
            pickle.dump(goodinfoes, f)

    def query_db(self, isbn="", author="", goodname=""):
        self.goods = self.load()
        if isbn:
            for i, good in enumerate(self.goods):
                if good["isbn"] == isbn:
                    return i
                else:
                    return -1
        if author:
            for i, good in enumerate(self.goods):
                if good["author"] == author:
                    return i
                else:
                    return -1
        if goodname:
            for i, good in enumerate(self.goods):
                if good["subtitle"] == goodname:
                    return i
                else:
                    return -1

    def load(self):
        pathname = "good.dat"

        if not (os.path.exists(pathname) and os.path.isfile(pathname)):
            with codecs.open("good.dat", "wb") as f:
                pickle.dump(self.goods, f)
        with codecs.open("good.dat", "rb") as f:
            goods = pickle.load(f)
        return goods
