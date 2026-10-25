# Lesson 26 — Kubernetes automation with Python

## Goal
Use the official Kubernetes Python client to inspect namespaces and pods without modifying cluster resources.

## Setup

Use your existing kubeconfig and context. Confirm access before running Python:

```bash
kubectl config current-context
kubectl get namespaces
uv venv .venv
uv pip install --python .venv/bin/python -r lesson-26-k8s/requirements.txt
.venv/bin/python lesson-26-k8s/26_k8s.py
```

## Core operations

| Python SDK | kubectl equivalent |
| --- | --- |
| `config.load_kube_config()` | Use local kubeconfig/current context |
| `client.CoreV1Api()` | Core Kubernetes API |
| `list_namespace()` | `kubectl get namespaces` |
| `list_namespaced_pod("default")` | `kubectl get pods -n default` |
| `list_pod_for_all_namespaces()` | `kubectl get pods -A` |

## Example

```python
from kubernetes import client, config

config.load_kube_config()
api = client.CoreV1Api()

for ns in api.list_namespace().items:
    print(ns.metadata.name)
```

## Notes

- SDK responses are model objects; for example `pod.metadata.name`, not `pod["metadata"]["name"]`.
- `config.load_kube_config(context="...")` selects an explicit context.
- `config.load_incluster_config()` is for workloads running inside Kubernetes.
- Handle `ApiException` for 403 Forbidden, 404 Not Found and other API failures.
- Be careful with cluster-wide queries and RBAC permissions; this lesson is **read-only**.
- For large inventories, use API pagination (`limit` and `_continue`) rather than requesting everything in one response.

[DIY](diy.md) · [Reference](26_k8s.py) · [Official Python client](https://github.com/kubernetes-client/python) · [API reference](https://kubernetes.readthedocs.io/en/stable/).
