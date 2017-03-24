# Smart Classroom Analyst

The project aims to provide deep insights into student-teacher interaction that may be used by any educational institute. It automates the reviewing process of conventional feedback systems. It takes feedback from students, not only through the textual means, but also by monitoring the parameters like their engagement during the class. It also gives the teachers scope for improvement by the analysis provided by it. Automation of this system helps in maintaining anonymity of the person giving feedback, and hence removing any bias that may be involved in conventional feedback systems.
This project is a proof of concept of the system explained above.

## AWS HOSTED
http://35.154.211.96:8000/

## Getting Started

To start using Smart Classroom Analyst, you should follow these steps:- (For Windows 8.1 and Windows 10)
Clone the repository and get a copy into your system.
``` 
set GOOGLE_APPLICATION_CREDENTIALS=cred.json 
```
Download the following packages:-
* python3.5 from the official website
```	
pip install virtualenv
pip install -r requirements.txt
python manage.py makemigrations classroom_analyst
python manage.py migrate
python manage.py runserver
```

### Prerequisites

* Google developer account
* Cloud vision API by google
* Cloud Natural language API

## Running the tests

Open the web browser and go to the address:
```
127.0.0.1:8000
```
This will take you to the index page.

## Built With

### Front End
* [Semantic UI](https://github.com/Semantic-Org/Semantic-UI-Docs/) - Framework for front end development

### Back End
* [Django](https://docs.djangoproject.com/en/1.10/) - The web framework used
* [Google Vision API](https://cloud.google.com/vision/) - Used for image processing tasks.

## Contributing

(https://github.com/lordzuko/DeepEduVision) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Himanshu Maurya** - [lordzuko](https://github.com/lordzuko/)

* **Utsav Poddar** - [utsavvicky](https://github.com/utsavvicky/)

* **Sachin Kukreja** - [sk364](https://github.com/sk364/)

* **Ameya Datar** - [ameyalfcdatar](https://github.com/ameyalfcdatar/)

* **Kanishka Munshi** - [kmunshi97](https://github.com/kmunshi97/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Developed during a hackathon hosted at PDPM IIITDM Jabalpur, sponsored by VassarLabs, Hyderabad,India.

