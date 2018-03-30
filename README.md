# Algorithm_Assignment1

We will find optimal solutions for given mazes using A*, Breadth First Search(BFS) and Uniform Cost Search(UCS) algorithms and find normal solutions using Depth First Search(DFS), Greedy algorithms.  
The start point of the maze is (0,0) and the end point is bottom right of the maze.  

input.txt example, there are no comments in actual input file
-------------------------------------------------------------  
3 // the number of mazes.  
  
6 6 // height, width of the maze.  
0,0,0,0,0,1 // 0 is a path, 1 is a wall.  
1,1,0,0,0,1 // coordinates notation is (y,x).  
0,0,0,1,0,0 // maze starts from (0,0) and ends to (height-1, width-1).  
0,1,1,0,0,1  
0,1,0,0,1,0  
0,1,0,0,0,0  
  
8 8  
0,0,1,0,1,0,0,0  
1,0,0,0,1,0,1,1  
0,0,0,1,1,0,1,0  
1,1,0,0,0,0,0,1  
1,0,1,0,0,0,1,0  
0,0,0,0,1,1,1,0  
0,0,1,0,0,0,0,1  
0,0,0,1,0,1,0,0  
  
15 25  
0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1  
0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1  
1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1  
0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1  
0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0  
0,0,1,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0  
0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0  
0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0  
0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,1  
0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1  
0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1  
0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0  
0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1  
0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0  
0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0  

---------------------------------------------------------------  
  
output.txt example, there are no comments in actual output file  
---------------------------------------------------------------  
0 0 // an explored node (y,x) by the algorithm.  
0 1  
0 2  
1 2  
2 2  
1 3  
1 4  
2 4  
3 4  
2 5  
3 3  
4 3  
5 3  
5 4  
5 5  
(0, 0)(0, 1)(0, 2)(1, 2)(1, 3)(1, 4)(2, 4)(3, 4)(3, 3)(4, 3)(5, 3)(5, 4)(5, 5) // path nodes of a solution of the algorithm.   
  
0 0  
0 1  
1 1  
2 1  
2 2  
3 2  
3 3  
4 3  
5 3  
6 3  
6 4  
7 4  
6 5  
6 6  
7 6  
7 7  
(0, 0)(0, 1)(1, 1)(2, 1)(2, 2)(3, 2)(3, 3)(4, 3)(5, 3)(6, 3)(6, 4)(6, 5)(6, 6)(7, 6)(7, 7)  
  
0 0  
1 0  
1 1  
2 1  
2 2  
3 2  
4 2  
4 3  
4 4  
3 4  
3 5  
2 5  
2 4  
1 5  
1 6  
1 7  
1 8  
2 8  
2 9  
3 9  
3 10  
4 10  
5 10  
6 10  
7 10  
8 10  
9 10  
10 10  
11 10  
9 11  
9 12  
9 13  
9 14  
9 15  
10 15  
11 15  
12 15  
13 15  
13 16  
14 16  
14 17  
14 18  
14 19  
14 20  
13 19  
12 19  
12 20  
12 21  
13 21  
13 22  
14 22  
14 23  
14 24  
(0, 0)(1, 0)(1, 1)(2, 1)(2, 2)(3, 2)(4, 2)(4, 3)(4, 4)(3, 4)(3, 5)(2, 5)(1, 5)(1, 6)(1, 7)(1, 8)(2, 8)(2, 9)(3, 9)(3, 10)(4, 10)(5, 10)(6, 10)(7, 10)(8, 10)(9, 10)(9, 11)(9, 12)(9, 13)(9, 14)(9, 15)(10, 15)(11, 15)(12, 15)(13, 15)(13, 16)(14, 16)(14, 17)(14, 18)(14, 19)(13, 19)(12, 19)(12, 20)(12, 21)(13, 21)(13, 22)(14, 22)(14, 23)(14, 24)  

---------------------------------------------------------------
