import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load('celloA3.mp3', sr=None)

cqt = librosa.core.cqt(y, sr=sr)
#librosa.display.specshow(librosa.amplitude_to_db(cqt, ref=np.max),
#                         sr=sr, x_axis='time', y_axis='cqt_note')
librosa.display.specshow(np.abs(cqt),
                         sr=sr, x_axis='time', y_axis='cqt_note')
plt.title('Constant-Q power spectrum')
plt.tight_layout()
