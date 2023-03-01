## PostMate: Your Ultimate Blogging Companion

### Description:

PostMate is a Python Flask-based application that serves as the perfect companion for bloggers. The application provides users with an easy-to-use platform to create and publish their own blog posts. PostMate also includes a feature that suggests new topics based on the blogger's interests and previous posts, making it easy to stay inspired and create engaging content. With PostMate, users can also discover new blogs and connect with other bloggers, creating a thriving community of like-minded individuals.

### Prerequisites:
1. Python Programming language
2. MySql
3. flask
4. flask_restful
5. Docker (Optional)

### Technologies Used:

In the project I have used the below technologies:
1. flask - Utilized flask to create a dynamic and robust web application in my project.
2. flask_restful - Implemented flask_restful to enhance functionality and create RESTful APIs
3. flask_sqlalchemy - Used Flask_sqlalchemy to effectively interact with databases(ORM)
4. HTML - Employed HTML to structure and create well-formed web pages.
5. CSS - Incorporated CSS to provide a polished and visually appealing user interface in my project.

```
Note:
Python is the main programming language used in the flask and flask_restful and flask_sqlalchemy and
flask_sqlalchemy and is the foundation for the project.
```

### API DESIGN:
The CRUD (Create, Read, Update, and Delete) operations for both user and blogpost entities have been 
implemented and documented in the OpenAPI specification, utilizing the YAML format. The file containing the 
API definition is named "blogpost.yaml" for easy reference and management.

```Server URL : http://127.0.0.1:5000/```

| Request Type | Endpoints               | Description                                        |
| ------------|------------------------|----------------------------------------------------|
| GET         | /signup                 | Returns the signup page                            |
| POST        | /signup                 | Creates a new user                                 |
| GET         | /logout                 | Logsout the user from the session                   |
| GET         | /updateuser/{user_id}   | Returns the update user page                        |
| POST        | /updateuser/{user_id}   | Updates the user information                        |
| GET         | /deleteuser/{username}  | Deletes the user                                   |
| GET         | /profile/{username}     | Returns the user's profile page                     |
| POST        | /createpost             | Creates a new blog post                             |
| GET         | /createpost             | Returns the create post page                        |
| POST        | /deletepost/{post_id}   | Deletes a blog post                                 |
| GET         | /updatepost/{post_id}   | Returns the update post page                        |
| POST        | /updatepost/{post_id}   | Updates the blog post information                   |
| GET         | /viewpost/{post_id}     | Returns the single view post page                   |
| GET         | /viewposts              | Returns the viewposts page                          |


### Usage:

__Without Docker__

First change the directory to TaskMaster by executing the below command in the terminal

```
cd TaskMaster
```

To install the required packages and libraries, run the following command:


```
pip install -r requirements.txt
```

This command will install all the necessary dependencies listed in the requirements.txt file, allowing you to run the
project without any issues.

To run the application, execute the following command

```
python main.py
```

This will start the application, and you should be able to use it. (or) Directly run the main.py file


__With Docker__

run the below commands in the terminal to run the app using the docker

```
cd TaskMaster
docker build -t taskmaster -f Dockerfile/ .
docker run -p 5000:5000 taskmaster
```

### Architecture and Features:

The below diagram shows the Architecture of the Blog Application:

![Alt Text](https://drive.google.com/file/d/1G2BFN0y7QfHIiUSOSXzT5usZrmp4PAbZ/view?usp=share_link)


### Contact:

Name : Ujit Kumar

Email : ujitkumar1@gmail.com