# Image Analyzer Service

## How to run the service


```bash
# setup environment .venv
# Mac
python3 -m venv .venv

# windows
python -m venv .venv

# activate environment
# Windows	Command Prompt (cmd.exe)	
.venv\Scripts\activate.bat

# Windows	PowerShell	
.venv\Scripts\Activate.ps1

# macOS/Linux	Bash/Zsh	
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the service
uvicorn main:app --reload
```

The service will be available at `http://localhost:8000`.

## Available endpoints

- `GET /docs` - Interactive API documentation
- `GET /redoc` - Interactive API documentation
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Authenticate a user and get a token
- `POST /images/upload` - Upload an image for analysis
- `GET /images/{image_id}/analysis` - Retrieve analysis results for a specific image

## Any assumptions you made

- Images are provided as multipart/form-data
- The service runs on a single instance
- Python 3.10+ is available

## What you would improve if this were production

- Add database persistence for image metadata and analysis results
- Deploy with load balancing, auto-scaling, and containerization (Docker, Kubernetes)
- Implement robust input validation, security headers, and vulnerability scanning
- Add caching for frequently accessed analysis results
- Implement monitoring, alerting, and distributed tracing for observability
- Establish a CI/CD pipeline with automated testing and deployment
- Configure CORS for cross-origin requests
- Store all sensitive data in environment variables (.env)
- Implement rate limiting to prevent API abuse and DDoS attacks
- Add login attempt throttling with account lockout after failed attempts
