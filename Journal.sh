# Créer un nouveau dépôt GitHub 
git init
git branch -M main
git add .
git commit -m "first commit"
gh repo create indé_test --public
git remote add origin https://github.com/JXPM/indé_test.git
git push --set-upstream origin main

#fichier Maj et push
git status
git add .
git commit -m "maj de readme"
git push origin main