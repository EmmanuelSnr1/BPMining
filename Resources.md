# Github Repos. 
- General Library Information on PM - https://github.com/TheWoops/awesome-processmining

# Database Design. 
Certainly! Below is a documentation of the purpose, use cases, types of data stored, and relevance of each entity in your project.

### Users Entity

#### Purpose
The `Users` entity represents the users of the web application. It is used for managing user authentication and authorization.

#### Use Cases
- Registering new users.
- Authenticating users during login.
- Managing user profiles and permissions.

#### Data Stored
- `userId`: A unique identifier for the user.
- `email`: The user's email address, used for communication and as a unique identifier.
- `fullName`: The full name of the user.
- `password`: The user's password, stored securely.

#### Relevance
The `Users` entity is fundamental for managing who has access to the system and for tracking user-specific actions, queries, and preferences within the application.

### Processes Entity

#### Purpose
The `Processes` entity represents business processes being analyzed by the application. It stores metadata about each process.

#### Use Cases
- Defining and categorizing different business processes.
- Associating event logs and analysis results with specific processes.

#### Data Stored
- `id`: A unique identifier for the process.
- `name`: The name of the process.
- `description`: A detailed description of the process.

#### Relevance
The `Processes` entity is critical for organizing and managing the various business processes that the application will analyze using process mining techniques.

### EventLogs Entity

#### Purpose
The `EventLogs` entity stores detailed event logs related to business processes. These logs are essential for process mining activities.

#### Use Cases
- Ingesting and storing event data from different business processes.
- Analyzing events to identify patterns, bottlenecks, and performance issues.

#### Data Stored
- `id`: A unique identifier for the event log entry.
- `processId`: The identifier of the process this event belongs to.
- `eventName`: The name of the event.
- `eventTimestamp`: The timestamp when the event occurred.
- `resource`: The resource or entity involved in the event.
- `eventData`: Additional data related to the event, stored as JSON or text.

#### Relevance
The `EventLogs` entity is crucial for capturing the raw data necessary for performing process mining. It enables detailed analysis and visualization of business processes.

### NLPQueries Entity

#### Purpose
The `NLPQueries` entity records natural language queries made by users and their corresponding results.

#### Use Cases
- Storing user queries for future reference and analysis.
- Tracking and improving the accuracy and performance of NLP components.
- Providing query history to users.

#### Data Stored
- `id`: A unique identifier for the NLP query.
- `userId`: The identifier of the user who made the query.
- `queryText`: The text of the natural language query.
- `queryResult`: The result of the query, stored as JSON or text.
- `createdAt`: The timestamp when the query was made.

#### Relevance
The `NLPQueries` entity is important for enabling natural language interactions with the system. It helps in tracking user queries and enhancing the NLP model based on historical data.

### ProcessBottlenecks Entity

#### Purpose
The `ProcessBottlenecks` entity stores information about identified bottlenecks within business processes.

#### Use Cases
- Recording bottlenecks detected during process mining analysis.
- Providing insights to users for process optimization.

#### Data Stored
- `id`: A unique identifier for the bottleneck entry.
- `processId`: The identifier of the process where the bottleneck was identified.
- `description`: A detailed description of the bottleneck.
- `createdAt`: The timestamp when the bottleneck was recorded.

#### Relevance
The `ProcessBottlenecks` entity is essential for highlighting areas within processes that need improvement. It supports business process optimization efforts by identifying points of inefficiency.

### DecisionPaths Entity

#### Purpose
The `DecisionPaths` entity captures information about decision-making paths in business processes.

#### Use Cases
- Storing and analyzing decision points within processes.
- Helping users understand the flow of decisions and their impact on process outcomes.

#### Data Stored
- `id`: A unique identifier for the decision path entry.
- `processId`: The identifier of the process related to the decision path.
- `pathData`: Data representing the decision path, stored as JSON or text.
- `createdAt`: The timestamp when the decision path was recorded.

#### Relevance
The `DecisionPaths` entity is useful for understanding and optimizing decision points within business processes. It helps in visualizing and improving decision-making flows.

### PerformanceIssues Entity

#### Purpose
The `PerformanceIssues` entity stores information about performance issues identified in business processes.

#### Use Cases
- Recording performance issues detected during process mining.
- Providing insights to users for addressing and resolving performance problems.

#### Data Stored
- `id`: A unique identifier for the performance issue entry.
- `processId`: The identifier of the process where the performance issue was identified.
- `issueDescription`: A detailed description of the performance issue.
- `createdAt`: The timestamp when the performance issue was recorded.

#### Relevance
The `PerformanceIssues` entity is crucial for tracking and resolving issues that affect the performance of business processes. It supports continuous process improvement by identifying and addressing performance bottlenecks.

### Summary

Each entity in the database serves a specific role in supporting the functionality and objectives of the application. Together, they enable comprehensive process mining, natural language querying, and business process optimization. The data stored in these entities provide the foundation for detailed analysis, insights, and decision-making within the system.

