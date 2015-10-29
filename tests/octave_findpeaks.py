#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from vector import vector, plot_peaks
from oct2py import octave

# Load the Octage-Forge signal package.
octave.eval("pkg load signal")

print('Detect peaks without any filters.')
(_, indices) = octave.findpeaks(np.array(vector), 'DoubleSided',
    'MinPeakHeight', 0, 'MinPeakDistance', 0, 'MinPeakWidth', 0)
# Convert peak indices to integer.
indices = indices[0].astype(int) - 1
print('Peaks are: %s' % (indices))
plot_peaks(np.array(vector), indices,
    algorithm='Octave-Forge findpeaks')

print('Detect peaks with minimum height and distance filters.')
(pks, indices) = octave.findpeaks(np.array(vector), 'DoubleSided',
    'MinPeakHeight', 6, 'MinPeakDistance', 2, 'MinPeakWidth', 0)
# Convert peak indices to integer.
indices = indices[0].astype(int) - 1
print('Peaks are: %s' % (indices))
plot_peaks(np.array(vector), indices, mph=6, mpd=2,
    algorithm='Octave-Forge findpeaks')