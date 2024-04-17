update_env:
	@echo "Updating the 'real_estate_broker_python' Conda environment from environment.yml..."
	conda env update --name real_estate_broker_python --file environment.yml
	@echo "Please activate the Conda environment with the following command: conda activate real_estate_broker_python"