# API Doc
To effectively interact with the entities in your application, you'll need to create a set of RESTful API endpoints. These endpoints will allow clients (like your frontend built with Vue.js) to perform CRUD (Create, Read, Update, Delete) operations and some additional actions specific to your application's needs. Below are the suggested API endpoints for each entity:

### Users API Endpoints

1. **Create a new user**
   - **Endpoint**: `POST /api/users`
   - **Description**: Registers a new user.
   - **Request Body**: `{ "email": "user@example.com", "fullName": "User Name", "password": "password123" }`

2. **Get a user by ID**
   - **Endpoint**: `GET /api/users/{id}`
   - **Description**: Retrieves a user's details by their ID.

3. **Update a user's information**
   - **Endpoint**: `PUT /api/users/{id}`
   - **Description**: Updates a user's details.
   - **Request Body**: `{ "email": "newemail@example.com", "fullName": "New Name", "password": "newpassword123" }`

4. **Delete a user**
   - **Endpoint**: `DELETE /api/users/{id}`
   - **Description**: Deletes a user by their ID.

5. **Authenticate user (Login)**
   - **Endpoint**: `POST /api/users/login`
   - **Description**: Authenticates a user and generates a token.
   - **Request Body**: `{ "email": "user@example.com", "password": "password123" }`

### Processes API Endpoints

1. **Create a new process**
   - **Endpoint**: `POST /api/processes`
   - **Description**: Adds a new business process.
   - **Request Body**: `{ "name": "Process Name", "description": "Process Description" }`

2. **Get all processes**
   - **Endpoint**: `GET /api/processes`
   - **Description**: Retrieves a list of all processes.

3. **Get a process by ID**
   - **Endpoint**: `GET /api/processes/{id}`
   - **Description**: Retrieves details of a specific process by its ID.

4. **Update a process**
   - **Endpoint**: `PUT /api/processes/{id}`
   - **Description**: Updates a specific process.
   - **Request Body**: `{ "name": "Updated Process Name", "description": "Updated Description" }`

5. **Delete a process**
   - **Endpoint**: `DELETE /api/processes/{id}`
   - **Description**: Deletes a specific process by its ID.

### EventLogs API Endpoints

1. **Create a new event log**
   - **Endpoint**: `POST /api/eventlogs`
   - **Description**: Adds a new event log entry.
   - **Request Body**: `{ "processId": 1, "eventName": "Event Name", "eventTimestamp": "2024-08-03T10:00:00Z", "resource": "Resource Name", "eventData": "Additional data in JSON or text" }`

2. **Get all event logs for a process**
   - **Endpoint**: `GET /api/eventlogs?processId={processId}`
   - **Description**: Retrieves all event logs for a specific process.

3. **Get an event log by ID**
   - **Endpoint**: `GET /api/eventlogs/{id}`
   - **Description**: Retrieves details of a specific event log by its ID.

4. **Update an event log**
   - **Endpoint**: `PUT /api/eventlogs/{id}`
   - **Description**: Updates a specific event log.
   - **Request Body**: `{ "eventName": "Updated Event Name", "eventTimestamp": "2024-08-04T10:00:00Z", "resource": "Updated Resource", "eventData": "Updated additional data" }`

5. **Delete an event log**
   - **Endpoint**: `DELETE /api/eventlogs/{id}`
   - **Description**: Deletes a specific event log by its ID.

### NLPQueries API Endpoints

1. **Create a new NLP query**
   - **Endpoint**: `POST /api/nlpqueries`
   - **Description**: Submits a new NLP query.
   - **Request Body**: `{ "userId": 1, "queryText": "What are the bottlenecks in process X?" }`

2. **Get all NLP queries for a user**
   - **Endpoint**: `GET /api/nlpqueries?userId={userId}`
   - **Description**: Retrieves all NLP queries made by a specific user.

3. **Get an NLP query by ID**
   - **Endpoint**: `GET /api/nlpqueries/{id}`
   - **Description**: Retrieves details of a specific NLP query by its ID.

4. **Update an NLP query result**
   - **Endpoint**: `PUT /api/nlpqueries/{id}`
   - **Description**: Updates the result of a specific NLP query.
   - **Request Body**: `{ "queryResult": "Updated result in JSON or text" }`

5. **Delete an NLP query**
   - **Endpoint**: `DELETE /api/nlpqueries/{id}`
   - **Description**: Deletes a specific NLP query by its ID.

### ProcessBottlenecks API Endpoints

1. **Create a new process bottleneck**
   - **Endpoint**: `POST /api/processbottlenecks`
   - **Description**: Records a new process bottleneck.
   - **Request Body**: `{ "processId": 1, "description": "Description of the bottleneck" }`

2. **Get all bottlenecks for a process**
   - **Endpoint**: `GET /api/processbottlenecks?processId={processId}`
   - **Description**: Retrieves all bottlenecks for a specific process.

