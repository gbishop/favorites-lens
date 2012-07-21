import logging
logging.basicConfig(filename='/tmp/fav.txt', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

import os.path as osp
from glob import glob
import time

from singlet.lens import SingleScopeLens, ListViewCategory

from favorites import favoritesconfig

import sqlite3
dbname = glob(osp.expanduser('~/.mozilla/firefox/*.default/places.sqlite'))[0]
logging.info('firefox db is "%s"' % dbname)
conn = sqlite3.connect(dbname)
cursor = conn.cursor()

select = "select b.title,p.url from moz_bookmarks as b left join moz_places as p on (b.fk = p.id) where b.title like '%s' order by p.visit_count desc limit 10;"


class FavoritesLens(SingleScopeLens):

    def __init__(self):
        SingleScopeLens.__init__(self)
        self._lens.props.search_in_global = True

    class Meta:
        name = 'favorites'
        description = 'Favorites Lens'
        search_hint = 'Search Favorites'
        icon = 'favorites.svg'
        search_on_blank = False
        search_in_global = True

    # TODO: Add your categories
    link_category = ListViewCategory("Links", "dialog-information-symbolic")

    def bookmarks_query(self, search):
        t0 = time.time()
        search = "%" + search.strip().replace(' ', '%') + "%"
        res = list(cursor.execute(select % search))
        t1 = time.time()
        logging.debug('query takes %.2f seconds' % (t1 - t0))
        return res

    def search(self, search, results):
        # TODO: Add your search results
        logging.debug('search "%s"' % search)

        for row in self.bookmarks_query(search):
            results.append(row[1],
                             'ubuntu-logo',
                             self.link_category,
                             "text/html",
                             row[0],
                             'Bookmark',
                             'https://wiki.ubuntu.com/Unity/Lenses/Singlet')
        pass
