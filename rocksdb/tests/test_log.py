import rocksdb
from random import randbytes
db = rocksdb.DB('test.db', rocksdb.Options(create_if_missing=True, wal_size_limit_mb=10))
k = randbytes(8)
db.put(k, randbytes(8))
print(k, db.get(k))
print(db.latestSequenceNumber)
while 1:
    it = db.getUpdateSince(40)
    for seq, data in it:
        # print(seq, data)
        pass

import os
os.system('rm -rf test2.db')
print('checkpoint:', db.checkpoint('test2.db'))

db2 = rocksdb.DB('test2.db', rocksdb.Options(create_if_missing=True, wal_size_limit_mb=10))

seq = db.latestSequenceNumber
k = randbytes(8)
v = randbytes(8)
db.put(k, v)

it = db.getUpdateSince(seq+1)
for seq, data in it:
    print(seq, data)
    db2.putLogData(data)

print('nn', db2.latestSequenceNumber, db2.get(k))
assert(db2.get(k)==v)
    


