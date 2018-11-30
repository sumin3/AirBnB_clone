<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# AirBnB_clone Project
Higher-level programming ― AirBnB clone

## Contents
* [Purpose](https://github.com/sumin3/AirBnB_clone#Purpose)
* [Coding style](https://github.com/sumin3/AirBnB_clone#Coding-style)
* [Installation](https://github.com/sumin3/AirBnB_clone#installation)
* [Usage](https://github.com/sumin3/AirBnB_clone#usage)
* [Usage Example](https://github.com/sumin3/AirBnB_clone#Usage-Example)
* [Command](https://github.com/sumin3/AirBnB_clone#Command)
* [File](https://github.com/sumin3/AirBnB_clone#File)
* [Author](https://github.com/sumin3/AirBnB_clone#author)
## Purpose
learn how to build a full web application: the 'AirBnB clone'

## Coding style
- All python files are interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3) and use the [PEP 8 style (version 1.7.*)](https://github.com/PyCQA/pycodestyle) for checking coding style

## Installation
To use, first download this repository into your local machine by issuing the following command in your local terminal. 
```
git clone https://github.com/thrownblown/AirBnB_clone.git
```
## Usage 
#### Interactive Mode
```
$./console.py 
(hbnb) <command>
```
#### Non-Interactive Mode
```
$ echo "<command>" | ./console.py
```

## Usage Example
```
$./console.py 
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

## Command
command | desc
--- | ---
help | display help information
quit | exit the program
Ctrl+D | exit the program
create \<class Name\> | create a new instance/object
all | Prints all string representation of all instances
all \<class Name\> | Prints all string representation of all instances based on the class name
\<class Name\>.all() | display all the object of the class
show \<class Name\> \<id\> | Prints the string representation of an instance based on the class name and id
\<class Name\>.show(\<id\>) | Prints the string representation of an instance based on the class name and id
destroy \<class Name\> \<id\> | Deletes an instance based on the class name and id
\<class Name\>.destroy(\<id\>) | Deletes an instance based on the class name and id
update \<class Name\> \<id\> \<attr name\> \<attr value\> | Updates an instance based on the class name and id by adding or updating attribute
\<class Name\>.update(\<id\>, \<attr name\>, "\<attr value\>") | Updates an instance based on the class name and id by adding or updating attribute
\<class Name\>.update(\<id\>, {\<attr name\>: "\<attr value\>", \<attr name\>: "\<attr value\>"}) | Updates an instance based on the class name and id with dictionary
\<class name\>.count() | retrieve the number of instances of a class

## File
|    Directory | File Hierarchy |   Description  |
|------------|-----------------|-------------
| root | [console.py](console.py)                                        | The main console file     
| models | [click this to see the models Files description](https://github.com/sumin3/AirBnB_clone/tree/master/web_static#Files) | The second step of the AirBnB Clone project - build the front end step-by-step
| tests | [click this to see the tests Files description](https://github.com/sumin3/AirBnB_clone/tree/master/web_static#Files) | The second step of the AirBnB Clone project - build the front end step-by-step
| web_static | [click this to see the web_static Files description](https://github.com/sumin3/AirBnB_clone/tree/master/web_static#Files) | The second step of the AirBnB Clone project - build the front end step-by-step

## Author
- Sumin Yu - [Twitter: @3_sumin](https://twitter.com/3_sumin)
- Alex Farioletti - [Twitter: @ThrownBlown](https://twitter.com/ThrownBlown)