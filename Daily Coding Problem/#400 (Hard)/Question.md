# Daily Coding Problem #400 Rated "Hard"
<b>This question was asked on July 25th, 2022</b>

# Question:
```
Good morning! Here's your coding interview problem for today.

This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.

```

# Answer (Usage):
<b>(View the Answer in Answer.py)</b>

```python
L = [1,2,3,4,5]

sum(L, 1, 3)
>>> 5
```