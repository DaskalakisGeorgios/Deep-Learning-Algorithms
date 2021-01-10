# Build the project on your platform.

Install (git) and (cmake):

- sudo apt-get update
- sudo apt-get install git cmake

Then clone the (jetson-inference) project:

- git clone https://github.com/dusty-nv/jetson-inference
- cd jetson-inference
- git submodule update --init

Create bindings for Python 3.6. Install these packages before proceeding:

- sudo apt-get install libpython3-dev python3-numpy

Confinguring with CMake:

Next, create a (build) directory within the project and run (cmake) to configure the (build). 
When (cmake) is run, a script is launched (CMakePreBuild.sh) that will install any required dependencies and download DNN models for you.
Omit if working directory is already jetson-inference from above. 
- cd jetson-inference                   
- mkdir build
- cd build
- cmake ../

Downloading Models & Installing PyTorch
Compiling the Project
Make sure you are still in the (jetson-inference/build) directory, created in the above step
Then run (make) followed by (sudo make install) to build the libraries, Python extension bindings, and code samples:
Omit if working directory is already build/ from above.
- cd jetson-inference/build            
- make
- sudo make install
- sudo ldconfig
