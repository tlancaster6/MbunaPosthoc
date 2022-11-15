import seaborn as sns
import pandas as pd
from definitions import PROJ_DIR

def plot_hit_records(project):
    hit_records = (PROJ_DIR / project / 'HitRecords').iterdir()
    df = pd.concat([pd.read_csv(hr) for hr in hit_records])
    return df