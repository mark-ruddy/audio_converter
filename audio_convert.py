import os
import sys
import tkinter as tk
from tkinter import filedialog

from pydub import AudioSegment

supported_exts = ['mp3', 'ogg', 'wav', 'aac', 'mp4']

print('Pydub Audio Converter'.center(40, '-'))
print('Currently supported formats:')
for supp in supported_exts:
    print(supp + '  ', end='')
print('\n')

root = tk.Tk()
root.withdraw()

print('File selector opening - please only select supported filetypes.\n')
files = filedialog.askopenfilenames(parent=root, title='Select Audio Files To Convert')

if not files:
    print('No files selected, quitting.')
    sys.exit(0)

for f in files:
    print(os.path.basename(f))
print('\nThe selected files are ready to be converted.')

ext_selected = False
while not ext_selected:
    new_ext = input('Enter the filetype to convert to: ')
    print()
    new_ext.strip()
    if new_ext[0] == '.':
        new_ext = new_ext[1:]
    if new_ext not in supported_exts:
        print(f'{new_ext} is not a valid extension, please enter a supported extension.')
        continue
    else:
        print(f'Beginning conversion...\n')
        ext_selected = True

errors = 0
for file in files:
    current_file = os.path.splitext(file)[0]
    current_ext = os.path.splitext(file)[1]
    current_ext = current_ext[1:]

    basename = os.path.basename(file)
    no_ext = basename.split('.')[0]

    if current_ext not in supported_exts:
        errors += 1
        print(f'\nERROR: for file: {current_file}.{current_ext}')
        print(f'File Type {current_ext} is not supported, moving on to next file.\n')
        continue

    print(f'CONVERTING - \'{basename}\' to \'{no_ext}.{new_ext}\': ', end='')
    current_audio = AudioSegment.from_file(file, format=current_ext)
    if new_ext == 'aac':
        current_audio.export(f'{no_ext}.{new_ext}', format='adts')
    else:
        current_audio.export(f'{no_ext}.{new_ext}', format=f'{new_ext}')

    print('DONE')

if errors == 0:
    print('\nAll files converted successfully')
elif len(files) > 1 and errors < len(files):
    print(f'\nSome Files Converted - {errors} Errors (wrong file extension)')
else:
    print(f'\n{errors} Errors (wrong file extension)')
