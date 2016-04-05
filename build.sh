echo 'requires basebox to be built'
docker build -t maximz/tracker -f Dockerfile .;
docker tag -f maximz/tracker maximz/tracker:latest ;