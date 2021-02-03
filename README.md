# LaticeProteins
A study of lattice proteins


Use simulated annealing (or any other optimization method of your choice) to solve the lattice protein structure prediction and design problems. Please plot your fitness function vs. number of iterations to analyze the convergence characteristics of the model.



Part-1: Optimal Structure Prediction Problem



Consider a 2D grid of size $n \times n$ in which each position can be occupied by at most one amino acid. Given a sequence of hydrophobic or polar amino acids (H or P) of length $$n$$, find the optimal structure of the protein by assigning positions $$r_i$$ to amino acid $$p_i$$ at positions $$i=1...n$$. The optimal structure should minimizes the energy function:

$$H=\sum_{i,j=1...n,i < j}E_{p_ip_j}\delta(r_i-r_j)$$

where $$\delta \left ( r_i-r_j \right )=1$$ if positions $$r_i$$ and $$r_j$$ contain two non-bonded amino acids in neighboring locations (such that $$\left \| r_i-r_j \right \|_1 \leq 1$$) and $$0$$ otherwise. The pairwise energy potentials are: $$E_{HH}=-3, E_{PP}=E_{PH}=E_{HP}=0$$.

Use your method to find the optimal structure of the string "H-H-P-P-H-H-P-H-H-P-P-H-H-P-H-H-P-P-H-H".



Hint: Model the structure as a string of directions (North, East, West, South or NEWS).



Part-2 Find the optimal sequence

Find the sequence that "folds" into the following structure "NNNESSENN".

You can use plotpath.py to plot paths.
