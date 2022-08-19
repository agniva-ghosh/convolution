import numpy as np
import conv # importing the wrapped C-library we created

# Creating input parameters
input_size = 10
num_input_channel = 3
kernel_size = 3
batch_num = 100
filter_num = 2

# Creating input and kernel using np.rand
input_arr = np.random.rand(input_size,input_size,num_input_channel,batch_num)
kernel = np.random.rand(kernel_size,kernel_size,num_input_channel,filter_num)

# Creating a zeros array for storing the output later
output_arr = np.zeros((input_size+kernel_size-1,input_size+kernel_size-1,filter_num,batch_num))

# Creating the convolution and storing it in output_arr
c = conv.conv2d(input_arr, output_arr, kernel)

# print(output_arr[:,:,1,20])


# Convolution with SciPy recipe
from scipy import signal
result = np.zeros((num_input_channel,output_arr.shape[0],output_arr.shape[0]))
for i in range(num_input_channel):
    result[i,:,:] = signal.convolve2d(input_arr[:,:,i,20],kernel[:,:,i,0],mode='full')

# Comparing our C-results with the Scipy results
print('output:\n',np.isclose(np.sum(result,axis=0),output_arr[:,:,0,20], rtol=1e-05, atol=1e-08, equal_nan=False))

