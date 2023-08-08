
import os
from gtts import gTTS
import playsound
import speech_recognition as sr

"""

    playsound: Python programlama dilinde ses çalmak için kullanılan bir modüldür.
    speech_recognition: Python programlama dilinde ses tanıma (speech recognition) işlemleri yapmak için kullanılan bir kütüphanedir.

"""

record_take = sr.Recognizer()


def listening():
    with sr.Microphone() as source:
        print("Dinliyorum ...")
        microphone = record_take.listen(source)
        sound = ""

        try:
            sound = record_take.recognize_google(microphone, language="tr-TR")

        except sr.RequestError:
            print("Asistan : Sistem şu an aktif değil.")

        except sr.UnknownValueError:
            print("Asistan : Konuşmanız şu an anlaşılmadı.")

        return sound  # Yakalanan ses metni döndürülmeli, source yerine sound döndürüldü.


captured_sound = listening()  # listening fonksiyonundan dönen ses metni captured_sound adlı değişkene atandı.

print("Yakalanan Ses:", captured_sound)  # captured_sound değişkeni ekrana yazdırıldı.
