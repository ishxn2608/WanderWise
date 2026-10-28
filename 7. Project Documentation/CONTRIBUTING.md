# Contributing to WanderWise

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/WanderWise.git`
3. Follow the [SETUP.md](SETUP.md) guide to run locally
4. Create a feature branch: `git checkout -b feature/your-feature-name`

## Code Standards

- Python: follow PEP 8, use type hints
- JavaScript/JSX: functional components, hooks only
- Keep components small and single-purpose
- Never commit `.env` files or API keys

## Pull Request Process

1. Make sure all 6 backend tests pass: `pytest -v`
2. Make sure frontend builds: `npm run build`
3. Write a clear PR description
4. Reference any related issues

## Project Structure

```
WanderWise/
├── backend/          FastAPI Python API
├── frontend/         React + Vite UI
├── supabase/         Database schema
├── 1. Brainstorming and Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
├── 6. Project Testing/
├── 7. Project Documentation/
└── 8. Project Demonstration/
```
