./build_base.sh
./build_test.sh && ./run_test.sh
docker exec -it maximz-tracker-test bash
> cat /var/log/uwsgi/uwsgi.log