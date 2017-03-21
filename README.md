### Item Catalog Project - Jeopardy! Question Bank  

This catalog project contains a question bank of the popular TV game show Jeopardy!.
The catalog consists of unordered list of questions from a limited set of 6 categories, namely:
*History, People in History, Annual Events, World Geography, U.S. Cities, Foreign Words & Phrases*.
Each item in a category has details about the question, its value, answer, category, show number which featured the question, air date of the show and the game round which had the question.

Any user can view existing questions in the above specified categories by visiting the catalog.
Users can choose to login via Facebook or Google+. Once logged in, users can add new questions in the available categories and edit/delete questions that they created.

For users interested in only the data, JSON APIs are made available.

*Note:* Sample questions to add can be found here:
https://drive.google.com/file/d/0BwT5wj_P7BKXb2hfM3d2RHU1ckE/view?usp=sharing  
Source credit: https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/

*This catalog project is for educational purpose only.*


#### Project Setup:
 - Download the fullstack nanodegree VM and launch the Vagrant VM: `$ vagrant up` and `$ vagrant ssh`
 - Navigate to the project folder `$ cd /vagrant/catalog`
 - Setup database schema: `$ python database_setup.py`
 - Pre-populate database with few items: `$ python populatedb.py`
 - Run the project: `$ python application.py`
 - Catalog can now be accessed at `http://localhost:5000/catalog`

#### HTML endpoints:

*Home Page - List of categories:*  `/` or `/catalog`

*User authorization:*  
&nbsp;&nbsp;&nbsp;*Login:*
  `/login`  
&nbsp;&nbsp;&nbsp;*Logout:*
  `/disconnect`

*List of items in specified category:*  
`/catalog/<category_id>` or
`/catalog/<category_id>/items`

*Add new item:*  
`/catalog/<category_id>/items/new`

*Edit item:*  
`/catalog/<category_id>/items/<item_id>/edit`

*Delete item:*  
`/catalog/<category_id>/items/<item_id>/delete`

#### JSON APIs:

*List of categories:*
`/catalog/JSON`

*List of items in specified category:*
`/catalog/<category_id>/items/JSON`

*Specified item details:*
`/catalog/<category_id>/items/<item_id>/JSON`
