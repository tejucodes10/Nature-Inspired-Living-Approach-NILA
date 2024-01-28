.PHONY: init run request push_first_event push_second_event

init:
	@echo "Installin Python Poetry and Python dependencies inside a virtual environment"
	curl -sSL https://install.python-poetry.org | python3 -
	poetry env use $(shell which python3.10) && \
	poetry install

run:
	@echo "Starting The Route Optimization Bot"
	poetry run python src/app.py

request:
	@echo "Sending A Request To The Route Optimization Bot"
	curl --data '{"user": "user", "query": "Do I have any meeting tomorrow? Notify me about changes, please"}' http://localhost:8080/


push_first_event:
	@echo "Pushing first event to the Model"
	cp ./data/first_event.jsonl ./data/events/
	
push_second_event:
	@echo "Pushing second event to the Model"
	cp ./data/second_event.jsonl ./data/events/