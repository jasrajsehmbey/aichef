import cohere
import re

# Read the content of "afterdetect/currentfolder.txt"
with open("afterdetect/currentfolder.txt", 'r') as f:
    data = f.read()

# Extract the number and increment it
match = re.search(r'exp(\d+)', data)
numplusone = 0
if match:
    numplusone = int(match.group(1)) + 1

# Replace the old number with the new one
new_text = re.sub(r'exp\d+', f'exp{numplusone}', data)

# Write the updated content back to "currentfolder.txt"
with open("currentfolder.txt", 'w') as file:
    file.write(new_text)

print(f'Text written: {new_text}')

# # Get the prefix from "currentfolder.txt"
with open("currentfolder.txt", 'r') as f:
    prefix = f.read()

img_path = ""
img_path +=data+ "/test"+ str(numplusone-1)+".jpg" # Replace with the actual path or provide the path dynamically
img = img_path.split("/")[-1]

# Create the destination path for the txtfile
dot_index = img.rfind('.')
result = img[:dot_index] if dot_index != -1 else img
txtfile = result + ".txt"
mid = "/labels/"
destpath = f'{prefix}{mid}{txtfile}'
print(destpath)

# Initialize cohere client
co = cohere.Client('J4Syy5U88TUc8KxWiFsG8K3OQQqPRGOjQCWGIodj')

# Prepare the prompt message
premessage = "You are an expert chef. I will give you a list of ingredients separated by a comma followed by the flavour of the dish, and you will give me a recipe using all or most of them but not supplementing outside of what might appear on this list. If an ingredient is shown as None, ignore it. If flavour is any then ignore it. Give each recipe a catchy title, an approximate time to complete and a count of people served. Also like any recipe, include the ingredient portions in the list labelled Ingredients: and then the Instructions section as a numbered list. Here's the ingredient list:"
postmessage = ""
flavtext = ".Here's the flavour of the dish: "
with open(destpath, 'r') as file:
    postmessage = file.read()

# Get the flavour variable from the form or wherever it comes from
flavour = "sweet"

# Construct the message
message = f'{premessage}{postmessage}{flavtext}{flavour}'
# print(message)

# Generate response using cohere
response = co.generate(prompt=message)

# Print the response
print(response[0])
