# Task Manager - Streamlit Productivity App

A comprehensive task management and productivity tracking application built with Streamlit. This application helps you manage your daily tasks, track time spent, analyze productivity patterns, and optimize your work schedule.

## Features

- **Task Management**
  - Create and track tasks with priorities
  - Set estimated completion times
  - Organize tasks by topics/categories
  - Real-time task tracking

- **Time Tracking**
  - Start/stop timer for each task
  - Track actual time spent vs. estimated time
  - Automatic break reminders every 45 minutes
  - Visual time progress indicators

- **Performance Analytics**
  - Track productivity ratings
  - Monitor goal achievement
  - Analyze performance by topic
  - Compare estimated vs. actual time spent
  - Visual analytics with interactive charts

- **Task Optimization**
  - Performance tracking by time of day
  - Topic-based productivity analysis
  - Break time recommendations
  - Task completion statistics

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
```

3. Activate the virtual environment

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

4. Install required packages
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application
```bash
streamlit run task_manager.py
```

2. Open your web browser and go to the URL shown in your terminal (typically `http://localhost:8501`)

3. Start managing your tasks:
   - Create new tasks with the input form at the top
   - Start/stop time tracking for active tasks
   - Complete tasks and rate your performance
   - View statistics and analytics in the dashboard

## Project Structure

```
task-manager/
├── README.md
├── requirements.txt
├── task_manager.py
└── .gitignore
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Data visualization powered by [Plotly](https://plotly.com/)
- Data handling with [Pandas](https://pandas.pydata.org/)
