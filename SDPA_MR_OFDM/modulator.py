from SDPA_MR_OFDM.pn9 import pn9
from SDPA_OFDM import ofdm_modulator
import numpy as np
#from numpy import array

# FFT size as function of OFDM option
FFT_SIZE = {
    1: 128,
    2: 64,
    3: 32,
    4: 16}

# Shape of pilots for each
# Number of rows : pilots in a symbol
# Number of columns : amout of pilot sets (change of positions)
PILOTS_SHAPE = {
    1: (8, 13),
    2: (4, 7),
    3: (2, 7),
    4: (2, 4)}

# Position of pilots
# (See Table 153 page 88 of 802.15.4g)
# warning : The array is transposed (see .T at the end)
PILOTS_INDICES_OPTION_1 = np.array([
    [-38, -26, -14, -2, 10, 22, 34, 46],  # Set 1
    [-46, -34, -22, -10, 2, 14, 26, 38],  # Set 2
    [-42, -30, -18, -6, 6, 18, 30, 42],  # Set 3
    [-50, -38, -26, -14, -2, 10, 22, 50],  # Set 4
    [-46, -34, -22, -10, 2, 14, 34, 46],  # Set 5
    [-42, -30, -18, -6, 6, 18, 26, 38],  # Set 6
    [-50, -38, -26, -14, -2, 30, 42, 50],  # Set 7
    [-46, -34, -22, -10, 10, 22, 34, 46],  # Set 8
    [-42, -30, -18, -6, 2, 14, 26, 38],  # Set 9
    [-50, -38, -26,  6, 18, 30, 42, 50],  # Set 10
    [-46, -34, -14, -2, 10, 22, 34, 46],  # Set 11
    [-42, -30, -22, -10, 2, 14, 26, 38],  # Set 12
    [-50, -18, -6, 6, 18, 30, 42, 50]  # Set 13
]).T

# See table 154
PILOTS_INDICES_OPTION_2 = np.array([
    [-14, -2, 10, 22],  # Set 1
    [-22, -10, 2, 14],  # Set 2
    [-18, -67, 6, 18],  # Set 3
    [-26, -14, -2, 26],  # Set 4
    [-22, -10, 10, 22],  # Set 5
    [-18, -6, 2, 14],  # Set 6
    [-26,  6, 18, 26]  # Set 7
]).T

# See table 155
PILOTS_INDICES_OPTION_3 = np.array([
    [-7, 7],  # Set 1
    [-11, 3],  # Set 2
    [-3, 11],  # Set 3
    [-9, 5],  # Set 4
    [-5, 9],  # Set 5
    [-13, 1],  # Set 6
    [-1, 13]  # Set 7
])

# See table 156
PILOTS_INDICES_OPTION_4 = np.array([
    [-3, 5],  # Set 1
    [-7, 1],  # Set 2
    [-5, 3],  # Set 3
    [-1, 7]  # Set 4
])

# Pilots indices as a function of OFDM option
PILOTS_INDICES = {
    1: PILOTS_INDICES_OPTION_1,
    2: PILOTS_INDICES_OPTION_2,
    3: PILOTS_INDICES_OPTION_3,
    4: PILOTS_INDICES_OPTION_4}

# Modulation as a function of MCS (See table )
MODULATION = {
    0 : 'BPSK',
    1 : 'BPSK',
    2 : 'QPSK',
    3 : 'QPSK',
    4 : 'QPSK',
    5 : 'QAM16',
    6 : 'QAM16'
}

# Number of active tones (pilots + data) for each option
ACTIVE_TONES = {
    1 : 104,
    2 : 52,
    3 : 26,
    4 : 14
}

# Spacing between FFT channels (See 18.2 page 70)
SUB_CARRIER_SPACING = 31250/3 # Hz

class mr_ofdm_modulator():
    def __init__(self, MCS=0, OFDM_Option=1, verbose=False):
        """
        MR-OFDM Modulator

        Parameters
        ----------
        MCS : int
            Modulation coding scheme (0 - 7)
        OFDM_Option : int
            OFDM Option (1 - 4)
        verbose : bool
            if True, print additionnal information




        """
        # Check types and values
        if not isinstance(MCS, int):
            raise ValueError("MCS must be int")
        if not (0 <= MCS <= 7):
            raise ValueError(f"Invalid MCS value ({MCS} instead of [0 - 7])")
        if not isinstance(OFDM_Option, int):
            raise ValueError("OFDM_Option must be int")
        if not (1 <= OFDM_Option <= 4):
            raise ValueError(
                f"Invalid OFDM_Option ({OFDM_Option} instead of [1-4])")

        # Sets the pilots (PN9 sequence)
        pn9_inst = pn9(seed=0x1FF)
        pn9_sequence = np.array(pn9_inst.nextN(
            np.prod(PILOTS_SHAPE[OFDM_Option])))
        pilots = pn9_sequence.reshape(PILOTS_SHAPE[OFDM_Option], order='F')

        # Sets the padding (one less on the right than on the left because of the DC tone)
        padding = (FFT_SIZE[OFDM_Option] - ACTIVE_TONES[OFDM_Option]) // 2

        # Instanciate OFDM modulator from SDPA_OFDM package
        self.ofdm_modulator = ofdm_modulator(
            N_FFT=FFT_SIZE[OFDM_Option],
            BW = SUB_CARRIER_SPACING * (FFT_SIZE[OFDM_Option]-1) / 2,
            modulation=MODULATION[MCS],
            padding_left=padding,
            padding_right=padding - 1, 
            pilots_indices=PILOTS_INDICES[OFDM_Option],
            pilots=pilots,
            rate=None, #todo
            rep=None, #todo
            MSB_first=True, # TODO : find in the specs if this is valid
            verbose=verbose)
