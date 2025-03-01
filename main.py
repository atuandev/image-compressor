import os
from PIL import Image

# Mapping for correct image format names required by Pillow
OUTPUT_FORMAT_MAPPING = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "webp": "WEBP"
}

def optimize_images(
        folder_path: str,
        input_image_types: str = "jpg,png",  # Default value is "jpg,png"
        output_image_type: str = None,
        output_folder: str = None
):
    # "jpg, png" -> ["jpg", "png"]
    input_types = [ext.strip().lower() for ext in input_image_types.split(",")]

    # If no output folder is specified, use the input folder
    if not output_folder:
        output_folder = folder_path

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    total_original_size = 0
    total_optimized_size = 0
    processed_files = 0

    # Loop through files in the folder
    for filename in os.listdir(folder_path):
        input_ext = os.path.splitext(filename)[-1].lower().lstrip(".")
        if input_ext in input_types:
            input_path = os.path.join(folder_path, filename)
            
            # Get original file size
            original_size = os.path.getsize(input_path)
            total_original_size += original_size

            # Determine output extension: keep original if not specified
            output_ext = output_image_type if output_image_type else input_ext
            output_filename = os.path.splitext(filename)[0] + f".{output_ext}"
            output_path = os.path.join(output_folder, output_filename)

            # Get the correct format for Pillow
            output_format = OUTPUT_FORMAT_MAPPING.get(output_ext, output_ext.upper())

            try:
                # Open and optimize image
                with Image.open(input_path) as img:
                    img.save(output_path, format=output_format, optimize=True)
                    
                    # Get optimized file size
                    optimized_size = os.path.getsize(output_path)
                    total_optimized_size += optimized_size
                    processed_files += 1
                    
                    # Calculate compression ratio for this file
                    ratio = (1 - optimized_size / original_size) * 100
                    
                    print(f"Optimized: {input_path} -> {output_path}")
                    print(f"Size: {original_size/1024:.1f}KB -> {optimized_size/1024:.1f}KB (saved {ratio:.1f}%)")
                    
            except Exception as e:
                print(f"Failed to process {input_path}: {e}")

    if processed_files > 0:
        # Calculate overall compression ratio
        total_ratio = (1 - total_optimized_size / total_original_size) * 100
        print("\nSummary:")
        print(f"Total original size: {total_original_size/1024/1024:.2f}MB")
        print(f"Total optimized size: {total_optimized_size/1024/1024:.2f}MB")
        print(f"Overall compression ratio: {total_ratio:.1f}%")
        print(f"Processed {processed_files} files")


if __name__ == "__main__":
    folder_path = input("Input path: ")
    output_folder = input("Output path (Enter -> same input path): ") or None
    input_image_types = input("Input formats (Default: jpg,png): ") or "jpg,png"
    output_image_type = input("Output format (Enter -> keep origin format): ") or None

    optimize_images(folder_path, input_image_types, output_image_type, output_folder)