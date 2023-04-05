docker run \
-d --name was-flask \
--net reverb-net \
-v /var/run/docker.sock:/var/run/docker.sock \
-p 8080:8080 was-flask