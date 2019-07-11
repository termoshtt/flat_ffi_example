#include <boost/python.hpp>
#include <boost/python/numpy.hpp>

namespace p = boost::python;
namespace np = boost::python::numpy;

np::ndarray new_zero1(unsigned int N) {
  p::tuple shape = p::make_tuple(N);
  np::dtype dtype = np::dtype::get_builtin<double>();
  return np::zeros(shape, dtype);
}

BOOST_PYTHON_MODULE(flat_cpp) {
  Py_Initialize();
  np::initialize();

  p::def("new_zero", new_zero1);
}
