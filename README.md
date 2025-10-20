# up-functions

Module utilitaire regroupant les Custom Post Types (CPT) et taxonomies génériques utilisés sur les projets hôteliers UP.

## Contenu

- **[CPT principale]** `inc/up-cpt/cpt-rooms.php` (slug par défaut `chambres`).
- **[CPT complémentaires]** `cpt-events.php`, `cpt-offers.php`, `cpt-reviews.php`, `cpt-testimonials.php`, `cpt-portfolio.php`, `cpt-news.php`, `cpt-land.php`, `cpt-property.php`.
- **[Taxonomies]** `inc/up-cpt/tax-rooms.php` (catégories et équipements pour les chambres).
- **[Traductions]** Fichiers PO/MO dans `inc/up-cpt/languages/` (`up-cpt-fr_FR.po`, `up-cpt-fr_FR.mo`).

## Hooks et filtres

- **[Slug CPT]** `up_cpt_{posttype}_slug` permet de personnaliser le slug public (ex. `up_cpt_rooms_slug`).
- **[Args CPT]** `up_cpt_{posttype}_args`, `up_cpt_{posttype}_{slug}_args` pour ajuster les paramètres `register_post_type`.
- **[Taxonomies]** `up_tax_rooms_category_slug`, `up_tax_rooms_feature_slug` et filtres associés pour modifier slug et arguments.
- **[Textdomain]** `up_cpt_textdomain_path` pour redéfinir le chemin de chargement du textdomain `up-cpt`.

## Installation

- **[Chargement]** Inclure les fichiers nécessaires dans le bootstrap du plugin (ex. via `require_once __DIR__ . '/inc/up-cpt/cpt-rooms.php';`).
- **[Permaliens]** Après activation ou modification de slug, visiter `Réglages > Permaliens` pour régénérer les règles.
- **[Traductions]** Compiler `up-cpt-fr_FR.mo` si le fichier n’existe pas (`msgfmt inc/up-cpt/languages/up-cpt-fr_FR.po -o inc/up-cpt/languages/up-cpt-fr_FR.mo`).

## Gestion des sous-modules Git

- **[Ajout]** `git submodule add <ssh|https> inc/mon-module`
- **[Synchronisation]** `git submodule update --init --recursive`
- **[Mise à jour]** `git submodule update --remote inc/mon-module`
- **[Consignation]** Vérifier que `.gitmodules` référence le dépôt et consigner toute nouvelle dépendance dans ce README.

Chaque sous-module doit fournir un fichier principal (`php`, `js`, etc.) muni d’un bloc PHPDoc/JsDoc en français décrivant au minimum : `Catégorie`, `Description`, `Version`.

## Manifest pour Up Bulk Plugin Installer

- **[Compatibilité]** Le fichier `manifest.json` à la racine est compatible avec `up-bulk-plugins-installer` (`@[wp-content/plugins/up-bulk-plugins-installer]`).
- **[Contenu]** Chaque entrée du manifest expose `slug`, `name`, `description`, `categories`, `files`, `install` afin d’alimenter un onglet `manifest` dans l’interface d’installation.
- **[Source]** Les données sont générées automatiquement depuis les blocs PHPDoc/JsDoc des fichiers du dossier `inc/`.

## Génération automatique

- **[Script Python]** `build_manifest.py` scanne `inc/**/*.php` et `inc/**/*.js` et produit `manifest.json`.
- **[Exécution]**
  ```bash
  cd wp-content/plugins/up-functions
  python3 build_manifest.py
  ```
- **[Workflow]** Après toute modification (nouveau sous-module, mise à jour d’en-tête, changement de chemin), relancer le script puis valider `manifest.json` dans le commit.
- **[Personnalisation]** Adapter `SOURCE_GLOBS` ou la logique d’installation (`install`) dans le script si de nouveaux types de fichiers doivent être pris en charge.

## Tests rapides

- **[Vérification admin]** Contrôler la présence des CPT dans le menu WordPress et la traduction des libellés.
- **[REST]** Tester un endpoint CRUD (`/wp-json/wp/v2/rooms`) pour s’assurer que `show_in_rest` est actif.
- **[Taxos chambres]** Créer une catégorie et un équipement, vérifier leur liaison à une chambre.
