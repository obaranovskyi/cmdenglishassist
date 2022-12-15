from pydub import AudioSegment
from gtts import gTTS
from io import BytesIO


class AudioGenerator:

    def __init__(self):
        self.original_lang = 'en'
        self.translation_lang = 'uk'

    def convert(self, words):
        combined = AudioSegment.empty()
        for word in words: 
            combined += self.convert_word(word)
        output_filename = f"{self.translation_lang}_{self.original_lang}.mp3"
        combined.export(output_filename, format="mp3")
        combined = AudioSegment.empty()

    def convert_word(self, word):
        translation_mp3 = self.word_to_audio_segment(word.get('translation'), self.translation_lang)
        original_mp3 = self.word_to_audio_segment(word.get('original_value'), self.original_lang)
        two_sec_silence = AudioSegment.silent(duration=2000)
        five_sec_silence = AudioSegment.silent(duration=5000)
        mp3_to_combine = [
            translation_mp3,
            five_sec_silence,
            original_mp3,
            two_sec_silence
        ]
        combined = AudioSegment.empty()
        for mp3 in mp3_to_combine:
            combined += mp3
        return combined

    def word_to_audio_segment(self, value, lang):
        mp3_fp = BytesIO()
        audio_obj = gTTS(text=value, lang=lang, slow=False)
        audio_obj.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return  AudioSegment.from_mp3(mp3_fp)

