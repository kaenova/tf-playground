lab:
	jupyter-lab --ContentsManager.allow_hidden=True

lib:
	pip install -r requirements.txt
	jupyter labextension install @jupyterlab/debugger @jupyterlab/toc
