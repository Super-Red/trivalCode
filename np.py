import numpy as np
import time
# import matplotlib.pyplot as plt
import csv
from scipy import fftpack

def returnPrime(n):
    is_prime = np.ones((n,), dtype=bool)

    # cross out 0 and 1
    is_prime[:2] = 0

    # for each integer j starting from 2, cross out its higher multiples:
    N_max = int(np.sqrt(len(is_prime)))
    for j in range(2, N_max):
        is_prime[2*j::j] = 0

def loadtxt():
    data = np.loadtxt("data.csv", delimiter=",", usecols=([0, 1, 2, 3]))
    name = np.loadtxt("data.csv", delimiter=",", usecols=([4]), dtype=np.str)
    
    data2 = np.zeros((6,), dtype=[("sepal_length", float),("sepal_width", float), ("petal_length", float), ("petal_width", float), ("Iris", "U13")])
    data2 = data + name
    
    sepal_length, sepal_width, petal_length, petal_width = data.T

def plotLines():
    x = np.linspace(0, 1, 20)
    y = np.cos(x) + 0.3*np.random.rand(20)
    p = np.poly1d(np.polyfit(x, y, 3))
    t = np.linspace(0, 1, 200)
    plt.plot(x, y, "o", t, p(t), "-")

# a = np.genfromtxt(StringIO("data.csv"), delimiter=",")

def simplePlot():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    plt.plot(X, C)
    plt.plot(X, S)

    plt.show()

def Mandelbrot(N_max=50, threshold=50):
    N = 500
    x = np.linspace(-2, 1, N)
    y = np.linspace(-1.5, 1.5, N)[:,np.newaxis]
    c = x + 1j*y
    z = np.zeros(N**2).reshape(N, N)
    for j in range(N_max):
        z = z**2 + c
    mask = abs(z) < threshold
    plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig("mandelbrot.png")
    print("Done!")

def fourierTransforms():
    time_step = 0.02
    period = 5
    time_vec = np.arange(0, 20, time_step)
    sig = np.sin(2 * np.pi/period * time_vec) + 0.5 * np.random.randn(time_vec.size)

    sample_freq = fftpack.fftfreq(sig.size, d=time_step) #频率
    sig_fft = fftpack.fft(sig)          #离散傅立叶变化

    pidxs = np.where(sample_freq > 0)   #去掉负频率
    freqs = sample_freq[pidxs]          #freqs就是所有的正频率
    power = np.abs(sig_fft)[pidxs]      #power看的是正频率里的正弦的振幅

    freq = freqs[power.argmax()]        #通过power来取出临界的的频率，要过滤的频率

    # Now the high-frequency noise will be removed from the Fourier transformed signal:
    sig_fft[np.abs(sample_freq) != freq] = 0    #对离散变换后的信号进行滤波

    main_sig = fftpack.ifft(sig_fft)

    plt.plot(time_vec, sig)
    plt.plot(time_vec, main_sig, linewidth=5)
    plt.show()

print("Done!")


