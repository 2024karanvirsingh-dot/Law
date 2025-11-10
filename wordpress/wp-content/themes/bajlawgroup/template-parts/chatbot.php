<?php
/**
 * Template part for chatbot interface.
 */
?>
<div class="baj-chatbot">
    <div class="baj-chatbot__header">
        <h3>Immigration Guidance Chat</h3>
        <p>Ask about visas, green cards, court defense, timelines, or fees. Responses are for education only.</p>
        <div class="baj-chatbot__suggestions" aria-label="Suggested questions"></div>
    </div>
    <ol class="baj-chatbot__messages" aria-live="polite"></ol>
    <form class="baj-chatbot__form">
        <label for="baj-chatbot-input" class="screen-reader-text"><?php esc_html_e( 'Ask a question', 'bajlawgroup' ); ?></label>
        <input type="text" id="baj-chatbot-input" class="baj-chatbot__input" name="message" placeholder="Type your question" autocomplete="off">
        <button type="submit"><?php esc_html_e( 'Send', 'bajlawgroup' ); ?></button>
    </form>
</div>
