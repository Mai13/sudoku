# Sudoku

This are different ways to solve the sudoku game

## Data

The data for this project was downloaded from (kaggle)[https://www.kaggle.com/rohanrao/sudoku], cuted the first 10 lines.

##Methods

There are many ways to solve a sudoku and the aim of this project is to try different ones.

### Sove it like a human

As the name says this is an algorithm that solves the suduku like a human being would. 
The idea behind is simple: save all the possible numbers that could be fitted instead of a 0 in every grid, and select the number for the grid with just one posibility. 

This method does not work for every sudoku, because is based on the idea that a every grid will have an spot with one only possibilty, which is not true. 