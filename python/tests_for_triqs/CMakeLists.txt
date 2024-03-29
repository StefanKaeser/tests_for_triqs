# Configure the version
configure_file(version.py.in version.py)

# All Python files. Copy them in the build dir to have a complete package for the tests.
file(GLOB_RECURSE python_sources RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.py)
file(GLOB_RECURSE wrap_generators RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *_desc.py)
list(REMOVE_ITEM python_sources "${wrap_generators}")
foreach(file ${python_sources})
  configure_file(${file} ${file} COPYONLY)
endforeach()

# Build any python modules
foreach(gen ${wrap_generators})
  string(REPLACE "_desc.py" "" module_name ${gen})
  add_cpp2py_module(${module_name})
  target_link_libraries(${module_name} tests_for_triqs_c)
endforeach()

# Install python modules to proper location
set(PYTHON_LIB_DEST ${TRIQS_PYTHON_LIB_DEST_ROOT}/tests_for_triqs)
get_property(CPP2PY_MODULES_LIST GLOBAL PROPERTY CPP2PY_MODULES_LIST)
install(TARGETS ${CPP2PY_MODULES_LIST} DESTINATION ${PYTHON_LIB_DEST})
install(FILES ${python_sources} ${CMAKE_CURRENT_BINARY_DIR}/version.py DESTINATION ${PYTHON_LIB_DEST})
