import rocksdb
from random import randbytes
db = rocksdb.DB('test.db', rocksdb.Options(create_if_missing=True, wal_size_limit_mb=10))
k = randbytes(8)
db.put(k, randbytes(8))
print(k, db.get(k))
print(db.latestSequenceNumber)
it = db.getUpdateSince(30)
for seq, data in it:
    pass