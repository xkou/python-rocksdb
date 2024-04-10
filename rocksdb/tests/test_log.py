import rocksdb
db = rocksdb.DB('test.db', rocksdb.Options(create_if_missing=True, wal_size_limit_mb=10))
db.put(b'a', b'data')
print(db.get(b'a'))
print(db.latestSequenceNumber)
it = db.getUpdateSince(2)
print('it', it)
print('it', next(it))
for e in it:
    print('!!', e)