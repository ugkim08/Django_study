FROM python:3.9.0
WORKDIR /home/
RUN git clone https://github.com/ugkim08/Django_study.git
WORKDIR /home/Django_study/
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN echo "SECRET_KEY=django-insecure-$31-6mesxgo6$3)kwb@)dq3nlh&dv&sjtmx$h^-0zl%939@xt@" > .env
RUN python manage.py migrate
EXPOSE 8000
CMD ["gunicorn", "ugkim08.wsgi", "--bind", "0.0.0.0:8000"]