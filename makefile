python:
	python3 -B main.py

docker:
	docker build -t gen .

rd:
	docker run -it --rm gen