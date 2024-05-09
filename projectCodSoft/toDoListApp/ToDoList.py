import streamlit as st

# Title and Input field with placeholder text
st.title("To-Do List ")
task = st.text_input("Add a new task...", "")

# Add Task button with conditional check
if st.button("Add Task"):
    if task:  # Check if task is not empty
        st.session_state["task_list"].append(task)
        st.success(f"✅ Task '{task}' added!")  # Success message
        # Empty the textbox after adding the task
        task = ""

# Initialize task list if not present in session state
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

# Display tasks with checkboxes for completion
for i, task in enumerate(st.session_state["task_list"]):
    # Checkbox displayed next to the task using a column
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{i+1}. {task}")
    with col2:
        completed = st.checkbox("", key=f"task-{i}")  # Empty checkbox label

    # Deletion when 
    if completed:
        del st.session_state["task_list"][i]
        st.success(f"️ Task '{task}' deleted!") 

# Display Message for when there are no Tasks
if not st.session_state["task_list"]:
    st.info(" You don't have any tasks yet!")
