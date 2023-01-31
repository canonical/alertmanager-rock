# alertmanager-rock
Build an alertmanager image using rockcraft

## Usage
```shell
rockcraft pack -v
```

## Manual verification
```shell
tar tf alertmanager_0.24.0_amd64.rock
tar -O -xf alertmanager_0.24.0_amd64.rock oci-layout

skopeo --insecure-policy copy oci-archive:alertmanager_0.24.0_amd64.rock docker-daemon:alertmanager:0.24.0
dive alertmanager:0.24.0

docker run --rm -d -p 9093:9093 alertmanager:0.24.0
curl localhost:9093/api/v1/alerts
```

## References
- https://github.com/jnsgruk/traefik-rock
- https://rockcraft.readthedocs.io/en/latest/reference.html
- https://github.com/prometheus/alertmanager/blob/main/Dockerfile

