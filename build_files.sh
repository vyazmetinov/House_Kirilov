echo "BUILD START"
pip install -r requirenments.txt
python 3.9 manage.py collectstatic
pip install psycopg2-binary
echo "BUILD END"