# Add this temporary block to run download_data.py
def download_dataset_from_script():
    import zipfile
    from kaggle.api.kaggle_api_extended import KaggleApi

    def download_dataset():
        """
        Download dataset from Kaggle and unzip it into the data directory.
        """
        # Initialize Kaggle API
        api = KaggleApi()
        api.authenticate()

        # Define the Kaggle dataset path and destination file
        dataset_path = 'your-kaggle-username/dataset-name'  # Replace with actual "username/dataset-name"
        download_path = 'data/original_dataset.zip'

        # Create a 'data' directory if it doesn't exist
        os.makedirs('data', exist_ok=True)

        # Download the dataset
        print("Downloading dataset...")
        api.dataset_download_files(dataset_path, path='data', unzip=False)

        # Unzip the dataset
        print("Extracting dataset...")
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall('data/original_dataset')
        print("Download and extraction complete.")

        # Clean up the downloaded zip file
        os.remove(download_path)

    download_dataset()

if __name__ == "__main__":
    download_dataset_from_script()"""import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from federated_learning import FederatedLearning
from diffusion_model import generate_synthetic_images

# Initialize the Federated Learning system
fl_system = FederatedLearning()

# Streamlit app configuration
st.set_page_config(page_title="Federated Learning for Brain Tumor Detection", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = ["Home", "Data Augmentation", "Training Metrics", "Federated Learning Process", "Final Report"]
page = st.sidebar.radio("Go to", pages)

# Home Page
if page == "Home":
    st.title("Federated Learning for Brain Tumor Detection")
    st.write("""
        Welcome to our project on federated learning for brain tumor detection using MRI scans.
        This project leverages distributed data across multiple hospitals while preserving data privacy.
        By utilizing advanced techniques like diffusion models for data augmentation, we aim to improve
        the accuracy and robustness of tumor detection models.
    """)
    st.image("static/brain_tumor.jpg", use_column_width=True)

# Data Augmentation Page
elif page == "Data Augmentation":
    st.title("Data Augmentation")
    st.write("""
        Data augmentation is a crucial step in preparing our dataset for training robust machine learning models.
        By artificially expanding the dataset, we can improve the model's ability to generalize and reduce overfitting.
    """)
    generate_synthetic_images()
    st.write("Synthetic images have been generated and added to the training dataset.")

# Training Metrics Page
elif page == "Training Metrics":
    st.title("Training Metrics")
    st.write("Explore the detailed training metrics and progress of the federated learning model across multiple rounds.")
    # Example of displaying a chart
    rounds = np.arange(1, 6)
    accuracy = np.random.rand(5) * 100
    plt.plot(rounds, accuracy, marker='o')
    plt.title("Global Model Accuracy Over Rounds")
    plt.xlabel("Round")
    plt.ylabel("Accuracy (%)")
    st.pyplot(plt)

# Federated Learning Process Page
elif page == "Federated Learning Process":
    st.title("Federated Learning Process")
    st.write("""
        Federated learning is a decentralized approach to machine learning where models are trained across multiple devices
        or servers holding local data samples, without exchanging them. This method is particularly beneficial in scenarios
        where data privacy is paramount, such as in medical imaging.
    """)

# Final Report Page
elif page == "Final Report":
    st.title("Final Report")
    st.write("This report provides a comprehensive overview of the federated learning process and final metrics.")
    
    # User Input Form
    st.subheader("Simulate Federated Learning")
    with st.form("federated_learning_form"):
        client_allocation = st.text_input("Initial Individual Client Data Allocation Percentage", "Client A: 20%, Client B: 30%")
        categories = st.multiselect("Categories Available", ["glioma", "meningioma", "pituitary", "notumor"])
        num_rounds = st.number_input("Number of Rounds", min_value=1, max_value=10, value=5)
        client_participation = st.text_area("Client Participation for Each Round", "Round 1: Client A, Client B; Round 2: Client C, Client D")
        submitted = st.form_submit_button("Start Simulation")

    if submitted:
        # Parse user inputs
        client_allocations = {client.split(":")[0].strip(): int(client.split(":")[1].strip().replace("%", "")) for client in client_allocation.split(",")}
        client_participation_list = [round.strip() for round in client_participation.split(";")]

        # Run federated learning simulation
        results = fl_system.simulate(client_allocations, categories, num_rounds, client_participation_list)

        # Display results
        st.subheader("Simulation Results")
        for round_num, metrics in enumerate(results['rounds']):
            st.write(f"### Round {round_num + 1}")
            st.write(f"Global Model Accuracy: {metrics['global_accuracy']}%")
            st.write(f"Client Metrics: {metrics['client_metrics']}")
            # Example of displaying a graph
            fig, ax = plt.subplots()
            ax.bar(metrics['client_metrics'].keys(), metrics['client_metrics'].values())
            ax.set_title(f"Client Metrics for Round {round_num + 1}")
            ax.set_xlabel("Clients")
            ax.set_ylabel("Accuracy (%)")
            st.pyplot(fig)

        # Final stacked bar chart
        st.subheader("Final Metrics Visualization")
        fig, ax = plt.subplots()
        for client, metrics in results['final_metrics'].items():
            ax.bar(client, metrics, label=client)
        ax.set_title("Final Metrics for Each Client")
        ax.set_xlabel("Clients")
        ax.set_ylabel("Metrics")
        ax.legend()
        st.pyplot(fig)

# Footer
st.sidebar.info("© 2023 Federated Learning Project Team. All rights reserved.")"""
