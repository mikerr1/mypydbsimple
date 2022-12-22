from mypydb import DB
from pprint import pprint

db = DB('mypydb.conf')

pprint(db.__dict__)
db.connect('proxies')
db.connect()

query = 'select * from proxies limit %s, %s'
data = (1,2)
rs = db.execute(query, data)

pprint(db.__dict__)
#value = rs[0]['key_name'] # if only return one value
pprint(rs)
#pprint(vars(db))

exit()

data = {
    'title':'contoh article judul baru',
    'source_url':'contoh source url',
    'author_name':'contoh author name',
    'unique_id':'254622345234523'
}

query = """INSERT INTO articles 
    (title, source_url, author_name, unique_id)  
    VALUES (%(title)s, %(source_url)s, %(author_name)s, %(unique_id)s)"""


db.execute(query, data)

pprint(vars(db))