3. **Get a bottleneck by ID**
   - **Endpoint**: `GET /api/processbottlenecks/{id}`
   - **Description**: Retrieves details of a specific bottleneck by its ID.

4. **Update a bottleneck**
   - **Endpoint**: `PUT /api/processbottlenecks/{id}`
   - **Description**: Updates a specific bottleneck.
   - **Request Body**: `{ "description": "Updated description of the bottleneck" }`

5. **Delete a bottleneck**
   - **Endpoint**: `DELETE /api/processbottlenecks/{id}`
   - **Description**: Deletes a specific bottleneck by its ID.

### DecisionPaths API Endpoints

1. **Create a new decision path**
   - **Endpoint**: `POST /api/decisionpaths`
   - **Description**: Records a new decision path.
   - **Request Body**: `{ "processId": 1, "pathData": "Decision path data in JSON or text" }`

2. **Get all decision paths for a process**
   - **Endpoint**: `GET /api/decisionpaths?processId={processId}`
   - **Description**: Retrieves all decision paths for a specific process.

3. **Get a decision path by ID**
   - **Endpoint**: `GET /api/decisionpaths/{id}`
   - **Description**: Retrieves details of a specific decision path by its ID.

4. **Update a decision path**
   - **Endpoint**: `PUT /api/decisionpaths/{id}`
   - **Description**: Updates a specific decision path.
   - **Request Body**: `{ "pathData": "Updated decision path data in JSON or text" }`

5. **Delete a decision path**
   - **Endpoint**: `DELETE /api/decisionpaths/{id}`
   - **Description**: Deletes a specific decision path by its ID.

### PerformanceIssues API Endpoints

1. **Create a new performance issue**
   - **Endpoint**: `POST /api/performanceissues`
   - **Description**: Records a new performance issue.
   - **Request Body**: `{ "processId": 1, "issueDescription": "Description of the performance issue" }`

2. **Get all performance issues for a process**
   - **Endpoint**: `GET /api/performanceissues?processId={processId}`
   - **Description**: Retrieves all performance issues for a specific process.

3. **Get a performance issue by ID**
   - **Endpoint**: `GET /api/performanceissues/{id}`
   - **Description**: Retrieves details of a specific performance issue by its ID.

4. **Update a performance issue**
   - **Endpoint**: `PUT /api/performanceissues/{id}`
   - **Description**: Updates a specific performance issue.
   - **Request Body**: `{ "issueDescription": "Updated description of the performance issue" }`

5. **Delete a performance issue**
   - **Endpoint**: `DELETE /api/performanceissues/{id}`
   - **Description**: Deletes a specific performance issue by its ID


#### FileMetadata Entity

##### Purpose
The `FileMetadata` entity stores metadata about the files uploaded to the system. This includes the file's name, path, size, and upload timestamp.

##### Use Cases
- Tracking uploaded files and their storage locations.
- Retrieving file metadata for preprocessing and analysis.
- Managing file-related operations, such as deletions or updates.

##### Data Stored
- `id`: A unique identifier for the file metadata.
- `filename`: The name of the uploaded file.
- `filepath`: The path where the file is stored.
- `filesize`: The size of the file in bytes.
- `uploadTimestamp`: The timestamp when the file was uploaded.

##### Relevance
The `FileMetadata` entity is essential for managing large file uploads efficiently. It decouples file storage from the database, ensuring that the database handles only metadata while the actual files are stored in a suitable storage system.

#### PreprocessedData Entity

##### Purpose
The `PreprocessedData` entity stores information about the data that has been preprocessed from the uploaded files. This includes references to the original file and the associated process, as well as the preprocessed data itself.

##### Use Cases
- Storing results of data preprocessing for further analysis.
- Linking preprocessed data to specific processes and files.
- Retrieving preprocessed data for process mining and analysis tasks.

##### Data Stored
- `id`: A unique identifier for the preprocessed data.
- `fileId`: The identifier of the file from which this data was preprocessed.
- `processId`: The identifier of the process associated with this data.
- `data`: The preprocessed data, stored as JSON or text.
- `createdAt`: The timestamp when the data was created.

##### Relevance
The `PreprocessedData` entity plays a crucial role in managing the results of data preprocessing tasks. It ensures that the processed data is stored in a structured manner, linked to the original files and processes, facilitating efficient data retrieval and analysis.


### Summary

These endpoints provide a comprehensive set of operations to manage users, processes, event logs, NLP queries, bottlenecks, decision paths, and performance issues. They enable full CRUD operations and allow for the essential functionalities needed to support the application's objectives in process mining and business process optimization.
These additional entities (`FileMetadata` and `PreprocessedData`) and their corresponding tables help manage the large file uploads and the resulting preprocessed data efficiently. By storing metadata and preprocessed data separately from the actual files, the system can handle large datasets without overwhelming the database, ensuring scalability and performance.
