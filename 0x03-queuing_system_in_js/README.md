# 0x03. Queuing System in JS

## Description

This project focuses on implementing a queuing system using Redis and Node.js. It involves setting up a basic queuing system to handle tasks asynchronously. 

## Requirements

- Node.js
- Redis

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SHEFOO10/alx-backend.git
    cd alx-backend/0x03-queuing_system_in_js
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start Redis server if it’s not already running:

    ```bash
    redis-server
    ```
---

### Redis and Node.js Tasks

#### 0. Install a Redis Instance

1. Download and compile Redis:
    - `wget http://download.redis.io/releases/redis-6.0.10.tar.gz`
    - `tar xzf redis-6.0.10.tar.gz`
    - `cd redis-6.0.10`
    - `make`
2. Start Redis server in the background:
    - `src/redis-server &`
3. Verify Redis server is working:
    - `src/redis-cli ping`
4. Set and get a value in Redis:
    - `set Holberton School`
    - `get Holberton`
5. Kill Redis server:
    - Use `ps` and `grep` to find the PID and `kill [PID]`
6. Copy `dump.rdb` to the root of the Queuing project.

#### 1. Node Redis Client

1.  Install `node_redis` using npm.
2. Create a script `0-redis_client.js`:
    - [ ] Connect to Redis and log connection status using ES6 `import`.

#### 2. Node Redis Client and Basic Operations

- Create a script `1-redis_op.js`:
    - [ ] Implement `setNewSchool` and `displaySchoolValue` functions.
    - [ ] Use callbacks to perform Redis operations.

#### 3. Node Redis Client and Async Operations

- Create a script `2-redis_op_async.js`:
    - [ ] Modify `displaySchoolValue` to use `async/await` with `promisify`.

#### 4. Node Redis Client and Advanced Operations

- Create a script `4-redis_advanced_op.js`:
    - [ ] Store and display a hash value using Redis.

#### 5. Node Redis Client Publisher and Subscriber

1. Create `5-subscriber.js`:
    - [ ] Connect, subscribe to a channel, and handle incoming messages.
2. Create `5-publisher.js`:
    - [ ] Connect, publish messages to a channel with a delay.

#### 6. Create the Job Creator

- Create `6-job_creator.js`:
    - [ ] Use Kue to create and log job status.

#### 7. Create the Job Processor

- Create `6-job_processor.js`:
    - [ ] Use Kue to process jobs, handle job completion, and log messages.

#### 8. Track Progress and Errors with Kue: Create the Job Creator

 - Create `7-job_creator.js`:
    - [ ] Create multiple jobs with Kue and log job status, completion, and progress.

#### 9. Track Progress and Errors with Kue: Create the Job Processor

 - Create `7-job_processor.js`:
    - [ ] Handle blacklisted phone numbers, track job progress, and log errors.
