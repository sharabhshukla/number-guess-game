# Number Guessing Game

Welcome to the Number Guessing Game! This application is a fun and interactive game where you try to guess a randomly generated number. The app is built using Streamlit, utilizes Univariate (UV) analysis for number generation, and is deployed on AWS Elastic Beanstalk.

## Features

- Simple and intuitive user interface
- Random number generation using UV analysis
- Real-time feedback on your guesses
- Easy deployment on AWS Elastic Beanstalk

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- AWS account

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/number-guessing-game.git
    cd number-guessing-game
    ```

2. Install the required packages:
    Assuming you have uv installed.
    ```bash
    uv sync
    ```

### Running the Application Locally

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to play the game.

### Deploying to AWS Elastic Beanstalk

1. Initialize your Elastic Beanstalk application:
    ```bash
    eb init -p python-3.7 number-guessing-game --region us-west-2
    ```

2. Create an environment and deploy the application:
    ```bash
    eb create number-guessing-game-env
    eb deploy
    ```

3. Open your web browser and go to the provided AWS Elastic Beanstalk URL to play the game.

## Usage

1. Enter your guess in the input box.
2. Click the "Submit" button.
3. Receive feedback on whether your guess is too high, too low, or correct.
4. Continue guessing until you find the correct number.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

Enjoy the game and happy guessing!