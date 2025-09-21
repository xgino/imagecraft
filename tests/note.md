# Run ALL tests
pytest -v

# Run tests inside one file
pytest tests/test_utils.py -v

# Run one test function
pytest tests/test_utils.py::test_resize_to_square -v

# Stop at first failure
pytest -x

# Show print() and verbose logs
pytest -s -v


# Install package localy
pip install -e .