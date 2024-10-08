from project import Image

def encrypt_image(image_path, encrypted_image_path):
    """
    Encrypt an image by swapping red and blue pixel values.
    """
    image = Image.open(image_path)
    pixels = list(image.getdata())
    encrypted_pixels = [(pixel[2], pixel[1], pixel[0]) for pixel in pixels]
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(encrypted_image_path)

def decrypt_image(encrypted_image_path, decrypted_image_path):
    """
    Decrypt an image by swapping red and blue pixel values.
    """
    image = Image.open(encrypted_image_path)
    pixels = list(image.getdata())
    decrypted_pixels = [(pixel[2], pixel[1], pixel[0]) for pixel in pixels]
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(decrypted_image_path)

def main():
    image_path = input("Enter the path to the image to encrypt: ")
    encrypted_image_path = input("Enter the path to save the encrypted image: ")
    encrypt_image(image_path, encrypted_image_path)
    print("Image encrypted successfully!")

    encrypted_image_path = input("Enter the path to the encrypted image to decrypt: ")
    decrypted_image_path = input("Enter the path to save the decrypted image: ")
    decrypt_image(encrypted_image_path, decrypted_image_path)
    print("Image decrypted successfully!")

if __name__ == "__main__":
    main()
