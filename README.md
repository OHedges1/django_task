# q_interview

Requires:

    - Docker

    - Docker-compose

To-do:

    - Prevent data replication on multiple "fetch_and_save" calls

    - Make data persist when the container is taken down

    - Add style sheet

References:

    - https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ 

        - used for Docker setup

Challenges:

    - using queries combined with a foreign key

Task feedback:

    - I'm impressed with how well the task isolated the assessed skills

To use:

    - Just run start.sh

    - http://localhost:8000/fetch_and_save/

    - http://localhost:8000/retrieve_from_db/AU/
