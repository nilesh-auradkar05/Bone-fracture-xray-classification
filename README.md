# End-TO-End Bone-fracture-xray-classification

# About

The goal of creating this project was to learn how to implement end-to-end MLOps in practice. As a result, the machine learning pipeline was built that fine-tunes a pre-trained model and the web application for detecting fracture in bones in a photo that interacts with the model via an API. This repository contains the source code of the pipeline, including the source code of the web app and API, and some of its run results, which are needed to reproduce the pipeline and demonstrate its work.

# Installation

### First, clone the repository and go to it's root directory.

```bash
https://github.com/nilesh-auradkar05/Bone-fracture-xray-classification.git
```

### Then, create a virtual environment with python 3.10 and activate the environment.

#### Conda environment

```bash
conda create -n bone-fracture-classification python==3.10 -y
```

```bash
conda activate bone-fracture-classification
```

#### Python environment creation

```bash
python -m venv bone-fracture-classification
                OR
python3 -m venv bone-fracture-classification
```

```bash
bone-fracture-classification\Scripts\activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

```bash
Now, open the local host and port
```
