import os

base_dir = os.path.dirname(os.path.abspath(__file__))

MODEL_CLS_PATH = os.path.join(base_dir, 'model.py')
MODEL_CLS_NAME = 'ViewModality'
MODEL_LOAD_ARGS = {
    'data_dir': os.path.join(base_dir, 'data-vol'),
}
