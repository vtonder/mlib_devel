export XILINX_PATH=/opt/Xilinx/Vivado/2016.1
export USE_VIVADO_RUNTIME_FOR_MATLAB=1
export MATLAB_PATH=/usr/local/MATLAB/R2015b
export MLIB_DEVEL_PATH=/home/vtonder/mlib_devel
export PLATFORM=lin64
export XILINXD_LICENSE_FILE=/home/jackh/.Xilinx/Xilinx.lic

export SYSGEN_SCRIPT=$MLIB_DEVEL_PATH/startsg
export MATLAB=$MATLAB_PATH
export CASPER_BASE_PATH=$MLIB_DEVEL_PATH
export HDL_ROOT=$CASPER_BASE_PATH/jasper_library/hdl_sources
export XPS_BASE_PATH=$MLIB_DEVEL_PATH/xps_base
source $XILINX_PATH/settings64.sh

export LD_LIBRARY_PATH=""
