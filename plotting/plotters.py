import numpy as np
import seaborn as sns
import pandas as pd
from definitions import PROJ_DIR
import matplotlib.pyplot as plt
from glob import glob
import datetime as dt

TESTING = True

def plot_hit_line(project):
    hit_records = sorted(glob(str(PROJ_DIR / project / 'HitRecords' / '*.csv')))
    n_records = len(hit_records)
    fig, axes = plt.subplots(n_records, 1, figsize=(8.5, 2*n_records))
    axes = axes.flatten()
    for i, hr in enumerate(hit_records):
        df = pd.read_csv(hr)
        df['datetime'] = pd.to_datetime(df['time_ms'], unit='ms') - dt.timedelta(hours=5)
        sns.lineplot(df, x='datetime', y='count', ax=axes[i], linewidth=0.5)
        axes[i].axhline(y=20.0, color='r', linestyle='--')
    fig.suptitle(f'Spawning Activity for {project}')
    fig.tight_layout()
    fig.savefig(PROJ_DIR / project / 'HitRecords' / 'hit_plot.pdf')


def plot_hit_scatter(project):
    hit_records = sorted(glob(str(PROJ_DIR / project / 'HitRecords' / '*.csv')))
    n_records = len(hit_records)
    fig, axes = plt.subplots(n_records, 1, figsize=(8.5, 2*n_records))
    axes = axes.flatten()
    for i, hr in enumerate(hit_records):
        df = pd.read_csv(hr)
        df['datetime'] = pd.to_datetime(df['time_ms'], unit='ms') - dt.timedelta(hours=5)
        df['above_thresh'] = df['count'] >= 20
        sns.scatterplot(df, x='datetime', y='count', ax=axes[i], linewidth=0, size=2, hue='above_thresh', alpha=0.25, legend=False)
        axes[i].axhline(y=20.0, color='r', linestyle='--')
    fig.suptitle(f'Spawning Activity for {project}')
    fig.tight_layout()
    fig.savefig(PROJ_DIR / project / 'HitRecords' / 'hit_scatter.pdf')


