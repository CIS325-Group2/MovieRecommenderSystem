FROM python:3.8.8
COPY ./final_project_app /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python
RUN pip install -r requirements.txt
CMD python Netflix_Recommender_Flask.py
