import pandas as pd

# In order to run this, install the following:
# pip install python-snappy
# pip install pyarrow
# pip install fastparquet
df = pd.read_parquet('/Users/adamstreich/Desktop/2020-01-01_performance_fixed_tiles.parquet')
df.to_csv('/Users/adamstreich/Desktop/data506MOD.csv')