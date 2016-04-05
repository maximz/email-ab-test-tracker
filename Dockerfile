from maximz/tracker-basebox:latest

# install our code
add . /home/docker/code/

# pip install run in basebox

workdir /home/docker/code/app
volume /home/docker/code/app/data

# need environment vars for this
env APP_SETTINGS="config.ProductionConfig"
env DATABASE_URL="sqlite:///data.db"
#run python manage.py db init
run python manage.py db migrate
run python manage.py db upgrade

expose 80
cmd ["supervisord", "-n"]
