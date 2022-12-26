GitHub Readme
=====================================
Installation & Parallel Execution 
------------

To install grip, simply:

```console
-->To install
pip install -U selenium 
pip install webdriver-manager 
pip install pytest

-->To individual RUN

pytest Tests/test_GoogleSearch.py
pytest Tests/test_BingSearch.py
pytest Tests/test_YahooSearch.py

-->To Parallel Execution 
-->For same time opening of 3 browsers
pytest -n 3   