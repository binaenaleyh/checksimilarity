<div align="center">
  
![check-similarity-logo](https://checksimilarity.com/static/images/logo.png)

[![enter image description here](https://badgen.net/static/api/docs) ](https://checksimilarity.com/docs) [![enter image description here](https://badgen.net/static/web/interface/green)](https://checksimilarity.com)
</div>

# Check Similarity

Check Similarity is a Python-based application developed to measure the similarity ratio between two texts. The key feature of this project is its ability to compute similarity scores by selecting and combining various vectorization and similarity algorithms.

The application offers functionality through both a web interface and an API. You can test and examine the project at [checksimilarity.com](http://checksimilarity.com/) and access API documentation at [checksimilarity.com/docs](http://checksimilarity.com/docs).

## Features

-   **Vectorization Algorithms**: The application leverages vectorization algorithms like TF-IDF (Term Frequency-Inverse Document Frequency) and One-Hot-Encoding to convert text into vectors.
    
-   **Similarity Algorithms**: Various similarity calculation methods are available, including Cosine Similarity, Euclidean Distance, and Jaccard Distance.
    
-   **Flexibility**: Users can select and combine these vectorization and similarity algorithms as per their requirements to measure text similarity.
    
-   **Web Interface and API**: Check Similarity provides both a user-friendly web interface and an API, catering to a wide range of users and applications.
    

## Built With

-   **Python**: The core programming language used for developing the application.
    
-   **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
    
-   **Scikit-Learn**: A machine learning library in Python, used here to provide the vectorization (TF-IDF and One-Hot-Encoding) and similarity (Cosine Similarity, Euclidean Distance, and Jaccard Distance) algorithms.
    
-   **Uvicorn**: A lightning-fast ASGI server, built on uvloop and httptools, used to serve our FastAPI application.
    
-   **Nginx**: A powerful, open-source, HTTP server and reverse proxy server. In our deployment, Nginx is used to route requests to the Uvicorn server.
    

These technologies combined allow for efficient processing and flexible configuration of our text comparison services.

## Getting Started

Check Similarity can be used directly via its web interface or API, but if you wish to run it locally on your machine, please follow the instructions below.

### Prerequisites

Ensure that you have Python installed on your machine. If not, you can download and install Python from the official [website](https://www.python.org/).

### Installation

1.  Install Uvicorn, an ASGI server used to serve the FastAPI application, using pip (Python's package installer):

   ```
pip install uvicorn
```

2.  Clone the repository or download the source code.
    
3.  Navigate to the directory containing the application.
    
4.  Run the application using Uvicorn:

 ```
uvicorn main:app --reload
```

This command starts the Uvicorn server with the application, the `--reload` flag enables hot reloading, which means the server will automatically update as you make changes to the source code.

Now, you can visit `localhost:8000` in your web browser to interact with the application.

### Online Usage

For online usage, visit my website at [checksimilarity.com](http://checksimilarity.com/). If you are a developer interested in integrating our service into your applications, please refer to the API documentation at [checksimilarity.com/docs](http://checksimilarity.com/docs).

## Contributing

We welcome all kinds of contributions. Please feel free to contribute and help improve Check Similarity. For more information, contact me [here.](https://www.linkedin.com/in/enestuzlu)

**Happy Text Comparing!**
