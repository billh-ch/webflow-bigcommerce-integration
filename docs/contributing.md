# Contribution Guide

## Welcome
Thank you for your interest in contributing to the Webflow-BigCommerce Integration Plugin! We welcome contributions from the community to help improve and expand this project.

## Code of Conduct
Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## How to Contribute

### Reporting Bugs
1. Check if the issue already exists in GitHub Issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Environment details (browser, OS, etc.)

### Suggesting Enhancements
1. Check existing feature requests
2. Create a new issue with:
   - Problem statement
   - Proposed solution
   - Use cases
   - Alternatives considered

### Code Contributions

#### Development Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/webflow-bigcommerce.git
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   pip install -r backend/requirements-dev.txt
   ```

5. Set up environment variables (see README.md)

#### Making Changes
1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Add tests for your changes
4. Run tests:
   ```bash
   cd backend
   pytest
   ```

5. Format code:
   ```bash
   black .
   ```

6. Check code style:
   ```bash
   flake8 .
   ```

#### Commit Messages
Follow conventional commit format:
- `feat: Add new feature`
- `fix: Resolve issue with cart`
- `docs: Update README`
- `test: Add unit tests`
- `refactor: Improve code structure`

#### Pull Request Process
1. Ensure all tests pass
2. Update documentation if needed
3. Squash commits if necessary
4. Submit pull request with:
   - Clear title
   - Description of changes
   - Issue references
   - Screenshots if UI changes

## Development Guidelines

### Python Code Standards
- Follow PEP 8 style guide
- Use type hints where possible
- Write docstrings for public functions
- Keep functions small and focused
- Handle errors gracefully

### JavaScript Code Standards
- Use modern ES6+ features
- Write modular, reusable code
- Comment complex logic
- Follow consistent naming conventions

### Testing
- Write unit tests for new functionality
- Maintain test coverage above 80%
- Test edge cases and error conditions
- Use mocking for external API calls

### Documentation
- Update README.md for major changes
- Add docstrings for new functions
- Update API documentation
- Include examples for new features

## Architecture Overview

### Backend (Python/Flask)
- `app.py`: Main application entry point
- `api/bigcommerce_client.py`: BigCommerce API integration
- `api/webflow_client.py`: Webflow API integration
- `tests/`: Unit and integration tests

### Frontend (JavaScript)
- `webflow-widgets/product-display.js`: Product display widget
- `webflow-widgets/cart-widget.js`: Shopping cart widget

### Key Concepts
- Environment variables for configuration
- RESTful API design
- Webhook handling for real-time updates
- Error handling and logging

## Areas Needing Contribution

### High Priority
- Enhanced error handling
- Additional Webflow widget features
- Performance optimizations
- Expanded test coverage

### Medium Priority
- Documentation improvements
- New Webflow widget components
- Additional API integrations
- User interface enhancements

### Low Priority
- Code comments and docstrings
- Minor bug fixes
- Typo corrections
- Example projects

## Getting Help
- Check the documentation
- Review existing issues
- Join our community chat
- Contact maintainers directly

## Recognition
Contributors will be recognized in:
- Release notes
- Contributors list
- Social media shout-outs
- Special badges for significant contributions

Thank you for helping make this project better!