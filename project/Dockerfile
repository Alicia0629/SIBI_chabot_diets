# Miniconda image
FROM continuumio/miniconda3

#Install dependecies
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    libopenblas-dev \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y xdg-utils && rm -rf /var/lib/apt/lists/*

# Set up conda environment
COPY conda-env/environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
ENV PATH /opt/conda/envs/diet-recommender/bin:$PATH

# Copy files of the project
WORKDIR /app
COPY . .

# Make python search the modules
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Default run
CMD ["make", "run"]

