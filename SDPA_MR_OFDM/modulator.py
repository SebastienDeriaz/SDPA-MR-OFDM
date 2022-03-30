from SDPA_MR_OFDM.pn9 import pn9
from SDPA_OFDM import ofdm_modulator
from SDPA_MR_OFDM.rate_encoder import rate_one_half, rate_three_quarter
from SDPA_MR_OFDM.fields import PHR
import numpy as np


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
    [-18, -6, 6, 18],  # Set 3
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

# See Table 140
STF_OPTION_1 = np.zeros(FFT_SIZE[1])
STF_OPTION_1[np.array([-48, -40, -32, -24, -16, -8, 8, 16,
                      24, 32, 40, 48])+STF_OPTION_1.size//2] = np.sqrt(104/12)

# See Table 141
STF_OPTION_2 = np.zeros(FFT_SIZE[2])
STF_OPTION_2[np.array([-24, -20, -16, 8, 20]) +
             STF_OPTION_2.size//2] = -np.sqrt(52/12)
STF_OPTION_2[np.array([-12, -8, -4, 4, 12, 16, 24]) +
             STF_OPTION_2.size//2] = np.sqrt(52/12)

# See Table 142
STF_OPTION_3 = np.zeros(FFT_SIZE[3])
STF_OPTION_3[np.array([-12, -8, -4, 4, 8, 12]) +
             STF_OPTION_3.size//2] = np.sqrt(26/6)

# See Table 143
STF_OPTION_4 = np.zeros(FFT_SIZE[4])
STF_OPTION_4[np.array([-6, -4, -2, 2, 4, 6]) +
             STF_OPTION_4.size//2] = np.sqrt(14/6)

# The square roots are due to Power Boosting (See 18.2.1.1.4)

STF = {
    1: STF_OPTION_1,
    2: STF_OPTION_2,
    3: STF_OPTION_3,
    4: STF_OPTION_4
}
# Modulation as a function of MCS (See table )
MODULATION = {
    0: 'BPSK',
    1: 'BPSK',
    2: 'QPSK',
    3: 'QPSK',
    4: 'QPSK',
    5: 'QAM16',
    6: 'QAM16'
}

N_BPSC = {
    0: 1,
    1: 1,
    2: 2,
    3: 2,
    4: 2,
    5: 4,
    6: 4
}

RATE = {
    0: "1/2",
    1: "1/2",
    2: "1/2",
    3: "1/2",
    4: "3/4",
    5: "1/2",
    6: "3/4"
}

# Modulation factor (See table 149)
K_MOD = {
    'BPSK': 1,
    'QPSK': 1/np.sqrt(2),
    'QAM16': 1/np.sqrt(10)
}

# Number of active tones (pilots + data) for each option
ACTIVE_TONES = {
    1: 104,
    2: 52,
    3: 26,
    4: 14
}

# Frequency spreading depending on MCS
FREQUENCY_SPREADING = {
    0: 4,
    1: 2,
    2: 2,
    3: 1,
    4: 1,
    5: 1,
    6: 1
}


# Valid MCS - OFDM option combinations (see table 148 page 80)
VALID_MCS_OFDM_COMBINATIONS = (
    (True, True, False, False),
    (True, True, True, False),
    (True, True, True, True),
    (True, True, True, True),
    (False, True, True, True),
    (False, True, True, True),
    (False, False, True, True),
)


# Spacing between FFT channels (See 18.2 page 70)
SUB_CARRIER_SPACING = 31250/3  # Hz

# Long training fields (LTF) subcarriers
# LTF1 -> 128 elements
LTF_1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1,
                 1, 1, 0, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# LTF2 -> 64 elements
LTF_2 = np.array([0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -
                 1, -1, 0, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 0, 0, 0, 0, 0])
# LTF3 -> 32 elements
LTF_3 = np.array([0, 0, 0, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1,
                 1, -1, 0, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 0, 0])
# LTF4 -> 16 elements
LTF_4 = np.array([0, 1, -1, 1, 1, -1, 1, 1, 0, -1, 1, 1, 1, -1, -1, -1])

LTF = {
    1: LTF_1,
    2: LTF_2,
    3: LTF_3,
    4: LTF_4
}


class mr_ofdm_modulator():
    def __init__(self, MCS=0, OFDM_Option=1, phyOFDMInterleaving = 0, scrambler = 0, verbose=False):
        """
        MR-OFDM Modulator

        Parameters
        ----------
        MCS : int
            Modulation coding scheme (0 - 7)
        OFDM_Option : int
            OFDM Option (1 - 4)
        phyOFDMInterleaving : int (0 or 1)
            Interleaving depth. 0 means an interleaving depth of one. 1 means an interleaving depth of the number of symbols equal to the frequency domain spreading factor
        scrambler : int
            Scrambler value (0-3). See 18.2.3.11
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
        if not VALID_MCS_OFDM_COMBINATIONS[MCS][OFDM_Option]:
            raise ValueError(
                f"Invalid MCS ({MCS})- OFDM Option combination ({OFDM_Option})")
        if not isinstance(phyOFDMInterleaving, int):
            raise ValueError("Invalid phyOFDMInterleaving type")
        if not phyOFDMInterleaving in [0, 1]:
            raise ValueError("Invalid phyOFDMInterleaving value")
        if not isinstance(scrambler, int):
            raise ValueError("Invalid scrambler type. Must be int")
        if not (0 <= scrambler <= 3):
            raise ValueError("Invalid scrambler value (0 <= scrambler <= 3)")

        
        
        self._phyOFDMInterleaving = phyOFDMInterleaving
        self._scrambler = scrambler
        self._OFDM_Option = OFDM_Option
        self._verbose = verbose
        self._MCS = MCS

        self._print_verbose(f"Instanciating a modulator with OFDM Option = {OFDM_Option} and MCS = {MCS}")

        # Sets the pilots (PN9 sequence)
        pn9_inst = pn9(seed=0x1FF)
        pn9_sequence = np.array(pn9_inst.nextN(
            np.prod(PILOTS_SHAPE[OFDM_Option])))
        pilots = pn9_sequence.reshape(PILOTS_SHAPE[OFDM_Option], order='F')

        # Sets the padding (one less on the right than on the left because of the DC tone)
        padding = (FFT_SIZE[OFDM_Option] - ACTIVE_TONES[OFDM_Option]) // 2

        # Instanciate OFDM modulator from SDPA_OFDM package
        # self.ofdm_modulator = ofdm_modulator(
        #     N_FFT=FFT_SIZE[OFDM_Option],
        #     BW=SUB_CARRIER_SPACING * (FFT_SIZE[OFDM_Option]-1) / 2,
        #     modulation=MODULATION[MCS],
        #     modulation_factor=K_MOD[MODULATION[MCS]],
        #     padding_left=padding,
        #     padding_right=padding - 1,
        #     pilots_indices=PILOTS_INDICES[OFDM_Option],
        #     pilots=pilots,
        #     frequency_spreading=FREQUENCY_SPREADING[MCS],
        #     MSB_first=False,  # 18.2.1
        #     verbose=verbose)

    def _STF(self):
        """
        Generates STF signal (as I and Q)
        The second half of the fourth symbol is inverted in the time domain :

          symbol 1   symbol 2   symbol 3   symbol 4
        |CP++++++++|CP++++++++|CP++++++++|CP++++----|

        +  : samples of the symbol (after IFFT)
        CP : cyclic prefix
        -  : negated samples

        Returns
        -------
        I : ndarray
            Real part of the signal
        Q : ndarray
            Imaginary part of the signal
        """
        self._print_verbose("Creating STF....")
        self._print_verbose(
        """
          symbol 1   symbol 2   symbol 3   symbol 4
        |CP++++++++|CP++++++++|CP++++++++|CP++++----|

        +  : samples of the symbol (after IFFT)
        CP : cyclic prefix
        -  : negated samples (end of fourth symbol)
        """)

        STF_CP = 1/4
        # OFDM modulator for the STF symbols specifically
        mod = ofdm_modulator(N_FFT=FFT_SIZE[self._OFDM_Option], CP=STF_CP)

        # Time domain STF symbol with cyclic prefix
        STF_I, STF_Q, _ = mod.subcarriersToIQ(STF[self._OFDM_Option])
        STF_time_domain = (STF_I + STF_Q * 1j).squeeze()
        # Fourth symbol (inverted end)
        STF_time_domain_fourth = STF_time_domain * \
            np.block([np.ones(STF_time_domain.size // 5 * 3),
                     -np.ones(STF_time_domain.size // 5 * 2)])
        # Create the signal with the four symbols
        signal = np.block([STF_time_domain, STF_time_domain,
                          STF_time_domain, STF_time_domain_fourth])
        I, Q = signal.real, signal.imag

        self._print_verbose(f"    STF signal is {signal.size} elements")

        return I, Q

    def _LTF(self):
        """
        Generates Long Training Field (LTF) signal in the time domain

        The LTF contains a double-size cyclic prefix (CP) at the beginning and two LTF symbols.
        The CP is calculated on the second half of the first symbol (both symbols are identical anyway)
        The time domain signal looks something like this :

        |CP----|----|

        Returns
        -------
        I : ndarray
            Real part of the signal
        Q : ndarray
            Imaginary part of the signal
        """
        self._print_verbose("Generating LTF...")
        self._print_verbose("    LTF signal looks like : |CP----|----|")

        # OFDM modulator for the LTF excusively. No padding because we will add it manually
        mod = ofdm_modulator(N_FFT=FFT_SIZE[self._OFDM_Option], CP=0)
        # LTF signal without cyclic prefix (CP)
        LTF_I, LTF_Q, _ = mod.subcarriersToIQ(LTF[self._OFDM_Option])
        LTF_signal = (LTF_I + 1j*LTF_Q).squeeze()
        # Create the cyclic prefix (second half of the first symbol)
        CP = LTF_signal[LTF_signal.size//2:]
        # Create the complete signal
        signal = np.block([CP, LTF_signal, LTF_signal])
        I, Q = signal.real, signal.imag

        self._print_verbose(f"    LTF signal is {signal.size} elements")

        return I, Q

    def _encoder(self, x):
        """
        Applies encoding to the given signal
        See 18.2.3.4

        Rate is 1/2 or 3/4 depending on MCS value

        Parameters
        ----------
        x : ndarray
            Input signal
        
        Returns
        -------
        x_encoded : ndarray
            Encoded signal
        """
        if RATE[self._MCS] == "1/2":
            # Rate 1/2
            encoder = rate_one_half()
        else:
            # Rate 3/4
            encoder = rate_three_quarter()

        _, _, x_encoded = encoder.sequence()

    def _interleaver(self, x):
        """
        Applies interleaver to the given signal
        See 18.2.3.5
        
        Parameters
        ----------
        x : ndarray
            Input signal
        
        Returns
        -------
        x_interleaved : ndarray
            Interleaved signal
        """
        SF = FREQUENCY_SPREADING[self._MCS]
        N_FFT = FFT_SIZE[self._OFDM_Option]
        N_bpsc = N_BPSC[self._MCS]

        if self._phyOFDMInterleaving == 0:
            # interleaving depth of 1
            N_cbps = N_FFT * N_bpsc / SF * (3/4)
        else:
            # interleaving depth of SF
            # See table
            N_cbps = N_FFT * N_bpsc * (3/4)
            # NOTE: //1 gives the right result but it should be //SF
            N_row = 12 // 1

        k = np.arange(N_cbps, dtype=int)
        i = ((N_cbps / N_row) * (np.mod(k, N_row)) + np.floor(k / N_row)).astype(int)

        s = np.max([1, N_bpsc/2])
        j = (s * np.floor(i / s) + np.mod(i + N_cbps - np.floor(N_row * i / N_cbps), s)).astype(int)

        ij = i[j]

        x_interleaved = np.zeros_like(x)
        for s in range(x.size // k.size):
            x_interleaved[s*k.size + ij] = x_interleaved[s*k.size + k]

        return x_interleaved


    def messageToIQ(self, message):
        """
        Encodes the given message with MR-OFDM modulator

        Parameters
        ----------
        message : ndarray
            Message to encode

        Returns
        -------
        I : ndarray
            Real part of the signal
        Q : ndarray
            Imaginary part of the signal
        """
        # Generate STF
        STF_I, STF_Q = self._STF()
        # Generate LTF
        LTF_I, LTF_Q = self._LTF()

        # Generate header
        # TODO : set length correctly
        PHY_HEADER = PHR(rate=self._MCS, length=1, scrambler=self._scrambler)

        



        return I, Q

    

    def _print_verbose(self, message: str):
        """
        Prints additionnal information if the verbose flag is True
        """
        if(self._verbose):
            print(message)
