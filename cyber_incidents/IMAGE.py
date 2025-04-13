from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Set the image size
width, height = 1500, 1000
background_color = (30, 30, 30)
text_color = (255, 255, 255)
box_color = (50, 50, 50)

# Create a blank image
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load a font
font_path = "/path/to/your/font.ttf"  # Replace with a valid font file path
font_title = ImageFont.truetype(font_path, 40)
font_section = ImageFont.truetype(font_path, 30)
font_text = ImageFont.truetype(font_path, 20)

# Draw the header
draw.text((50, 20), "Feasibility & Viability of Cyber Incident Dashboard", font=font_title, fill=text_color)

# Draw rectangles for sections
draw.rectangle([50, 100, 700, 400], fill=box_color)
draw.rectangle([800, 100, 1450, 400], fill=box_color)
draw.rectangle([50, 450, 700, 800], fill=box_color)
draw.rectangle([800, 450, 1450, 800], fill=box_color)

# Add text for each section
draw.text((80, 120), "Technical Feasibility", font=font_section, fill=text_color)
draw.text((80, 160), "Integration of Dash, Plotly, AWS, MySQL, and AI.", font=font_text, fill=text_color)

draw.text((80, 300), "Operational Feasibility", font=font_section, fill=text_color)
draw.text((80, 340), "User-friendly interface, cloud platform.", font=font_text, fill=text_color)

draw.text((830, 120), "Market Demand", font=font_section, fill=text_color)
draw.text((830, 160), "High demand for real-time cybersecurity solutions.", font=font_text, fill=text_color)

draw.text((830, 300), "Scalability", font=font_section, fill=text_color)
draw.text((830, 340), "Cloud infrastructure scalability.", font=font_text, fill=text_color)

draw.text((80, 480), "Financial Feasibility", font=font_section, fill=text_color)
draw.text((80, 520), "Cost-effective, open-source solutions.", font=font_text, fill=text_color)

draw.text((830, 480), "Challenges", font=font_section, fill=text_color)
draw.text((830, 520), "Data privacy and security challenges.", font=font_text, fill=text_color)

# Footer
draw.text((50, 850), "Sustainability: Long-term adaptability, AI updates.", font=font_section, fill=text_color)

# Save the image
image.save("cyber_dashboard_feasibility.png")
image.show()
