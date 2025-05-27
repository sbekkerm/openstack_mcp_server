"""
This module provides a FastMCP server for interacting with OpenStack
"""
from mcp.server.fastmcp import FastMCP
from server.config import config
from server.openstack_client import OpenStackClient


# Create server
mcp = FastMCP("Openstack MCP Server", host=config.host, port=config.port)
os_client = OpenStackClient(config.cloud_config)


@mcp.tool()
def list_servers() -> list:
    """List Servers"""
    return os_client.list_servers()


@mcp.tool()
def list_images() -> list:
    """List images"""
    return os_client.list_images()


@mcp.tool()
def list_flavors() -> list:
    """List flavors"""
    return os_client.list_flavors()


@mcp.tool()
def list_keypairs() -> list:
    """List keypair"""
    return os_client.list_keypairs()


@mcp.tool()
def list_networks() -> list:
    """List Networks"""
    return os_client.list_networks()


@mcp.tool()
def list_subnets() -> list:
    """List Subnets"""
    return os_client.list_subnets()


@mcp.tool()
def list_ports() -> list:
    """List Ports"""
    return os_client.list_ports()


@mcp.tool()
def list_security_groups() -> list:
    """List Security Groups"""
    return os_client.list_security_groups()


@mcp.tool()
def list_routers() -> list:
    """List Routers"""
    return os_client.list_routers()


@mcp.tool()
def list_network_agents() -> list:
    """List Network Agents"""
    return os_client.list_network_agents()


@mcp.tool()
def network_info(network_name: str) -> str:
    """Get detailed info about a network"""
    return os_client.network_info(network_name)


@mcp.tool()
def list_share_availability_zones() -> list:
    """List Shared File System Availability Zones"""
    return os_client.list_share_availability_zones()


def main():
    """Entry point"""
    mcp.run(transport="sse")


if __name__ == "__main__":
    main()
