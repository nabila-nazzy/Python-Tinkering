import face_recognition
from PIL import Image, ImageDraw
from face_recognition.api import face_encodings, face_locations
# Drawing Boxes on faces.

Bowie_face_image = face_recognition.load_image_file('./img/known/David_Bowie.jpg')
Bowie_face_encoding = face_recognition.face_encodings(Bowie_face_image) [0]
# Get face encoding, these are the facial features scanned that can be used to compare with other images to match.

# Need an image to compare it to.
Freddie_face_image = face_recognition.load_image_file('./img/known/Freddie_Mercury.jpg')
Freddie_face_encoding = face_recognition.face_encodings(Freddie_face_image) [0] #pass in the unknown image

# Create Array of the encodings and the names
known_face_encodings = [  #face encoding array
    Bowie_face_encoding,
    Freddie_face_encoding
]

known_face_names = [      # face names array
    "David Bowie",
    "Freddie Mercury"
]

# Load test images to find faces in
test_image = face_recognition.load_image_file('./img/Groups/David_Freddie.jpeg')

# Find the faces in the [test_image]
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)


# Convert to the PIL format so that the squares can be drawn on.
pil_image = Image.fromarray(test_image)

# Draw on the image by creating an Image Draw instance.
draw = ImageDraw.Draw(pil_image) 


# Loop through the faces on the test image.
for(top,right,bottom,left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    #If it matches
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw the box around the face.
    draw.rectangle(((left,top), (right,bottom)), outline=(255,255,255,255)) #draws a black box

    # Draw the box of the label.
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10),(right, bottom)), fill=(255,255,255,255), outline=(255,255,255,255)) #Black Label box

    #Draw the text
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0)) #White text!

del draw

# Display the Image!
pil_image.show()

#use [ python identify.py ] in the terminal to run.
