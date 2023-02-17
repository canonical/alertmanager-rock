# alertmanager-rock

[![Build ROCK](https://github.com/canonical/alertmanager-rock/actions/workflows/build-rock.yaml/badge.svg)](https://github.com/canonical/alertmanager-rock/actions/workflows/build-rock.yaml)

Build an alertmanager image using
[rockcraft](https://github.com/canonical/rockcraft), maintaining the same file
hierarchy as the
[`prometheus/alertmanager`](https://github.com/prometheus/alertmanager/blob/main/Dockerfile)
image.

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

## Build automation
This repo has workflows in place to:
- update `rockcraft.yaml` when new versions of alertmanager are published;
- publish a new rock on every merge.
