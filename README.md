# AirBnB_clone


[![hbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210630%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210630T103636Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=21ed3569299860cd7625afe6a66cfa3c6b06be4b25e54619ae1c4b0916148aad "hbnb")](https://www.holbertonschool.com/tn/en/ "hbnb")

## Description of the project

This is the first step towards building our first full web application: the AirBnB clone.
This first step is very important because we will use what we build during this project with all other following projects, in it we are going to write a command interpreter to manage our AirBnB objects:

  *  Create a new object (ex: a new User or a new Place)
  *  Retrieve an object from a file, a database etc…
   * Do operations on objects (count, compute stats, etc…)
   * Update attributes of an object
   * Destroy an object



## Installation

To use our AirBnB clone console you need to:

Clone This Repository:
```git clone https://github.com/RimJoudi/AirBnB_clone.git```

Change the directory to AirBnB_clone:

```cd AirBnB_clone```

Use  the command interpreter hbnb in an interactive mode:

`
./console.py
`
`
  (hbnb)  (command)
`

Use hbnb in non-interactive mode too by:
`echo "command" | ./console.py`


HBNB Console Commands :

|   Command|   Action|
| ------------ | ------------ |
|   quit, EOF |  commands used  to quit the console |
|   help|  command used for help purpose |
|   all|  command that displays all the HBNB instances |
|   create|  command that creates an instance of class_name and display the related id |
|   show |  command that displays all attributes of class_name.object_id |
|   destroy|  command used to delete all attributes of class_name.object_id |
|   update|  command used to update an instance|

HBNB Console files :

|files/ directories|     description|
| ------------ | ------------ |
| console.py |  The console file |
| tests| directory containing all the unittest done for all files|
|base_model.py|  BaseModel superclass |
| amenity.py  | Amenty class inherited from BaseModel  |
| city.py |   City class inherited from BaseModel|
| place.py  |   Place class inherited from BaseModel|
| review.py  |   Review class inherited from BaseModel|
| state.py  | State  class inherited from BaseModel |
| user.py |   User class inherited from BaseModel|
|  engine| file_storage.py/FileStorage class|

### examples of use:
In an interactive mode:
```
./console.py
(hbnb) 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
0e616da4-59f8-44ec-b550-2132c27588f0
(hbnb) all BaseModel
["[BaseModel] (0865a469-f9a1-4d9f-9945-af04d2a8792d) {'id': '0865a469-f9a1-4d9f-9945-af04d2a8792d', 'created_at': datetime.datetime(2021, 6, 30, 14, 14, 17, 484598), 'updated_at': datetime.datetime(2021, 6, 30, 14, 14, 17, 484632)}", "[BaseModel] (0e616da4-59f8-44ec-b550-2132c27588f0) {'id': '0e616da4-59f8-44ec-b550-2132c27588f0', 'created_at': datetime.datetime(2021, 6, 30, 14, 14, 32, 470143), 'updated_at': datetime.datetime(2021, 6, 30, 14, 14, 32, 470204)}"]
(hbnb) show BaseModel 0e616da4-59f8-44ec-b550-2132c27588f0
[BaseModel] (0e616da4-59f8-44ec-b550-2132c27588f0) {'id': '0e616da4-59f8-44ec-b550-2132c27588f0', 'created_at': datetime.datetime(2021, 6, 30, 14, 14, 32, 470143), 'updated_at': datetime.datetime(2021, 6, 30, 14, 14, 32, 470204)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 0e616da4-59f8-44ec-b550-2132c27588f0 first_name "Betty"
(hbnb) show BaseModel 0e616da4-59f8-44ec-b550-2132c27588f0
[BaseModel] (0e616da4-59f8-44ec-b550-2132c27588f0) {'id': '0e616da4-59f8-44ec-b550-2132c27588f0', 'created_at': datetime.datetime(2021, 6, 30, 14, 14, 32, 470143), 'updated_at': datetime.datetime(2021, 6, 30, 14, 14, 32, 470204), 'first_name': '"Betty"'}
(hbnb) create BaseModel
00d3ad7f-b1a1-451d-922a-e950c0a36c53
(hbnb) all BaseModel
["[BaseModel] (0865a469-f9a1-4d9f-9945-af04d2a8792d) {'id': '0865a469-f9a1-4d9f-9945-af04d2a8792d', 'created_at': datetime.datetime(2021, 6, 30, 14, 14, 17, 484598), 'updated_at': datetime.datetime(2021, 6, 30, 14, 14, 17, 484632)}", '[BaseModel] (0e616da4-59f8-44ec-b550-2132c27588f0) {\'id\': \'0e616da4-59f8-44ec-b550-2132c27588f0\', \'created_at\': datetime.datetime(2021, 6, 30, 14, 14, 32, 470143), \'updated_at\': datetime.datetime(2021, 6, 30, 14, 14, 32, 470204), \'first_name\': \'"Betty"\'}', "[BaseModel] (00d3ad7f-b1a1-451d-922a-e950c0a36c53) {'id': '00d3ad7f-b1a1-451d-922a-e950c0a36c53', 'created_at': datetime.datetime(2021, 6, 30, 14, 19, 12, 165597), 'updated_at': datetime.datetime(2021, 6, 30, 14, 19, 12, 165622)}"]
(hbnb) destroy BaseModel 00d3ad7f-b1a1-451d-922a-e950c0a36c53
(hbnb) show BaseModel 00d3ad7f-b1a1-451d-922a-e950c0a36c53
** no instance found **
(hbnb) 

```

In non interactive mode:
```
echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

Authors:

*  Maroua Alaya - (https://github.com/maroua199525)

* Rim Joudi - (https://github.com/RimJoudi)


[![Holberton school](https://camo.githubusercontent.com/c274b9dc7dcbfd7bb13147323147538ce07d3087ec7fb859f4a4ef658281e0cb/68747470733a2f2f656e637279707465642d74626e302e677374617469632e636f6d2f696d616765733f713d74626e3a414e643947635438673843767177395a375278394948477139674b596e65654d3155345f4b76554e54656143426b58324c35704645334968772d35754e4773397850536d5562356b584126757371703d434155 "Holberton school")](https://www.holbertonschool.com/tn/en/ "Holberton school")


Project made for [Holberton school](https://www.holbertonschool.com/tn/en/ "Holberton school") by Maroua Alaya and Rim Joudi.
