# Compiling on 🍎 macOS
- Similar to Windows
- For M chips, use ARM64 binaries
- Note that default `CMakeLists.txt` format is not compatible with new CMake (e.g., 4+), so use `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` flag (or downgrade CMake, or update `CMakeLists.txt`
- Static libraries are different on macOS, so that part of the build is different

``` sh 
mkdir build
cd build
cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5
make -j$(sysctl -n hw.ncpu)

cmake .. -DCMAKE_BUILD_TYPE=Release \
         -DCMAKE_EXE_LINKER_FLAGS="-static-libgfortran -static-libgcc"
make
```
