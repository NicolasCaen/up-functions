# Ajouter un sous-module Git

## Pré-requis

- **[Accès GitHub]** Disposer des droits lecture/écriture sur le dépôt distant à ajouter.
- **[Clés SSH]** S’assurer que les clés SSH sont configurées pour `git@github.com`.
- **[Dépôt]** Se placer à la racine de `wp-content/plugins/up-functions/`.

## Étapes

1. **[Ajouter le sous-module]**
   ```bash
   git submodule add git@github.com:NicolasCaen/up-module-scss.git inc/up-module-scss
   ```

2. **[Synchroniser la configuration]**
   ```bash
   git submodule sync
   ```

3. **[Initialiser et mettre à jour]**
   ```bash
   git submodule update --init --recursive
   ```

4. **[Commiter les changements]**
   ```bash
   git add .gitmodules inc/mon-sous-module
   git commit -m "Ajout du sous-module mon-sous-module"
   ```

5. **[Pousser vers l'origine]**
   ```bash
   git push origin Master
   ```

## Commandes utiles

- **[Lister l’état des sous-modules]**
  ```bash
  git submodule status
  ```

- **[Mettre à jour tous les sous-modules]**
  ```bash
  git submodule update --remote --merge
  ```

- **[Retirer un sous-module]**
  ```bash
  git submodule deinit -f inc/mon-sous-module
  git rm -f inc/mon-sous-module
  rm -rf .git/modules/inc/mon-sous-module
  ```

## Astuces

- **[Configuration partagée]** Documenter les sous-modules dans `COMMENTAIRES_MANIFEST.md` et/ou un README local.
- **[Scripts manifest]** Copier `manifest_build_sample.py` dans chaque sous-module pour générer `manifest.json`.
- **[Hooks CI/CD]** Vérifier que la CI initialise les sous-modules (`git submodule update --init --recursive`).
- **[Commentaires manifest]** Voir `COMMENTAIRES_MANIFEST.md` pour rédiger les blocs PHPDoc/JsDoc compatibles `up-bulk-plugins-installer`.
