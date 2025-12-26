# ML Learning Repository

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) <!-- Add if you have a license -->

A comprehensive collection of machine learning examples and tutorials for learning supervised and unsupervised learning techniques using Python and scikit-learn.

## 📋 Table of Contents

- [Purpose](#purpose)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples Overview](#examples-overview)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Purpose

This repository serves as a personal learning journey through machine learning concepts. It contains runnable Python scripts and Jupyter notebooks that demonstrate fundamental algorithms in supervised and unsupervised learning, along with natural language processing basics. Each example is designed to be self-contained and educational, helping to understand the practical implementation of ML algorithms.

## 📁 Project Structure

```
ML_learning/
├── README.md                           # This file
├── iris_dataset_practise.ipynb         # Iris dataset analysis notebook
├── simple_chatbot.py                   # Basic chatbot implementation
├── supervised_learning/                # Supervised learning examples
│   ├── data/                          # Datasets for supervised learning
│   │   ├── loan.csv
│   │   ├── product.csv
│   │   ├── rain.csv
│   │   ├── rent.csv
│   │   ├── result.csv
│   │   ├── room.csv
│   │   └── student_attendance.csv
│   ├── output/                        # Output directory
│   ├── decision_tree_loan_buy_decision.py
│   ├── decision_tree_rain_prediction.py
│   ├── linear_regression_csv.py
│   ├── linear_regression_student_study_hrs.py
│   ├── linear_regression.py
│   ├── logistic_regression_on_product.py
│   ├── logistic_regression_sigmoid_function.py
│   ├── logistic_regression.py
│   ├── multiple_regression_rent_prediction.py
│   ├── SVM_linear_kernel.py
│   ├── SVM_polynomial_eg_pass_fail_prediction.py
│   └── SVM_rbf_eg_student_attendence.py
├── unsupervised_learning/              # Unsupervised learning examples
│   ├── data/                          # Datasets for unsupervised learning
│   │   ├── hierarchical_clustring_income_expense.csv
│   │   ├── people_income.csv
│   │   └── points_data_set.csv
│   ├── output/                        # Output directory
│   ├── hierarchical_clustring_income_expense.py
│   ├── hierarchical_clustring_points.py
│   ├── k_means_fruits_cluster.py
│   ├── k_means_unsupervised.py
│   └── nlp/                           # Natural Language Processing
│       ├── lematization.py
│       ├── module1.py
│       ├── paragraph_sentiment_analysis.py
│       ├── sentiment_analysis.py
│       ├── stemming.py
│       ├── text_serialization.py
│       ├── textblob_sentiment_analysis.py
│       └── word_tokenization.py
├── cache/                             # Cached data and joblib caches
│   └── joblib/
│       └── mglearn/
└── sample_file.txt                    # Sample text file
```

## 📋 Prerequisites

- Python 3.8 or higher
- Basic understanding of Python programming
- Familiarity with NumPy and Pandas (helpful but not required)

## 🚀 Installation

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install numpy pandas matplotlib scikit-learn scipy jupyter mglearn textblob nltk
   ```

   For NLP examples, you may need additional NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

## 💻 Usage

### Running Python Scripts

Most examples can be run directly from the command line:

```bash
python supervised_learning/linear_regression.py
```

### Running Jupyter Notebooks

For interactive examples:

```bash
jupyter notebook iris_dataset_practise.ipynb
```

### Important Notes

- Run scripts from the repository root directory to ensure relative paths work correctly
- Some scripts generate output files in their respective `output/` directories
- Notebooks may require `mglearn` for certain visualizations

## 📚 Examples Overview

### Supervised Learning

#### Linear Regression
- `linear_regression.py` - Basic linear regression example
- `linear_regression_csv.py` - Linear regression with CSV data
- `linear_regression_student_study_hrs.py` - Predicting student performance
- `multiple_regression_rent_prediction.py` - Multiple regression for rent prediction

#### Logistic Regression
- `logistic_regression.py` - Basic logistic regression
- `logistic_regression_sigmoid_function.py` - Understanding the sigmoid function
- `logistic_regression_on_product.py` - Product classification example

#### Decision Trees
- `decision_tree_loan_buy_decision.py` - Loan approval decision tree
- `decision_tree_rain_prediction.py` - Weather prediction using decision trees

#### Support Vector Machines (SVM)
- `SVM_linear_kernel.py` - Linear kernel SVM
- `SVM_polynomial_eg_pass_fail_prediction.py` - Polynomial kernel for pass/fail prediction
- `SVM_rbf_eg_student_attendence.py` - RBF kernel for attendance prediction

### Unsupervised Learning

#### Clustering
- `k_means_unsupervised.py` - Basic K-means clustering
- `k_means_fruits_cluster.py` - Fruit clustering example
- `hierarchical_clustring_points.py` - Hierarchical clustering on points
- `hierarchical_clustring_income_expense.py` - Income/expense clustering

#### Natural Language Processing
- `word_tokenization.py` - Text tokenization
- `stemming.py` - Word stemming
- `lematization.py` - Word lemmatization
- `sentiment_analysis.py` - Basic sentiment analysis
- `textblob_sentiment_analysis.py` - Sentiment analysis with TextBlob
- `paragraph_sentiment_analysis.py` - Paragraph-level sentiment analysis
- `text_serialization.py` - Text data serialization

### Notebooks
- `iris_dataset_practise.ipynb` - Comprehensive Iris dataset analysis with visualizations

## 🤝 Contributing

This is a personal learning repository, but suggestions for improvements or additional examples are welcome. Feel free to:

- Report bugs or issues
- Suggest new examples or improvements
- Share your learning insights

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Learning!** 🎓

If you find this repository helpful, consider starring it or sharing it with fellow ML enthusiasts.
