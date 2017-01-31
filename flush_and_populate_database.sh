source venv/bin/activate

rm *.sqlite3
rm -r app_forum/migrations/*
touch app_forum/migrations/__init__.py


python manage.py makemigrations app_forum
python manage.py migrate

python manage.py shell < populate_models.py

