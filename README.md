# Health Prediction Website

## Project Overview
This project is a web application that predicts the likelihood of cancer, diabetes, and heart failure using machine learning models. The application is built using Flask for the web framework, SQLite3 for the database, and Pandas, NumPy, and regular expressions (re) for data manipulation and processing.

## Features
- Predicts the risk of cancer, diabetes, and heart failure.
- User-friendly web interface.
- Secure and efficient data handling.

## Tech Stack
- **Flask**: Web framework
- **SQLite3**: Database
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations
- **re**: Regular expressions for pattern matching

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Step-by-Step Guide

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/health-prediction-website.git
    cd health-prediction-website
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**

    On Windows:
    ```sh
    venv\Scripts\activate
    ```

    On macOS/Linux:
    ```sh
    source venv/bin/activate
    ```

4. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application**
    ```sh
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter the required details in the form provided.
3. Click on the "Predict" button to see the prediction results.

## Project Structure
```sh
health-prediction-website/
│
├── scirpt.py # Main application file
├── models/ # Directory containing the machine learning models
├── static/ # Static files (CSS, JS, images)
├── templates/ # HTML templates
├── data/ # Directory for the dataset
├── users.db # SQLite3 database
├── requirements.txt # List of dependencies
└── README.md # Project README file
```

## Machine Learning Models
The prediction models are trained using datasets for cancer, diabetes, and heart failure. The models use various features from these datasets to predict the likelihood of each condition.

## Dataset
The datasets used for training the models are stored in the `data/` directory. Ensure the data is properly formatted before running the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any inquiries or issues, please contact chakraborty.shankha@gmail.com.
