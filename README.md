<h1 align="center"> AirBnB_clone </h1>
<p align="center">
<img src="https://user-images.githubusercontent.com/68792144/141602345-7b71c4ea-a4dd-42d9-b706-7fc2c7b85ca5.png">
</p>


## Welcome to the AirBnB clone project!

### Authors
1. Miguel Grillo
2. Miguel Barrera


## Description


## Format Specifiers

### Classes
<li>BaseModel</li>
<li>FileStorage</li>
<li>State</li>
<li>City</li>
<li>Amenity </li>
<li>Place</li>
<li>Review</li>

### Commands

| cmd   | Description | Usage |
|--------|--------|--------|
| **`help`**   | Displays help manual and usage of command specified | `help` `<command>` <br> `Empty`|
| **`quit`**   | Exit the program | `quit` |
| **`EOF`**    | Exit the program | `EOF` <br>`Ctrl + D`|
| **`create`** | Creates new id for a new class | `create <class name>` |
| **`show`**   |  Prints the string representation of an instance based on the class name  | `show <class name> id`|
| **`destroy`**| Deletes an instance based on the class name and id | `destroy <class name> id`|
| **`all`**    | Prints all string representation of all instances based or not on the class name | `all` <br> `all <class name>`|
| **`update`** | Updates an instance based on the class name and id by adding or updating attribute | `update <class name> <id> <attribute> <value>` |

## Examples
`Create User`
```python3
(hbnb) create User
633dd39d-1614-41b0-8e1e-eb8472cacea3
```

`Update User`
```python3
(hbnb) User.update("633dd39d-1614-41b0-8e1e-eb8472cacea3", {'first_name': "Miguel", "age": 22})
(hbnb) User.show("633dd39d-1614-41b0-8e1e-eb8472cacea3")
[User] (633dd39d-1614-41b0-8e1e-eb8472cacea3) {'id': '633dd39d-1614-41b0-8e1e-eb8472cacea3', 'created_at': datetime.datetime(2022, 3, 3, 14, 20, 32, 70949), 'updated_at': datetime.datetime(2022, 3, 3, 14, 20, 32, 70949), 'first_name': 'Miguel', 'age': 22}
```
`Command help`
```c
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  dupdate  help  quit  show  update
```
