#include <stdio.h>
#include <stdlib.h>

void conv(int input_size, 
          int kernel_size, 
          int filter_num, 
          int batch_num, 
          int channel_num, 
          double input[input_size][input_size][channel_num][batch_num],
          double output[input_size+kernel_size-1][input_size+kernel_size-1][filter_num][batch_num], 
          double kernel[kernel_size][kernel_size][channel_num][filter_num])    
{

    // indices of 'for-loop'
    int ind,iC,iF,ii,jj,j,k,p,q;

    // padding
    int shape;
    shape=2*(kernel_size-1)+input_size;
    double padded_input[2*(kernel_size-1)+input_size][2*(kernel_size-1)+input_size][channel_num][batch_num]; 
    
    for (ind=0; ind<batch_num; ind++)
    {
        for (iC=0; iC<channel_num; iC++)
        {
            for (ii=0; ii<shape; ii++)
            {
                for (jj=0; jj<shape; jj++)
                {
                    if (ii>=kernel_size-1 && ii<kernel_size-1+input_size && jj>=kernel_size-1 && jj<kernel_size-1+input_size) 
                    {
                        padded_input[ii][jj][iC][ind]=input[ii-kernel_size+1][jj-kernel_size+1][iC][ind];
                    }
                    else padded_input[ii][jj][iC][ind]=0;
                }
            }
        }
    }


    // convolution
    int clen;
    clen=input_size+kernel_size-1;

    for (ind=0; ind<batch_num; ind++)
    {
        for (iF=0;iF<filter_num; iF++)
        {         
            for (j=0; j<clen; j++)
            {
                for (k=0; k<clen; k++)
                {
                    for (iC=0; iC<channel_num; iC++)   
                    {
                        for (p=0; p<kernel_size; p++)
                        {
                            for (q=0; q<kernel_size; q++)
                            {
                                output[j][k][iF][ind] += kernel[p][q][iC][iF]*padded_input[j-p+kernel_size-1][k-q+kernel_size-1][iC][ind]; 

                            }                       
                        }
                    }                 
                }                            
            }     
        }
    }  
}


