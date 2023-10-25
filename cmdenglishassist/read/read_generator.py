from datetime import datetime
from pydub import AudioSegment
from gtts import gTTS
from io import BytesIO
from ..shared.date_core import format_dt
from ..shared.read_markdown import read_markdown_lines


class ReadGenerator:

    def __init__(self):
        self.lang = 'en'
        self.date = format_dt(datetime.now()).replace(' ', '_')

    def convert(self, filename):
        markdown_lines = read_markdown_lines(filename)
        output_filename = f"{filename.split('.')[0]}.mp3"
        combined = AudioSegment.empty()
        for index, ml in enumerate(markdown_lines):
            if len(ml) == 1 and '\n' in ml:
                continue
            if '#' in ml:
                if index != 0:
                    combined += self.make_pause()
                ml = self.prepare_text(ml)
            combined += self.convert_text(ml)
        combined.export(output_filename, format="mp3")
        combined = AudioSegment.empty()

    def prepare_text(self, text):
        return text.replace('#', '')

    def make_pause(self, pause_duration=2000):
        combined = AudioSegment.empty()
        combined += AudioSegment.silent(duration=pause_duration)
        return combined
        
    def convert_text(self, text):
        audio = self.word_to_audio_segment(text)
        mp3_to_combine = [
            audio,
            self.make_pause()
        ]
        combined = AudioSegment.empty()
        for mp3 in mp3_to_combine:
            combined += mp3
        return combined

    def word_to_audio_segment(self, value):
        mp3_fp = BytesIO()
        audio_obj = gTTS(text=value, lang=self.lang, slow=False, tld='us')
        audio_obj.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return  AudioSegment.from_mp3(mp3_fp)

