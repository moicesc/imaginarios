# imaginarios
Essential implementation for Imaginary numbers

## Usage
```python
>>> import math
>>> from imaginario import Imaginario

>>> a = Imaginario(1.0, 2.0)
>>> b = Imaginario(2.1, 3.5)

>>> a 
1.0 + 2.0j
>>> b
2.1 + 3.5j

```

### Addition

```python
>>> a + b
3.1 + 5.5j
```
### Subtraction

```python
>>> a - b
-1.1 + -1.5j
```

### Multiplication

```python
>>> a * b
-4.9 + 7.7j
```

### Division
```python
>>> a / b
0.5462184873949579 + 0.042016806722689086j
```

### Magnitude & Phase

```python
>>> a.magnitude
2.23606797749979
>>> a.phase
1.1071487177940904
```

### Conversion to polar form

```python
>>> a.to_polar()
var = (2.23606797749979, 1.1071487177940904)
```

### Alternate creation from polar from
```python
>>> c = Imaginario.from_polar(1, math.pi/2)
>>> c
6.123233995736766e-17 + 1.0j

>>> d = Imaginario.from_polar(2.23606797749979, 1.1071487177940904)
>>> d
1.0000000000000002 + 2.0j

```


## License

[MIT](https://choosealicense.com/licenses/mit/)
