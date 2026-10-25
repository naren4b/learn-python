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

## Understanding the namespace loop

```python
response = api.list_namespace()  # Returns a V1NamespaceList model
namespaces = response.items      # List of V1Namespace objects

for namespace in namespaces:
    name = namespace.metadata.name
    print(name)
```

| Expression | Meaning |
| --- | --- |
| `api` | `CoreV1Api` client |
| `api.list_namespace()` | Request namespace objects from the Kubernetes API |
| `response.items` | Attribute containing a list of namespace objects |
| `for namespace in response.items` | Visit each namespace object |
| `namespace.metadata.name` | Read the namespace's name from its metadata |

The result is a **Python SDK model** rather than a raw dictionary. Its structure is conceptually similar to `{"items": [{"metadata": {"name": "default"}}]}`, but access is through attributes.

**Frequently asked: Why `.items`, not `.items()`?** In a normal Python dictionary `data.items()` is a method that returns key/value pairs. Here `response.items` is an attribute holding a list, so it needs **no parentheses**. Calling `response.items()` would raise a `TypeError`.

**Expected output** depends on the cluster, such as `default`, `kube-system`, and `monitoring`.

## Learning questions and answers

**Is `kubernetes` a package?** Yes, it is the installed third-party Python package. `client` and `config` are imported from it. `client.CoreV1Api()` constructs an API client object; `config.load_kube_config()` loads credentials and the selected cluster context.

**Why `pod.metadata.name` instead of `pod["metadata"]["name"]`?** The Python client normally returns typed Kubernetes model objects, whereas `json.load()` returns Python dictionaries/lists. Use attribute access for model objects.

**What is a safe first automation?** List namespaces and pods without mutation. Confirm the current context with `kubectl config current-context` before running.

## Notes

- SDK responses are model objects; for example `pod.metadata.name`, not `pod["metadata"]["name"]`.
- `config.load_kube_config(context="...")` selects an explicit context.
- `config.load_incluster_config()` is for workloads running inside Kubernetes.
- Handle `ApiException` for 403 Forbidden, 404 Not Found and other API failures.
- Be careful with cluster-wide queries and RBAC permissions; this lesson is **read-only**.
- For large inventories, use API pagination (`limit` and `_continue`) rather than requesting everything in one response.

[DIY](diy.md) · [Reference](26_k8s.py) · [Official Python client](https://github.com/kubernetes-client/python) · [API reference](https://kubernetes.readthedocs.io/en/stable/).
