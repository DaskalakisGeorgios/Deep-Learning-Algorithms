# Build the project on your platform.

# Install git and cmake:

- sudo apt-get update
- sudo apt-get install git cmake

# Then clone the jetson-inference project:

- git clone https://github.com/dusty-nv/jetson-inference
- cd jetson-inference
- git submodule update --init

# Create bindings for Python 3.6. Install these packages before proceeding:

- sudo apt-get install libpython3-dev python3-numpy

# Confinguring with CMake:

Next, create a build directory within the project and run cmake to configure the build. 
When cmake is run, a script is launched (CMakePreBuild.sh) that will install any required dependencies and download DNN models for you.

- cd jetson-inference
Omit if working directory is already jetson-inference/ from above
- mkdir build
- cd build
- cmake ../
