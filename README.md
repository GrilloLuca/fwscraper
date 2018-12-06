// Django api installation</br></br>
git clone https://github.com/GrilloLuca/fwscraper.git</br>
virtualenv fwscraper_env</br>
source fwscraper_env/bin/activate</br>
cd fwscraper</br>
pip install -r requirements.txt</br>
python manage.py migrate</br>
python manage.py createsuperuser (provide user and password for admin console)</br>
python manage.py runserver</br>
