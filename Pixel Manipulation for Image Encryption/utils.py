import numpy as np
from PIL import Image

def load_image(image_path):
    """Load an image and convert it to a numpy array."""
    try:
        img = Image.open(image_path)
        return np.array(img)
    except Exception as e:
        raise Exception(f"Error loading image: {str(e)}")

def save_image(image_array, output_path):
    """Save a numpy array as an image."""
    try:
        img = Image.fromarray(image_array.astype('uint8'))
        img.save(output_path)
    except Exception as e:
        raise Exception(f"Error saving image: {str(e)}")

def validate_key(key):
    """Validate and convert the encryption key to a suitable format."""
    if isinstance(key, str):
        # Convert string key to integer using sum of ASCII values
        return sum(ord(c) for c in key) % 256
    elif isinstance(key, int):
        return key % 256
    else:
        raise ValueError("Key must be either a string or an integer") 