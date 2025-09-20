from PIL import ImageEnhance

def adjust_brightness(image, factor=1.0, verbose=False):
    if verbose:
        print(f"[adjust_brightness] Factor: {factor}")
    return ImageEnhance.Brightness(image).enhance(factor)

def adjust_contrast(image, factor=1.0, verbose=False):
    if verbose:
        print(f"[adjust_contrast] Factor: {factor}")
    return ImageEnhance.Contrast(image).enhance(factor)

def adjust_sharpness(image, factor=1.0, verbose=False):
    if verbose:
        print(f"[adjust_sharpness] Factor: {factor}")
    return ImageEnhance.Sharpness(image).enhance(factor)