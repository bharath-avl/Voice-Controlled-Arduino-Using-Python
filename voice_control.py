import speech_recognition as sr
import serial

ser = serial.Serial('COM4', 9600)

def process_speech(text):
    text_lower = text.lower()
    if text_lower == 'goodbye' or text_lower == 'good bye' or text_lower == 'bye':
        ser.write(b'2')
    elif text_lower == 'good morning' or text_lower == 'thank you' or text_lower == 'thankyou' or text_lower == 'morning':
        ser.write(b'1')
    elif text_lower == 'how are you':
        ser.write(b'3')
    elif text_lower == 'where are you from' or text_lower == 'are you from':
        ser.write(b'4')
    elif 'drink water' in text_lower or 'drink' in text_lower or 'water' in text_lower:
        ser.write(b'5')
    elif text_lower == 'i am fine':
        ser.write(b'6')
    elif text_lower == 'lunch':
        ser.write(b'7')
    elif text_lower == 'welcome':
        ser.write(b'8')
    elif text_lower == 'we are from vit ap' or text_lower == 'ap':
        ser.write(b'9')

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print('Say something')
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                process_speech(text)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except KeyboardInterrupt:
                print("Exiting...")
                break

if __name__ == "__main__":
    main()
