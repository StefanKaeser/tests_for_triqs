configure_file(tests_for_triqs-config.cmake.in tests_for_triqs-config.cmake @ONLY)
configure_file(tests_for_triqs-config-version.cmake.in tests_for_triqs-config-version.cmake @ONLY)
install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/tests_for_triqs-config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/tests_for_triqs-config-version.cmake
  DESTINATION lib/cmake/tests_for_triqs
)

install(EXPORT tests_for_triqs-targets NAMESPACE tests_for_triqs:: DESTINATION lib/cmake/tests_for_triqs)
