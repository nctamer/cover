import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load('banderas.mp3', sr=None)

cqt = librosa.amplitude_to_db(librosa.core.cqt(y, sr=sr))
librosa.display.specshow(cqt, sr=sr, x_axis='time', y_axis='cqt_note')
plt.title('Constant-Q power spectrum')
plt.tight_layout()

onset = librosa.onset.onset_strength_multi(S=cqt, sr=sr, max_size=84)
librosa.display.specshow(onset, sr=sr, x_axis='time', y_axis='cqt_note')
