# Use the Python3.8 image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#RUN apk add uwsgi
# Install the dependencies
RUN pip3 install uwsgi
RUN pip3 install -r requirement.txt
RUN python3 manage.py makemigrations
RUN python manage.py collectstatic --no-input --clear
EXPOSE 8181

# run the command to start uWSGI
CMD ["uwsgi","--ini", "greenely_uwsgi.ini"]