# Tech Spec
## Stack
* Language: Python 3.10
* Framework: FastAPI 0.92.0
* Runtime: Uvicorn 0.20.0
* Database: PostgreSQL 14.5

## Hosting
* Platform: AWS (free tier available)
* Services:
	+ EC2 (t2.micro)
	+ RDS (PostgreSQL, t2.micro)
	+ S3 (for storage)
* Alternative platforms:
	+ Google Cloud Platform (GCP)
	+ Microsoft Azure

## Data Model
### Tables/Collections
#### mcp_servers
| Field | Type | Description |
| --- | --- | --- |
| id | UUID | Unique identifier |
| name | String | Server name |
| ip_address | String | Server IP address |
| port | Integer | Server port |
| status | String | Server status (online/offline) |
#### organizations
| Field | Type | Description |
| --- | --- | --- |
| id | UUID | Unique identifier |
| name | String | Organization name |
| mcp_servers | List[UUID] | List of MCP server IDs |

## API Surface
### Endpoints
1. **GET /mcp-servers**: Retrieve a list of all MCP servers
	* Method: GET
	* Path: /mcp-servers
	* Purpose: Retrieve a list of all MCP servers
2. **POST /mcp-servers**: Create a new MCP server
	* Method: POST
	* Path: /mcp-servers
	* Purpose: Create a new MCP server
3. **GET /mcp-servers/{id}**: Retrieve a specific MCP server by ID
	* Method: GET
	* Path: /mcp-servers/{id}
	* Purpose: Retrieve a specific MCP server by ID
4. **PUT /mcp-servers/{id}**: Update a specific MCP server
	* Method: PUT
	* Path: /mcp-servers/{id}
	* Purpose: Update a specific MCP server
5. **DELETE /mcp-servers/{id}**: Delete a specific MCP server
	* Method: DELETE
	* Path: /mcp-servers/{id}
	* Purpose: Delete a specific MCP server
6. **GET /organizations**: Retrieve a list of all organizations
	* Method: GET
	* Path: /organizations
	* Purpose: Retrieve a list of all organizations
7. **POST /organizations**: Create a new organization
	* Method: POST
	* Path: /organizations
	* Purpose: Create a new organization
8. **GET /organizations/{id}**: Retrieve a specific organization by ID
	* Method: GET
	* Path: /organizations/{id}
	* Purpose: Retrieve a specific organization by ID
9. **PUT /organizations/{id}**: Update a specific organization
	* Method: PUT
	* Path: /organizations/{id}
	* Purpose: Update a specific organization
10. **DELETE /organizations/{id}**: Delete a specific organization
	* Method: DELETE
	* Path: /organizations/{id}
	* Purpose: Delete a specific organization

## Security Model
* Authentication: OAuth 2.0 with JWT tokens
* Authorization: Role-based access control (RBAC) with three roles:
	+ Admin: full access to all resources
	+ Manager: read/write access to organizations and MCP servers
	+ User: read-only access to organizations and MCP servers
* Secrets management: AWS Secrets Manager
* IAM: AWS IAM roles and policies

## Observability
* Logging: AWS CloudWatch Logs
* Metrics: AWS CloudWatch Metrics
* Tracing: AWS X-Ray

## Build/CI
* Build tool: Docker
* CI/CD pipeline: GitHub Actions
* Testing framework: Pytest
* Code coverage: 80%