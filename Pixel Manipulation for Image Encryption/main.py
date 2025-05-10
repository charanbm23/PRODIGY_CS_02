import argparse
import os
from encrypt import encrypt_image, shuffle_pixels
from decrypt import decrypt_image, unshuffle_pixels

def main():
    parser = argparse.ArgumentParser(description='Image Encryption and Decryption Tool')
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], required=True,
                      help='Mode: encrypt or decrypt')
    parser.add_argument('--method', choices=['xor', 'shuffle'], required=True,
                      help='Encryption method: xor or shuffle')
    parser.add_argument('--input', required=True,
                      help='Input image path')
    parser.add_argument('--output', required=True,
                      help='Output image path')
    parser.add_argument('--key', required=True,
                      help='Encryption/decryption key (string or integer)')

    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)

    try:
        if args.mode == 'encrypt':
            if args.method == 'xor':
                encrypt_image(args.input, args.key, args.output)
            else:  # shuffle
                shuffle_pixels(args.input, args.key, args.output)
            print(f"Image encrypted successfully. Saved to: {args.output}")
        else:  # decrypt
            if args.method == 'xor':
                decrypt_image(args.input, args.key, args.output)
            else:  # shuffle
                unshuffle_pixels(args.input, args.key, args.output)
            print(f"Image decrypted successfully. Saved to: {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main() 