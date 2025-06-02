# 🌿 Living Roots Inventory Dashboard

A small Flask app to track spice and tea inventory for Living Roots.

## 🚀 Features
- Displays current inventory from a JSON file
- Dockerized for deployment
- GitHub Actions workflow for CI checks

## 🧪 Run Locally
```bash
docker build -t inventory-app .
docker run -p 5000:5000 inventory-app
```

Then visit `http://localhost:5000`

## 📦 Deploy

You can deploy on AWS EC2 or Heroku. See the `.github/workflows/deploy.yml` for GitHub Actions automation.