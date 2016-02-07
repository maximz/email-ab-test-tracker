from ubuntu:14.04
run apt-get update
run apt-get install -y build-essential git
run apt-get install -y python python-dev python-setuptools
run apt-get install -y nginx supervisor
run easy_install pip

run mkdir -p /var/log/uwsgi
#run chown -R user:user /var/log/uwsgi

# install uwsgi now because it takes a little while
run pip install uwsgi

# install nginx
run apt-get install -y software-properties-common python-software-properties
run apt-get update
run add-apt-repository -y ppa:nginx/stable
run apt-get install -y sqlite3

# install our code
add . /home/docker/code/

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip install -r /home/docker/code/app/requirements.txt

workdir /home/docker/code/app

# need environment vars for this
env APP_SETTINGS="config.ProductionConfig"
env DATABASE_URL="sqlite:///data.db"
#run python manage.py db init
run python manage.py db migrate
run python manage.py db upgrade

expose 80
cmd ["supervisord", "-n"]
