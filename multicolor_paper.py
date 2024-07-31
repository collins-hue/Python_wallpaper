from PIL import Image, ImageDraw
import random

# Define image dimensions
width, height = 1080, 1920

# Define the color palette
colors = [
    (240, 255, 255),  # Azure
    (0, 0, 255),      # Blue
    (41, 171, 135),   # Jungle Green
    (220, 20, 60),    # Crimson
    (255, 215, 0),    # Gold
    (230, 230, 250),  # Lavender
    (255, 127, 80),   # Coral
    (250, 128, 114),  # Salmon
    (128, 128, 0),    # Olive
    (0, 128, 128),    # Teal
    (255, 0, 255),    # Magenta
    (75, 0, 130),     # Indigo
    (64, 224, 208),   # Turquoise
    (255, 99, 71),    # Tomato
    (218, 112, 214)   # Orchid
]

# Define background colors
background_colors = [
    (240, 255, 255),  # Azure
    (230, 230, 250),  # Lavender
    (250, 128, 114),  # Salmon
    (255, 215, 0),    # Gold
    (64, 224, 208)    # Turquoise
]

# Select a random background color
background_color = random.choice(background_colors)

# Create a new image with the selected background color
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Generate random geometric shapes
for _ in range(20):  # Adjust the range for more or fewer shapes
    shape_type = random.choice(['rectangle', 'ellipse'])
    x1, y1 = random.randint(0, width), random.randint(0, height)
    x2, y2 = random.randint(0, width), random.randint(0, height)
    color = random.choice(colors)
    if shape_type == 'rectangle':
        draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
    else:
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)

# Save the image as a .jpg file
image.save('/home/montego/git/Python_wallpaper/media/abstract_geometric_wallpaper.jpg', 'JPEG')

# Display the image (if running locally)
image.show()

