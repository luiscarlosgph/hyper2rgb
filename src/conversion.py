"""
@brief   Set of functions to convert hyperspectral images to RGB.

@author  Luis Carlos Garcia Peraza Herrera (luiscarlos.gph@gmail.com).
@date    30 Aug 2022.
"""

import numpy as np
import colour
import scipy

## -- Private part of the API  -- ##

def _bgr2rgb(bgr: np.ndarray) -> np.ndarray:
    return bgr[..., ::-1].copy()


def _rgb2bgr(rgb: np.ndarray) -> np.ndarray:
    return rgb[..., ::-1].copy()


def _get_cmf(cmf_name: str) -> TODO:
    """
    @brief Get colour matching funtions for different standards.
    @param[in]  cmf_name  Choose one from [cie1931_2, cie1964_10, 
                          cie2012_2, cie2012_10].
                          From Wikipia: the CIE's color matching 
                          functions are the numerical description of 
                          the chromatic response of the observer. 
                          They can be thought of as the spectral 
                          sensitivity curves of three linear light 
                          detectors yielding the CIE tristimulus 
                          values X, Y and Z. 
                          Collectively, these three functions describe 
                          the CIE standard observer.
    """
    cmf_full_name = {
        'cie_2_1931':  'CIE 1931 2 Degree Standard Observer',
        'cie_10_1964': 'CIE 1964 10 Degree Standard Observer',
        'cie_2_2012':  'CIE 2012 2 Degree Standard Observer',
        'cie_10_2012': 'CIE 2012 10 Degree Standard Observer',
    }
    if cmf_name not in cmf_full_name: 
        err_msg = '[ERROR] Wrong CMF name. The available options are: '
        err_msg += ', '.join(cmf_full_name.keys())
        raise AttributeError(err_msg)
    standard_obs = colour.colorimetry.MSDS_CMFS_STANDARD_OBSERVER

    return standard_obs[cmf_full_name[cmf_name]]


def _get_corrected_cmf(cmf_name: str, wl_vec: np.ndarray) -> TODO:
    """
    @brief Get colour matching function modified to colour-compensate 
           for missing wavelengths in the input images.
    @param[in]  cmf_name  TODO
    @param[in]  wl_vec    TODO
    @returns TODO
    """
    # Get colour matching function (wavelength -> xyz_bar)
    cmfs = _get_cmfs(cmf_name)
    xbar_y, ybar_y, zbar_y = colour.utilities.tsplit(cmfs.values)
    f_xbar = scipy.interpolate.PchipInterpolator(cmfs.wavelengths, 
                                                 xbar_y, 
                                                 extrapolate=False)
    f_ybar = scipy.interpolate.PchipInterpolator(cmfs.wavelengths, 
                                                 ybar_y, 
                                                 extrapolate=False)
    f_zbar = scipy.interpolate.PchipInterpolator(cmfs.wavelengths, 
                                                 zbar_y, 
                                                 extrapolate=False)

    # Get additive correction for missing wavelengths (e.g. Nuance EX)
    f_xbar_corr, f_ybar_corr, f_zbar_corr = \
        OdsiDbDataLoader.LoadImage.get_additive_correction(cmf_name, wl)
    
    # Get corrected colour matching function 
    xbar_y = np.nan_to_num(f_xbar(wl)) + np.nan_to_num(f_xbar_corr(wl))
    ybar_y = np.nan_to_num(f_ybar(wl)) + np.nan_to_num(f_ybar_corr(wl))
    zbar_y = np.nan_to_num(f_zbar(wl)) + np.nan_to_num(f_zbar_corr(wl))
    f_xbar = scipy.interpolate.PchipInterpolator(wl, xbar_y, extrapolate=False)
    f_ybar = scipy.interpolate.PchipInterpolator(wl, ybar_y, extrapolate=False)
    f_zbar = scipy.interpolate.PchipInterpolator(wl, zbar_y, extrapolate=False)
    
    return f_xbar, f_ybar, f_zbar




## -- Public part of the API -- ##


def get_single_wl_im(im_hyper: np.ndarray, wl_vec: np.ndarray, wl: float) -> np.ndarray:
    """
    @brief Given an image and the corresponding wavelengths this function 
           returns the image corresponding to a specific wavelength using
           interpolation.
    @param[in]  im_hyper  Hyperspectral image, shape (H, W, C).
    @param[in]  wl_vec    Wavelengths, shape (C,).
    @param[in]  wl        Wavelegth of the image you want to extract. 
    @returns an array of dimenstion (H, W).
    """
    # TODO


def reconstruct(im_hyper: np.ndarray, wl_vec: np.ndarray) -> np.ndarray:
    """
    @brief Convert hyperspectral image to RGB.
    @param[in]  im_hyper  Hyperspectral image normalised to range [0, 1],
                          shape = (H, W, C).
    @param[in]  wl_vec    Numpy array indicating the wavelength of each of the
                          channels in the hyperspectral image, shape = (C,).
    @returns a BGR Numpy/OpenCV image, dtype = np.uint8, range [0, 255].
    """
    # Assert that the image is in range [0, 1]
    # TODO

    # Get image dimensions
    h, w, nbands = im_hyper.shape

    # TODO


def get_modified_cmf_plot(im_hyper, wl):
    """
    @brief TODO
    """
    # TODO
    pass


if __name__ == '__main__':
    raise RuntimeError('[ERROR] This file (conversion.py) is not a script and cannot be executed as such.')
