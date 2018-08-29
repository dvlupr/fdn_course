# Darkweb Process
This file folder contains the final project for the foundations course in python.

There are three files:

1) create_mastercard_list.py: this file will only run on a windows machine and will create a list of 10,000 test mastercard files.
2) create_darkweb_list.py: this file will also only run on a windows machine and will create a list of fictious darkweb files.
3) darkweb_process.py: this file will slurp both of the output files in from the file folder, then compare and output files.

This process requires three commands:

```
python create_mastercard_list.py

python create_darkweb_list.py

python darkweb_process.py
```
If done properly, this process will run on it's own as an example of what would be needed to vet a list of provided darkweb mastercard numbers. 
