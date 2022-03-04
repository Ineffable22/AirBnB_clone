<h1 align="center"> AirBnB_clone </h1>
<p align="center">
<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png">
</p>

## Welcome to the AirBnB clone project!

### Authors
1. Miguel Grillo
2. Miguel Barrera

## Description
<p>
This project is the first step of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database.

It consists of the implementation of a command line interface in the PYTHON programming language, which simulates the interaction with a RESTful API and data persistence. As well as basic functions such as create, show, update, destroy that simulate a CRUD (Create, Read, Update, Delete) of a lifetime towards a database.
</p>

## Representation

<p align="center"><img src="https://user-images.githubusercontent.com/68792144/141602516-90e36740-e66e-4edd-8baf-08f318b10a58.png" width="700"></p>

## How to Start it
`Install`
```python3
git clone https://github.com/Ineffable22/AirBnB_clone
```
`Open AirBnb_clone directory`
```python3
cd AirBnb_clone
```
`Execute`
```python3
./console
```

<h1>Classes</h1>
<p align="center"><img src="https://user-images.githubusercontent.com/82726832/156699714-53df4235-7e62-4bb2-ab35-ca018f2b11fc.png" width="100%"></p>
<br>


## Commands
| CMD   | Description | Usage |
|--------|--------|--------|
| **`help`**   | Displays help manual and usage of command specified | `help` `<command>` <br> `help`|
| **`quit`**   | Exit the program | `quit` |
| **`EOF`**    | Exit the program | `EOF` <br>`Ctrl + D`|
| **`create`** | Creates new id for a new class | `create <class name>` |
| **`show`**   |  Prints the string representation of an instance based on the class name  | `show <class name> id`|
| **`destroy`**| Deletes an instance based on the class name and id | `destroy <class name> id`|
| **`all`**    | Prints all string representation of all instances based or not on the class name | `all` <br> `all <class name>`|
| **`update`** | Updates an instance based on the class name and id by adding or updating attribute | `update <class name> <id> <attribute> <value>` |

## Examples
`Create <class name>`
```python3
(hbnb) create User
633dd39d-1614-41b0-8e1e-eb8472cacea3
```

`Update <class name>`
```python3
(hbnb) User.update("633dd39d-1614-41b0-8e1e-eb8472cacea3", {'first_name': "Miguel", "age": 22})
```
`Show <class name>`
```python3
(hbnb) User.show("633dd39d-1614-41b0-8e1e-eb8472cacea3")
[User] (633dd39d-1614-41b0-8e1e-eb8472cacea3) {'id': '633dd39d-1614-41b0-8e1e-eb8472cacea3', 'created_at': datetime.datetime(2022, 3, 3, 14, 20, 32, 70949), 'updated_at': datetime.datetime(2022, 3, 3, 14, 20, 32, 70949), 'first_name': 'Miguel', 'age': 22}
```
`Command help`
```python3
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  dupdate  help  quit  show  update
```
<p align="center"><img src="https://images.squarespace-cdn.com/content/v1/56a7f187a2bab83fab5d4afc/1539942258535-T72FPLOO53S2HXIAU74F/BBC3_Walk.gif?format=1500w" width="700"></p>

# Authors
* Miguel Grillo - [GitHub](https://github.com/Ineffable22) - [Medium](https://medium.com/@Miguel_Grillo) - [Linkedin](https://www.linkedin.com/in/miguel-enrique-grillo-orellana/)
* Miguel Barrera - [GitHub](https://github.com/MiguelBarreraDev) - [Medium](https://medium)- [Linkedin](https://www.linkedin.com/in/miguel-barrera-dev/)
