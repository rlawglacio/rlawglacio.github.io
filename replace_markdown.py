import re
import os
import sys
from pathlib import Path

os.chdir(os.path.dirname(sys.argv[0]))

# Path to your markdown file
input_md = "photos.md"
output_md = "photos_html.md"

# Regex to match Markdown image and caption pairs
pattern = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\((?P<path>\.\/assets\/img\/(?P<filename>[^)]+))\)\n\*(?P<caption>.*?)\*",
    re.MULTILINE,
)

# Responsive image template
template = """<figure>
  <img 
    src="./assets/img/resized/{base}-800.{ext}" 
    srcset="
      ./assets/img/resized/{base}-400.{ext} 400w,
      ./assets/img/resized/{base}-800.{ext} 800w,
      ./assets/img/resized/{base}-1200.{ext} 1200w
    " 
    sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 800px"
    alt="{alt}">
  <figcaption><em>{caption}</em></figcaption>
</figure>
"""

# Read input markdown
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

# Replace all markdown-style images with responsive HTML
def replace_func(match):
    alt = match.group("alt").strip()
    path = match.group("path").strip()
    caption = match.group("caption").strip()

    filename = match.group("filename")
    base, ext = filename.rsplit(".", 1)

    return template.format(base=base, ext=ext, alt=alt, caption=caption)

new_content = pattern.sub(replace_func, content)

# Write to new file
with open(output_md, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Converted markdown saved to: {output_md}")
