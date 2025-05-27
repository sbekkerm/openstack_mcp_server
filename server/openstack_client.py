"""
This module provides a wrapper class around the OpenStack SDK for easy access
to Openstack resources
"""
import openstack
from openstack.config.loader import OpenStackConfig


class OpenStackClient:
    """
    A client wrapper around OpenStack SDK
    """
    def __init__(self, config: OpenStackConfig):
        """Initialize the OpenStack connection with the given configuration"""
        self.conn = openstack.connection.Connection(config=config)

    def list_servers(self):
        """List all compute servers"""
        return list(self.conn.compute.servers())

    def list_images(self):
        """List all available compute images"""
        return list(self.conn.compute.images())

    def list_flavors(self):
        """List all available compute flavors"""
        return list(self.conn.compute.flavors())

    def list_keypairs(self):
        """List all keypairs associated with the compute service"""
        return list(self.conn.compute.keypairs())

    def list_networks(self):
        """List all available networks"""
        return list(self.conn.network.networks())

    def list_subnets(self):
        """List all available subnets"""
        return list(self.conn.network.subnets())

    def list_ports(self):
        """List all available network ports"""
        return list(self.conn.network.ports())

    def list_security_groups(self):
        """List all security groups"""
        return list(self.conn.network.security_groups())

    def list_routers(self):
        """List all network routers"""
        return list(self.conn.network.routers())

    def list_network_agents(self):
        """List all network agents"""
        return list(self.conn.network.agents())

    def network_info(self, name: str):
        """Get detailed information about a specific network by name"""
        return self.conn.network.find_network(name)

    def list_share_availability_zones(self):
        """List all availability zones for the Shared File System service"""
        return list(self.conn.share.availability_zones())
