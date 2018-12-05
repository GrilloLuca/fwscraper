// Django api installation
git clone https://github.com/GrilloLuca/fwscraper.git
virtualenv fwscraper_env
source fwscraper_env/bin/activate
cd fwscraper
pip install -r requirements.txt
python manage.py migrate       
python manage.py createsuperuser (provide user and password for admin console)
python manage.py runserver
