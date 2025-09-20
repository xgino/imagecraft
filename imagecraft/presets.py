from .resize_crop import resize_with_aspect

def convert_icon(image, size=(256, 256), verbose=False):
    """
    Convert image into icon style (square, sharp).
    """
    if verbose:
        print(f"[convert_icon] Target size: {size}")
    return resize_with_aspect(image, size, crop=True, verbose=verbose)

def convert_profile_picture(image, size=(512, 512), verbose=False):
    """
    Convert image to profile picture (sharp, square by default).
    """
    if verbose:
        print(f"[convert_profile_picture] Target size: {size}")
    return resize_with_aspect(image, size, crop=True, verbose=verbose)