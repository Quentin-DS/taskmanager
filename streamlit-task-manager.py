import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import time

# Initialize session state variables
if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=[
        'title', 'priority', 'estimated_time', 'actual_time', 
        'start_time', 'topic', 'is_running', 'completed',
        'productivity_rating', 'goal_achieved', 'feeling_rating'
    ])
if 'active_timer' not in st.session_state:
    st.session_state.active_timer = None
if 'last_break' not in st.session_state:
    st.session_state.last_break = datetime.now()

def start_timer(task_index):
    st.session_state.tasks.loc[task_index, 'is_running'] = True
    st.session_state.tasks.loc[task_index, 'start_time'] = datetime.now()
    st.session_state.active_timer = task_index

def stop_timer(task_index):
    if st.session_state.tasks.loc[task_index, 'start_time']:
        elapsed = (datetime.now() - st.session_state.tasks.loc[task_index, 'start_time']).total_seconds()
        st.session_state.tasks.loc[task_index, 'actual_time'] = (
            st.session_state.tasks.loc[task_index, 'actual_time'] or 0
        ) + elapsed
    st.session_state.tasks.loc[task_index, 'is_running'] = False
    st.session_state.tasks.loc[task_index, 'start_time'] = None
    st.session_state.active_timer = None

def complete_task(task_index):
    stop_timer(task_index)
    st.session_state.tasks.loc[task_index, 'completed'] = True

def main():
    st.title("Task Manager")
    
    # Task Creation Section
    st.header("Create New Task")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        title = st.text_input("Task Title")
    with col2:
        priority = st.selectbox("Priority", ['High', 'Medium', 'Low'])
    with col3:
        estimated_time = st.number_input("Estimated Time (minutes)", min_value=1, value=30)
    
    topic = st.text_input("Topic/Category")
    
    if st.button("Add Task"):
        new_task = pd.DataFrame([{
            'title': title,
            'priority': priority,
            'estimated_time': estimated_time,
            'actual_time': 0,
            'start_time': None,
            'topic': topic,
            'is_running': False,
            'completed': False,
            'productivity_rating': 0,
            'goal_achieved': False,
            'feeling_rating': 0
        }])
        st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)

    # Active Tasks Section
    st.header("Active Tasks")
    active_tasks = st.session_state.tasks[~st.session_state.tasks['completed']]
    
    for idx, task in active_tasks.iterrows():
        with st.expander(f"{task['title']} ({task['priority']} Priority)"):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if task['is_running']:
                    if st.button("Stop", key=f"stop_{idx}"):
                        stop_timer(idx)
                else:
                    if st.button("Start", key=f"start_{idx}"):
                        start_timer(idx)
            
            with col2:
                current_time = task['actual_time']
                if task['is_running']:
                    current_time += (datetime.now() - task['start_time']).total_seconds()
                st.write(f"Time: {int(current_time)}s / {int(task['estimated_time']*60)}s")
            
            with col3:
                if st.button("Complete", key=f"complete_{idx}"):
                    st.session_state.tasks.loc[idx, 'productivity_rating'] = st.slider(
                        "Productivity (1-10)", 1, 10, 5, key=f"prod_{idx}")
                    st.session_state.tasks.loc[idx, 'goal_achieved'] = st.checkbox(
                        "Goal Achieved?", key=f"goal_{idx}")
                    st.session_state.tasks.loc[idx, 'feeling_rating'] = st.slider(
                        "Feeling (1-10)", 1, 10, 5, key=f"feel_{idx}")
                    complete_task(idx)
            
            with col4:
                st.write(f"Topic: {task['topic']}")

    # Statistics Section
    if not st.session_state.tasks.empty:
        st.header("Statistics")
        completed_tasks = st.session_state.tasks[st.session_state.tasks['completed']]
        
        if not completed_tasks.empty:
            # Time Analysis
            fig_time = px.bar(completed_tasks, 
                            x='title', 
                            y=['estimated_time', 'actual_time'],
                            title='Estimated vs Actual Time',
                            barmode='group')
            st.plotly_chart(fig_time)
            
            # Productivity Analysis
            fig_prod = px.scatter(completed_tasks,
                                x='actual_time',
                                y='productivity_rating',
                                color='priority',
                                title='Productivity vs Time Spent')
            st.plotly_chart(fig_prod)
            
            # Topic Analysis
            topic_stats = completed_tasks.groupby('topic')['productivity_rating'].mean().reset_index()
            fig_topic = px.bar(topic_stats,
                             x='topic',
                             y='productivity_rating',
                             title='Average Productivity by Topic')
            st.plotly_chart(fig_topic)

    # Break Reminder
    if (datetime.now() - st.session_state.last_break).total_seconds() > 45 * 60:  # 45 minutes
        st.warning("Time for a break! You've been working for 45 minutes.")
        if st.button("Take Break"):
            st.session_state.last_break = datetime.now()
            st.success("Enjoy your 5-minute break!")
            time.sleep(5)

if __name__ == "__main__":
    main()
