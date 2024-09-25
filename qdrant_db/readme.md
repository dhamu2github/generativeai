# Qdrant Installation on Red Hat Linux

This guide will walk you through the process of installing and running Qdrant on Red Hat Linux. You can choose between using the Qdrant binary or running it with Docker. 

## Prerequisites

- Red Hat Linux or any RHEL-based distribution
- Administrator (root) access to install required packages

## Option 1: Running Qdrant Using Docker (Recommended)

Docker is the easiest and most reliable way to run Qdrant as it handles dependencies and environment configurations automatically.


### Step 1: Install Docker

1. Install Docker on your Red Hat system:

    ```bash
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo yum install docker-ce docker-ce-cli containerd.io
    ```

2. Start Docker:

    ```bash
    sudo systemctl start docker
    ```

3. Enable Docker to start at boot:

    ```bash
    sudo systemctl enable docker
    ```

4. Verify Docker is installed correctly:

    ```bash
    docker --version
    ```

### Step 2: Run Qdrant Using Docker

1. Run Qdrant with the following command:

    ```bash
    docker run -p 6333:6333 qdrant/qdrant
    ```

This command will download the latest Qdrant Docker image and run it, exposing the Qdrant API on port `6333`.

### Step 3: Verify Qdrant is Running

You can verify that Qdrant is running by accessing `http://localhost:6333` in your browser or using a Python client (described in **Usage with Python** below).





## Option 2: Running Qdrant Using the Binary

If you prefer not to use Docker, you can run Qdrant by downloading the binary directly.

### Step 1: Download the Qdrant Binary

Download the latest Qdrant release for Linux from GitHub. For example, to download version `v1.3.0`:

```bash
curl -LO https://github.com/qdrant/qdrant/releases/download/v1.3.0/qdrant-linux-x86_64



