# from yolov5.detect import run as run_detection
from plotting import plotters

pipe_weights = 'justpipe.pt'
fish_weights = 'justfish.pt'


def detect(source, weights, device=0, save_txt=True, **kwargs):
    run_detection(source=source, weights=weights, device=device, save_txt=save_txt, **kwargs)



