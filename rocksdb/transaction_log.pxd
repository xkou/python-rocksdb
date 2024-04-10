from libcpp cimport bool as cpp_bool
from libcpp.string cimport string
from .types cimport SequenceNumber

cdef extern from "rocksdb/transaction_log.h" namespace "rocksdb":
    cdef cppclass BatchResult:
        BatchResult()
        BatchResult(const BatchResult&)
        SequenceNumber sequence

    cdef cppclass TransactionLogIterator:
        TransactionLogIterator()
        cpp_bool Valid() nogil
        void Next() nogil 
        BatchResult GetBatch() nogil const