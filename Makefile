setup:
 # You may want to do this
    virtualenv --python python3 ~/deploy_env
 # afterward then source
    source ~/deploy_env/bin/activate
install:
	pip install -r requirements.txt

lint:
    pylint --disable=R,C main.py
    
all: install lint