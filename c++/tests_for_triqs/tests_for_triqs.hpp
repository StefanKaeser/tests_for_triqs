#pragma once
#include <triqs/gfs.hpp>

namespace tests_for_triqs {

  using namespace triqs::gfs;
  typedef gf<cartesian_product<imfreq, brillouin_zone>, matrix_valued> g_wk_t;
  
  std::tuple<g_wk_t, g_wk_t> test_tuple(g_wk_t g_wk);
} // namespace tests_for_triqs
