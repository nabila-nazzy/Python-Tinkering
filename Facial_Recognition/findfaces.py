import face_recognition

image = face_recognition.load_image_file('./img/Groups/King_Crimson.png') # loads the image as a NUMPY Array
#Get's location of the faces.
#The Beatles = 4
#King Crimson = 7
face_locations = face_recognition.face_locations(image) 

#Gets an array of coordinates for each face.
#print(face_locations)

#find the number of people in an image
print(f'There are {len(face_locations)} people in this image')

    #use [ python findfaces.py ] in the terminal to run.
