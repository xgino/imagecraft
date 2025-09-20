from PIL import Image

def resize_with_aspect(image, target_size, crop=True, verbose=False):
    """
    Resize image while keeping aspect ratio.
    If crop=True, crops the excess to fit target_size.
    """
    if verbose:
        print(f"[resize_with_aspect] Target: {target_size}, Original: {image.size}")

    image = image.copy()
    image.thumbnail(target_size, Image.Resampling.LANCZOS)

    if crop:
        width, height = image.size
        target_w, target_h = target_size
        left = (width - target_w) // 2
        top = (height - target_h) // 2
        right = left + target_w
        bottom = top + target_h
        image = image.crop((max(left, 0), max(top, 0), min(right, width), min(bottom, height)))
    
    return image