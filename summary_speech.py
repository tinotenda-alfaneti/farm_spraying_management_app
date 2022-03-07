import pyttsx3

class ReadSummary:

    def __init__(self, message_to_read):
        self.engine = pyttsx3.init(driverName=None, debug=True)
        self.message = message_to_read

    def read_aloud(self):

        self.engine.say(self.message)

        # set voice speed
        self.engine.setProperty("rate", 10)

        # get available voices
        voices = self.engine.getProperty("voices")

        # selecting the voice
        self.engine.setProperty("voice", voices[0].id)

        self.engine.runAndWait()

# test_voice_output = ReadSummary("The message to be read will be here")
# test_voice_output.read_aloud()


