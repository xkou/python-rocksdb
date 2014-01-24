from libcpp cimport bool as cpp_bool
from libcpp.string cimport string
from libc.string cimport const_char
from slice_ cimport Slice

cdef extern from "rocksdb/filter_policy.h" namespace "rocksdb":
    cdef cppclass FilterPolicy:
        void CreateFilter(const Slice*, int, string*) nogil except+
        cpp_bool KeyMayMatch(const Slice&, const Slice&) nogil except+
        const_char* Name() nogil except+

    cdef extern const FilterPolicy* NewBloomFilterPolicy(int) nogil except+

ctypedef void (*create_filter_func)(void*, const Slice*, int, string*)
ctypedef cpp_bool (*key_may_match_func)(void*, const Slice&, const Slice&)

cdef extern from "cpp/filter_policy_wrapper.hpp" namespace "py_rocks":
    cdef cppclass FilterPolicyWrapper:
        FilterPolicyWrapper(
            string,
            void*,
            create_filter_func,
            key_may_match_func) nogil except+
