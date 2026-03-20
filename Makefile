# Makefile for Webflow-BigCommerce Integration Plugin

.PHONY: install run test test-unit test-integration clean

# Install dependencies
install:
	pip install -r backend/requirements.txt
	pip install -r backend/requirements-dev.txt

# Run the development server
run:
	cd backend && python app.py

# Run all tests
test: test-unit test-integration

# Run unit tests
test-unit:
	cd backend && pytest tests/ -v

# Run integration tests
test-integration:
	python test_integration.py

# Clean up temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf backend/htmlcov/
	rm -rf backend/.coverage

# Format code with black
format:
	black backend/

# Check code style with flake8
lint:
	flake8 backend/

# Run all checks
check: lint test

# Deploy to Heroku (requires Heroku CLI)
deploy:
	git push heroku main

# Show help
help:
	@echo "Available targets:"
	@echo "  install          Install dependencies"
	@echo "  run              Run the development server"
	@echo "  test             Run all tests"
	@echo "  test-unit        Run unit tests"
	@echo "  test-integration Run integration tests"
	@echo "  clean            Clean up temporary files"
	@echo "  format           Format code with black"
	@echo "  lint             Check code style with flake8"
	@echo "  check            Run all checks"
	@echo "  deploy           Deploy to Heroku"
	@echo "  help             Show this help"