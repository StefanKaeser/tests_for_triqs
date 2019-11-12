# Generated automatically using the command :
# c++2py ../../c++/tests_for_triqs/tests_for_triqs.hpp -p --members_read_only -N tests_for_triqs -a tests_for_triqs -m tests_for_triqs_module -o tests_for_triqs_module --moduledoc="The tests_for_triqs python module" -C pytriqs --cxxflags="-std=c++17" --target_file_only
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "tests_for_triqs_module", doc = r"The tests_for_triqs python module", app_name = "tests_for_triqs")

# Imports
module.add_imports(*['pytriqs.gf', 'pytriqs.lattice'])

# Add here all includes
module.add_include("tests_for_triqs/tests_for_triqs.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <cpp2py/converters/tuple.hpp>
#include <triqs/cpp2py_converters/gf.hpp>

using namespace tests_for_triqs;
""")


module.add_function ("std::tuple<g_wk_t,g_wk_t> tests_for_triqs::test_tuple (tests_for_triqs::g_wk_t g_wk)", doc = r"""""")



module.generate_code()