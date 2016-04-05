docker stop maximz-tracker-test; docker rm maximz-tracker-test;
docker run --name maximz-tracker-test -p 3181:80 -d maximz/tracker-test:latest;