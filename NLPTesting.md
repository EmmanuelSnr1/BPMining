# Test Cases
---

### **1. Process Discovery Intents**

#### **a. "process discovery - alpha"**

**Example Sentence:**

- "Please discover the process using the alpha algorithm."

**Explanation:**

- Contains required keyword: `"discover"`
- Contains optional keyword: `"alpha"`
  
#### **b. "process discovery - inductive"**

**Example Sentence:**

- "Could you discover the process model using the inductive method?"

**Explanation:**

- Contains required keyword: `"discover"`
- Contains optional keyword: `"inductive"`
  
#### **c. "process discovery - heuristics"**

**Example Sentence:**

- "I want to discover the process using the heuristics miner."

**Explanation:**

- Contains required keyword: `"discover"`
- Contains optional keyword: `"heuristics"`
  
#### **d. "process discovery - bpmn inductive"**

**Example Sentence:**

- "Please discover the BPMN process model using the inductive miner."

**Explanation:**

- Contains required keywords: `"discover"`, `"bpmn"`
- Contains optional keyword: `"inductive"`
  
#### **e. "process discovery - dfg"**

**Example Sentence:**

- "Can you discover the Directly Follows Graph for this process?"

**Explanation:**

- Contains required keyword: `"discover"`
- Contains optional keyword: `"dfg"`
  
#### **f. "process discovery" (Default)**

**Example Sentence:**

- "Discover the process for me."

**Explanation:**

- Contains required keyword: `"discover"`
- No optional keywords required

---

### **2. Performance Analysis Intents**

#### **a. "performance analysis - bottleneck"**

**Example Sentence:**

- "Analyze the bottlenecks in the current process."

**Explanation:**

- Contains required keyword: `"analyze"`
- Contains optional keyword: `"bottleneck"`
  
#### **b. "performance analysis - case duration"**

**Example Sentence:**

- "Could you analyze the case durations?"

**Explanation:**

- Contains required keyword: `"analyze"`
- Contains optional keywords: `"case"`, `"duration"`
  
#### **c. "performance analysis - frequency"**

**Example Sentence:**

- "Please analyze the frequency of activities in the process."

**Explanation:**

- Contains required keyword: `"analyze"`
- Contains optional keyword: `"frequency"`
  
#### **d. "performance analysis - resource utilization"**

**Example Sentence:**

- "Analyze the resource utilization for this process."

**Explanation:**

- Contains required keywords: `"analyze"`, `"resource"`
- Contains optional keyword: `"utilization"`
  
#### **e. "performance analysis" (Default)**

**Example Sentence:**

- "I need a performance analysis of the process."

**Explanation:**

- Contains required keyword: `"analyze"`
- No optional keywords required

---

### **3. Process Overview Intent**

#### **"process overview"**

**Example Sentence:**

- "Could you provide an overview of the process?"

**Explanation:**

- Contains required keyword: `"overview"`
- No optional keywords required

---

### **Additional Notes on Testing**

- **Ensure Correct Tokenization:**
  - The system lemmatizes and removes stop words. Words like "discovering" will be lemmatized to "discover".
  - The stop words list includes common words like "the", "is", "at", "which", "on", etc.

- **Case Insensitivity:**
  - The matching is case-insensitive due to converting tokens to lowercase.

- **Variations in Sentences:**
  - You can rephrase the sentences as long as they include the required and optional keywords.

---

### **Testing Each Sentence**

When you input each of these sentences into your system, the `getQueryType` method should classify them into the corresponding `queryType`. Here's how you can verify this:

1. **Input the Sentence:**
   - Use the sentence as the `query` parameter in your API request.

2. **Check the Response:**
   - The response should include the `queryType` matching the intent associated with the sentence.
   - For example, when you input "Please discover the process using the alpha algorithm.", the `queryType` should be `"process discovery - alpha"`.

3. **Verify the Action:**
   - The system should perform the appropriate action based on the `queryType`, such as calling `discoverProcessAndSaveAlpha` for `"process discovery - alpha"`.

---

### **Example API Requests**

**HTTP POST** `/nlp/query`

**Headers:**

```
Content-Type: application/json
```

**Request Body Examples:**

#### **1. Process Discovery - Alpha**

```json
{
    "query": "Please discover the process using the alpha algorithm.",
    "processFileId": 1
}
```

#### **2. Performance Analysis - Bottleneck**

```json
{
    "query": "Analyze the bottlenecks in the current process.",
    "processFileId": 2
}
```

#### **3. Process Overview**

```json
{
    "query": "Could you provide an overview of the process?",
    "processFileId": 3
}
```

---

### **Handling Unsupported Queries**

If you input a sentence that doesn't match any intent, such as:

- **Sentence:**
  - "Tell me something about the weather today."

- **Expected Behavior:**
  - The system should throw an `UnsupportedOperationException` with a message indicating an unknown query type.

- **Response:**

  ```json
  {
      "error": "Unsupported query type: Tell me something about the weather today."
  }
  ```

---

### **Ensuring Correctness**

To confirm that your system correctly classifies each query:

- **Check the Logs:**
  - Ensure that the `getQueryType` method returns the expected `queryType`.

- **Verify the Actions:**
  - Confirm that the `interpretAndExecute` method calls the correct service methods.

- **Inspect the Responses:**
  - The response should include the `status`, `queryType`, `result`, and `detailsUrl`.

---

### **Testing Edge Cases**

- **Missing Optional Keywords:**
  - Try sentences that only include required keywords to see if they default to a more general intent.

  **Example:**

  - **Sentence:** "Analyze the process."
  - **Expected `queryType`:** `"performance analysis"`

- **Additional Irrelevant Words:**
  - Include extra words to test robustness.

  **Example:**

  - **Sentence:** "Hey, could you please possibly analyze the frequency in the process when you get a chance?"
  - **Expected `queryType`:** `"performance analysis - frequency"`

---

### **Final Thoughts**

By testing your system with these example sentences, you should be able to validate that:

- **Intent Classification Works Correctly:**
  - The system accurately identifies the user's intent based on the presence of required and optional keywords.

- **Actions Are Executed Properly:**
  - The appropriate methods in your services are called in response to each query.

- **Error Handling Is Appropriate:**
  - Unsupported queries result in informative error messages.

---

**Feel free to use these example sentences to thoroughly test each intent in your NLP system. Let me know if you need any further assistance or have questions about specific intents or test cases!**
