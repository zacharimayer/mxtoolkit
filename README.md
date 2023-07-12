# mxtoolkit

This repository is a collection of python scripts that allow DNS, MX, SMTP and SSL tests in bulk.

Requirements:
  - python 3.8+
  - pip
  - dnspython
  


  1. Download the code:
  
  ```git clone https://github.com/zacharimayer/mxtoolkit```
  ```cd mxtoolkit```
  
  2. Install packages:
  
  ```apt install python3-pip```
  ```pip install dnspython```
  
  3. Run the code:
  
  - cd to the mxtoolkit
  - Add the domains or targets into the text file in the directory
  - run the code with ```python3 main.py```
  - choose the adequate scan to you want to run
  
  4. Results
  
  The results are automatically exported to a txt file upon completion. 
  
  WARNING: If the script is used multiple times, it will override previous results if you do not save them.
