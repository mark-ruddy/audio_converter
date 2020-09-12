# audio_converter
Pydub Command-Line Audio Converter

Basic python audio converter, opens a file selector on launch to select audio files to be converted.
Uses https://github.com/jiaaro/pydub to convert the audio and places the converted audio in the current working directory.

Has some problems with conversion to AAC, ffmpeg requires a switch the format to "adts", which is then converted to AAC.
This seems to result in a lower sound quality AAC conversion.
