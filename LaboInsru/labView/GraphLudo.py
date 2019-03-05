import lvm_read as lvm
import numpy as np
import matplotlib
matplotlib.use("Tkagg")
from matplotlib import pyplot as plt
# from scipy import optimize

Fe = [50, 100, 150, 200,  1000]
#
phase = [4.4, 0.4, 0.8, 1, 2.8, 1.2, -0.1, 3.05, 2.5]
polyCut = [1, 140, 175, 420, 390, 250, 350, 400, 470]


def sinus(x, a, b, c, d):
    return a * np.sin(b*x + c) + d


def plotSignal():
    data2 = lvm.read('data/Fe_1000.lvm', read_from_pickle=False)
    tempsech2 = data2[0]['data'][:, 0]
    Vechantillon2 = data2[0]['data'][:, 1]
    plt.plot(tempsech2, Vechantillon2, label='Tension échantillonnée')
    plt.xlabel('Temps [s]')
    plt.ylabel('Tension [V]')
    plt.title('Signal échantillonné, partie 2 du laboratoire')
    plt.show()


def plotProcessedSignals():
    fig, axes = plt.subplots(1, 1, figsize=(17, 9))

    for i, F in enumerate(Fe):
        data1 = lvm.read('data/Fe' +  '_' + str(F) + '.lvm', read_from_pickle=False)
        tempsech = data1[0]['data'][:, 0]
        tempsech = tempsech[0:int(F * 0.1)]
        Vechantillon = data1[0]['data'][:, 1]
        Vechantillon = Vechantillon[0:int(F * 0.1)]
        tempsreconstruction = data1[0]['data'][:, 2]
        VreconstFourier = data1[0]['data'][:, 3]
        VreconstPolynomial = data1[0]['data'][:, 5]

        # a, b = i//3, i % 3
        a, b = 0, 0
        pCut = polyCut[i]

        params = [4.7, 6.28/0.01 * 1.009, phase[i], -0.4]
        xtheo = np.linspace(tempsech[0], tempsech[-1], 10000)
        axes[a, b].plot(xtheo, sinus(xtheo, params[0], params[1], params[2], params[3]), label='Théorique')

        RMS = []
        for T, V in zip([tempsreconstruction, tempsreconstruction[pCut: -pCut]], [VreconstFourier, VreconstPolynomial[pCut: -pCut]]):
            Vtheo = sinus(T, params[0], params[1], params[2], params[3])
            RMS.append(np.sqrt(1/len(Vtheo) * np.sum((Vtheo - V)**2)))

        axes[a, b].plot(tempsreconstruction, VreconstFourier, label='Fourier (RMS = {})'.format(round(RMS[0], 3)))
        axes[a, b].plot(tempsreconstruction[pCut: -pCut], VreconstPolynomial[pCut: -pCut], label='Polynomiale (RMS = {})'.format(round(RMS[1], 3)))
        axes[a, b].plot(tempsech, Vechantillon, '--', label='Échantillon')
        axes[a, b].set_ylim(-6, 6)
        axes[a, b].set_xlabel('Temps [s]')
        axes[a, b].set_ylabel('Tension [V]')
        axes[a, b].legend(loc='upper right', mode='expend', ncol=2)
        axes[a, b].set_title(str(F) + 'Hz')

        # plt.subplot(2, 1, 2)
        # plt.plot(tempsreconstruction, VreconstPolynomial, label='Reconstruction polynomiale')
        # plt.title('Dépassements de la reconstruction polynomiale')
        # plt.xlabel('Temps [s]')
        # plt.ylabel('Tension [V]')
        # plt.subplots_adjust(hspace=0.5)

    plt.tight_layout()
    plt.show()


def plotRmsSignal():
    fft = []
    XF = []
    Nt = []
    Fr = []
    Fv = []
    for i in range(5):
    #     i = 4
        F = Fe[i]
        pCut = polyCut[i]

        data1 = lvm.read('data/Fe' +  '_' + str(F) + '.lvm', read_from_pickle=False)
        tempsech = data1[0]['data'][:, 0]
        tempsech = tempsech[0:int(F * 0.1)]
        Vechantillon = data1[0]['data'][:, 1]
        Vechantillon = Vechantillon[0:int(F * 0.1)]
        tempsreconstruction = data1[0]['data'][:, 2]
        VreconstFourier = data1[0]['data'][:, 3]
        VreconstPolynomial = data1[0]['data'][:, 5]

        # params, params_covariance = optimize.curve_fit(sinus, tempsech, Vechantillon)
        params = [4.9, 6.28/0.01 * 1.0008, phase[i], -0.2]
        xtheo = np.linspace(tempsech[0], tempsech[-1], 10000)
        # plt.plot(xtheo, sinus(xtheo, params[0], params[1], params[2], params[3]), label='Théorique')

        RMS = []
        for T, V in zip([tempsreconstruction, tempsreconstruction[pCut: -pCut]], [VreconstFourier, VreconstPolynomial[pCut: -pCut]]):
            Vtheo = sinus(T, params[0], params[1], params[2], params[3])
            RMS.append(np.sqrt(1/len(Vtheo) * np.sum((Vtheo - V)**2)))



        import scipy.fftpack

        # Number of samplepoints
        N = len(tempsreconstruction)
        # sample spacing
        T = np.amax(tempsreconstruction) / N
        yf = scipy.fftpack.fft(VreconstFourier)
        yff = [i/np.amax(yf) for i in yf]

        xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))

        XF.append(xf)
        fft.append(yff)
        Nt.append(N)
        if i==4:
            N = len(tempsech)
            T = np.amax(tempsech) / N
            yf = scipy.fftpack.fft(Vechantillon)
            yff = yf/np.amax(yf)
            xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
            XF.append(xf)
            fft.append(yff)
            Nt.append(N)


    # plt.plot(tempsreconstruction, VreconstFourier,'-.', label='Fourier (RMS = {})'.format(round(RMS[0], 3)))
    # plt.plot(tempsreconstruction[pCut: -pCut], VreconstPolynomial[pCut: -pCut],'--', label='Polynomiale (RMS = {})'.format(round(RMS[1], 3)))
    # plt.plot(tempsech, Vechantillon, 'o', label='Échantillon')
    plt.plot(XF[0], np.abs(fft[0][:Nt[0]//2]),label='50Hz')
    plt.plot(XF[1], np.abs(fft[1][:Nt[1]//2]),label='100Hz')
    plt.plot(XF[2], np.abs(fft[2][:Nt[2]//2]),label='150Hz')
    plt.plot(XF[3], np.abs(fft[3][:Nt[3]//2]),label='200Hz')
    plt.plot(XF[4], np.abs(fft[4][:Nt[4]//2]),label='1000Hz')
    plt.plot(XF[5], np.abs(fft[5][:Nt[5]//2]),label='Théorique')




    plt.xlim(0, 200)
    plt.ylim(0,1)
    plt.ylabel('Intensité normalisée [-]')
    plt.xlabel('Fréquence [Hz]')
    plt.legend(loc='upper right', mode='expend', ncol=2)
    # plt.title(str(F) + 'Hz')

    plt.show()


# plotSignal()
# plotProcessedSignals()
plotRmsSignal()
