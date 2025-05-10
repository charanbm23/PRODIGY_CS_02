# Image Encryption Tool

A simple command-line tool for encrypting and decrypting images using pixel manipulation techniques.

## Features

- Two encryption methods:
  1. XOR encryption: Performs bitwise XOR operation on each pixel
  2. Pixel shuffling: Randomly shuffles pixels based on a key
- Simple command-line interface
- Support for both string and integer keys
- Reversible encryption/decryption

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The tool provides two encryption methods and can be used from the command line:

### XOR Encryption

```bash
# Encrypt an image
python main.py --mode encrypt --method xor --input input.jpg --output encrypted.jpg --key "your_secret_key"

# Decrypt an image
python main.py --mode decrypt --method xor --input encrypted.jpg --output decrypted.jpg --key "your_secret_key"
```

### Pixel Shuffling

```bash
# Encrypt an image
python main.py --mode encrypt --method shuffle --input input.jpg --output encrypted.jpg --key "your_secret_key"

# Decrypt an image
python main.py --mode decrypt --method shuffle --input encrypted.jpg --output decrypted.jpg --key "your_secret_key"
```

## Parameters

- `--mode`: Choose between 'encrypt' or 'decrypt'
- `--method`: Choose between 'xor' or 'shuffle'
- `--input`: Path to the input image
- `--output`: Path where the output image will be saved
- `--key`: Encryption/decryption key (can be a string or integer)

## Notes

- The same key must be used for encryption and decryption
- The tool supports common image formats (JPEG, PNG, etc.)
- For best results, use the same image format for input and output 