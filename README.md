# Flask Dev Project

Just a simple quarantine project to learn a little web dev and to act as a reference for future projects using these technologies.
Allows a user to create notes with or without sections.

## Tech used

* Flask 1.1.2
* Python 3.6
* Ruby Sass 3.7.2
* Jinja 2.11.2


## Use

It might be useful to use multiple terminal windows or something like tmux since multiple programs will be running.

### Setup

Source the setup file to export the necessary environment variables (edit the Display variable if necessary. I'm using wsl and xming).

```
. setup.sh
```

### Sass

To have sass watch the scss file 

```
sass --watch style.scss:style.css
```

from the /static/css directory or 

```
sass --watch static/css/style.css:static/css/style.css &
```

to run from the top directory and in the background.

### Flask

To run flask, use 

```
flask run
```

or 

```
flask run &
```

This will also tell you the local host page which you can update in 'run _browser.sh' if you want to.
