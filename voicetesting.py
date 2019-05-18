import speech_recognition as sr

bw = 'Black and white'

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say something')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if audio == bw:
            image1 = Image.open('roadster.jpg')

            #Convert from RGB to Black and White
            image2 = image1.convert('L')

            #Save Image in the Folder
            image2.save('roadster1.png')

            #Displays images in an image app
            image2.show()
            image1.show()







    except:
        print("Could not recognize your voice")
