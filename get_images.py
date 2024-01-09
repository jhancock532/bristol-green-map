import os
import requests
import shutil

def download_image(image_url, file_path):
    """Downloads an image from the given URL and saves it to the specified file path."""

    response = requests.get(image_url, stream=True)

    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            response.raw.decode_content = True  # Handle compressed images
            shutil.copyfileobj(response.raw, f)

        print("Image downloaded successfully!")
    else:
        print("Failed to download image. Status code:", response.status_code)

def create_folder(folder_path):
    """Creates a folder at the specified path if it doesn't already exist."""

    try:
        os.mkdir(folder_path)  # Create the folder
        # print(f"Folder {folder_path} created successfully!")
    except FileExistsError:
        print(f"Folder {folder_path} already exists.")


minZoom = 15
maxZoom = 16

minZoomMinX = 2015
minZoomMaxX = 2021
minZoomMinY = 1360
minZoomMaxY = 1365

base_folder_name = "downloaded_tiles"

def total_tiles():
    total = 0
    for zoom_level in range(minZoom, maxZoom):
        multiplier = 2 ** (zoom_level - minZoom)
        min_x_tile = minZoomMinX * multiplier
        max_x_tile = minZoomMaxX * multiplier
        min_y_tile = minZoomMinY * multiplier
        max_y_tile = minZoomMaxY * multiplier
        total += (max_x_tile - min_x_tile) * (max_y_tile - min_y_tile)
    return total

print("Total tiles to download:", total_tiles())

for zoom_level in range(minZoom, maxZoom):
    zoom_folder = base_folder_name + "/" + str(zoom_level)  # Convert number to string for folder name

    create_folder(zoom_folder)

    multiplier = 2 ** (zoom_level - minZoom)

    min_x_tile = minZoomMinX * multiplier
    max_x_tile = minZoomMaxX * multiplier
    min_y_tile = minZoomMinY * multiplier
    max_y_tile = minZoomMaxY * multiplier

    for x_tile_number in range(min_x_tile, max_x_tile):
        x_folder = zoom_folder + "/" + str(x_tile_number)

        create_folder(x_folder)

        for y_tile_number in range(min_y_tile, max_y_tile):
            y_folder = x_folder + "/" + str(y_tile_number)

            file_path = y_folder + ".png"
            # image_url in env

            download_image(image_url, file_path)

  