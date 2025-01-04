from picamera2 import Picamera2
import time

# Initialize the Picamera2 instance
picam2 = Picamera2()

# Configure the camera with default preview and still capture settings
config = picam2.create_still_configuration()
picam2.configure(config)

# Start the camera
picam2.start()

# Wait for a brief moment to let the camera adjust
time.sleep(2)

# Capture the image and save it
image_filename = "captured_image.jpg"
picam2.capture_file(image_filename)

# Stop the camera
picam2.stop()

print(f"Image saved as {image_filename}")
