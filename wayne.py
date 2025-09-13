from PIL import Image, ImageDraw, ImageFont

# Create canvas
W, H = 600, 700
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

center_x = W // 2

# --- TROPHY USING ONLY ARC, RECTANGLE, POLYGON ---

# Cup (arc for bowl)
cup_bbox = [center_x-150, 200, center_x+150, 400]
draw.arc(cup_bbox, start=0, end=180, fill="gold", width=6)

# Cup body (polygon)
cup_body = [
    (center_x-150, 300),
    (center_x-100, 450),
    (center_x+100, 450),
    (center_x+150, 300)
]
draw.polygon(cup_body, fill="gold", outline="black")

# Neck (rectangle)
draw.rectangle([center_x-40, 450, center_x+40, 500], fill="gold", outline="black")

# Base (rectangle)
draw.rectangle([center_x-100, 500, center_x+100, 550], fill="black", outline="black")
draw.rectangle([center_x-70, 550, center_x+70, 580], fill="gray", outline="black")

# Handles (polygon left + right)
left_handle = [(center_x-150, 250), (center_x-200, 200), (center_x-180, 180), (center_x-140, 230)]
right_handle = [(center_x+150, 250), (center_x+200, 200), (center_x+180, 180), (center_x+140, 230)]
draw.polygon(left_handle, fill="gold", outline="black")
draw.polygon(right_handle, fill="gold", outline="black")

# --- TEXT ---
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
except:
    font = ImageFont.load_default()

text = "Overall Champion"

# ✅ Use textbbox instead of textsize
bbox = draw.textbbox((0, 0), text, font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

draw.text((center_x - w//2, 50), text, font=font, fill="black")

# Save and show
#img.save("CSELEC SAlUBREJOHNWAYNE Activity1.png")
img.show()
