# Educational Content Payment System

This project is an educational content payment system built on the Pi blockchain. It allows users to purchase access to educational materials securely and efficiently using cryptocurrency.

## Project Structure

```
educational-content-payment-system
├── app.py                     # Entry point of the application
├── license.md                 # License information
├── content.txt                # Educational content data
├── variables.py               # Configuration and variables
├── requirements.txt           # Lists project dependencies
├── templates                  # HTML templates for the web application
│   ├── index.html             # Main page template
│   └── back.html              # Back page template
├── static
│   └── css
│       └── styles.css         # CSS styles for the web application
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd odoo-pi-pay-example/educational-content-payment-system
   ```

2. **Install dependencies:**
   Ensure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Create the `variables.py` file:**
   Create a file named `variables.py` in the root directory with the following content:
   ```python
   apikey = "YOUR API KEY HERE"
   ```

   Follow the instructions in [this link](https://minepi.com/blog/build-blockchain-app/) to generate your API Key.

4. **Configure `.gitignore`:**
   Create a `.gitignore` file in the root directory with the following content to ensure `variables.py` is not pushed to the repository:
   ```
   variables.py
   ```

5. **Run the application:**
   Start the Flask server by executing:
   ```
   python app.py
   ```

## Usage Guidelines

- Access the application through your web browser at `http://127.0.0.1:8080/`.
- Users can browse available educational content and make payments using the Pi blockchain.
- After a successful payment, users will gain access to the purchased content.

## Overview of Functionality

- **app.py:** Main application file that initializes the Flask server and handles routes.
- **content.txt:** Contains the educational content data.
- **variables.py:** Stores configuration and variables used throughout the application.
- **HTML Templates:** `index.html` and `back.html` provide the structure for the web pages.
- **CSS Styles:** `styles.css` contains the styling for the web application.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the PiOS License. See the LICENSE file for more details.