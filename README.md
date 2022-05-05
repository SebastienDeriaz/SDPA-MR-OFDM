# SDPA-MR-OFDM
MR-OFDM Modulator (HES-SO Master, PA 2022)


This package adds another layer on top of the SDPA-OFDM package to support MR-OFDM specifications. These specifications are given by 802.15.4g


## Installation

The package can be installed from pip

	pip install SDPA-MR-OFDM

## Usage


Instanciate a MR-OFDM modulator

	from SDPA_MR_OFDM import mr_ofdm_modulator
	
	mod = mr_ofdm_modulator(MCS=3, OFDM_Option=2, phyOFDMInterleaving=1)
	
Generate I and Q signals from a message (message must be a list of bits)

	I, Q, f = mod.messageToIQ(message)

f is the frequency of I and Q, this is useful for implementing in a vector signal generator

## Validation

The current protocol has been tested with all tables from the MR-OFDM example (annex M of the 802.15.4g specifications).

The table M.11 (complete package in the time domain) shows no error (up to a rounding of 4 decimals due to table being in PDF format)

## Current version : 1.0.0

The system is operational and agrees with 802.15.4g examples