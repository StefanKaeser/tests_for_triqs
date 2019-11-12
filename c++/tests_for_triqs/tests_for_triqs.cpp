#include <triqs/gfs.hpp>
#include <omp.h>

namespace tests_for_triqs {

using namespace triqs::gfs;
typedef gf<cartesian_product<imfreq, brillouin_zone>, matrix_valued> g_wk_t;

g_wk_t test(g_wk_t g_wk) {

  auto [wmesh, kmesh] = g_wk.mesh();

#pragma omp parallel for
  for(unsigned int idx = 0; idx < kmesh.size(); idx++) {}

    return g_wk;
}
} // namespace tests_for_triqs
