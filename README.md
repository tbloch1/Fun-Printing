# Fun-Printing
Modification of the python print function to print monospaced 8x8-bit characters.

================================================
** Example

By default, printing should be identical to normal python printing
``` python
from fun_print import print
print('Hello, World!')
```
```
Hello, World!
```
With `fun=True` the function maps the characters to 8-bit representation.
By default thishas positive space take by 'X' and negative space by a
space(' ').
``` python
print('Hello, World!', fun=True)
```
```
XX  XX           XXX     XXX                            XX   XX                  XXX       XXX     XX   
XX  XX            XX      XX                            XX   XX                   XX        XX    XXXX  
XX  XX   XXXX     XX      XX     XXXX                   XX   XX  XXXX   XX XXX    XX        XX    XXXX  
XXXXXX  XX  XX    XX      XX    XX  XX                  XX X XX XX  XX   XXX XX   XX     XXXXX     XX   
XX  XX  XXXXXX    XX      XX    XX  XX                  XXXXXXX XX  XX   XX  XX   XX    XX  XX     XX   
XX  XX  XX        XX      XX    XX  XX    XX            XXX XXX XX  XX   XX       XX    XX  XX          
XX  XX   XXXX    XXXX    XXXX    XXXX     XX            XX   XX  XXXX   XXXX     XXXX    XXX XX    XX   
                                         XX                                                             
```
Note, however, that the positive and negative space can be changed to
anything. (Though, using more than a single character makes it very
difficult to read).
``` python
print('Hello, World!', fun=True, positive_space=' ', negative_space='x')
```
```
  xx  xxxxxxxxxxx   xxxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxx  xxxxxxxxxxxxxxxxxx   xxxxxxx   xxxxx  xxx
  xx  xxxxxxxxxxxx  xxxxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxx  xxxxxxxxxxxxxxxxxxx  xxxxxxxx  xxxx    xx
  xx  xxx    xxxxx  xxxxxx  xxxxx    xxxxxxxxxxxxxxxxxxx  xxx  xx    xxx  x   xxxx  xxxxxxxx  xxxx    xx
      xx  xx  xxxx  xxxxxx  xxxx  xx  xxxxxxxxxxxxxxxxxx  x x  x  xx  xxx   x  xxx  xxxxx     xxxxx  xxx
  xx  xx      xxxx  xxxxxx  xxxx  xx  xxxxxxxxxxxxxxxxxx       x  xx  xxx  xx  xxx  xxxx  xx  xxxxx  xxx
  xx  xx  xxxxxxxx  xxxxxx  xxxx  xx  xxxx  xxxxxxxxxxxx   x   x  xx  xxx  xxxxxxx  xxxx  xx  xxxxxxxxxx
  xx  xxx    xxxx    xxxx    xxxx    xxxxx  xxxxxxxxxxxx  xxx  xx    xxx    xxxxx    xxxx   x  xxxx  xxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
