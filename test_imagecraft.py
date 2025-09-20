from PIL import Image
import imagecraft as it

def run_tests():
    img = Image.open("./testimg/cpied-cuckoo-9750790.jpg")

    # Info
    it.get_image_info(img)

    # Conversion
    png_img = it.to_png(img, remove_bg=True, verbose=True)
    jpg_img = it.to_jpg(img, verbose=True)

    # Resize & crop
    resized = it.resize_with_aspect(img, (512, 312), verbose=True)

    # Enhancements
    brighter = it.adjust_brightness(img, 1.2, verbose=True)
    sharper = it.adjust_sharpness(img, 2.0, verbose=True)

    # Presets
    icon = it.convert_icon(img, size=(128, 128), verbose=True)
    profile = it.convert_profile_picture(img, size=(512, 512), verbose=True)

    # Bulk
    images = [img, img.copy()]
    bulk_results = it.bulk_process(images, it.to_png, remove_bg=False, verbose=True)

    print("✅ All tests executed.")

if __name__ == "__main__":
    run_tests()