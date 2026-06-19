# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""Tests to verify the alertmanager rock runs as a non-root user."""

import subprocess

import pytest

IMAGE = "alertmanager:0.31.1"


def _docker_run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", *args],
        capture_output=True,
        text=True,
    )


@pytest.mark.abort_on_fail
def test_runtime_uid():
    """Assert the container runs as uid 584792 (_daemon_)."""
    result = subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", "id", "-u"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "584792", (
        f"Expected uid 584792, got {result.stdout.strip()!r}"
    )


@pytest.mark.abort_on_fail
def test_runtime_gid():
    """Assert the container runs as gid 584792 (_daemon_)."""
    result = subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", "id", "-g"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "584792", (
        f"Expected gid 584792, got {result.stdout.strip()!r}"
    )


@pytest.mark.abort_on_fail
def test_alertmanager_config_dir_writable():
    """Assert /etc/alertmanager/ is writable by the runtime user."""
    result = subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", "sh", "-c", "test -w /etc/alertmanager/"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "/etc/alertmanager/ is not writable by _daemon_"


@pytest.mark.abort_on_fail
def test_amtool_config_dir_writable():
    """Assert /etc/amtool/ exists and is writable by the runtime user."""
    result = subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", "sh", "-c",
         "test -d /etc/amtool/ && test -w /etc/amtool/"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "/etc/amtool/ does not exist or is not writable by _daemon_"


@pytest.mark.abort_on_fail
def test_ca_certificates_dir_writable():
    """Assert /usr/local/share/ca-certificates/ is writable by the runtime user."""
    result = subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", "sh", "-c",
         "test -w /usr/local/share/ca-certificates/"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        "/usr/local/share/ca-certificates/ is not writable by _daemon_"
    )


@pytest.mark.abort_on_fail
def test_ssl_certs_dir_writable():
    """Assert /etc/ssl/certs/ is writable by the runtime user (for update-ca-certificates)."""
    result = subprocess.run(
        ["docker", "run", "--rm", IMAGE, "exec", "sh", "-c", "test -w /etc/ssl/certs/"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "/etc/ssl/certs/ is not writable by _daemon_"
