#!/bin/bash

# Set target widths
sizes=(400 800 1200)

# Directory with original images
input_dir="$HOME/Documents/_Bergen/everything_else/web/rlawglacio.github.io/assets/img"
output_dir="$input_dir/resized"

echo "Input directory: $input_dir"
echo "Output directory: $output_dir"
mkdir -p "$output_dir"

# Loop through all image files in the directory
for img in "$input_dir"/*.{jpg,jpeg,png,JPG,JPEG,PNG}; do
    # Skip if no files found
    [ -e "$img" ] || continue

    echo "Processing $img"
    filename=$(basename "$img")
    extension="${filename##*.}"
    name="${filename%.*}"

    for size in "${sizes[@]}"; do
        output="$output_dir/${name}-${size}.${extension}"
        echo "  -> Resizing to $size px → $output"

        # Only resize if output doesn't exist or is older
        if [ ! -f "$output" ] || [ "$img" -nt "$output" ]; then
            convert "$img" -resize "${size}" "$output"
            echo "     ✓ Created"
        else
            echo "     ⏩ Skipped (up to date)"
        fi
    done
done

