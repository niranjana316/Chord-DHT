import streamlit as st
from chord import Chord

st.title("Chord DHT Lookup Simulation")

n = st.slider("Number of Nodes", 3, 15, 5)
key = st.number_input("Enter Key", min_value=0, max_value=15, value=4)

chord = Chord(n)
chord.build_finger_table()

# SHOW NODES
st.subheader("Nodes in Ring")
st.write(chord.nodes)

# SHOW FINGER TABLE
st.subheader("Finger Tables")
for node in chord.node_objs:
    st.write(f"Node {node.id} → {node.finger}")

# RUN LOOKUP
if st.button("Run Lookup"):
    start = chord.nodes[0]
    path = chord.lookup(start, key)

    st.subheader("Lookup Path")
    st.write(" → ".join(map(str, path)))

    st.subheader("Number of Hops")
    st.write(len(path))
