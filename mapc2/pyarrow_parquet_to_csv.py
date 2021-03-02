import pandas as pd

# In order to run this, install the following:
# pip install python-snappy
# pip install pyarrow
# pip install fastparquet
def read_parquet_to_csv(filepath):
    name = filepath.split('/')[-1].split('.parquet')[0]
    # name = name[-1]
    df = pd.read_parquet(filepath, engine='pyarrow') # OR engine='fastparquet'
    df.to_csv('./csv_data/'+name+'.csv')
    
# Replace file path here
read_parquet_to_csv('./parquet_files/2020-07-01_performance_fixed_tiles.parquet')