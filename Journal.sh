# Créer un nouveau dépôt GitHub 
git init
git branch -M main
git add .
git commit -m "first commit"
gh repo create inde_test --public
git remote add origin https://github.com/JXPM/inde_test.git
git push --set-upstream origin main

#fichier Maj et push
git status
git add .
git commit -m "maj de readme"
git push origin main


python3 -m venv nike_venv

source nike_venv/bin/activate

pip install -r requierements.txt
python3 nike_formulaire.py
