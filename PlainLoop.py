from PIL import Image

# Define image dimensions
width, height = 1080, 1920

# List of colors
colors = [
    (41, 171, 135),   # Jungle Green
    (252, 186, 3),    # Another Color
    (8, 73, 158),     # Another Color
    (0, 3, 8),        # Another Color
    (46, 191, 177),   # Another Color
    (21, 52, 69),     # Another Color
    (155, 157, 158),  # Another Color
    (189, 222, 71)    # Another Color
]

# Loop through each color and create a wallpaper
for i, color in enumerate(colors, start=1):
    # Create a new image with the selected color
    image = Image.new('RGB', (width, height), color)
    
    # Save the image as a .jpg file with a unique name
    image.save(f'/home/montego/git/Python_wallpaper/media/PlainLoop/plain_color_wallpaper{i}.jpg', 'JPEG')
    
    # Optional: Display the image (if running locally)
    image.show()

