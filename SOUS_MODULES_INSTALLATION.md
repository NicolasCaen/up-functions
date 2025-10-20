# Installation des sous-modules après duplication du dépôt

## Objectif

- **[Restauration]** Recréer les liens vers les sous-modules Git après avoir cloné ou dupliqué `up-functions`.
- **[Synchronisation]** S’assurer que chaque sous-module est initialisé et prêt à être utilisé (manifest, scripts, etc.).

## Structure attendue

`wp-content/plugins/up-functions/` contient plusieurs sous-modules Git déclarés dans `.gitmodules`. Exemple :

```ini
[submodule "inc/gutenberg-restrictions"]
    path = inc/gutenberg-restrictions
    url = git@github.com:NicolasCaen/gutenberg-restrictions.git
[submodule "inc/up-module-cpt"]
    path = inc/up-module-cpt
    url = git@github.com:NicolasCaen/up-module-cpt.git
[submodule "inc/up-module-gsap"]
    path = inc/up-module-gsap
    url = git@github.com:NicolasCaen/up-module-gsap.git
[submodule "inc/up-module-js"]
    path = inc/up-module-js
    url = git@github.com:NicolasCaen/up-module-js.git
[submodule "inc/up-module-php"]
    path = inc/up-module-php
    url = git@github.com:NicolasCaen/up-module-php.git
```

## Étapes après duplication

1. **[Synchroniser les URLs]**
   ```bash
   git submodule sync
   ```

2. **[Initialiser les sous-modules]**
   ```bash
   git submodule update --init --recursive
   ```

3. **[Vérifier l’état]**
   ```bash
   git submodule status
   ```
   La commande doit afficher chaque sous-module avec son commit courant. Exemple :
   ```
    71a02b1a80a9ad26325f5c8f233232ce2ff89c29 inc/up-module-cpt
   ```

4. **[Mettre à jour (optionnel)]**
   Pour tirer les dernières modifications depuis les dépôts distants :
   ```bash
   git submodule update --remote --merge
   ```

## Problèmes fréquents

- **`fatal: not a git repository`** : supprimer le dossier du sous-module puis relancer `git submodule update --init`. Exemple :
  ```bash
  rm -rf inc/up-module-cpt
  git submodule update --init inc/up-module-cpt
  ```

- **Chemins résiduels** : si un ancien sous-module n’existe plus, retirer son entrée du cache Git :
  ```bash
  git submodule deinit -f inc/ancien-module
  git rm -f inc/ancien-module
  rm -rf .git/modules/inc/ancien-module
  ```

## Ressources complémentaires

- **[Ajout d’un sous-module]** Voir `AJOUTER_SUBMODULE.md`.
- **[Commentaires manifest]** Voir `COMMENTAIRES_MANIFEST.md` pour rédiger les métadonnées obligatoires.
- **[Manifest Tabs]** La configuration de `up-bulk-plugins-installer` se trouve dans `up-bulk-plugins-installer/config/manifest-tabs.php`.
- **[Scripts manifest]** Utiliser `manifest_build_sample.py` ou les scripts locaux `manifest_build.py` pour générer les fichiers `manifest.json` dans chaque sous-module.
