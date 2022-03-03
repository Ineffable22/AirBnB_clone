<h1 align="center"> AirBnB_clone </h1>
<img src="https://cutt.ly/BAgrgRL" height="150px" width="800px">


## Welcome to the AirBnB clone project!

### Authors
1. Miguel Grillo
2. Miguel Barrera


## Description



## Format Specifiers



### Value Return 

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