"""  audio record using Pyhton

Name  : Yash vyavahare
mail  : yashvyawahare02@gmail.com
"""
"Ya Download karna padenga 2 files"
"""
install: 
 $ pip install sounddevice
 $ pip install scipy
"""

import sounddevice as sd
from scipy.io.wavfile import write

sample_rate = 44100   # Sample rate
duration = 3          # Duration in seconds

recorder = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()                                   # Wait until recording is finished
write('output.wav', sample_rate, recorder)  # Save as WAV file 