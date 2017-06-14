import nbformat
from nbconvert import PythonExporter

def convertNotebook(notebookPath, modulePath):

  with open(notebookPath) as fh:
    nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

  exporter = PythonExporter()
  source, meta = exporter.from_notebook_node(nb)

  with open(modulePath, 'w+') as fh:
    fh.writelines(source.encode('utf-8'))

convertNotebook(/Users/marcello/GitHub/MachineLearning/Iris/Iris.ipynb,/Users/marcello/GitHub/MachineLearning/Iris/Iris.py)

