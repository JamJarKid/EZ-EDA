"""File for running the EZ EDA App and associated functions."""
import os
import subprocess


def main():
    """Entry point to the app, runs through stramlit."""
    app_path = os.path.join(os.path.dirname(__file__), "EZ_EDA_app.py")
    subprocess.run(["streamlit", "run", app_path])
