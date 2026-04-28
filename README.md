# Fake News Detection System using Machine Learning & NLP

## 1. Project Description
This project focuses on detecting whether a news article is Fake or Real using Machine Learning and Natural Language Processing (NLP) techniques. The system analyzes textual data and classifies news to prevent the spread of misinformation.

---

## 2. Objective
- Detect whether a news article is Fake or Real  
- Prevent misinformation spread  
- Provide an automated verification system  
- Use NLP techniques for text analysis  

---

## 3. Problem Statement
With the rapid growth of social media:
- Fake news spreads faster than real news  
- Manual verification is time-consuming  
- People cannot easily differentiate between real and fake information  

This project aims to automate fake news detection using ML.

---

## 4. Proposed Solution
- Input: News text  
- Process: NLP + Machine Learning  
- Output:  
  - Fake News (0)  
  - Real News (1)  

---

## 5. Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- NLTK (NLP)  
- Matplotlib, Seaborn  
- Streamlit  

---

## 6. Dataset Description
Dataset used from Kaggle containing:
- id  
- title  
- text  
- author  
- label (Fake = 0, Real = 1)  

---

## 7. System Architecture
1. Data Collection  
2. Data Preprocessing  
3. Text Cleaning  
4. Feature Extraction  
5. Model Training  
6. Model Testing  
7. Prediction  

---

## 8. Methodology

### Step 1: Data Collection
- Dataset from Kaggle (Fake & Real news CSV files)

### Step 2: Data Preprocessing
- Removed missing values  
- Removed duplicate records  
- Converted labels (Fake = 0, Real = 1)  

### Step 3: Text Cleaning (NLP)
- Converted text to lowercase  
- Removed punctuation  
- Removed stopwords  
- Tokenization  

### Step 4: Feature Extraction
- TF-IDF (Term Frequency – Inverse Document Frequency)  

### Step 5: Model Selection
- Logistic Regression  
- Naive Bayes  
- Support Vector Machine (SVM)  
- Random Forest  

### Step 6: Model Training
- Training (80%)  
- Testing (20%)  

### Step 7: Prediction
- Input: News text  
- Output: Fake or Real  

### Step 8: Model Evaluation
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  

---

## 9. System Modules
- Data Collection Module  
- Text Processing Module  
- Feature Extraction Module  
- Model Training Module  
- Prediction Module  
- Visualization Module  

---

## 10. Expected Output
- Classification of news (Fake / Real)  
- Accuracy report  
- Graphs for model comparison  

---

## 11. Advantages
- Fast and automated detection  
- Reduces misinformation  
- Useful for social media platforms  
- Scalable system  

---

## 12. Limitations
- Depends on dataset quality  
- Cannot detect satire easily  
- May misclassify some news  

---

## 13. Future Enhancements
- Deep learning models (LSTM, BERT)  
- Real-time browser extension  
- Multilingual support  
- Integration with social media  

---

## 14. Conclusion
The Fake News Detection System uses Machine Learning and NLP techniques to classify news articles as fake or real. It helps reduce misinformation and supports reliable digital communication.

---

## How to Run
1. Install dependencies:
    pip install -r requirements.txt

2. Run the app:
    streamlit run app.py