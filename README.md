# alertmanager-rock
Build an alertmanager image using rockcraft

```shell
rockcraft pack -v
skopeo --insecure-policy copy oci-archive:alertmanager_0.24.0.rock docker-daemon:alertmanager:0.24.0
dive alertmanager:0.24.0

tar tf alertmanager_0.24.0.rock
tar -O -xf alertmanager_0.24.0.rock oci-layout
```

## References
- https://github.com/jnsgruk/traefik-rock
- https://rockcraft.readthedocs.io/en/latest/reference.html
- https://github.com/prometheus/alertmanager/blob/main/Dockerfile

