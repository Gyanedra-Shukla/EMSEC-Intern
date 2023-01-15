import numpy as np
import pandas as pd

file=pd.read_csv('IMDB Dataset.csv')
file=file.head(200)
w = pd.DataFrame({ 'Review': file['review']})
w.to_csv('IMDB_raw_data.csv', index=False)