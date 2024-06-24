test:
	python -m unittest discover -s tests -p 'test_*.py'

start_server:
	python main.py

cli_info:
	flask cv-info