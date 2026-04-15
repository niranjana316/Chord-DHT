import streamlit as st
from chord import Chord

st.title("Chord DHT Lookup Simulation")

n = st.slider("Number of Nodes", 3, 15, 5)
key = st.number_input("Enter Key", min_value=0, max_value=15, value=3)

chord = Chord(n)
chord.build_finger_table()

st.write("Nodes in Ring:", chord.nodes)

if st.button("Run Lookup"):
    start = chord.nodes[0]
    path = chord.lookup(start, key)

    st.write("Lookup Path:", path)
    st.write("Hops:", len(path))
