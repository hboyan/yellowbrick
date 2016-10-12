# yellowbrick.style.palettes
# Implements the variety of colors that yellowbrick allows access to by name.
#
# Author:   Patrick O'Melveny <pvomelveny@gmail.com>
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Contributor: Haley Boyan <hboyan@gmail.com>
# Created:  Tue Oct 04 15:30:15 2016 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: palettes.py [] pvomelveny@gmail.com $

"""
Implements the variety of colors that yellowbrick allows access to by name.
This code was originally based on Seaborn's rcmody.py but has since been
cleaned up to be Yellowbrick-specific and to dereference tools we don't use.

Note that these functions alter the matplotlib rc dictionary on the fly.
"""

##########################################################################
## Imports
##########################################################################

from __future__ import division
from itertools import cycle

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcol

from six import string_types
from six.moves import range

from .colors import get_color_cycle
from yellowbrick.exceptions import YellowbrickValueError

##########################################################################
## Exports
##########################################################################

__all__ = ["color_palette", "set_color_codes"]


##########################################################################
## Special, Named Colors
##########################################################################

YB_KEY = '#111111'  # The yellowbrick key (black) color is very dark grey


##########################################################################
## Color Palettes
## Note all 6/7 color palettes can be mapped to bgrmyck color codes
## via the `set_color_codes` function, make sure they are ordered!
##########################################################################

