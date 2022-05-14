
# Import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Function to perform histogram stretching and reshaping of the data !!! Remember to change the dimensions to fit the data !!!
def histogram_stretch(img):
    ''' Perform histogram stretching on the image '''
    m = img.shape[0]
    n = img.shape[1]
    new_img = np.empty([m, n])
    new_img = (((img - np.min(img))/(np.max(img)-np.min(img)))*256) + 0.5
    return new_img


def reshape_rows(full_array, filtermask, borderType, shape=(32,16)):
    ''' Reshape the data to a image. Remember to change the dimensions to fit the data !!!
    Filter the image and perform histogram stretching '''
    return_array = []
    for i in range(len(full_array)):
        img = np.reshape(full_array[i],shape) # must be changed to fitting dimensions
        Imoutput = cv2.filter2D(img,ddepth=-1,kernel=(filtermask*filtermask.T),borderType=borderType)
        return_array.append(Imoutput)
    
    return_array = np.array(return_array)
    for i in range(len(return_array)):
        return_array[i] = histogram_stretch(return_array[i])
    
    return return_array

def plot_FFT(img, side='left'):
    dft = np.fft.fft2(img)
    fshift = np.fft.fftshift(dft)
    
    angledft=np.angle(dft)
    abso=np.abs(np.log10(dft))

    plt.figure(figsize=(15,5))
    plt.subplot(211)
    plt.imshow(angledft)
    plt.title('Phase')
    plt.subplot(212)
    plt.imshow(abso)
    plt.title('Magnitude')
    plt.subplots_adjust(hspace=0.3)
    plt.suptitle(f'FFT of mean image of {side} leaning sites')
    plt.show()
    plt.savefig(f'fftmean_{side}_pages.png')

if __name__ == '__main__':
    # Test the functions
    img = np.random.rand(32,16)
    print(img)
    print(reshape_rows(img,np.ones((3,3)),cv2.BORDER_REPLICATE))
