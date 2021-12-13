<h1 align="center">Data Engineering project</h1>

<div align="center">
   <strong> Dockerized web interface for sentiment analysis </strong>
</div>
<div align="center">
  Project of a group of 2 persons at EFREI Paris for the Data Engineering course.
</div>

<br />

<div align="center">
  <!-- Maintenance -->
    <img src="https://img.shields.io/maintenance/yes/2021?style=for-the-badge"
      alt="Maintenance" />
  <!-- Last Commit -->
  <a href="https://github.com/EFR-AI/AIBSIF/commit/main">
    <img src="https://img.shields.io/github/last-commit/Duramann/Data_engineering_project?style=for-the-badge"
      alt="Last Commit" />
  </a>
  <!-- Activity -->
  <a href="https://github.com/EFR-AI/AIBSIF/graphs/commit-activity">
    <img src="https://img.shields.io/github/commit-activity/w/Duramann/Data_engineering_project?style=for-the-badge"
      alt="Activity" />
  </a>
  <!-- PR -->
  <!--  <img src="https://img.shields.io/github/status/contexts/pulls/Duramann/Data_engineering_project/0?style=for-the-badge"-->
  <!--    alt="pulls" />-->
  <!-- Size -->
    <img src="https://img.shields.io/github/repo-size/Duramann/Data_engineering_project?style=for-the-badge"
      alt="size" />
</div>

<br />

<div align="center">
<strong> Languages and Tools: </strong>
</div>
<br />
<div align="center">
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" />
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"/>
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" />
</div>

<br />

### Project Objective : <br />

Building a docker image containing a sentiment analysis application using Flask web app. <br />

### Project Management : <br />

A Trello was created to coordinate the tasks between the team members.

<div align="center">
  <sub>Link to the trello
  <a href="https://trello.com/b/X5G8QLou/data-engineering-project"><img src="https://logos-world.net/wp-content/uploads/2021/02/Trello-Logo.png"/></a>
</div>

### Project organization : <br />

├── README.md <br />
├── data <br />
│      ├── labelled_sentence <- Dataset used during the testing. It provides the function that check if the accuracy of our back-end model is above or equal to 70% <br />
│ <br />
├── static <br />
│      ├── CSS <br />
│      │      ├── style <- Setting the style of the web page <br />
│      ├── fonts   <- providing the fonts of the webpage's texts <br />  
│      ├── background  <- background image of the website <br />  
│      ├── Negative   <- demo of the web app use when the result is negative<br />  
│      └── Positive   <- demo of the web app use when the result is negative  <br />       
│ <br />
├── templates <br />
│      ├── index <- fonctional contents of the web page  <br />
│ <br />
├── docker-compose.yaml <- configure the web application's services, the port use for the run is "5000" <br />
│ <br />
├── dockerfile <- Building the Docker image with : Python/Flask/Libraries (from the requirements.txt), on the port "5000"  <br />
│ <br />
├── dockerfile <- Building the Docker image with : Python/Flask/Libraries (from the requirements.txt), on the port "5000"  <br />
│ <br />
├── requirements.txt <- The libaries used are : flask==1.1.2/ nltk>=3.4.5/ requests/ vaderSentiment==3.2.1<br />
│ <br />
├── web_app.py <- unit and integration tests for the application <br />
│ <br />
├── test_web_app.py <- unit and integration tests for the application <br />




<div align="center">
  <sub>Project made by
  <a href="https://github.com/Duramann">Théo Dura</a>,
  <a href="https://github.com/plao1996">Philippe Lao</a>,
  </a>
</div>



