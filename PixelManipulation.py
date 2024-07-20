from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            pixels[x, y] = (pixel[0] + key, pixel[1] + key, pixel[2] + key)

    image.save("encrypted_image.png")

def decrypt_image(encrypted_image_path, key):
    image = Image.open(encrypted_image_path)
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            pixels[x, y] = (pixel[0] - key, pixel[1] - key, pixel[2] - key)

    image.save("decrypted_image.png")

while True:
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        image_path = input("Enter the image path: ")
        key = int(input("Enter the encryption key: "))
        encrypt_image(image_path, key)
        print("Image encrypted successfully!")
    elif choice == "2":
        encrypted_image_path = input("Enter the encrypted image path: ")
        key = int(input("Enter the decryption key: "))
        decrypt_image(encrypted_image_path, key)
        print("Image decrypted successfully!")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")