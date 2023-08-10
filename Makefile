PI = python
ENTRYPOINT = ./main.py
SCRIPTS_DIR = ./app/core/scripts
DEPS_FILE = requirements.txt

# after any new 3rd-party package is installed, run this command to update the 
# project dependencies listed in the "requirements.txt" file. This will 
# allow for reproducible builds for the project
record-pkg:
	pip freeze > ${DEPS_FILE}


# when setting-up this project on a new machine, create a new virtual 
# environment and run the following command to install external dependencies
install-deps:
	pip install -r ${DEPS_FILE}


# run server in development mode, environment variables will be read from the
# ".env" file and start the server with development features (e.g live-reload 
# etc.) enabled
run-dev:
	dotenv ${PI} ${ENTRYPOINT}


# run the serve in production mode. Environment variables will not be loaded 
# from ".env" file and all development features will be disabled.
run-prod:
	${PI} ${ENTRYPOINT}


# app secret is used to sign JWT and cookies etc. Run the following command 
# to generate a new app secret
gen-secret:
	${PI} ${SCRIPTS_DIR}/generate_secret.py	


# run automated code tests
test:
	dotenv ${PI} -m unittest ./app/**/test_*.py
