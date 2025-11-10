<?php
/**
 * Theme bootstrap for Baj Law Group Immigration theme.
 */

define( 'BAJLAW_THEME_VERSION', '1.0.0' );

define( 'BAJLAW_THEME_DIR', get_template_directory() );
define( 'BAJLAW_THEME_URL', get_template_directory_uri() );

require_once BAJLAW_THEME_DIR . '/inc/chatbot-data.php';

add_action( 'after_setup_theme', function () {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    register_nav_menus(
        array(
            'primary' => __( 'Primary Navigation', 'bajlawgroup' ),
        )
    );
} );

add_action( 'wp_enqueue_scripts', function () {
    wp_enqueue_style( 'bajlaw-theme', BAJLAW_THEME_URL . '/style.css', array(), BAJLAW_THEME_VERSION );
    wp_enqueue_style( 'bajlaw-chatbot', BAJLAW_THEME_URL . '/assets/css/chatbot.css', array( 'bajlaw-theme' ), BAJLAW_THEME_VERSION );

    wp_enqueue_script( 'bajlaw-chatbot', BAJLAW_THEME_URL . '/assets/js/chatbot.js', array(), BAJLAW_THEME_VERSION, true );

    wp_localize_script( 'bajlaw-chatbot', 'BajLawChatbotData', array(
        'topics'     => bajlaw_get_chatbot_topics(),
        'disclaimer' => bajlaw_get_chatbot_disclaimer(),
        'closing'    => bajlaw_get_chatbot_closing(),
        'emergency'  => bajlaw_get_chatbot_emergency_message(),
        'ajaxUrl'    => admin_url( 'admin-ajax.php' ),
    ) );
} );

add_shortcode( 'bajlaw_chatbot', function () {
    ob_start();
    get_template_part( 'template-parts/chatbot' );
    return ob_get_clean();
} );

add_action( 'init', function () {
    add_rewrite_endpoint( 'immigration-guides', EP_ROOT );
} );

add_action( 'template_redirect', function () {
    global $wp_query;

    if ( isset( $wp_query->query_vars['immigration-guides'] ) ) {
        status_header( 200 );
        nocache_headers();
        header( 'Content-Type: application/json; charset=utf-8' );
        echo wp_json_encode( bajlaw_get_chatbot_topics() );
        exit;
    }
} );
