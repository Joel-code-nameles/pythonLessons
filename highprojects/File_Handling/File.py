import pyttsx3

def voiceAI(voice):
    voice_engine = pyttsx3.init()
    voice_speaker = voice_engine.say(voice(1))
    voice_engine.runAndWait()
    return voice_speaker

def fileloader():
    file_dir = 'File_Handling\myfile.txt'
    with open(file_dir,'rt') as myfile:
        filename = myfile.read()
    return voiceAI(filename)


if __name__ == '__main__':
    fileloader()