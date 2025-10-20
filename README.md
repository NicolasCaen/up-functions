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

## Manifest par sous-module

- **[Fichier dédié]** Chaque dépôt enfant expose son propre `manifest.json` compatible `up-bulk-plugins-installer`.
- **[Script modèle]** Copier `manifest_build_sample.py` → `build_manifest.py` dans le sous-module puis exécuter `python3 build_manifest.py`. Le script scanne `*.php` / `*.js` (et `inc/**`, `src/**`).
- **[Commandes]** Après modification d’un bloc PHPDoc/JsDoc, lancer `python3 build_manifest.py --output manifest.json` puis committer `manifest.json` avec le dépôt du sous-module.
- **[Manifest global]** Optionnellement, créer un manifest agrégé au niveau racine en fusionnant ceux des sous-modules (adapter `build_manifest.py`).

### Champs PHPDoc/JsDoc attendus

Entête `/** ... */` au début de chaque fichier, format `Clé: valeur`. Principales clés :

- **`Slug`** *(requis)* : identifiant unique.
- **`Nom`** : libellé lisible (défaut basé sur le slug).
- **`Description`** : courte description (facultatif, défaut générique).
- **`Version`** : version du module (`1.0.0` par défaut).
- **`Catégories`** : liste séparée par `,`, `;` ou `|`.
- **`Type`** : clé primaire dans `files` (`php`, `script`, etc.).
- **`Files`/`Fichiers`** : fichiers additionnels via `clé=chemin` (séparés par `,`, `;` ou `|`).
- **`Install`** : chemin(s) de destination. Valeur générique ou par clé (`Install (php): functions/inc/up-cpt`).
- **`Preview`** : vignette optionnelle.

#### Exemple PHP (`cpt-rooms.php`)

```php
/**
 * Slug: cpt-rooms
 * Nom: Custom Post Type Rooms
 * Description: Enregistre le CPT « Rooms » pour les chambres de l'hôtel.
 * Version: 1.2.0
 * Catégories: CPT, Hôtel
 * Type: php
 * Files: style=assets/css/rooms.css|script=assets/js/rooms.js
 * Install (php): functions/inc/up-cpt
 * Install (style): assets/css
 * Install (script): assets/js
 * Preview: previews/cpt-rooms.png
 */
```

#### Exemple JavaScript (`rooms-frontend.js`)

```js
/**
 * Slug: rooms-frontend
 * Nom: Rooms Frontend Enhancements
 * Description: Comportements JS pour l'affichage des chambres (animation + filtres).
 * Version: 1.0.0
 * Catégories: Front, Animation
 * Type: script
 * Install: script=assets/js
 */
```

## Manifest pour Up Bulk Plugin Installer

- **[Compatibilité]** Les manifest des sous-modules (et optionnellement celui de la racine) sont consommés par `@[wp-content/plugins/up-bulk-plugins-installer]`.
- **[Contenu]** Chaque entrée du manifest expose `slug`, `name`, `description`, `categories`, `files`, `install` afin d’alimenter un onglet `manifest` dans l’interface d’installation.
- **[Source]** Les données sont générées automatiquement depuis les blocs PHPDoc/JsDoc décrits ci-dessus.

## Génération automatique

- **[Script Python]** Utiliser `manifest_build_sample.py` comme base pour chaque sous-module (`cp manifest_build_sample.py inc/mon-module/build_manifest.py`).
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
