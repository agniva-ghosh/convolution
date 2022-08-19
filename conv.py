import numpy as np
import ctypes

# input type for the function; must be a double array, with dimensions that are contiguous
array_4d_double = np.ctypeslib.ndpointer(dtype=np.double, ndim=4, flags='C_CONTIGUOUS')

# load the library, using ctypes load library module
libcd = ctypes.cdll["libconv.so"]

# setup the return types and argument types
libcd.conv.restype = None
libcd.conv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, 
                        array_4d_double, array_4d_double, array_4d_double]

# wrapping the C-function 'conv' in python
def conv2d(input_arr, output_arr, kernel):
    return libcd.conv(input_arr.shape[0], 
                    kernel.shape[0], 
                    kernel.shape[3], 
                    input_arr.shape[3], 
                    input_arr.shape[2],
                    input_arr, 
                    output_arr, 
                    kernel)

