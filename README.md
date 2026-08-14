# Zepto AI Platform

An end-to-end AI/ML project containing three connected modules:

-  Data Pipeline 
-  Analytics 
-  Support Assistant 

## Modules

### 1. Data Pipeline

Collects, cleans, transforms, and stores data for analysis.

### 2. Analytics

Performs data analysis, visualization, and machine learning.

### 3. Support Assistant

A grounded GenAI service for answering Zepto policy questions using 8 Zepto policy documents.

Technologies used:

-  Python 
-  Sentence Transformers 
-  ChromaDB 
-  LangGraph 
-  Pydantic 
-  FastAPI 

## Support Assistant Architecture

```
Zepto Policy Documents
```

        |

        v

    Ingestion

        |

        v

    Embeddings

        |

        v

     ChromaDB

        |

        v

    User Query

        |

        v

  classify\_intent

      /     \\

 Policy     General

    \|           |

    v           v

retrieve\_    direct\_

and\_answer   answer

    |

    v

Final Response

    |

    v

  FastAPI

## RAG Pipeline

The 8 Zepto policy documents are stored in the `support_assistant/docs/` folder.

The documents are converted into embeddings using the `all-MiniLM-L6-v2` Sentence Transformer model and stored in ChromaDB.

For policy questions, the `retrieve_and_answer` node retrieves the top 3 relevant documents from ChromaDB and generates an answer using the retrieved context.

For general questions, the `direct_answer` node provides a fixed response without retrieval.

The default `MOCK_LLM` mode works without an external LLM API or API key.

## Example API Tests

### Policy Question

Request:

```
{
```

  "query": "How much does Zepto charge for delivery?"

}

Response:

```
{
```

  "answer": "Based on the retrieved context: Zepto delivers grocery and household essentials...",

  "sources": ["doc\_01.txt"],

  "confidence": 1.0

}

### General Question

Request:

```
{
```

  "query": "What is artificial intelligence?"

}

Response:

```
{
```

  "answer": "I can only answer questions about Zepto policies right now.",

  "sources": [],

  "confidence": 1.0

}

## Running the Project

### Data Pipeline

The data pipeline is located in the `data_pipeline/` folder.

### Analytics

The analytics module is located in the `analytics/` folder.

### Support Assistant

```
cd support_assistant
```

pip install -r requirements.txt

uvicorn main\:app --reload

API:

`http://127.0.0.1:8000`

## Docker

Build the Support Assistant Docker image:

```
docker build -t zepto-support-assistant .
```

Run the container:

```
docker run -p 7860:7860 zepto-support-assistant
```

## Project Structure

```
zepto-ai-platform/
```

├── data\_pipeline/

├── analytics/

├── support\_assistant/

└── README.md

## Technologies

-  Python 
-  FastAPI 
-  LangGraph 
-  ChromaDB 
-  Sentence Transformers 
-  Pydantic 
-  Docker 
-  Git/GitHub 

## Git Workflow

The Support Assistant was developed on the `feature/support-assistant` branch with multiple commits and then merged into `main`.

## Repository

This single repository contains all three modules:

-  Data Pipeline 
-  Analytics 
-  Support Assistant 
- can i paste it?
