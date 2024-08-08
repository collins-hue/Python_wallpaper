from PIL import Image

# Define image dimensions
width, height = 1080, 1920

# Define the color (e.g., Jungle Green)
#color = (41, 171, 135)  # Jungle Green
#color = (252, 186, 3) 
color = (8, 73, 158)
color = (0, 3, 8)
color = (46, 191, 177)
color = (21, 52, 69)
color = (155, 157, 158)
color = (189, 222, 71)
# Create a new image with the selected color
image = Image.new('RGB', (width, height), color)

# Save the image as a .jpg file
image.save('/home/montego/git/Python_wallpaper/media/plain/plain_color_wallpaper7.jpg', 'JPEG')

# Display the image (if running locally)
image.show()

