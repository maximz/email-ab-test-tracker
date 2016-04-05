echo 'requires basebox to be built'
docker build -t maximz/tracker-test -f Dockerfile.test .;
docker tag -f maximz/tracker-test maximz/tracker-test:latest ;