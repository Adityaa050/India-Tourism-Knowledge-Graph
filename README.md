This is a simple Semantic Web project that builds a Knowledge Graph for tourist attractions and restaurants across India. The project uses RDF to store data, RDFS to define the data model (ontology), and SPARQL to ask questions.

The entire application is served as an interactive web app using Streamlit.

🚀 Features
Knowledge Graph: All data is stored in a proper data.ttl file using RDF triples.

Ontology: A simple RDFS ontology defines classes (TouristAttraction, City, State, Restaurant) and properties (locatedIn, cityInState, servesCuisine).

Web Interface: A user-friendly Streamlit app allows users to query the graph dynamically.

Dynamic Queries:

Find all tourist attractions in a specific state.

Find all restaurants in a specific city.

🛠️ Technologies Used
Python 3

Semantic Web:

rdflib: A Python library for working with RDF.

RDF (Resource Description Framework): The data model for storing facts.

RDFS (RDF Schema): The language for defining the ontology (the rules).

SPARQL (SPARQL Protocol and RDF Query Language): The query language used to ask questions of the graph.

Web:

streamlit: A Python library to create and share web apps.

pandas: Used to display query results in a clean table.

📁 Project Structure
Tourism_KnowledgeGraph/
│
├── 📄 app.py          # The main Streamlit web application
├── 📄 data.ttl        # The knowledge graph (Ontology + Data)
├── 📄 requirements.txt # List of Python dependencies
└── 📄 README.md       # You are here
data.ttl: This is the heart of the project. It contains all the "facts" (the RDF triples) about states, cities, attractions, and restaurants. It also contains the "rules" (the RDFS ontology) that define the relationships between them.

app.py: This file loads the data.ttl graph, creates the website UI, and runs SPARQL queries against the graph based on user input.

🏃 How to Run
1. Prerequisites
Make sure you have Python 3.8 or newer installed.

2. Install Dependencies
You can install all the necessary libraries using pip. It's recommended to do this in a virtual environment.

Bash

pip install streamlit rdflib pandas
