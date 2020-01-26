# topsis-python
# Package Description : 
Python package for TOPSIS (The Technique for Order of Preference by Similarity to Ideal Solution) ALGORITHM.  
# Motivation :   
This is a part of project - I made for UCS633 - Data analytics and visualization at TIET.     
@Author : Sourav Kumar    
@Roll no. : 101883068    
# Algorithm :    
### STEP 1 :    
Create an evaluation matrix consisting of m alternatives and n criteria, with the intersection of each alternative and criteria.

### STEP 2 :   
The matrix is then normalised using the norm.

### STEP 3 : 
Calculate the weighted normalised decision matrix.

### STEP 4 : 
Determine the worst alternative and the best alternative.

### STEP 5 :
Calculate the L2-distance between the target alternative i and the worst condition.

### STEP 6 : 
Calculate the similarity to the worst condition.

### STEP 7 : 
Rank the alternatives according to final performance scores.   

### Getting started Locally :  
> Run On Terminal       
```python -m topsis.topsis <filename.csv> <weights> <impacts>```   
  ex. python python -m topsis.topsis topsis.csv 0.25,0.25,0.25,0.25 -,+,+,+     
  
> Run In IDLE   
```from topsis import topsis```      
```t = topsis.topsis('filepath', [list of weights], [list of impacts])```    
```t.topsis_main()```  

> Run on Jupyter   
Open terminal (cmd)   
```jupyter notebook```   
Create a new python3 file.     
If file <filename.csv> doesn't exists, then make sure to upload the file to jupyter env.    
```from topsis import topsis```      
```t = topsis.topsis('filepath', [list of weights], [list of impacts])```    
```t.topsis_main()``` 

* ```topsis_main()``` has been specifically designed to inhibit leakeage of inbuilt functions.  
* ```topsis_main(debug=True)``` use this to display all the intermediate matrices.   
* Make sure that ```filename.csv``` is in same directory where package is installed.
### PAPER : 
Find the research paper at [arxiv](https://arxiv.org/ftp/arxiv/papers/1412/1412.5077.pdf).

### OUTPUT :
Prints out the best model / alternative.

![output result on jupyter](/images/t.JPG)
![output result on idle](/images/t1.JPG)
![output result on cmd](/images/t2.JPG)

