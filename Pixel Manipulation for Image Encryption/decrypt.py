import numpy as np
from utils import load_image, save_image, validate_key

def decrypt_image(image_path, key, output_path):
    """
    Decrypt an image that was encrypted using XOR operation.
    
    Args:
        image_path (str): Path to the encrypted image
        key: Decryption key (string or integer)
        output_path (str): Path to save the decrypted image
    """
    # Load the encrypted image
    image_array = load_image(image_path)
    
    # Validate and process the key
    key_value = validate_key(key)
    
    # Create a key matrix of the same shape as the image
    key_matrix = np.full_like(image_array, key_value)
    
    # Perform XOR operation (same as encryption for XOR)
    decrypted_array = np.bitwise_xor(image_array, key_matrix)
    
    # Save the decrypted image
    save_image(decrypted_array, output_path)
    
    return output_path

def unshuffle_pixels(image_path, key, output_path):
    """
    Decrypt an image that was encrypted using pixel shuffling.
    
    Args:
        image_path (str): Path to the encrypted image
        key: Decryption key (string or integer)
        output_path (str): Path to save the decrypted image
    """
    # Load the encrypted image
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
    
    # Create inverse mapping
    inverse_indices = np.zeros_like(indices)
    inverse_indices[indices] = np.arange(len(indices))
    
    # Reshape image to 2D array of pixels
    pixels = image_array.reshape(-1, image_array.shape[-1])
    
    # Unshuffle pixels
    unshuffled_pixels = pixels[inverse_indices]
    
    # Reshape back to original dimensions
    decrypted_array = unshuffled_pixels.reshape(image_array.shape)
    
    # Save the decrypted image
    save_image(decrypted_array, output_path)
    
    return output_path 