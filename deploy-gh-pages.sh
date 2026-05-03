#!/bin/bash
# Manual deployment script for GitHub Pages
# This builds the site locally and pushes the dist/ folder to the gh-pages branch
# Needed because public/pdfs/ is gitignored and won't be available in CI

set -e

echo "=== Building TU QBank for deployment ==="
npm run build

echo "=== Deploying to gh-pages branch ==="
cd dist
git init
git add .
git commit -m "Deploy to GitHub Pages - $(date)"
git branch -M gh-pages
git remote add origin git@github.com:Raman21676/QBank.git || true
git push -f origin gh-pages

echo "=== Deployment complete! ==="
echo "Site should be available at: https://raman21676.github.io/QBank/"
