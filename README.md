# Sagittal Average Project

## Brief Introduction

This is a project of computing the average value of each collected brain sample data, stored in a file by rows.

## Installation

```bash
pip install git+git://github.com/Songzx07/sagittal_average.git
```

## Usage

Invoke the tool with sagittal_average_run <file_input> <file_output>

You can also use it in your own library:

```python
from sagittal_average import run_averages

run_averages(file_input="file_name",file_output="file_name")
```
