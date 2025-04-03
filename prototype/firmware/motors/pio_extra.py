import os
Import("env")

env.Replace(COMPILATIONDB_INCLUDE_TOOLCHAIN=True) # Needed for clangd IDE integration
