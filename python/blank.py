from PIL import Image

def load_img(filename):
  im = Image.open(filename)
  return im

def show_img(im):
  im.show()

def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

def obamicon(im):
    # Get size
    width, height = image.size
    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()
    # Transform to obamicon
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)

            # Get R, G, B values (This are int from 0 to 255)
            red =   pixel[0]
            green = pixel[1]
            blue =  pixel[2]

            # Transform to obamicon
            obamafilter = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            # Set Pixel in new image
            pixels[i, j] = (int(obamafilter), int(obamafilter), int(obamafilter))

          # Return new image
          return newImage
