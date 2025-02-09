# Project Name

## Overview
This project implements a gRPC-based server to manage and evaluate access control policies using Open Policy Agent (OPA). It also includes a client for testing the server.

---

## Requirements

- Python 3.8 or higher
- gRPC tools for Python
- Open Policy Agent (OPA)

---

## Installation and Setup

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/lironbilya/Rig.git
cd Rig
```

### 2. Install Python Dependencies and 

Use `pip` to install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Install and Run OPA

#### Install OPA on Linux
Download and install OPA from the [official website](https://www.openpolicyagent.org/docs/latest/#running-opa):

```bash
# For Linux
curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64
chmod +x opa
sudo mv opa /usr/local/bin/

# Verify installation
opa version
```

#### Install OPA on Windows
1. Download the OPA binary for Windows from the [official releases page](https://github.com/open-policy-agent/opa/releases).
2. Extract the downloaded ZIP file.
3. Move the `opa.exe` file to a directory included in your system's `PATH` (e.g., `C:\Windows\System32` or another preferred location).
4. Verify the installation by opening a Command Prompt or PowerShell and running:
   ```cmd
   opa version
   ```

#### Run OPA Server
Start the OPA server:

```bash
opa run --server
```

By default, the OPA server runs on `http://localhost:8181`.

---

## Running the Server

Prepare and start the gRPC server by running the run.bat:

```bash
run.bat
```
The server will start listening on `localhost:50051`.

---

## Testing with the Client

Use the client to test the server:

```bash
python client.py
```

This sends test requests to the gRPC server and displays the results.
Edit the file for additional testings.

---

## Project Structure

- `main.py`: The main class of the project.
- `service.py`: Implements the gRPC server.
- `github_handler.py`: Fetches repository access data from the GitHub API.
- `policies_engine.py`: Evaluates given data with repository access data from GitHub using OPA.
- `policy.rego`: Contains OPA policy rules.
- `service.proto`: Defines the gRPC service and message structure.
- `requirements.txt`: Lists Python dependencies.
- `client.py`: Provides a simple client to test the server.

---

## Example Usage

1. Start OPA:

   ```bash
   opa run --server
   ```

2. Start the gRPC server:

   ```bash
   run.bat
   ```

3. Run the client to test:

   ```bash
   python client.py
   ```

---

## Notes
- Ensure OPA is running before starting the gRPC server.
- Ensure GitHub token is valid (github_handler file).
- Modify client data for additional testings.
---
