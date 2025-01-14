# **Noah Romo's Personal Portfolio Site**

Created my portfolio website based off of my team's portfolio project that won the MLH Fellowhip Hackathon. Allows users to learn more about me, such as my education, work experience, personal projects, technical skills, hobbies, and travel experiences.

## Tech Stack

This web application was built using HTML, Jinja2, CSS, and Javascript on the front-end, and the back-end was built using Flask. I also used the particles.js and leaflet.js frameworks to add some of the design features. The production environment was built using a Virtual Private Server, with a MySQL database and secure Nginx web server, containerized with Docker.

## Demo

[Watch Our Demo on YouTube!](https://youtu.be/y-RejqP_u1c)

## Getting Started

If you would like to visit the website, you can click this link here [Personal Portfolio](http://noahromo.duckdns.org)

If you would like to see the website on your local computer, follow these next steps (It is recommended to use the VSCode IDE).

First, clone the repository onto your local machine:
```bash
$ git clone https://github.com/noahromo/personal-portfolio.git
```

Now follow the installation and usage steps below to render the website!

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv:
```bash
$ virtualenv env
$ source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Now check out the main branch if you aren’t already on it:
```bash
$ git checkout main
```

Create a .env file and add the variable: URL=localhost:5000

Start flask development server:
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. It will be hosted in the cloud soon so stay tuned!* 

## Troubleshooting

1. Make sure that you do not have any other environments open in the background when creating the virtual environment. This will prevent you from rendering the site. 

2. If the localhost:5000/ is in use then make sure to kill the application that is using the local server in the background or change the port to another by modifying the URL environment variable located in the .env file you created (Ex: URL=localhost:5001 instead of URL=localhost:5000)

## Contributing

Contributions to this project are [released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license) to the public under the [project's open source license](LICENSE).
