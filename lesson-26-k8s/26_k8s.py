"""Lesson 26: read-only Kubernetes namespace and pod inventory."""

from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from kubernetes.config.config_exception import ConfigException


def main() -> None:
    try:
        config.load_kube_config()  # Use the current kubeconfig context.
        core = client.CoreV1Api()
        print("Namespaces:")
        for namespace in core.list_namespace().items:
            print("-", namespace.metadata.name)

        print("Pods in default:")
        for pod in core.list_namespaced_pod(namespace="default").items:
            print("-", pod.metadata.name, pod.status.phase)
    except ConfigException as exc:
        print(f"Kubeconfig error: {exc}")
    except ApiException as exc:
        print(f"Kubernetes API error: {exc.status} {exc.reason}")


if __name__ == "__main__":
    main()