PALETTES = {
    # "name": ['blue', 'green', 'red', 'maroon', 'yellow', 'cyan']
    # The yellowbrick default palette
    "yellowbrick": ['#0272a2', '#9fc377', '#ca0b03', '#a50258', '#d7c703', '#88cada'],

    # The following are from ColorBrewer
    "Accent-3": ['#7FC97F', '#BEAED4', '#FDC086']
    "Accent-4": ['#7FC97F', '#BEAED4', '#FDC086', '#FFFF99']
    "Accent-5": ['#7FC97F', '#BEAED4', '#FDC086', '#FFFF99', '#386CB0']
    "Accent-6": ['#7FC97F', '#BEAED4', '#FDC086', '#FFFF99', '#386CB0', '#F0027F']
    "Accent-7": ['#7FC97F', '#BEAED4', '#FDC086', '#FFFF99', '#386CB0', '#F0027F', '#BF5B17']
    "Accent-8": ['#7FC97F', '#BEAED4', '#FDC086', '#FFFF99', '#386CB0', '#F0027F', '#BF5B17', '#666666']
    "Blues-3": ['#DEEBF7', '#9ECAE1', '#3182BD']
    "Blues-4": ['#EFF3FF', '#BDD7E7', '#6BAED6', '#2171B5']
    "Blues-5": ['#EFF3FF', '#BDD7E7', '#6BAED6', '#3182BD', '#08519C']
    "Blues-6": ['#EFF3FF', '#C6DBEF', '#9ECAE1', '#6BAED6', '#3182BD', '#08519C']
    "Blues-7": ['#EFF3FF', '#C6DBEF', '#9ECAE1', '#6BAED6', '#4292C6', '#2171B5', '#084594']
    "Blues-8": ['#F7FBFF', '#DEEBF7', '#C6DBEF', '#9ECAE1', '#6BAED6', '#4292C6', '#2171B5', '#084594']
    "Blues-9": ['#F7FBFF', '#DEEBF7', '#C6DBEF', '#9ECAE1', '#6BAED6', '#4292C6', '#2171B5', '#08519C', '#08306B']
    "BrBG-10": ['#543005', '#8C510A', '#BF812D', '#DFC27D', '#F6E8C3', '#C7EAE5', '#80CDC1', '#35978F', '#01665E', '#003C30']
    "BrBG-11": ['#543005', '#8C510A', '#003C30', '#BF812D', '#DFC27D', '#F6E8C3', '#F5F5F5', '#C7EAE5', '#80CDC1', '#35978F', '#01665E']
    "BrBG-3": ['#D8B365', '#F5F5F5', '#5AB4AC']
    "BrBG-4": ['#A6611A', '#DFC27D', '#80CDC1', '#018571']
    "BrBG-5": ['#A6611A', '#DFC27D', '#F5F5F5', '#80CDC1', '#018571']
    "BrBG-6": ['#8C510A', '#D8B365', '#F6E8C3', '#C7EAE5', '#5AB4AC', '#01665E']
    "BrBG-7": ['#8C510A', '#D8B365', '#F6E8C3', '#F5F5F5', '#C7EAE5', '#5AB4AC', '#01665E']
    "BrBG-8": ['#8C510A', '#BF812D', '#DFC27D', '#F6E8C3', '#C7EAE5', '#80CDC1', '#35978F', '#01665E']
    "BrBG-9": ['#8C510A', '#BF812D', '#DFC27D', '#F6E8C3', '#F5F5F5', '#C7EAE5', '#80CDC1', '#35978F', '#01665E']
    "BuGn-3": ['#E5F5F9', '#99D8C9', '#2CA25F']
    "BuGn-4": ['#EDF8FB', '#B2E2E2', '#66C2A4', '#238B45']
    "BuGn-5": ['#EDF8FB', '#B2E2E2', '#66C2A4', '#2CA25F', '#006D2C']
    "BuGn-6": ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#2CA25F', '#006D2C']
    "BuGn-7": ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824']
    "BuGn-8": ['#F7FCFD', '#E5F5F9', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824']
    "BuGn-9": ['#F7FCFD', '#E5F5F9', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B']
    "BuPu-3": ['#E0ECF4', '#9EBCDA', '#8856A7']
    "BuPu-4": ['#EDF8FB', '#B3CDE3', '#8C96C6', '#88419D']
    "BuPu-5": ['#EDF8FB', '#B3CDE3', '#8C96C6', '#8856A7', '#810F7C']
    "BuPu-6": ['#EDF8FB', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8856A7', '#810F7C']
    "BuPu-7": ['#EDF8FB', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#6E016B']
    "BuPu-8": ['#F7FCFD', '#E0ECF4', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#6E016B']
    "BuPu-9": ['#F7FCFD', '#E0ECF4', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#810F7C', '#4D004B']
    "Dark2-3": ['#1B9E77', '#D95F02', '#7570B3']
    "Dark2-4": ['#1B9E77', '#D95F02', '#7570B3', '#E7298A']
    "Dark2-5": ['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E']
    "Dark2-6": ['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02']
    "Dark2-7": ['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D']
    "Dark2-8": ['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D', '#666666']
    "GnBu-3": ['#E0F3DB', '#A8DDB5', '#43A2CA']
    "GnBu-4": ['#F0F9E8', '#BAE4BC', '#7BCCC4', '#2B8CBE']
    "GnBu-5": ['#F0F9E8', '#BAE4BC', '#7BCCC4', '#43A2CA', '#0868AC']
    "GnBu-6": ['#F0F9E8', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#43A2CA', '#0868AC']
    "GnBu-7": ['#F0F9E8', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E']
    "GnBu-8": ['#F7FCF0', '#E0F3DB', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E']
    "GnBu-9": ['#F7FCF0', '#E0F3DB', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#0868AC', '#084081']
    "Greens-3": ['#E5F5E0', '#A1D99B', '#31A354']
    "Greens-4": ['#EDF8E9', '#BAE4B3', '#74C476', '#238B45']
    "Greens-5": ['#EDF8E9', '#BAE4B3', '#74C476', '#31A354', '#006D2C']
    "Greens-6": ['#EDF8E9', '#C7E9C0', '#A1D99B', '#74C476', '#31A354', '#006D2C']
    "Greens-7": ['#EDF8E9', '#C7E9C0', '#A1D99B', '#74C476', '#41AB5D', '#238B45', '#005A32']
    "Greens-8": ['#F7FCF5', '#E5F5E0', '#C7E9C0', '#A1D99B', '#74C476', '#41AB5D', '#238B45', '#005A32']
    "Greens-9": ['#F7FCF5', '#E5F5E0', '#C7E9C0', '#A1D99B', '#74C476', '#41AB5D', '#238B45', '#006D2C', '#00441B']
    "Greys-3": ['#F0F0F0', '#BDBDBD', '#636363']
    "Greys-4": ['#F7F7F7', '#CCCCCC', '#969696', '#525252']
    "Greys-5": ['#F7F7F7', '#CCCCCC', '#969696', '#636363', '#252525']
    "Greys-6": ['#F7F7F7', '#D9D9D9', '#BDBDBD', '#969696', '#636363', '#252525']
    "Greys-7": ['#F7F7F7', '#D9D9D9', '#BDBDBD', '#969696', '#737373', '#525252', '#252525']
    "Greys-8": ['#FFFFFF', '#F0F0F0', '#D9D9D9', '#BDBDBD', '#969696', '#737373', '#525252', '#252525']
    "Greys-9": ['#FFFFFF', '#F0F0F0', '#D9D9D9', '#BDBDBD', '#969696', '#737373', '#525252', '#252525', '#000000']
    "OrRd-3": ['#FEE8C8', '#FDBB84', '#E34A33']
    "OrRd-4": ['#FEF0D9', '#FDCC8A', '#FC8D59', '#D7301F']
    "OrRd-5": ['#FEF0D9', '#FDCC8A', '#FC8D59', '#E34A33', '#B30000']
    "OrRd-6": ['#FEF0D9', '#FDD49E', '#FDBB84', '#FC8D59', '#E34A33', '#B30000']
    "OrRd-7": ['#FEF0D9', '#FDD49E', '#FDBB84', '#FC8D59', '#EF6548', '#D7301F', '#990000']
    "OrRd-8": ['#FFF7EC', '#FEE8C8', '#FDD49E', '#FDBB84', '#FC8D59', '#EF6548', '#D7301F', '#990000']
    "OrRd-9": ['#FFF7EC', '#FEE8C8', '#FDD49E', '#FDBB84', '#FC8D59', '#EF6548', '#D7301F', '#B30000', '#7F0000']
    "Oranges-3": ['#FEE6CE', '#FDAE6B', '#E6550D']
    "Oranges-4": ['#FEEDDE', '#FDBE85', '#FD8D3C', '#D94701']
    "Oranges-5": ['#FEEDDE', '#FDBE85', '#FD8D3C', '#E6550D', '#A63603']
    "Oranges-6": ['#FEEDDE', '#FDD0A2', '#FDAE6B', '#FD8D3C', '#E6550D', '#A63603']
    "Oranges-7": ['#FEEDDE', '#FDD0A2', '#FDAE6B', '#FD8D3C', '#F16913', '#D94801', '#8C2D04']
    "Oranges-8": ['#FFF5EB', '#FEE6CE', '#FDD0A2', '#FDAE6B', '#FD8D3C', '#F16913', '#D94801', '#8C2D04']
    "Oranges-9": ['#FFF5EB', '#FEE6CE', '#FDD0A2', '#FDAE6B', '#FD8D3C', '#F16913', '#D94801', '#A63603', '#7F2704']
    "PRGn-10": ['#40004B', '#762A83', '#9970AB', '#C2A5CF', '#E7D4E8', '#D9F0D3', '#A6DBA0', '#5AAE61', '#1B7837', '#00441B']
    "PRGn-11": ['#40004B', '#762A83', '#00441B', '#9970AB', '#C2A5CF', '#E7D4E8', '#F7F7F7', '#D9F0D3', '#A6DBA0', '#5AAE61', '#1B7837']
    "PRGn-3": ['#AF8DC3', '#F7F7F7', '#7FBF7B']
    "PRGn-4": ['#7B3294', '#C2A5CF', '#A6DBA0', '#008837']
    "PRGn-5": ['#7B3294', '#C2A5CF', '#F7F7F7', '#A6DBA0', '#008837']
    "PRGn-6": ['#762A83', '#AF8DC3', '#E7D4E8', '#D9F0D3', '#7FBF7B', '#1B7837']
    "PRGn-7": ['#762A83', '#AF8DC3', '#E7D4E8', '#F7F7F7', '#D9F0D3', '#7FBF7B', '#1B7837']
    "PRGn-8": ['#762A83', '#9970AB', '#C2A5CF', '#E7D4E8', '#D9F0D3', '#A6DBA0', '#5AAE61', '#1B7837']
    "PRGn-9": ['#762A83', '#9970AB', '#C2A5CF', '#E7D4E8', '#F7F7F7', '#D9F0D3', '#A6DBA0', '#5AAE61', '#1B7837']
    "Paired-10": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6', '#6A3D9A']
    "Paired-11": ['#A6CEE3', '#1F78B4', '#FFFF99', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6', '#6A3D9A']
    "Paired-12": ['#A6CEE3', '#1F78B4', '#FFFF99', '#B15928', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6', '#6A3D9A']
    "Paired-3": ['#A6CEE3', '#1F78B4', '#B2DF8A']
    "Paired-4": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C']
    "Paired-5": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99']
    "Paired-6": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C']
    "Paired-7": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F']
    "Paired-8": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00']
    "Paired-9": ['#A6CEE3', '#1F78B4', '#B2DF8A', '#33A02C', '#FB9A99', '#E31A1C', '#FDBF6F', '#FF7F00', '#CAB2D6']
    "Pastel1-3": ['#FBB4AE', '#B3CDE3', '#CCEBC5']
    "Pastel1-4": ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4']
    "Pastel1-5": ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6']
    "Pastel1-6": ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6', '#FFFFCC']
    "Pastel1-7": ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6', '#FFFFCC', '#E5D8BD']
    "Pastel1-8": ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6', '#FFFFCC', '#E5D8BD', '#FDDAEC']
    "Pastel1-9": ['#FBB4AE', '#B3CDE3', '#CCEBC5', '#DECBE4', '#FED9A6', '#FFFFCC', '#E5D8BD', '#FDDAEC', '#F2F2F2']
    "Pastel2-3": ['#B3E2CD', '#FDCDAC', '#CBD5E8']
    "Pastel2-4": ['#B3E2CD', '#FDCDAC', '#CBD5E8', '#F4CAE4']
    "Pastel2-5": ['#B3E2CD', '#FDCDAC', '#CBD5E8', '#F4CAE4', '#E6F5C9']
    "Pastel2-6": ['#B3E2CD', '#FDCDAC', '#CBD5E8', '#F4CAE4', '#E6F5C9', '#FFF2AE']
    "Pastel2-7": ['#B3E2CD', '#FDCDAC', '#CBD5E8', '#F4CAE4', '#E6F5C9', '#FFF2AE', '#F1E2CC']
    "Pastel2-8": ['#B3E2CD', '#FDCDAC', '#CBD5E8', '#F4CAE4', '#E6F5C9', '#FFF2AE', '#F1E2CC', '#CCCCCC']
    "PiYG-10": ['#8E0152', '#C51B7D', '#DE77AE', '#F1B6DA', '#FDE0EF', '#E6F5D0', '#B8E186', '#7FBC41', '#4D9221', '#276419']
    "PiYG-11": ['#8E0152', '#C51B7D', '#276419', '#DE77AE', '#F1B6DA', '#FDE0EF', '#F7F7F7', '#E6F5D0', '#B8E186', '#7FBC41', '#4D9221']
    "PiYG-3": ['#E9A3C9', '#F7F7F7', '#A1D76A']
    "PiYG-4": ['#D01C8B', '#F1B6DA', '#B8E186', '#4DAC26']
    "PiYG-5": ['#D01C8B', '#F1B6DA', '#F7F7F7', '#B8E186', '#4DAC26']
    "PiYG-6": ['#C51B7D', '#E9A3C9', '#FDE0EF', '#E6F5D0', '#A1D76A', '#4D9221']
    "PiYG-7": ['#C51B7D', '#E9A3C9', '#FDE0EF', '#F7F7F7', '#E6F5D0', '#A1D76A', '#4D9221']
    "PiYG-8": ['#C51B7D', '#DE77AE', '#F1B6DA', '#FDE0EF', '#E6F5D0', '#B8E186', '#7FBC41', '#4D9221']
    "PiYG-9": ['#C51B7D', '#DE77AE', '#F1B6DA', '#FDE0EF', '#F7F7F7', '#E6F5D0', '#B8E186', '#7FBC41', '#4D9221']
    "PuBu-3": ['#ECE7F2', '#A6BDDB', '#2B8CBE']
    "PuBu-4": ['#F1EEF6', '#BDC9E1', '#74A9CF', '#0570B0']
    "PuBu-5": ['#F1EEF6', '#BDC9E1', '#74A9CF', '#2B8CBE', '#045A8D']
    "PuBu-6": ['#F1EEF6', '#D0D1E6', '#A6BDDB', '#74A9CF', '#2B8CBE', '#045A8D']
    "PuBu-7": ['#F1EEF6', '#D0D1E6', '#A6BDDB', '#74A9CF', '#3690C0', '#0570B0', '#034E7B']
    "PuBu-8": ['#FFF7FB', '#ECE7F2', '#D0D1E6', '#A6BDDB', '#74A9CF', '#3690C0', '#0570B0', '#034E7B']
    "PuBu-9": ['#FFF7FB', '#ECE7F2', '#D0D1E6', '#A6BDDB', '#74A9CF', '#3690C0', '#0570B0', '#045A8D', '#023858']
    "PuBuGn-3": ['#ECE2F0', '#A6BDDB', '#1C9099']
    "PuBuGn-4": ['#F6EFF7', '#BDC9E1', '#67A9CF', '#02818A']
    "PuBuGn-5": ['#F6EFF7', '#BDC9E1', '#67A9CF', '#1C9099', '#016C59']
    "PuBuGn-6": ['#F6EFF7', '#D0D1E6', '#A6BDDB', '#67A9CF', '#1C9099', '#016C59']
    "PuBuGn-7": ['#F6EFF7', '#D0D1E6', '#A6BDDB', '#67A9CF', '#3690C0', '#02818A', '#016450']
    "PuBuGn-8": ['#FFF7FB', '#ECE2F0', '#D0D1E6', '#A6BDDB', '#67A9CF', '#3690C0', '#02818A', '#016450']
    "PuBuGn-9": ['#FFF7FB', '#ECE2F0', '#D0D1E6', '#A6BDDB', '#67A9CF', '#3690C0', '#02818A', '#016C59', '#014636']
    "PuOr-10": ['#7F3B08', '#B35806', '#E08214', '#FDB863', '#FEE0B6', '#D8DAEB', '#B2ABD2', '#8073AC', '#542788', '#2D004B']
    "PuOr-11": ['#7F3B08', '#B35806', '#2D004B', '#E08214', '#FDB863', '#FEE0B6', '#F7F7F7', '#D8DAEB', '#B2ABD2', '#8073AC', '#542788']
    "PuOr-3": ['#F1A340', '#F7F7F7', '#998EC3']
    "PuOr-4": ['#E66101', '#FDB863', '#B2ABD2', '#5E3C99']
    "PuOr-5": ['#E66101', '#FDB863', '#F7F7F7', '#B2ABD2', '#5E3C99']
    "PuOr-6": ['#B35806', '#F1A340', '#FEE0B6', '#D8DAEB', '#998EC3', '#542788']
    "PuOr-7": ['#B35806', '#F1A340', '#FEE0B6', '#F7F7F7', '#D8DAEB', '#998EC3', '#542788']
    "PuOr-8": ['#B35806', '#E08214', '#FDB863', '#FEE0B6', '#D8DAEB', '#B2ABD2', '#8073AC', '#542788']
    "PuOr-9": ['#B35806', '#E08214', '#FDB863', '#FEE0B6', '#F7F7F7', '#D8DAEB', '#B2ABD2', '#8073AC', '#542788']
    "PuRd-3": ['#E7E1EF', '#C994C7', '#DD1C77']
    "PuRd-4": ['#F1EEF6', '#D7B5D8', '#DF65B0', '#CE1256']
    "PuRd-5": ['#F1EEF6', '#D7B5D8', '#DF65B0', '#DD1C77', '#980043']
    "PuRd-6": ['#F1EEF6', '#D4B9DA', '#C994C7', '#DF65B0', '#DD1C77', '#980043']
    "PuRd-7": ['#F1EEF6', '#D4B9DA', '#C994C7', '#DF65B0', '#E7298A', '#CE1256', '#91003F']
    "PuRd-8": ['#F7F4F9', '#E7E1EF', '#D4B9DA', '#C994C7', '#DF65B0', '#E7298A', '#CE1256', '#91003F']
    "PuRd-9": ['#F7F4F9', '#E7E1EF', '#D4B9DA', '#C994C7', '#DF65B0', '#E7298A', '#CE1256', '#980043', '#67001F']
    "Purples-3": ['#EFEDF5', '#BCBDDC', '#756BB1']
    "Purples-4": ['#F2F0F7', '#CBC9E2', '#9E9AC8', '#6A51A3']
    "Purples-5": ['#F2F0F7', '#CBC9E2', '#9E9AC8', '#756BB1', '#54278F']
    "Purples-6": ['#F2F0F7', '#DADAEB', '#BCBDDC', '#9E9AC8', '#756BB1', '#54278F']
    "Purples-7": ['#F2F0F7', '#DADAEB', '#BCBDDC', '#9E9AC8', '#807DBA', '#6A51A3', '#4A1486']
    "Purples-8": ['#FCFBFD', '#EFEDF5', '#DADAEB', '#BCBDDC', '#9E9AC8', '#807DBA', '#6A51A3', '#4A1486']
    "Purples-9": ['#FCFBFD', '#EFEDF5', '#DADAEB', '#BCBDDC', '#9E9AC8', '#807DBA', '#6A51A3', '#54278F', '#3F007D']
    "RdBu-10": ['#67001F', '#B2182B', '#D6604D', '#F4A582', '#FDDBC7', '#D1E5F0', '#92C5DE', '#4393C3', '#2166AC', '#053061']
    "RdBu-11": ['#67001F', '#B2182B', '#053061', '#D6604D', '#F4A582', '#FDDBC7', '#F7F7F7', '#D1E5F0', '#92C5DE', '#4393C3', '#2166AC']
    "RdBu-3": ['#EF8A62', '#F7F7F7', '#67A9CF']
    "RdBu-4": ['#CA0020', '#F4A582', '#92C5DE', '#0571B0']
    "RdBu-5": ['#CA0020', '#F4A582', '#F7F7F7', '#92C5DE', '#0571B0']
    "RdBu-6": ['#B2182B', '#EF8A62', '#FDDBC7', '#D1E5F0', '#67A9CF', '#2166AC']
    "RdBu-7": ['#B2182B', '#EF8A62', '#FDDBC7', '#F7F7F7', '#D1E5F0', '#67A9CF', '#2166AC']
    "RdBu-8": ['#B2182B', '#D6604D', '#F4A582', '#FDDBC7', '#D1E5F0', '#92C5DE', '#4393C3', '#2166AC']
    "RdBu-9": ['#B2182B', '#D6604D', '#F4A582', '#FDDBC7', '#F7F7F7', '#D1E5F0', '#92C5DE', '#4393C3', '#2166AC']
    "RdGy-10": ['#67001F', '#B2182B', '#D6604D', '#F4A582', '#FDDBC7', '#E0E0E0', '#BABABA', '#878787', '#4D4D4D', '#1A1A1A']
    "RdGy-11": ['#67001F', '#B2182B', '#1A1A1A', '#D6604D', '#F4A582', '#FDDBC7', '#FFFFFF', '#E0E0E0', '#BABABA', '#878787', '#4D4D4D']
    "RdGy-3": ['#EF8A62', '#FFFFFF', '#999999']
    "RdGy-4": ['#CA0020', '#F4A582', '#BABABA', '#404040']
    "RdGy-5": ['#CA0020', '#F4A582', '#FFFFFF', '#BABABA', '#404040']
    "RdGy-6": ['#B2182B', '#EF8A62', '#FDDBC7', '#E0E0E0', '#999999', '#4D4D4D']
    "RdGy-7": ['#B2182B', '#EF8A62', '#FDDBC7', '#FFFFFF', '#E0E0E0', '#999999', '#4D4D4D']
    "RdGy-8": ['#B2182B', '#D6604D', '#F4A582', '#FDDBC7', '#E0E0E0', '#BABABA', '#878787', '#4D4D4D']
    "RdGy-9": ['#B2182B', '#D6604D', '#F4A582', '#FDDBC7', '#FFFFFF', '#E0E0E0', '#BABABA', '#878787', '#4D4D4D']
    "RdPu-3": ['#FDE0DD', '#FA9FB5', '#C51B8A']
    "RdPu-4": ['#FEEBE2', '#FBB4B9', '#F768A1', '#AE017E']
    "RdPu-5": ['#FEEBE2', '#FBB4B9', '#F768A1', '#C51B8A', '#7A0177']
    "RdPu-6": ['#FEEBE2', '#FCC5C0', '#FA9FB5', '#F768A1', '#C51B8A', '#7A0177']
    "RdPu-7": ['#FEEBE2', '#FCC5C0', '#FA9FB5', '#F768A1', '#DD3497', '#AE017E', '#7A0177']
    "RdPu-8": ['#FFF7F3', '#FDE0DD', '#FCC5C0', '#FA9FB5', '#F768A1', '#DD3497', '#AE017E', '#7A0177']
    "RdPu-9": ['#FFF7F3', '#FDE0DD', '#FCC5C0', '#FA9FB5', '#F768A1', '#DD3497', '#AE017E', '#7A0177', '#49006A']
    "RdYlBu-10": ['#A50026', '#D73027', '#F46D43', '#FDAE61', '#FEE090', '#E0F3F8', '#ABD9E9', '#74ADD1', '#4575B4', '#313695']
    "RdYlBu-11": ['#A50026', '#D73027', '#313695', '#F46D43', '#FDAE61', '#FEE090', '#FFFFBF', '#E0F3F8', '#ABD9E9', '#74ADD1', '#4575B4']
    "RdYlBu-3": ['#FC8D59', '#FFFFBF', '#91BFDB']
    "RdYlBu-4": ['#D7191C', '#FDAE61', '#ABD9E9', '#2C7BB6']
    "RdYlBu-5": ['#D7191C', '#FDAE61', '#FFFFBF', '#ABD9E9', '#2C7BB6']
    "RdYlBu-6": ['#D73027', '#FC8D59', '#FEE090', '#E0F3F8', '#91BFDB', '#4575B4']
    "RdYlBu-7": ['#D73027', '#FC8D59', '#FEE090', '#FFFFBF', '#E0F3F8', '#91BFDB', '#4575B4']
    "RdYlBu-8": ['#D73027', '#F46D43', '#FDAE61', '#FEE090', '#E0F3F8', '#ABD9E9', '#74ADD1', '#4575B4']
    "RdYlBu-9": ['#D73027', '#F46D43', '#FDAE61', '#FEE090', '#FFFFBF', '#E0F3F8', '#ABD9E9', '#74ADD1', '#4575B4']
    "RdYlGn-10": ['#A50026', '#D73027', '#F46D43', '#FDAE61', '#FEE08B', '#D9EF8B', '#A6D96A', '#66BD63', '#1A9850', '#006837']
    "RdYlGn-11": ['#A50026', '#D73027', '#006837', '#F46D43', '#FDAE61', '#FEE08B', '#FFFFBF', '#D9EF8B', '#A6D96A', '#66BD63', '#1A9850']
    "RdYlGn-3": ['#FC8D59', '#FFFFBF', '#91CF60']
    "RdYlGn-4": ['#D7191C', '#FDAE61', '#A6D96A', '#1A9641']
    "RdYlGn-5": ['#D7191C', '#FDAE61', '#FFFFBF', '#A6D96A', '#1A9641']
    "RdYlGn-6": ['#D73027', '#FC8D59', '#FEE08B', '#D9EF8B', '#91CF60', '#1A9850']
    "RdYlGn-7": ['#D73027', '#FC8D59', '#FEE08B', '#FFFFBF', '#D9EF8B', '#91CF60', '#1A9850']
    "RdYlGn-8": ['#D73027', '#F46D43', '#FDAE61', '#FEE08B', '#D9EF8B', '#A6D96A', '#66BD63', '#1A9850']
    "RdYlGn-9": ['#D73027', '#F46D43', '#FDAE61', '#FEE08B', '#FFFFBF', '#D9EF8B', '#A6D96A', '#66BD63', '#1A9850']
    "Reds-3": ['#FEE0D2', '#FC9272', '#DE2D26']
    "Reds-4": ['#FEE5D9', '#FCAE91', '#FB6A4A', '#CB181D']
    "Reds-5": ['#FEE5D9', '#FCAE91', '#FB6A4A', '#DE2D26', '#A50F15']
    "Reds-6": ['#FEE5D9', '#FCBBA1', '#FC9272', '#FB6A4A', '#DE2D26', '#A50F15']
    "Reds-7": ['#FEE5D9', '#FCBBA1', '#FC9272', '#FB6A4A', '#EF3B2C', '#CB181D', '#99000D']
    "Reds-8": ['#FFF5F0', '#FEE0D2', '#FCBBA1', '#FC9272', '#FB6A4A', '#EF3B2C', '#CB181D', '#99000D']
    "Reds-9": ['#FFF5F0', '#FEE0D2', '#FCBBA1', '#FC9272', '#FB6A4A', '#EF3B2C', '#CB181D', '#A50F15', '#67000D']
    "Set1-3": ['#E41A1C', '#377EB8', '#4DAF4A']
    "Set1-4": ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3']
    "Set1-5": ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00']
    "Set1-6": ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33']
    "Set1-7": ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628']
    "Set1-8": ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628', '#F781BF']
    "Set1-9": ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628', '#F781BF', '#999999']
    "Set2-3": ['#66C2A5', '#FC8D62', '#8DA0CB']
    "Set2-4": ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3']
    "Set2-5": ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3', '#A6D854']
    "Set2-6": ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3', '#A6D854', '#FFD92F']
    "Set2-7": ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3', '#A6D854', '#FFD92F', '#E5C494']
    "Set2-8": ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3', '#A6D854', '#FFD92F', '#E5C494', '#B3B3B3']
    "Set3-10": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD']
    "Set3-11": ['#8DD3C7', '#FFFFB3', '#CCEBC5', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD']
    "Set3-12": ['#8DD3C7', '#FFFFB3', '#CCEBC5', '#FFED6F', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD']
    "Set3-3": ['#8DD3C7', '#FFFFB3', '#BEBADA']
    "Set3-4": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072']
    "Set3-5": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3']
    "Set3-6": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462']
    "Set3-7": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69']
    "Set3-8": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69', '#FCCDE5']
    "Set3-9": ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9']
    "Spectral-10": ['#9E0142', '#D53E4F', '#F46D43', '#FDAE61', '#FEE08B', '#E6F598', '#ABDDA4', '#66C2A5', '#3288BD', '#5E4FA2']
    "Spectral-11": ['#9E0142', '#D53E4F', '#5E4FA2', '#F46D43', '#FDAE61', '#FEE08B', '#FFFFBF', '#E6F598', '#ABDDA4', '#66C2A5', '#3288BD']
    "Spectral-3": ['#FC8D59', '#FFFFBF', '#99D594']
    "Spectral-4": ['#D7191C', '#FDAE61', '#ABDDA4', '#2B83BA']
    "Spectral-5": ['#D7191C', '#FDAE61', '#FFFFBF', '#ABDDA4', '#2B83BA']
    "Spectral-6": ['#D53E4F', '#FC8D59', '#FEE08B', '#E6F598', '#99D594', '#3288BD']
    "Spectral-7": ['#D53E4F', '#FC8D59', '#FEE08B', '#FFFFBF', '#E6F598', '#99D594', '#3288BD']
    "Spectral-8": ['#D53E4F', '#F46D43', '#FDAE61', '#FEE08B', '#E6F598', '#ABDDA4', '#66C2A5', '#3288BD']
    "Spectral-9": ['#D53E4F', '#F46D43', '#FDAE61', '#FEE08B', '#FFFFBF', '#E6F598', '#ABDDA4', '#66C2A5', '#3288BD']
    "YlGn-3": ['#F7FCB9', '#ADDD8E', '#31A354']
    "YlGn-4": ['#FFFFCC', '#C2E699', '#78C679', '#238443']
    "YlGn-5": ['#FFFFCC', '#C2E699', '#78C679', '#31A354', '#006837']
    "YlGn-6": ['#FFFFCC', '#D9F0A3', '#ADDD8E', '#78C679', '#31A354', '#006837']
    "YlGn-7": ['#FFFFCC', '#D9F0A3', '#ADDD8E', '#78C679', '#41AB5D', '#238443', '#005A32']
    "YlGn-8": ['#FFFFE5', '#F7FCB9', '#D9F0A3', '#ADDD8E', '#78C679', '#41AB5D', '#238443', '#005A32']
    "YlGn-9": ['#FFFFE5', '#F7FCB9', '#D9F0A3', '#ADDD8E', '#78C679', '#41AB5D', '#238443', '#006837', '#004529']
    "YlGnBu-3": ['#EDF8B1', '#7FCDBB', '#2C7FB8']
    "YlGnBu-4": ['#FFFFCC', '#A1DAB4', '#41B6C4', '#225EA8']
    "YlGnBu-5": ['#FFFFCC', '#A1DAB4', '#41B6C4', '#2C7FB8', '#253494']
    "YlGnBu-6": ['#FFFFCC', '#C7E9B4', '#7FCDBB', '#41B6C4', '#2C7FB8', '#253494']
    "YlGnBu-7": ['#FFFFCC', '#C7E9B4', '#7FCDBB', '#41B6C4', '#1D91C0', '#225EA8', '#0C2C84']
    "YlGnBu-8": ['#FFFFD9', '#EDF8B1', '#C7E9B4', '#7FCDBB', '#41B6C4', '#1D91C0', '#225EA8', '#0C2C84']
    "YlGnBu-9": ['#FFFFD9', '#EDF8B1', '#C7E9B4', '#7FCDBB', '#41B6C4', '#1D91C0', '#225EA8', '#253494', '#081D58']
    "YlOrBr-3": ['#FFF7BC', '#FEC44F', '#D95F0E']
    "YlOrBr-4": ['#FFFFD4', '#FED98E', '#FE9929', '#CC4C02']
    "YlOrBr-5": ['#FFFFD4', '#FED98E', '#FE9929', '#D95F0E', '#993404']
    "YlOrBr-6": ['#FFFFD4', '#FEE391', '#FEC44F', '#FE9929', '#D95F0E', '#993404']
    "YlOrBr-7": ['#FFFFD4', '#FEE391', '#FEC44F', '#FE9929', '#EC7014', '#CC4C02', '#8C2D04']
    "YlOrBr-8": ['#FFFFE5', '#FFF7BC', '#FEE391', '#FEC44F', '#FE9929', '#EC7014', '#CC4C02', '#8C2D04']
    "YlOrBr-9": ['#FFFFE5', '#FFF7BC', '#FEE391', '#FEC44F', '#FE9929', '#EC7014', '#CC4C02', '#993404', '#662506']
    "YlOrRd-3": ['#FFEDA0', '#FEB24C', '#F03B20']
    "YlOrRd-4": ['#FFFFB2', '#FECC5C', '#FD8D3C', '#E31A1C']
    "YlOrRd-5": ['#FFFFB2', '#FECC5C', '#FD8D3C', '#F03B20', '#BD0026']
    "YlOrRd-6": ['#FFFFB2', '#FED976', '#FEB24C', '#FD8D3C', '#F03B20', '#BD0026']
    "YlOrRd-7": ['#FFFFB2', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#B10026']
    "YlOrRd-8": ['#FFFFCC', '#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#B10026']
    "YlOrRd-9": ['#FFFFCC', '#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026']
    
    # The reset colors back to the original mpl color codes
    "reset":  ['#0000ff', '#008000', '#ff0000', '#bf00bf', '#bfbf00', '#00bfbf', '#000000'],

    # Colorblind colors
    "colorblind":     ["#0072B2", "#009E73", "#D55E00", "#CC79A7", "#F0E442", "#56B4E9"],
    "sns_colorblind": ["#0072B2", "#009E73", "#D55E00", "#CC79A7", "#F0E442", "#56B4E9"],

    # The following are Seaborn colors
    "sns_deep":   ["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974", "#64B5CD"],
    "sns_muted":  ["#4878CF", "#6ACC65", "#D65F5F", "#B47CC7", "#C4AD66", "#77BEDB"],
    "sns_pastel": ["#92C6FF", "#97F0AA", "#FF9F9A", "#D0BBFF", "#FFFEA3", "#B0E0E6"],
    "sns_bright": ["#003FFF", "#03ED3A", "#E8000B", "#8A2BE2", "#FFC400", "#00D7FF"],
    "sns_dark":   ["#001C7F", "#017517", "#8C0900", "#7600A1", "#B8860B", "#006374"],

    # Other palettes
    "flatui":   ["#34495e", "#2ecc71", "#e74c3c", "#9b59b6", "#f4d03f", "#3498db"],

    # Longer palettes that do not map to bgrmyck color space.
    "ddl_heat": ['#DBDBDB', '#DCD5CC', '#DCCEBE', '#DDC8AF', '#DEC2A0', '#DEBB91',
                 '#DFB583', '#DFAE74', '#E0A865', '#E1A256', '#E19B48', '#E29539'],

    "paired":   ["#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928",
                 "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#a6cee3", "#1f78b4"],

    "set1":     ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33",
                 "#a65628", "#f781bf", "#999999"],
}

## Special, backward compatible color map.
ddlheatmap = mplcol.ListedColormap(PALETTES["ddl_heat"])


##########################################################################
## Palette Object
##########################################################################

class ColorPalette(list):
    """
    A wrapper for functionality surrounding a list of colors, including a
    context manager that allows the palette to be set with a with statement.
    """

    def __init__(self, name_or_list):
        """
        Can initialize the ColorPalette with either a name or a list.

        Parameters
        ----------

        name_or_list :
            specify a palette name or a list of RGB or Hex values

        """
        if isinstance(name_or_list, string_types):
            if name_or_list not in PALETTES:
                raise YellowbrickValueError(
                    "'{}' is not a recognized palette!".format(name_or_list)
                )

            name_or_list = PALETTES[name_or_list]

        super(ColorPalette, self).__init__(name_or_list)

    def __enter__(self):
        """
        Open the context and assign the pallete to the mpl.rcParams
        """
        from .rcmod import set_palette
        self._orig_palette = color_palette()
        set_palette(self)
        return self

    def __exit__(self, *args):
        """
        Close the context and restore the original palette
        """
        from .rcmod import set_palette
        set_palette(self._orig_palette)

    def as_hex(self):
        """
        Return a color palette with hex codes instead of RGB values.
        """
        hex = [mpl.colors.rgb2hex(rgb) for rgb in self]
        return ColorPalette(hex)

    def as_rgb(self):
        """
        Return a color palette with RGB values instead of hex codes.
        """
        rgb = [mpl.colors.colorConverter.to_rgb(hex) for hex in self]
        return ColorPalette(rgb)

    def plot(self, size=1):
        """
        Plot the values in the color palatte as a horizontal array.
        See Seaborn's palplot function for inspiration.

        Parameters
        ----------
        size : int
            scaling factor for size of the plot

        """
        n = len(self)
        fig, ax = plt.subplots(1, 1, figsize=(n * size, size))
        ax.imshow(np.arange(n).reshape(1,n),
                  cmap=mpl.colors.ListedColormap(list(self)),
                  interpolation="nearest", aspect="auto")
        ax.set_xticks(np.arange(n) - .5)
        ax.set_yticks([-.5, .5])
        ax.set_xticklabels([])
        ax.set_yticklabels([])


##########################################################################
## Palette Functions
##########################################################################

def color_palette(palette=None, n_colors=None):
    """
    Return a color palette object with color definition and handling.

    Calling this function with ``palette=None`` will return the current
    matplotlib color cycle.

    This function can also be used in a ``with`` statement to temporarily
    set the color cycle for a plot or set of plots.

    Parameters
    ----------

    palette : None or str or sequence
        Name of a palette or ``None`` to return the current palette. If a
        sequence the input colors are used but possibly cycled.

        Available palette names from :py:mod:`yellowbrick.colors.palettes` are:

        .. hlist::
            :columns: 3

            * :py:const:`accent`
            * :py:const:`dark`
            * :py:const:`paired`
            * :py:const:`pastel`
            * :py:const:`bold`
            * :py:const:`muted`
            * :py:const:`colorblind`
            * :py:const:`sns_colorblind`
            * :py:const:`sns_deep`
            * :py:const:`sns_muted`
            * :py:const:`sns_pastel`
            * :py:const:`sns_bright`
            * :py:const:`sns_dark`
            * :py:const:`flatui`

    n_colors : None or int
        Number of colors in the palette. If ``None``, the default will depend
        on how ``palette`` is specified. Named palettes default to 6 colors
        which allow the use of the names "bgrmyck", though others do have more
        or less colors; therefore reducing the size of the list can only be
        done by specifying this parameter. Asking for more colors than exist
        in the palette will cause it to cycle.

    Returns
    -------
    list(tuple)
        Returns a ColorPalette object, which behaves like a list, but can be
        used as a context manager and possesses functions to convert colors.

    .. seealso::

        :func:`.set_palette`
            Set the default color cycle for all plots.
        :func:`.set_color_codes`
            Reassign color codes like ``"b"``, ``"g"``, etc. to
            colors from one of the yellowbrick palettes.
        :func:`..colors.resolve_colors`
            Resolve a color map or listed sequence of colors.

    """
    if palette is None:
        palette = get_color_cycle()
        if n_colors is None:
            n_colors = len(palette)

    elif not isinstance(palette, string_types):
        palette = palette
        if n_colors is None:
            n_colors = len(palette)

    else:
        if palette.lower() not in PALETTES:
            raise YellowbrickValueError(
                "'{}' is not a recognized palette!".format(palette)
            )

        palette = PALETTES[palette.lower()]
        if n_colors is None:
            n_colors = len(palette)

    # Always return as many colors as we asked for
    pal_cycle = cycle(palette)
    palette = [next(pal_cycle) for _ in range(n_colors)]

    # Always return in RGB tuple format
    try:
        palette = map(mpl.colors.colorConverter.to_rgb, palette)
        palette = ColorPalette(palette)
    except ValueError:
        raise YellowbrickValueError(
            "Could not generate a palette for %s" % str(palette)
        )

    return palette


def set_color_codes(palette="accent"):
    """
    Change how matplotlib color shorthands are interpreted.

    Calling this will change how shorthand codes like "b" or "g"
    are interpreted by matplotlib in subsequent plots.

    Parameters
    ----------
    palette : str
        Named yellowbrick palette to use as the source of colors.

    See Also
    --------
    set_palette : Color codes can also be set through the function that
                  sets the matplotlib color cycle.
    """

    if palette not in PALETTES:
        raise YellowbrickValueError(
            "'{}' is not a recognized palette!".format(palette)
        )

    # Fetch the colors and adapt the length
    colors = PALETTES[palette]

    if len(colors) > 7:
        # Truncate colors that are longer than 7
        colors = colors[:7]

    elif len(colors) < 7:
        # Add the key (black) color to colors that are shorter than 7
        colors = colors + [YB_KEY]

    # Set the color codes on matplotlib
    for code, color in zip("bgrmyck", colors):
        rgb = mpl.colors.colorConverter.to_rgb(color)
        mpl.colors.colorConverter.colors[code] = rgb
        mpl.colors.colorConverter.cache[code] = rgb
