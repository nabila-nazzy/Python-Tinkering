import face_recognition

Araki_face_image = face_recognition.load_image_file('./img/known/Hirohiko_Araki.jpg')
# get face encoding, these are the facial features scanned that can be used to compare with other images to match.
Araki_face_encoding = face_recognition.face_encodings(Araki_face_image) [0]

#---------------------------------------------------------------------------


#need an image to compare it to.
#unknown_face_image = face_recognition.load_image_file('./img/unknown/Hirohiko_Araki_2.jpg')
#unknown_face_encoding = face_recognition.face_encodings(unknown_face_image) [0] #pass in the unknown image

#different image test, comment out later.
unknown_face_image = face_recognition.load_image_file('./img/unknown/Soekarno_2.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_face_image) [0] #testing a different image without Araki (results will not match)


#---------------------------------------------------------------------------

# Time to compare the faces to print the matched up results.

# match the face encodings with each other.
results = face_recognition.compare_faces([Araki_face_encoding], unknown_face_encoding)

#check with true or false values.
if results[0]:
    print('This is definitely Araki :]')
else:
    print('This is NOT Araki.')

    #use [ python facematch.py ] in the terminal to run.
