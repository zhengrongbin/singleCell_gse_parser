# singleCell_gse_parser
single cell data parser from GEO 

**Clone the repository and do as follow:**
1. make sure that MySQL is isntalled in your device, and you have the account to create a new database,   
if no, install one, or contact your manager
2. install a miniconda3 and create a environment:
```
conda create -n py3_geo python=3
conda activate py3_geo
```
3. install requirements
```
pip install -r requirments.txt
```
4. create a mysql database (named by yourself), and fill in the SQL file
5. revise the database name and password in in ./dc2/dc2/setting.py, using the one you just set
6. test your environment deploy, it is ok, if no error report when you run:
```
python env.py
```
7. run parser:
```
python scrna_parser_runner.py -h
```
