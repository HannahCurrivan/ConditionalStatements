# Conditional Statements
This tutorial will cover If, Else, Elif, and nested.

## If Statements: 
If you are looking at the specfic impulse of rocket fuel. In this case you have a specific impulse of 289 Isp.

```python
if specific_impulse >= 289:
    print("This is greater than specific impulse that the engine can handle.")
```
We are saying in this code ```if``` the specific impulse is greater then ```>=``` the specfic impulse value of 289, then you can print the following statement: ```print("This is greater than specific impulse that the engine can handle.")```

## Else Statement:
If the specific impulse does not meet the requirmments in the ```if``` statement. This is where a ```Else``` statement; this lets you give yourself another option to give a condition to a different outcome.  

```python
else:
    print("Fuel type needed for a 289 Specific Impulse is Kerosene")
```
We see that if the ```if``` statement is not carried out, the ```Else``` statement is then giving another option of an outcome with the following statement: ```print("Fuel type needed for a 289 Specific Impulse is Kerosene")```.

## Elif Statement:
The ```Elif``` statement allows you to check many different expressions to see if they are TRUE to the given value and to excute the code as soon as one of the conditions matchs is TRUE. 

```python
elif specific_impulse == 320:
    print("This means you can use Kerosene with the Specific Impulse of 320.")
```
The ```Elif``` statement in this case is saying if the specfic impulse is equal to 320, the outcome will be the following: ``` print("This means you can use Kerosene with the Specific Impulse of 320.")```

## Nested:
This is were you can but another if statement into yor current if statements.

```python
if specific_impulse != 289:
    print("This is less than or greater than specific impulse that the engine needs.")
    
    if specific_impulse_2 == 256:
        print("Fuel type needed for a 256 Specific Impulse is Kerosene", specific_impulse_2)
        
    else: 
        print("This fuel is incapable to give the specific impulse needed to launch such rocket.")
    
elif specific_impulse == 320:
    print("This means you can use Kerosene with the Specific Impulse of 320.")
    
else:
    print("Fuel type needed for a 289 Specific Impulse is Kerosene")
```
