# LinkedIn Web Scraper

## Description
This project allows you to automate LinkedIn job searches. Enter your desired job title and location to get a response with available jobs filtered based on that input. The response includes the Job Title, Company Name, Location, and Posting Date.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact](#contact)

## Installation
### Prerequisites
- Python 3.x
- pip (Python package installer)
- Google Chrome browser
- ChromeDriver (ensure it's compatible with your Chrome version)

### Steps
1. Clone the repository:
    ```sh
    git clone git@github.com:RichardKaranuMbuti/Linkdin_Web_Scrapper.git
    cd LinkedIn_Web_Scraper
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download ChromeDriver:
    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory or in a directory that's in your system's PATH.

 **This project doesnt need you to setup a web driver**

## Usage
1. Navigate to the `src` directory:
    ```sh
    cd src
    ```

2. Run the scraper script:
    ```sh
    python Scrap.py
    ```

3. Enter the desired job title and location when prompted.

4. The script will scrape LinkedIn for job listings matching the input and save the results to a CSV file named `job_listings.csv`.

## Features
- Automated job search on LinkedIn based on user input.
- Outputs job title, company name, location, and posting date.
- Saves results to a CSV file for easy access and analysis.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Follow me on Linkdln** - [RichardKaranu](www.linkedin.com/in/richard-karanu-94b572241) 
- [Email me](mailto:officialforrichardk@gmail.com)

Feel free to open an issue if you have any questions or suggestions.

