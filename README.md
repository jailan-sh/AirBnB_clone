# Project: 0x00. AirBnB clone - The console

![Airbnb](https://peytonbrsmith.netlify.app/projects/web/airbnb/65f4a1dd9c51265f49d0_hu98d6ceda137062fd4edf4a7d705e7570_76537_700x0_resize_box_3.png)

This project is the first step towards building a full web application: the **AirBnB clone**. 

It is very important because it serves as the back-end base of other projects: 
HTML/CSS templating, database storage, API, front-end integration…

##The Console

![console](https://peytonbrsmith.netlify.app/projects/web/airbnb/815046647d23428a14ca_hu68774d5216c48b4f424f088e55e7a2ed_118703_700x0_resize_box_3.png)

This software is a command interpreter similar to a Linux shell but limited to a specific use-case; management of objects in the AirBnB Clone:

-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object
-   manage (create, update, destroy, read) objects via a console / command interpreter
-  store and persists objects to a file (JSON file)

## Usage

**Interactive** and **Non-interactive**.

## Commands 

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **help** | Provides a text describing how to use a command.  |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **count** | Retrieve the number of instances of a class.  |

<h3>General knowledge from this project </h3>

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the cmd module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage datetime</li>
<li>What is an UUID</li>
<li>What is *args and how to use it</li>
<li>What is **kwargs and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

## Authors

- Ghaidaa Reda Elsahafy <dodo.sa7afy@gmail.com>
- Jailan Fawzy Elsherbiny <jailan.elsherbiny@gmail.com>
