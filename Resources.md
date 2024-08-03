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
