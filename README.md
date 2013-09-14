Query-Location-Matcher
======================

To identify the location name, Given a list of web search queries where query has exactly one location name.

### Problem Statement:

***

You are given a list of web search queries, one in every line. Every query has exactly one location name. Your task is to identify the location name. You are given a list of location names which will include all the location names present in the input queries. 

However, when real users type in a query, they often make spelling mistakes (e.g., "Cijapur" instead of "Bijapur") or may not know the correct spelling of the location and therefore, type something which sounds similar (e.g., "Chitrakut" instead of "Chitrakoot"). Therefore, your task is not only to identify the location word but to replace it with the correct spelling from the list of locations whenever it is incorrect.

### Running for single queries: (Full Script)

***

*Input* for single query processing:

```python
python singlemain.py locations.txt
```
*Output* for single query:

```html
Enter Query: i am in bengaluru
i am in <loc>bangalore</loc>
```


### Sample Outputs: (Full Script)

***

The system marks every location word by a <loc> and </loc> label. 

Suppose the "List of Locations" contains:

> Amritsar, Bharatpur, Chitrakoot, Gorakhpur, Kolkata

Input queries are:

```html
computer dealers in bharatpur
reliance mall in chitrakut
how 2 go to amitsar
tourist places near gorakpur
victoria memorial kolkata 
```

The expected output is:

```html
computer dealers in <loc>bharatpur</loc>
reliance mall in <loc>chitrakoot</loc>
how 2 go to <loc>amritsar</loc>
tourist places near <loc>gorakhpur</loc>
victoria memorial <loc>kolkata</loc> 
```

