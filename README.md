# Baj Law Group WordPress Theme

This repository contains a custom WordPress theme that turns the former immigration chatbot project into a polished marketing site for the Baj Law Group PLLC. The theme highlights core practice areas, features testimonials, and includes an in-browser immigration guidance chatbot built entirely with JavaScript.

## Project Structure

```
wordpress/
└── wp-content/
    └── themes/
        └── bajlawgroup/
            ├── assets/
            │   ├── css/
            │   │   └── chatbot.css
            │   └── js/
            │       └── chatbot.js
            ├── front-page.php
            ├── functions.php
            ├── header.php
            ├── footer.php
            ├── inc/
            │   └── chatbot-data.php
            ├── index.php
            ├── style.css
            └── template-parts/
                └── chatbot.php
```

## Getting Started

1. Copy the `bajlawgroup` theme folder into your WordPress installation at `wp-content/themes/`.
2. From the WordPress admin dashboard, navigate to **Appearance → Themes** and activate “Baj Law Group Immigration.”
3. Set a static homepage using the included front-page template to display the hero, service highlights, testimonial, and chatbot section.
4. Add or edit pages and navigation menus as desired.

## Chatbot Shortcode

The interactive chatbot can appear on any page or post via the `[bajlaw_chatbot]` shortcode. The chatbot uses an internal knowledge base defined in `inc/chatbot-data.php` and requires no external services.

## Customization Tips

- Update the service descriptions, testimonials, and contact information in `front-page.php`.
- Adjust color tokens or typography in `style.css` for brand alignment.
- Extend the chatbot knowledge base by editing the PHP array inside `inc/chatbot-data.php`.

## License

This theme is distributed under the GNU General Public License v2 or later.
