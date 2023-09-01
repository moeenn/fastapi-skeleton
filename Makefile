PI = python
ENTRYPOINT = main:app
SCRIPTS_DIR = ./app/core/scripts
DEPS_FILE = requirements.txt
PORT = 5000
PROD_WORKERS = 4

# after any new 3rd-party package is installed, run this command to update the 
# project dependencies listed in the "requirements.txt" file. This will 
# allow for reproducible builds for the project
pkg-save:
	pip freeze > ${DEPS_FILE}


# when setting-up this project on a new machine, create a new virtual 
# environment and run the following command to install external dependencies
install-deps:
	pip install -r ${DEPS_FILE}


# run server in development mode, environment variables will be read from the
# ".env" file and start the server with development features (e.g live-reload 
# etc.) enabled
run-dev:
	dotenv uvicorn ${ENTRYPOINT} --reload --port ${PORT}


# run the serve in production mode. Environment variables will not be loaded 
# from ".env" file and all development features will be disabled.
run-prod: 
	gunicorn ${ENTRYPOINT} --workers ${PROD_WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT} --log-level info


# recursively remove __pycache__ directories from project
clean:
	@echo "cleaning pycache..."
	@find . -type d -name  "__pycache__" -exec rm -r {} +


# app secret is used to sign JWT and cookies etc. Run the following command 
# to generate a new app secret
gen-secret:
	${PI} ${SCRIPTS_DIR}/generate_secret.py	


# run automated code tests
test:
	dotenv ${PI} -m unittest ./app/**/test_*.py
	
