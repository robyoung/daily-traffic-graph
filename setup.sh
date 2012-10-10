curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
sudo rm get-pip.py
sudo pip install virtualenv
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
