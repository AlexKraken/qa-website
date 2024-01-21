# QA Website
[![QA Website Screen Shot][website-screenshot]](https://github.com/AlexKraken/qa-website)
This is a rough draft of a Flask website that provides barcode logging and weight calculations and used to make QA's job a little easier. 
Demo (hosted for free on render.com and takes a few minutes to spin up) located here: [https://alexkraken.pythonanywhere.com/](https://alexkraken.pythonanywhere.com/).

## Barcode Logger

Note that the 'Check Barcode' and 'Add Barcode' sections are actually implemented as two seperate forms. This means that the user can hit 'Enter' after scanning/typing in an input box and it will be equivalent to clicking the respective button. And regardless of which form is submitted, the focus is always returned to the first input box, with its contents selected - this allows repeated scanning to be faster as the user can scan a barcode, hit 'Enter' to check if it's in the log, and immediately scan the next barcode.


### Prerequisites
You should already have Python installed, check by opening the terminal and running
```sh
python --version
```

### Installation
1. Clone the repo (or alternatively download as a .zip file) and change to the directory in the terminal
   ```sh
   git clone https://github.com/AlexKraken/qa-website.git
   cd qa-website
   ```
   
2. Create a python virtual environment
   ```sh
   python -m venv venv
   ```
      
3. Enable the virtual environment
   ```sh
   source venv/bin/activate
   ```
      
4. Install all the required packages
   ```sh
   pip install --requirement requirements.txt
   ```
      
5. Start the server for the Flask app
   ```sh
   python main.py
   ```
      
6. In the terminal output there should be a line
   ```sh
   * Running on http://127.0.0.1:5000
   ```
      
   Enter `http://127.0.0.1:5000` in a web browser to access the website (don't exit out of that terminal!)
      
7. When finished, stop the server in the terminal by pressing `CRTL + C`, and deactivate the virtual environment by typing
   ```sh
   deactivate
   ```
      

## Roadmap


- [ ] Add ability to download barcode log as a .cvs file
- [ ] Add color highlighting to messages
- [ ] Add alternating colors to barcode log
- [ ] Add ability to populate 'Barcode Logger' with info from 'Weight Checker'

[website-screenshot]: images/screenshot.png
