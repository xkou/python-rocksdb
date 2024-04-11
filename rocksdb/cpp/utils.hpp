#include <vector>
#include <memory>
#include <utility>
namespace py_rocks {
    template <typename T>
    const T* vector_data(std::vector<T>& v) {
        return v.data();
    }

    template <typename T>
    std::unique_ptr<T> && unique_move(std::unique_ptr<T> && t){
        return std::move(t);
    }

    template <typename T>
    T && std_move(T & t){
        return std::move(t);
    }



    template <typename T>
    void unique_copy(std::unique_ptr<T> & a, std::unique_ptr<T> & b){
        a = std::move(b);
    }
}
