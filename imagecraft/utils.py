from PIL import Image

def get_image_info(image, verbose=True):
    info = {
        "format": image.format,
        "mode": image.mode,
        "size": image.size,
    }
    if verbose:
        print("[get_image_info]", info)
    return info

def bulk_process(images, func, **kwargs):
    """
    Apply a function to a list of images.
    """
    results = []
    for idx, img in enumerate(images):
        if kwargs.get("verbose", False):
            print(f"[bulk_process] Processing image {idx+1}/{len(images)}")
        results.append(func(img, **kwargs))
    return results