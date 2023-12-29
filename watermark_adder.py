from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark(input_dir, output_dir, watermark_text, file_name):
    # Open the image
    input_path = os.path.join(input_dir, file_name)
    image = Image.open(input_path)

    # Choose a font and size for the watermark
    font_size = 50
    font = ImageFont.truetype("font.ttf", font_size)

    # Choose a color for the watermark (you can use RGB values)
    text_color = (255, 0, 0)

    # Rotate the watermark
    angle = 45  # You can adjust the angle as needed
    watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_draw.text((0, 0), watermark_text, font=font, fill=text_color)
    watermark = watermark.rotate(angle, expand=1)

    # Calculate the position to center the watermark after rotation
    x = (watermark.width - image.width) // 2
    y = (image.height - watermark.height) // 2

    # Paste the rotated watermark onto the original image
    image.paste(watermark, (x, y), watermark)

    # Save the watermarked image to the output directory
    output_path = os.path.join(output_dir, watermark_text + file_name)
    image.save(output_path)

    # Close the image
    image.close()


def add_watermark_wrapper(input_dir, output_dir, watermark_texts):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the input directory
    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    # Loop through each file in the directory
    for file_name in files:
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            for watermark_text in watermark_texts:
                add_watermark(input_dir, output_dir, watermark_text, file_name)


if __name__ == "__main__":
    # Set your input directory, output directory, and watermark text
    input_directory = "input_imgs"
    output_directory = "output_imgs"
    watermark_texts = ["first watermark", "second watermark"]

    # Add watermark to images
    add_watermark_wrapper(input_directory, output_directory, watermark_texts)

    print("Watermarking complete.")
