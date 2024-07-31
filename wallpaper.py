from PIL import Image, ImageDraw
import random

# Define image dimensions
width, height = 1080, 1920

# Create a new image with white background
image = Image.new('RGB', (width, height), 'olive')
draw = ImageDraw.Draw(image)

# Generate random geometric shapes
for _ in range(20):  # Adjust the range for more or fewer shapes
    shape_type = random.choice(['rectangle', 'ellipse'])
    x1, y1 = random.randint(0, width), random.randint(0, height)
    x2, y2 = random.randint(0, width), random.randint(0, height)
    color = tuple(random.randint(0, 255) for _ in range(3))
    if shape_type == 'rectangle':
        draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
    else:
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)

# Save the image as a .jpg file
image.save('/home/montego/git/Python_wallpaper/media/abstract_geometric_wallpaper7.jpg', 'JPEG')

# Display the image (if running locally)
image.show()

