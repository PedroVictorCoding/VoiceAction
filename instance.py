import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say a command to edit')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print('Sorry could not recognize your voice')




#Grabs Image from the same folder and displays it
#image1 = Image.open('roadster.jpg')

#Convert from RGB to Black and White
#image2 = image1.convert('L')

#Save Image in the Folder
#image2.save('roadster1.png')

#Displays images in an image app
#image2.show()
#image1.show()



#TODO LIST
#Feed Image from the exterior
