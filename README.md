# topsis-python
# Package Description : 
Python package for TOPSIS (The Technique for Order of Preference by Similarity to Ideal Solution) ALGORITHM.  
# Motivation :   
This is a part of project - I made for UCS633 - Data analytics and visualization at TIET.
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
```python topsis.py <filename.csv> <weights> <impacts>```   
  ex. python topsis.py topsis.csv 0.25,0.25,0.25,0.25 -,+,+,+     
  
> Run In IDLE   
```from topsis import topsis```      
```t = topsis.topsis('filepath', [list of weights], [list of impacts])```    
```t.topsis_main()```        
```t.display()```     

### PAPER : 
Find the research paper at [arxiv](https://arxiv.org/ftp/arxiv/papers/1412/1412.5077.pdf).

### OUTPUT :
Prints out the best model / alternative.

![output result](/images/t.JPG)
