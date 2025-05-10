import numpy as np
from utils import load_image, save_image, validate_key

def encrypt_image(image_path, key, output_path):
    """
    Encrypt an image using XOR operation with the provided key.
    
    Args:
        image_path (str): Path to the input image
        key: Encryption key (string or integer)
        output_path (str): Path to save the encrypted image
    """
    # Load and validate the image
    image_array = load_image(image_path)
    
    # Validate and process the key
    key_value = validate_key(key)
    
    # Create a key matrix of the same shape as the image
    key_matrix = np.full_like(image_array, key_value)
    
    # Perform XOR operation
    encrypted_array = np.bitwise_xor(image_array, key_matrix)
    
    # Save the encrypted image
    save_image(encrypted_array, output_path)
    
    return output_path

def shuffle_pixels(image_path, key, output_path):
    """
    Encrypt an image by shuffling pixels based on a key.
    
    Args:
        image_path (str): Path to the input image
        key: Encryption key (string or integer)
        output_path (str): Path to save the encrypted image
    """
    # Load the image
    image_array = load_image(image_path)
    
    # Validate and process the key
    key_value = validate_key(key)
    
    # Set random seed for reproducibility
    np.random.seed(key_value)
    
    # Get image dimensions
    height, width = image_array.shape[:2]
    
    # Create indices for shuffling
    indices = np.arange(height * width)
    np.random.shuffle(indices)
    
    # Reshape image to 2D array of pixels
    pixels = image_array.reshape(-1, image_array.shape[-1])
    
    # Shuffle pixels
    shuffled_pixels = pixels[indices]
    
    # Reshape back to original dimensions
    encrypted_array = shuffled_pixels.reshape(image_array.shape)
    
    # Save the encrypted image
    save_image(encrypted_array, output_path)
    
    return output_path 