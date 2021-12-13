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

### Project organization : <br />

<h2 id="directory-structure">Directory structure</h2>
<pre><code class="language-nohighlight">
├── README.md               &lt;- The top-level README for developers using this project.
├── data                    &lt;- Dataset used to measure the model accuracy. Found at : https://www.kaggle.com/marklvl/sentiment-labelled-sentences-data-set
│   └── labelled_sentence.csv   
│   
│
├── static                  &lt;- The folder containing the css files.
│      └── css       
│ 
├── templates               &lt;- The folder containing the html files.
│
├── docker-compose.yaml     &lt;- The docker compose properties to define the multi-container docker application. <strong> The port used is "5000" </strong>
│
├── Dockerfile.dockerfile   &lt;- The docker image for the application.
│
├── requirements.txt        &lt;- The requirements for the Docker image <strong>[flask,nltk,vaderSentiment,requests].</strong>
│
├── web_app.py              &lt;- The python script to define the web application and link it to the model.
│
└── test_web_app.py         &lt;- The python script for unit and integration testing.

</code></pre>

### Demonstration : 

<div align="center">
<h2> When entering a positive sentence : </h2> <br />
<img align="center" src="static/Positive.gif" /> <br />
<h2> When entering a negative sentence : </h2> <br />
<img align="center" src="static/Negative.gif" />
</div>

### Project Management : <br />

A Trello was created to coordinate the tasks between the team members.

<div align="center">
  
  <a href="https://trello.com/b/X5G8QLou/data-engineering-project"><img width="300px" src="https://logos-world.net/wp-content/uploads/2021/02/Trello-Logo.png"/></a>
</div>

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




<div align="center">
  <sub>Project made by
  <a href="https://github.com/Duramann">Théo Dura</a>,
  <a href="https://github.com/plao1996">Philippe Lao</a>,
  </a>
</div>



