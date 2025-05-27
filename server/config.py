"""Configuration settings for the Openstack MCP Server"""
import os
import sys
import logging

from dataclasses import dataclass

from openstack.config.loader import OpenStackConfig
from openstack.exceptions import ConfigException


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@dataclass(frozen=True)
class Config:
    """Configuration class for the Openstack MCP server"""
    host: str
    port: int
    cloud_config: OpenStackConfig

    @classmethod
    def from_env(cls) -> 'Config':
        """Create Config instance from environment variables."""
        os_cloud_name = os.environ.get('OS_CLOUD', 'overcloud')
        os_cloud_conf_path = os.environ.get('OS_CLOUD_CONF_PATH', 'clouds.yaml')
        try:
            cloud_config = OpenStackConfig(
                config_files=[os_cloud_conf_path]
            ).get_one_cloud(cloud=os_cloud_name)
            logger.info("Loaded config for cloud %s from %s", os_cloud_name, os_cloud_conf_path)
        except ConfigException as e:
            logger.error("Failed to load cloud %s from %s: %s",
                         os_cloud_name,
                         os_cloud_conf_path,
                         e)
            sys.exit(1)
        return cls(
            host=os.environ.get('OS_MCP_SERVER_HOST', '127.0.0.1'),
            port=int(os.environ.get('OS_MCP_SERVER_PORT', 9001)),
            cloud_config=cloud_config
        )


# Initialize the configuration
config = Config.from_env()
