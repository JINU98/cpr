# Causal Process Knowledge-Infused Reasoning (CPR)

CPR is a novel approach that combines machine learning models with causal process knowledge structures to create explainable and reliable AI systems. By infusing domain-specific causal knowledge into the learning process, CPR enables the generation of interpretable predictions that can be audited and refined by subject matter experts.

## Overview

The CPR framework consists of the following components:

1. **Causal Process Knowledge Structure**: A representation of the domain-specific causal processes and relationships between concepts, typically in the form of a tree or graph structure.
2. **CPR Function Approximation**: A machine learning model that learns to map the input data to target outcomes while being constrained by the causal process knowledge structure.

By leveraging the causal process knowledge structure, CPR can provide human-understandable explanations for its predictions, tracing the causal reasoning process and enabling iterative refinement with domain experts in the loop.

## Key Features

- **Explainable Predictions**: CPR generates predictions accompanied by explanations that follow the causal process knowledge structure, making the reasoning process transparent and interpretable.
- **Domain Knowledge Integration**: CPR incorporates domain-specific causal knowledge into the learning process, ensuring that the model's predictions align with established domain principles and frameworks.
- **Open-Source and Extensible**: The CPR library is open-source and designed to be extensible, allowing researchers and practitioners to build upon and contribute to its development.

## Installation

To install the CPR library, you can use pip: ```pip install cpkil```


## Usage

Import the PKiL library First, ensure that you have installed the PKiL (Process Knowledge-infused Learning) library.

```python 
from PKiL import ProKnow

```

Prepare the concept and annotation files The PKiL library requires two files to load the causal process knowledge:
concepts_file.txt: This file should contain a list of concepts or entities relevant to your domain, each on a new line.
annotatation.txt: This file should contain the causal relationships or annotations between the concepts, represented in a structured format specified by the library documentation.
Modify the code snippet Replace 'concepts_file.txt' and 'annotatation.txt' in the process_knowledge method call with the actual filenames of your concept and annotation files, respectively.



```python 
pk1.process_knowledge('your_concepts_file.txt', 'your_annotation_file.txt')
```
Provide the input data Modify the test_point variable to hold the input data you want to evaluate using the causal process knowledge. This could be a text string, a file path, or any other data format supported by the library.


```python
test_point = 'This is a sample input text.'
```
Run the code Execute the code snippet, which will load the causal process knowledge, evaluate the input data (test_point), and return the predicted label and explanation (if explanation=True).

```python
label = pk1.evaluate_pk(test_point, explanation=True)
print(f"Predicted label: {label}")
```
Interpret the results The label variable will contain the predicted label for the input data based on the causal process knowledge. If explanation=True, the evaluate_pk method should also provide an explanation for the predicted label, which you can print or analyze as needed.


```python
test_point = "This is a sample input text."  

from PKiL import ProKnow

pk1 = ProKnow()
pk1.process_knowledge('your_concepts_file.txt', 'your_annotation_file.txt')

#test_point = test_point

label = pk1.evaluate_pk(test_point,explanation=True)
```
