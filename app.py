import streamlit as st
from rdflib import Graph
import pandas as pd

# Function to load the graph (cached so it only loads once)
@st.cache_resource
def load_graph():
    g = Graph()
    g.parse("data.ttl", format="turtle")
    return g

# Load the knowledge graph
g = load_graph()

# --- Website UI ---
st.set_page_config(layout="wide")
st.title("🇮🇳 India Tourism Knowledge Graph")
st.markdown("Ask questions about tourist places in India!")

# --- Dynamic Search Section ---
st.header("Find Attractions in a State")
st.markdown("Type a state name (e.g., **Rajasthan**, **Goa**, **Tamil Nadu**, **Kerala**)")

# Get user input from a text box
state_name = st.text_input("Enter State Name:", "Rajasthan")

# This is our dynamic SPARQL query.
# The f-string {state_name} inserts the user's input.
q1 = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX it: <http://example.org/india-tourism#>

    SELECT ?attractionName ?cityName ?bestTime
    WHERE {{
        ?attraction a it:TouristAttraction .
        ?attraction rdfs:label ?attractionName .
        ?attraction it:locatedIn ?city .
        ?attraction it:bestTimeToVisit ?bestTime .
        ?city rdfs:label ?cityName .
        
        ?city it:cityInState ?state .
        ?state rdfs:label "{state_name}" .
    }}
    ORDER BY ?cityName
"""

# Execute the query and show results
if st.button("Search Attractions"):
    results = []
    for row in g.query(q1):
        results.append({
            "Attraction": row.attractionName,
            "City": row.cityName,
            "Best Time to Visit": row.bestTime
        })
    
    if results:
        # Display results in a nice table
        st.dataframe(pd.DataFrame(results), use_container_width=True)
    else:
        st.warning(f"No attractions found for '{state_name}'. Check the spelling.")

st.divider()

# --- Second Dynamic Search ---
st.header("Find Restaurants in a City")
st.markdown("Type a city name (e.g., **Mumbai**, **Agra**, **Jaipur**, **Bengaluru**)")

city_name = st.text_input("Enter City Name:", "Mumbai")

q2 = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX it: <http://example.org/india-tourism#>

    SELECT ?restaurantName ?cuisine
    WHERE {{
        ?restaurant a it:Restaurant .
        ?restaurant rdfs:label ?restaurantName .
        ?restaurant it:servesCuisine ?cuisine .
        
        ?restaurant it:locatedIn ?city .
        ?city rdfs:label "{city_name}" .
    }}
"""

if st.button("Search Restaurants"):
    results = []
    for row in g.query(q2):
        results.append({
            "Restaurant": row.restaurantName,
            "Cuisine": row.cuisine
        })
    
    if results:
        st.dataframe(pd.DataFrame(results), use_container_width=True)
    else:
        st.warning(f"No restaurants found for '{city_name}'.")