from PIL import Image

# Define the ASCII characters from darkest to lightest
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resizes an image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55) # 0.55 adjusts for character height
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """Converts an image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Converts pixels from an image into a string of ASCII characters."""
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        # Map the 0-255 pixel value to an index in our ASCII_CHARS list
        characters += ASCII_CHARS[pixel // 25]
    return characters

def main():
    """Main function to run the ASCII art generator."""
    # Ask user for an image path
    path = input("Enter the path to an image file: ")
    
    try:
        image = Image.open(path)
    except Exception:
        print(f"Unable to open file: {path}")
        return

    # 1. Resize the image
    resized_image = resize_image(image)
    
    # 2. Convert to grayscale
    grayscale_image = grayify(resized_image)
    
    # 3. Convert pixels to ASCII string
    new_pixels = pixels_to_ascii(grayscale_image)
    
    # 4. Format the ASCII string
    pixel_count = len(new_pixels)
    ascii_image = "\n".join([new_pixels[i:(i+resized_image.width)] for i in range(0, pixel_count, resized_image.width)])
    
    # 5. Print the result
    print("\nHere is your ASCII art:\n")
    print(ascii_image)
    
    # Optional: Save to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    print("\nArt also saved to 'ascii_image.txt'")

# Run the main function
if __name__ == '__main__':
    main()