# Sorting Algorithms - readme.txt

Files Included With This Project:
 
      sort_Bubble.py    sort_Selection.py       Tester_sort.py
      
  * sort_Bubble.py sorts an array of numbers from lowest to highest using the Bubble Sort Method <br>
  * sort_Selection.py sorts an array of numbers from lowest to highest using the Selection Sort Method <br>
  * Tester_sort.py compares the speed of sort_Bubble.py, sort_Selection.py and an online solution for the Bubble Sort method  <br>

## How To Run "Sorting Algorithms":

  1) Ensure all project files are within the same directory
  2) All files can be ran individually from the command line or in the IDE of choice

## Notes on project:
 
  sort_Bubble.py has similar performance to an online solution but it's speed seems to fluctuate at higher number of cycles when tested with timeit <br>
  Between these 2 scripts, sort_Selection is the superior (faster) selection method when compared using timeit <br>
  
  Given an array [12,11,13,5,6,7,5,11,13,5,6,7,11,13,5,6,7,11,13,5,6,7], the follow timings were obtained using timeit for 1,000,000 cycles: <br>
  
  sort_Bubble.py              : 49.33 seconds <br>
  Bubble Sort online solution : 50.52 seconds <br>
  sort_Selection.py           : 30.23 seconds <br>
