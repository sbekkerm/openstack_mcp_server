# OpenStack MCP Server

OpenStack MCP Server is a Model Context Protocol (MCP) server that provides seamless integration with OpenStack API.

---

## 🚀 Deployment

To build the application container image, use the following Podman command:

```bash
podman build . -t openstack_mcp_server
```

## ▶️ Starting the Server

To start the OpenStack MCP Server, follow these steps:

### 1. Create `.env` file

Create a file named `.env` in the root directory of the project. This file will store essential environment variables for the server.

```bash
OS_CLOUD=overcloud
OS_CLOUD_CONF_PATH=/server/clouds.yaml
OS_MCP_SERVER_HOST=0.0.0.0
OS_MCP_SERVER_PORT=9001
```

### Variable Explanations

- **OS_CLOUD**: Specifies the name of the cloud configuration to use from your `clouds.yaml` file.
- **OS_CLOUD_CONF_PATH**: Defines the path to the `clouds.yaml` file.
- **OS_MCP_SERVER_HOST**: Sets the IP address the MCP server will listen on. `0.0.0.0` means it will listen on all available network interfaces.
- **OS_MCP_SERVER_PORT**: Sets the port number the MCP server will use.

---

### 2. Create `clouds.yaml`

Create a `clouds.yaml` file. This file contains the authentication details required to connect to your OpenStack environment. Ensure this file is placed at the path specified by `OS_CLOUD_CONF_PATH` in your `.env` file.

```yaml
clouds:
  overcloud: # This should match OS_CLOUD in your .env file
    auth:
      auth_url: http://X.X.X.X:5000
      password: PASSWORD
      project_domain_name: Default
      project_name: admin
      user_domain_name: Default
      username: admin
    cacert: ''
    identity_api_version: '3'
    region_name: regionOne
    volume_api_version: '3'
```

⚠️ **Important:**

- Replace `http://X.X.X.X:5000` with the actual Keystone authentication URL of your OpenStack cloud.
- Replace `PASSWORD` with your actual password for the specified user.
- Adjust other parameters like `project_name`, `username`, `region_name`, etc., to match your specific OpenStack setup.

---

## Run the Application

```bash
podman run -d --name openstack_mcp_server \
  -p 9001:9001 \
  --env-file .env \
  -v $(pwd)/clouds.yaml:/server/clouds.yaml:Z \
  localhost/openstack_mcp_server:latest
```
