# Lesson 26 — DIY

Use the existing ignored lab/app.py.

## Your Exercise

1. Load your current kubeconfig with config.load_kube_config().
2. Create a client.CoreV1Api instance.
3. Store the response from list_namespace(), then iterate over response.items and print each namespace.metadata.name.
4. List pods in the default namespace and print pod.metadata.name and pod.status.phase.
5. Handle ApiException and avoid modifying any resources.

## Questions to check

- Why does response.items have no parentheses?
- What is the difference between a Kubernetes model attribute and a JSON dictionary key?
