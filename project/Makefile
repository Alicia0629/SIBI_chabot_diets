DOCKER_IMAGE=sibi_chatbot
DOCKER_RUN=docker run -it -v $(shell pwd)/data:/app/data -v $(shell pwd)/htmlcov:/app/htmlcov -p 8000:8000 $(DOCKER_IMAGE)
PYTHON_RUN=$(DOCKER_RUN) python3

.PHONY: build run tests clean help



build:
	docker build -t $(DOCKER_IMAGE) .

	$(DOCKER_RUN) mkdir -p /app/data/datasets

	$(PYTHON_RUN) data/prep_scripts/createDatasetAllergies.py
	$(PYTHON_RUN) data/prep_scripts/dowloadFoodDataset.py
	$(PYTHON_RUN) data/prep_scripts/newFoodDataset.py
	$(PYTHON_RUN) data/prep_scripts/createTestRecipesDataset.py
	$(PYTHON_RUN) data/prep_scripts/createEmbbedingsPickle.py
	
	make clean-used-dockers

run:
	$(DOCKER_RUN) streamlit run ui/web.py
	make clean-used-dockers

tests:
	$(PYTHON_RUN) tests/run_tests.py
	make clean-used-dockers

clean-used-dockers:
	docker container prune -f

clean:
	sudo docker builder prune

help:
	@echo "Uso del Makefile:"
	@echo "  make build                 - Construir la imagen Docker"
	@echo "  make run                   - Ejecutar la aplicación web"
	@echo "  make tests                 - Ejecuta test en distintos métodos"
	@echo "  make clean                 - Limpiar todos los archivos en Docker"


