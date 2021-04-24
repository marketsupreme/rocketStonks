all: models.html IDB3.log

models.html: models.py
	py -m pydoc -w models
	
IDB3.log:
	git log > IDB3.log
