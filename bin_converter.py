# Open your text file and read the raw content
with open("fru.txt", "r", encoding="utf-8") as text_file:
    raw_text = text_file.read()

# Convert to binary
binary_data = raw_text.encode("utf-8")

# Save as your bin file
with open("0.bin", "wb") as bin_file:
    bin_file.write(binary_data)

print("Successfully converted input.txt to 0.bin!")