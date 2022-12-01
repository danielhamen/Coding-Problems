## **Python If-Else:**

**Task**

Given an integer, ***n***, perform the following conditional actions:

<ul>
<li>If  is odd, print <code>Weird</code></li>
<li>If  is even and in the inclusive range of  to , print <code>Not Weird</code></li>
<li>If  is even and in the inclusive range of  to , print <code>Weird</code></li>
<li>If  is even and greater than , print <code>Not Weird</code></li>
</ul>

**Input Format**

A single line containing a positive integer, .

**Constraints**

<ul>
<li><code>1 <= n <= 100</code></li>
</ul>

**Output Format**

Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

**Sample Input 0**

```
3
```

**Sample Output 0**

```
Weird
```

**Explanation 0**

`n = 3`

***n*** is odd and odd numbers are weird, so print `Weird`.

**Sample Input 1**

```
24
```

**Sample Output 1**

```
Not Weird
```

**Explanation 1**

`n = 24`

`n = 20` and ***n*** is even, so it is not weird.