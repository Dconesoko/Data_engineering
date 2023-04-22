FROM python:3.9.5

# set up location of code
WORKDIR /code
ENV PYTHONPATH=/code/src

# install cron
RUN apt-get update && apt-get install cron -y

# install python requirements
ADD ./container/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy repo
COPY ./ /code/

# Copy pipeline_cron file to the cron.d directory
COPY /scheduler/pipeline_cron /etc/cron.d/pipeline_cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/pipeline_cron

# Apply cron job
RUN crontab /etc/cron.d/pipeline_cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
 
# Run cron
CMD cron && tail -f /var/log/cron.log && make run