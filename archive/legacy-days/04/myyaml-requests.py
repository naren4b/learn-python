import requests
import yaml
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_and_save_yaml(url: str, output_file: str, timeout: int = 10) -> bool:
    """
    Download YAML from URL and save to file.

    Args:
        url: URL to fetch YAML from
        output_file: Path to save the file
        timeout: Request timeout in seconds

    Returns:
        True if successful, False otherwise
    """
    try:
        # Add timeout and error handling
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        # Parse YAML
        data = yaml.load(response.text, Loader=yaml.SafeLoader)

        # Use context manager - auto closes file
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            yaml.dump(data, f)

        logger.info(f"✓ Successfully saved YAML to {output_file}")
        return True

    except requests.exceptions.Timeout:
        logger.error(f"Timeout fetching {url}")
        return False

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e.response.status_code} - {e}")
        return False

    except yaml.YAMLError as e:
        logger.error(f"YAML parsing error: {e}")
        return False

    except OSError as e:
        logger.error(f"File I/O error: {e}")
        return False


# Main execution
if __name__ == "__main__":
    url = "https://gist.githubusercontent.com/crrobinson14/8290174/raw/ad4d8fb6dfa621f2d4bc689d3b83d0ffd0270894/api-docs.yml"
    download_and_save_yaml(url, "res/api-docs.yml")
