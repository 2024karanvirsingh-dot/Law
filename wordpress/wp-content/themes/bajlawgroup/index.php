<?php get_header(); ?>

<main id="primary" class="site-main section">
    <div class="section-inner">
        <?php if ( have_posts() ) : ?>
            <?php while ( have_posts() ) : the_post(); ?>
                <article <?php post_class( 'card' ); ?>>
                    <header class="entry-header">
                        <?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>
                    </header>
                    <div class="entry-content">
                        <?php the_content(); ?>
                    </div>
                </article>
            <?php endwhile; ?>
        <?php else : ?>
            <article class="card">
                <h1><?php esc_html_e( 'Content coming soon', 'bajlawgroup' ); ?></h1>
                <p><?php esc_html_e( 'Check back shortly for updates from the Baj Law Group team.', 'bajlawgroup' ); ?></p>
            </article>
        <?php endif; ?>
    </div>
</main>

<?php get_footer(); ?>
