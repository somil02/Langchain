from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = 'text-generation'
)

llm1 = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = 'text-generation'
)

model1 = ChatHuggingFace(llm = llm)

model2 = ChatHuggingFace(llm = llm1)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Support Vector Machines (SVMs) are powerful supervised machine learning algorithms used for both classification and regression tasks, as well as for outlier or anomaly detection. They are among the most widely used algorithms because of their ability to produce highly accurate models, especially when dealing with complex datasets. The main objective of an SVM is to find the best possible decision boundary, known as a hyperplane, that separates different classes of data while maximizing the distance between the boundary and the nearest data points. These nearest data points are called support vectors, and they play a crucial role in defining the position of the hyperplane. Since only the support vectors influence the model, SVMs are memory efficient and often generalize well to unseen data.

One of the greatest strengths of SVM is its effectiveness in high-dimensional spaces where the number of features is very large. This makes it particularly suitable for applications such as text classification, image recognition, handwriting recognition, medical diagnosis, bioinformatics, and spam detection. SVM also performs well in situations where the number of features is greater than the number of training samples, a common scenario in many scientific and research datasets. Unlike some other algorithms that rely heavily on the entire dataset, SVM focuses only on the support vectors, reducing the complexity of the final model.

A significant advantage of SVM is its ability to handle both linearly separable and non-linearly separable data. When the data cannot be separated by a straight line or plane, SVM uses the kernel trick to map the data into a higher-dimensional feature space where a linear separation becomes possible. Several kernel functions are available, including the Linear kernel, Polynomial kernel, Radial Basis Function (RBF) kernel, and Sigmoid kernel. The RBF kernel is one of the most commonly used because it can effectively model complex relationships. Users can also define custom kernel functions depending on the specific requirements of their applications.

Despite its advantages, SVM has certain limitations. Choosing the appropriate kernel function and tuning parameters such as the regularization parameter (C) and kernel coefficient (gamma) are critical for achieving good performance. Incorrect parameter selection may result in overfitting or underfitting. SVM training can also become computationally expensive and slow for very large datasets because the optimization process becomes more complex as the number of samples increases. Another drawback is that SVM does not directly provide probability estimates for predictions. In libraries such as scikit-learn, probability estimates are obtained using an additional five-fold cross-validation process, which increases the computational cost. Furthermore, models using nonlinear kernels are often difficult to interpret compared to simpler algorithms like decision trees or logistic regression.

Scikit-learn provides efficient implementations of SVM through classes such as SVC for classification, SVR for regression, and One-Class SVM for anomaly detection. The library supports both dense NumPy arrays and sparse SciPy matrices as input. However, if a model is trained on sparse data, prediction should also be performed using sparse data. For the best performance, it is recommended to use C-ordered NumPy arrays or SciPy CSR sparse matrices with the data type set to float64. Overall, Support Vector Machines remain one of the most reliable machine learning algorithms for solving complex classification and regression problems, particularly when working with high-dimensional datasets and moderate-sized training data.
"""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()