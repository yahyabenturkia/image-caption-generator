# src/utils.py
from PIL import ImageDraw, ImageFont

def wrap_lines(draw, text, font, max_width):
    """
    Wrap text into multiple lines so it fits within max_width.
    Returns a list of lines.
    """
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + w + " ").strip() + " "
        bbox = draw.textbbox((0, 0), test, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            line = test
        else:
            if line:
                lines.append(line.strip())
            line = w + " "
    if line:
        lines.append(line.strip())
    return lines

def draw_caption(image, caption, font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    """
    Draw caption on the image with a bottom black box, auto-wrapped and centered.
    Returns the image with the caption.
    """
    draw = ImageDraw.Draw(image)

    # Start font size proportional to image height
    font_size = max(20, image.height // 15)
    font = ImageFont.truetype(font_path, font_size)

    # Layout constraints
    side_margin = 20
    max_text_width = image.width - 2 * side_margin
    line_spacing = 10
    box_padding_x = 16
    box_padding_y = 12
    bottom_margin = 20
    max_block_ratio = 1/3

    # Wrap and shrink font until block fits
    while True:
        lines = wrap_lines(draw, caption, font, max_text_width)
        line_bboxes = [draw.textbbox((0, 0), ln, font=font) for ln in lines]
        line_heights = [(b[3] - b[1]) for b in line_bboxes]
        line_widths  = [(b[2] - b[0]) for b in line_bboxes]
        text_width   = max(line_widths) if line_widths else 0
        text_height  = sum(line_heights) + line_spacing * (len(lines) - 1)
        block_height = text_height + 2 * box_padding_y
        if block_height <= image.height * max_block_ratio or font_size <= 10:
            break
        font_size -= 2
        font = ImageFont.truetype(font_path, font_size)

    # Compute box position
    box_width  = text_width + 2 * box_padding_x
    box_height = text_height + 2 * box_padding_y
    x_box = max(side_margin, (image.width - box_width) // 2)
    y_box = image.height - bottom_margin - box_height

    # Draw black rectangle behind all lines
    draw.rectangle(
        [x_box, y_box, x_box + box_width, y_box + box_height],
        fill="black"
    )

    # Draw each line centered inside the box
    y_text = y_box + box_padding_y
    for h, w, ln in zip(line_heights, line_widths, lines):
        x_text = x_box + (box_width - 2 * box_padding_x - w) // 2 + box_padding_x
        draw.text((x_text, y_text), ln, font=font, fill="white")
        y_text += h + line_spacing

    return image
