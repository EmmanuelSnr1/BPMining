# NLP for Unstructured Data Integration in Process Mining

## Objective
Use Natural Language Processing (NLP) techniques to integrate unstructured data (e.g., emails, customer reviews) with structured event logs to enhance process analysis and decision-making.

### Petri Nets 
A mathematical model for modelling processes and data flow, showing states and so on. 

# Notes
Data found: from Process mining Website https://www.processmining.org/event-data.html 
1. Customer purchase order handling process
XES and CSV: https://data.4tu.nl/articles/_/12715853/1
Resources on Internet and Web application Configurations
https://www.youtube.com/watch?v=FBkZ2TJZZUY&t=3s

![image](https://github.com/user-attachments/assets/65194d00-433b-4c22-9a01-7215ca317ae4)
Advantages of Process Mining for organisations 
https://lingarogroup.com/blog/process-mining-models-and-how-to-use-them-in-your-business#:~:text=six%20steps%20of%20a%20proper,and%20process%20improvement%20and%20support. 

## Expanded Focus Areas
1. Text Mining: Techniques to extract meaningful patterns and knowledge from unstructured text.
2. Sentiment Analysis: Assessing the sentiments expressed in text data to gain insights into customer satisfaction and employee feedback.
3. Information Extraction: Identifying and extracting relevant entities, relationships, and events from unstructured text data.

## Key Questions
1. Integration Techniques:
   - How can unstructured text data be effectively integrated with event logs to enhance process analysis?
   - What are the challenges and best practices for integrating diverse data sources?

2. NLP Techniques:
   - What are the best NLP techniques to extract meaningful information from textual data in the context of process mining?
   - How can sentiment analysis improve the understanding of customer and employee experiences?
   - NLP

3. Impact on Process Mining:
   - How can integrated data improve process discovery, conformance checking, and enhancement?
   - What are the implications for process optimization and decision-making?

## Business Problem and Solutions
Many businesses face challenges in understanding their processes due to the fragmented nature of data. Structured event logs provide valuable insights into process sequences, but they often miss the context and qualitative aspects captured in unstructured data sources like emails, customer reviews, and service tickets. This lack of integration can lead to suboptimal decision-making and process inefficiencies.

### Proposed Solution
Integrating unstructured text data with structured event logs using advanced NLP techniques can provide a more holistic view of business processes. This integration can uncover hidden patterns, identify process bottlenecks, and enhance overall process efficiency.

### Potential Applications
1. **Customer Service Improvement**:
   - **Problem**: Customer service processes often miss critical insights from customer feedback, leading to unresolved issues and decreased satisfaction.
   - **Solution**: By integrating customer reviews and service emails with service logs, businesses can identify common pain points, improve response times, and tailor services to better meet customer needs.

2. **Product Development**:
   - **Problem**: Feedback from various channels (social media, support tickets, user reviews) is not systematically analyzed, delaying necessary product improvements.
   - **Solution**: NLP can extract key themes and sentiments from this unstructured data, informing product development teams about urgent fixes and feature enhancements.

3. **Employee Performance and Engagement**:
   - **Problem**: Employee feedback collected through surveys and emails is often underutilized, leading to poor engagement and high turnover.
   - **Solution**: Sentiment analysis on employee feedback can provide insights into workplace morale and highlight areas needing attention, enabling proactive management interventions.

4. **Compliance and Risk Management**:
   - **Problem**: Non-compliance issues are often buried in unstructured reports and communications, leading to regulatory risks.
   - **Solution**: Integrating textual data from audit reports and communications with compliance logs can help identify and address compliance issues more effectively.

## 2-Month Plan

### Week 1: Foundation and Planning
- **Day 1-2**: 
  - **Objective**: Understand the basics of NLP and Process Mining.
  - **Study Materials**: 
    - [Introduction to NLP (Coursera)](https://www.coursera.org/learn/language-processing)
    - [Introduction to Process Mining (Process Mining Book by Wil van der Aalst)](https://www.springer.com/gp/book/9783642193446)
- **Day 3-4**: 
  - **Objective**: Explore datasets and tools.
  - **Study Materials**:
    - Explore the datasets mentioned earlier (e.g., Enron Email Dataset, Amazon Reviews).
    - Install and familiarize yourself with ProM and Celonis Snap.
- **Day 5-7**:
  - **Objective**: Develop a detailed project plan.
  - **Tasks**: 
    - Define specific objectives and milestones.
    - Identify potential challenges and mitigation strategies.
    - Create a timeline for the remaining weeks.

### Week 2: Deep Dive into Text Mining and Sentiment Analysis
- **Day 1-3**: 
  - **Objective**: Learn text mining techniques.
  - **Study Materials**:
    - [Text Mining with R: A Tidy Approach](https://www.tidytextmining.com/)
    - [DataCamp’s Text Mining Course](https://www.datacamp.com/courses/author/juliam-gamper)
  - **Practice Tasks**: 
    - Perform basic text mining on the Enron Email Dataset.
- **Day 4-7**: 
  - **Objective**: Study sentiment analysis.
  - **Study Materials**:
    - [Sentiment Analysis with Python (Kaggle)](https://www.kaggle.com/ankurzing/sentiment-analysis-of-imdb-movie-reviews)
  - **Practice Tasks**:
    - Apply sentiment analysis to the Amazon Reviews Dataset.
    - Experiment with different sentiment analysis models (e.g., VADER, BERT).

### Week 3: Information Extraction and Data Integration
- **Day 1-3**: 
  - **Objective**: Learn about information extraction techniques.
  - **Study Materials**:
    - [Named Entity Recognition (NER) with spaCy](https://spacy.io/usage/linguistic-features#named-entities)
  - **Practice Tasks**:
    - Extract entities from the Enron Email Dataset.
- **Day 4-7**: 
  - **Objective**: Integrate text data with structured event logs.
  - **Study Materials**:
    - Research papers on data integration techniques.
  - **Practice Tasks**:
    - Align email data with synthetic event logs.
    - Develop scripts to merge text data with event logs based on timestamps.

### Week 4: Developing Initial Models
- **Day 1-3**: 
  - **Objective**: Build initial NLP models.
  - **Study Materials**:
    - Tutorials on building text classification and sentiment analysis models (e.g., using scikit-learn or TensorFlow).
  - **Practice Tasks**:
    - Train a text classification model on email data.
    - Evaluate model performance using appropriate metrics.
- **Day 4-7**: 
  - **Objective**: Implement information extraction models.
  - **Practice Tasks**:
    - Build and test NER models.
    - Extract and analyze entities from customer reviews.

### Week 5: Process Mining and Analysis
- **Day 1-3**: 
  - **Objective**: Study process mining techniques.
  - **Study Materials**:
    - [Process Mining: Data Science in Action by Wil van der Aalst](https://link.springer.com/book/10.1007/978-3-662-49851-4)
  - **Practice Tasks**:
    - Perform basic process mining using ProM.
- **Day 4-7**: 
  - **Objective**: Analyze integrated data with process mining tools.
  - **Practice Tasks**:
    - Import and analyze integrated data in ProM or Celonis Snap.
    - Identify process inefficiencies and suggest improvements.

### Week 6: Advanced Analysis and Model Improvement
- **Day 1-3**: 
  - **Objective**: Refine NLP models and integration techniques.
  - **Practice Tasks**:
    - Improve text mining and sentiment analysis models.
    - Enhance data integration scripts for better alignment.
- **Day 4-7**: 
  - **Objective**: Conduct advanced process analysis.
  - **Practice Tasks**:
    - Use integrated data to perform conformance checking and process enhancement.
    - Experiment with different process mining techniques.

### Week 7: Validation and Evaluation
- **Day 1-3**: 
  - **Objective**: Validate models and frameworks.
  - **Practice Tasks**:
    - Validate the accuracy and reliability of NLP models.
    - Ensure the integrated data improves process analysis outcomes.
- **Day 4-7**: 
  - **Objective**: Evaluate the impact on business processes.
  - **Practice Tasks**:
    - Conduct a case study to evaluate the practical implications of your framework.
    - Collect feedback and make necessary adjustments.

### Week 8: Documentation and Final Touches
- **Day 1-3**: 
  - **Objective**: Document findings and results.
  - **Tasks**:
    - Write detailed documentation of your methodology, results, and conclusions.
- **Day 4-7**: 
  - **Objective**: Prepare for dissertation submission.
  - **Tasks**:
    - Compile all work into a coherent dissertation document.
    - Review and proofread the final document.
    - Prepare a presentation of your findings if required.

## Additional Resources
- **Online Courses**:
  - [Coursera’s Natural Language Processing Specialization](https://www.coursera.org/specializations/natural-language-processing)
  - [DataCamp’s Process Mining Course](https://www.datacamp.com/courses/process-mining-in-power-bi)

- **Books**:
  - [Natural Language Processing with Python](https://www.oreilly.com/library/view/natural-language-processing/9780596516499/)
  - [Process Mining: Discovery, Conformance and Enhancement of Business Processes](https://www.springer.com/gp/book/9783642193446)

This plan provides a structured approach to developing your dissertation, ensuring you build a strong foundation in both NLP and process mining while applying practical tasks to reinforce your learning.
