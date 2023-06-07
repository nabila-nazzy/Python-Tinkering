from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/Groups/David_Freddie.jpeg') # loads the image as a NUMPY Array
face_locations = face_recognition.face_locations(image) 
#Get's location of the faces.


# Loop through the face locations
for face_locations in face_locations:
    top, right, bottom, left = face_locations

    face_image = image[top:bottom, left:right]
    # Get the actual image ugising the PIL library.
    pil_image = Image.fromarray(face_image)
    #Simply Show the image
    #pil_image.show()
    
    # Save the images in the unknown file
    pil_image.save(f'{top}.jpg') # loops the images, and then cuts the faces and generates jpg's in the file.

    # The outputs when run are the files:
    # 77.jpg and 116.jpg for faces on David Bowie and Freddie Mercury

    #use [ python identify.py ] in the terminal to run.
