# my_club
![example workflow](https://github.com/Kakoytobarista/my_club/actions/workflows/my_club.yml/badge.svg)
### How to run autotests:
Mac:
1. Installing brew:
```
brew install wget
```
2. Move to Download directory and download zip with webdriver:
```
cd ~/Downloads
wget https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_mac64.zip
```
3. Unzipping webdriver and move to /usr/local/bin:
```
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
```
4. Checking chromedriver version:
```
chromedriver --version
```
U will see 
```
ChromeDriver 100.0.4896.60 (6a5d10861ce8de5fce22564658033b43cb7de047-refs/branch-heads/4896@{#875})
```
5. Creating virtual environment and activating them:
```
python3 -m venv venv
source venv/bin/activate
```
6. Installing dependencies:
```
pip install -r requirements.txt (on my_club directory)
```
7. Run autotests! :
```
 pytest -n 2 test_properties_page.py
```
For check report open file report.html (in dir reports)
Have fun!)
