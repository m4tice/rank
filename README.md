# rank
A CLI application that produces a point table based on matches.  
Supported OS: Linux  

# how to run
Clone the repository and run the following lines: 
```
source .\venv\bin\activate
rank -i <input_file.txt>
```
Example:  
```
rank -i data\sample-input.txt  
```

# Application architecture  
The application is designed to be a ETL pipeline with 3 phases:
* Extract: extract data from text file into a list  
* Transform: transform the extracted data to the required format  
* Load: load the result into a text file  

<p align="center">
  <img src="https://github.com/m4tice/rank/blob/main/assets/rank_structure.png" width="700">
</p>

# Extract  
Homepage  
<p align="center">
  <img src="https://github.com/m4tice/rank/blob/main/assets/extract.png" width="700">
</p>

# Transforms  
<p align="center">
  <img src="https://github.com/m4tice/rank/blob/main/assets/transform.png" width="700">
</p>

# Load  
<p align="center">
  <img src="https://github.com/m4tice/rank/blob/main/assets/load.png" width="700">
</p>
