from PIL import Image
import os

def to_png(image, remove_bg=False, verbose=False):
    """
    Convert image to PNG.
    If remove_bg=True and image supports transparency, background is removed.
    """
    if verbose:
        print(f"[to_png] Original format: {image.format}, Mode: {image.mode}, Size: {image.size}")
    
    if remove_bg and image.mode in ("RGBA", "LA"):
        return image.convert("RGBA")  # Keep transparency
    else:
        return image.convert("RGB")  # Solid background
    
def to_jpg(image, verbose=False):
    """
    Convert image to JPG (background will be white if image has transparency).
    """
    if verbose:
        print(f"[to_jpg] Original format: {image.format}, Mode: {image.mode}, Size: {image.size}")
    
    if image.mode in ("RGBA", "LA"):
        bg = Image.new("RGB", image.size, (255, 255, 255))
        bg.paste(image, mask=image.split()[-1])
        return bg
    else:
        return image.convert("RGB")

def convert_to_format(image, target_format="PNG", verbose=False):
    """
    Generic converter to any format.
    """
    if verbose:
        print(f"[convert_to_format] Converting to {target_format}, Size: {image.size}")
    return image.convert("RGB") if target_format.upper() in ["JPG", "JPEG"] else image.convert("RGBA")