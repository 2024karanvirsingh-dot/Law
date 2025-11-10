<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<div id="page" class="site">
    <a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e( 'Skip to content', 'bajlawgroup' ); ?></a>
    <header class="site-banner">
        <div class="site-banner__inner" style="max-width:1040px;margin:0 auto;padding:1rem 1.25rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;">
            <div class="site-branding">
                <?php if ( has_custom_logo() ) {
                    the_custom_logo();
                } else { ?>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-title" style="font-weight:700;font-size:1.25rem;color:var(--baj-primary);text-decoration:none;">Baj Law Group PLLC</a>
                <?php } ?>
                <p class="site-description" style="margin:0;font-size:0.9rem;color:var(--baj-text-light);">Immigration Attorneys in Seattle, Washington</p>
            </div>
            <nav class="site-navigation" aria-label="Primary menu">
                <?php
                wp_nav_menu(
                    array(
                        'theme_location' => 'primary',
                        'menu_class'     => 'menu',
                        'container'      => false,
                        'fallback_cb'    => false,
                    )
                );
                ?>
            </nav>
        </div>
    </header>
