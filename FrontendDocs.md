# Joint JS Petri Net.
Tool for displaying interactive diagrams 
https://www.jointjs.com/demos/petri-nets

### Frontend Planning for Your Process Mining Application

Let's break down the frontend structure based on the features and endpoints we've discussed. Here's a detailed plan for each section of the application, including the appearance, functionality, and the underlying Vue.js components.

### 1. **Login and Authentication Page**

**Purpose:**  
To authenticate users before they can access the main application.

**Look and Feel:**  
- **Clean and Simple Design:** Use Tailwind CSS with Flowbite for form styling.
- **Form Elements:** Email/Username and Password fields, with "Login" and "Sign Up" buttons.
- **Branding:** A logo or title at the top to give a sense of identity to the application.

**Components:**
- **LoginForm.vue:** Handles the form submission and authentication logic.
- **AuthService.js:** Handles API calls for user authentication.

### 2. **Dashboard Overview**

**Purpose:**  
To give users a quick overview of their uploaded/available process files, recent activity, and general statistics.

**Look and Feel:**  
- **Card Layout:** Each card represents a different section, such as "Uploaded Files", "Recent Activity", "Quick Stats".
- **Navigation Bar:** At the top, with links to "Dashboard", "Process Files", "Analytics", and "Profile".

**Components:**
- **Dashboard.vue:** The main component that brings together all the dashboard elements.
- **ProcessFilesList.vue:** Displays a list of all process files with quick actions (view, edit, delete).
- **RecentActivity.vue:** A card showing the latest activity.
- **QuickStats.vue:** A card summarizing key metrics like the number of files, total events processed, etc.

### 3. **Process Files Page**

**Purpose:**  
To list all the available process files that users can select for analysis.

**Look and Feel:**  
- **Table/List View:** A table showing all the process files with columns like "File Name", "Upload Date", "File Type", "Actions".
- **File Selection:** Each row has a "Select" button that takes the user to the Process Workspace.
- **Search/Filter Options:** A search bar to filter files by name, date, or tag.

**Components:**
- **ProcessFiles.vue:** Main component managing the list of files.
- **FileTable.vue:** Handles the display of files in a table format.
- **FileActions.vue:** Contains buttons for viewing, editing, or deleting files.

### 4. **Process Workspace (Work Area)**

**Purpose:**  
This is the main interactive area where users analyze and visualize their process files.

**Look and Feel:**  
- **Tabbed/Accordion Layout:** A two-column layout with tabs or an accordion on the left to switch between different types of analysis (General, Performance, Frequency, Bottleneck, Resource Utilization).
- **Visualization Area:** The right side displays the corresponding visualizations or results based on the selected tab.
- **Interactive Queries:** A text input at the top allows users to type natural language queries, with results dynamically updating the visualizations.

**Components:**
- **Workspace.vue:** The main layout component for the workspace.
- **TabMenu.vue:** Handles the tab/accordion switching between different analytics.
- **VisualizationArea.vue:** Displays charts, graphs, and process models based on the selected tab.
- **NLQueryInput.vue:** An input field for users to type queries, with results updating the visualization area.

### 5. **Analytics Tabs**

Each of these tabs within the Process Workspace will handle different aspects of process mining and analytics:

- **General Analytics Tab:**
  - **Look and Feel:** Overview metrics and summary, with basic charts.
  - **Components:** 
    - **GeneralTab.vue:** Displays summary statistics, such as the number of events, unique activities, etc.
    - **SummaryChart.vue:** Simple charts summarizing the overall process flow.

- **Performance Analysis Tab:**
  - **Look and Feel:** Detailed performance metrics like bottlenecks, case durations.
  - **Components:** 
    - **PerformanceTab.vue:** Contains performance-related metrics and charts.
    - **BottleneckChart.vue:** Visualizes bottlenecks in the process.
    - **CaseDurationChart.vue:** Displays the distribution of case durations.

- **Frequency Analysis Tab:**
  - **Look and Feel:** Visualization of event frequency and common paths.
  - **Components:** 
    - **FrequencyTab.vue:** Displays frequency-related data.
    - **PathFrequencyChart.vue:** Visualizes the most frequent paths in the process.

- **Bottleneck Analysis Tab:**
  - **Look and Feel:** Focused on identifying bottlenecks and their impact.
  - **Components:** 
    - **BottleneckTab.vue:** Detailed view of identified bottlenecks.
    - **BottleneckDetails.vue:** Provides detailed insights into specific bottlenecks.

- **Resource Utilization Tab:**
  - **Look and Feel:** Charts and graphs showing how resources are utilized in the process.
  - **Components:** 
    - **UtilizationTab.vue:** Displays resource utilization metrics.
    - **ResourceChart.vue:** Visualizes resource allocation and usage.

### 6. **Profile and Settings Page**

**Purpose:**  
To allow users to manage their profile, adjust settings, and manage preferences.

**Look and Feel:**  
- **Form Layout:** Sections for updating user information, changing passwords, and setting preferences.
- **Tabs or Accordion:** Organize sections into "Profile", "Security", "Preferences".

**Components:**
- **Profile.vue:** The main profile management component.
- **ProfileForm.vue:** Form for updating user details.
- **SecuritySettings.vue:** Allows users to change passwords or enable 2FA.
- **Preferences.vue:** Set user preferences like notification settings, default analysis types.

### 7. **Logout**

**Purpose:**  
To securely log users out of the application.

**Look and Feel:**  
- **Simple Button:** Located in the navigation bar or user dropdown menu.

**Components:**
- **LogoutButton.vue:** Handles the logout action and redirects to the login page.

### Additional Considerations

- **Responsive Design:** Ensure that all components are responsive, especially the Process Workspace, which may require different layouts on mobile devices.
- **Error Handling:** Each page and component should handle errors gracefully, displaying user-friendly messages.
- **State Management:** Consider using Vuex for managing state across the application, especially for managing authentication states and process file data.
- **API Integration:** Axios or Fetch API for making HTTP requests to the backend endpoints we designed.

### Summary

This frontend plan outlines the structure of each page and component in your application, ensuring a smooth and interactive user experience. By using Vue.js with Tailwind CSS and Flowbite, you can create a clean, modern interface that is both functional and aesthetically pleasing. Each part of the application is designed to handle specific tasks, from viewing process files to performing detailed analytics, making it easier for users to interact with their data.
