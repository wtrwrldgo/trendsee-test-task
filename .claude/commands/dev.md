# /dev — Start Development Environment

Start the full development stack.

## Steps
1. Check if Docker is running
2. Run `docker-compose up --build` in background
3. Wait for health checks to pass
4. Report service URLs:
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:5173
   - API Docs: http://localhost:8000/docs
