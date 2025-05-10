from PIL import Image, ImageDraw

# Create a new image with a white background
img = Image.new('RGB', (400, 400), 'white')
draw = ImageDraw.Draw(img)

# Draw some shapes
draw.rectangle([50, 50, 350, 350], outline='black', width=2)
draw.ellipse([100, 100, 300, 300], fill='red')
draw.text((150, 200), "Test Image", fill='blue')

# Save the image
img.save('test_image.png')
print("Test image created: test_image.png") 