import numpy as np
import pandas as pd

encrypted_text = '''ХВ С Н АСЕУЭТАЬСИТ М ЕИНРЬЕ ЕСЕКЛЕ ИКЕОТЧКЛЫЛ 
НГВВОЕ О ЬТЗО ОК ИЛОЫААНР ЕЗННБА,И Т КИМКЮЗОЬЛПВОАТЬ ххххЯхххххС'''
string = list(encrypted_text)
reshaped_text = np.array(encrypted_text).reshape(1, -1)
frame_pd = pd.DataFrame()
reshaped_text = pd.DataFrame(reshaped_text)
frame_pd = pd.concat([frame_pd, reshaped_text])

print(frame_pd)
