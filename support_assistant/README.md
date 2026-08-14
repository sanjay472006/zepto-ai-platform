\# Zepto Support Assistant



\## Overview



This module implements a grounded GenAI support assistant for Zepto.



It uses Zepto policy documents, local embeddings with `all-MiniLM-L6-v2`, ChromaDB for vector retrieval, LangGraph for orchestration, Pydantic for structured output, and FastAPI for the API.



The required graded path uses `MOCK\_LLM` by default, so no LLM API key is required.



\## Architecture



```text

Zepto Policy Documents

&#x20;       |

&#x20;       v

&#x20;   Ingestion

&#x20;       |

&#x20;       v

&#x20;    Chunking

&#x20;       |

&#x20;       v

all-MiniLM-L6-v2

&#x20;       |

&#x20;       v

&#x20;    ChromaDB

&#x20;       |

&#x20;       v

&#x20;   User Query

&#x20;       |

&#x20;       v

&#x20;classify\_intent

&#x20;     /     \\

&#x20;    /       \\

&#x20;Policy     General

&#x20;  |           |

&#x20;  v           v

retrieve\_    direct\_

and\_answer   answer

&#x20;  |

&#x20;  v

Top-3 Retrieved Documents

&#x20;  |

&#x20;  v

Mock Answer Generation

&#x20;  |

&#x20;  v

Pydantic Response

&#x20;  |

&#x20;  v

FastAPI /ask

