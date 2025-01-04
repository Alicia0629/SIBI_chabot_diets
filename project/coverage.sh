#!/bin/bash

coverage run -m pytest
coverage report
coverage html

xdg-open htmlcov/index.html

