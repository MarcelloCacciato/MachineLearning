from nbformat import current as nbformat
from nbconvert import PythonExporter

filepath = '/Users/marcello/GitHub/MachineLearning/Iris/Iris.ipynb'
export_path = '/Users/marcello/GitHub/MachineLearning/Iris/Iris.py'

with open(filepath) as fh:
    nb = nbformat.reads_json(fh.read())

exporter = PythonExporter()

# source is a tuple of python source code
# meta contains metadata
source, meta = exporter.from_notebook_node(nb)

with open(export_path, 'w+') as fh:
    fh.writelines(source)
a
