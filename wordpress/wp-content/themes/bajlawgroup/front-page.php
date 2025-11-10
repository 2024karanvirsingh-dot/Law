<?php get_header(); ?>

<main id="primary" class="site-main">
    <header class="site-header">
        <div class="header-inner">
            <h1>Immigration Advocacy for Families, Workers, and Dreamers</h1>
            <p>The Baj Law Group PLLC combines strategic planning with compassionate advocacy to guide you from uncertainty to confidence. Explore our services and get plain-language answers to common immigration questions.</p>
            <div class="cta-group">
                <a class="button button-primary" href="tel:12065550123">Call (206) 555-0123</a>
                <a class="button button-outline" href="#chatbot">Talk with our guide</a>
            </div>
        </div>
    </header>

    <section class="section">
        <div class="section-inner">
            <h2>How We Support Your Immigration Journey</h2>
            <div class="service-grid">
                <article class="card">
                    <h3>Family Immigration</h3>
                    <p>Petitions for spouses, parents, children, and fiancés with meticulous evidence preparation and interview coaching.</p>
                </article>
                <article class="card">
                    <h3>Employment Visas</h3>
                    <p>Strategies for employers and professionals seeking H-1B, TN, O-1, L-1, and other employment-based visas.</p>
                </article>
                <article class="card">
                    <h3>Humanitarian Relief</h3>
                    <p>Trauma-informed support for asylum, VAWA, U visas, T visas, and parole requests when safety matters most.</p>
                </article>
                <article class="card">
                    <h3>Removal Defense</h3>
                    <p>Comprehensive court representation, evidence gathering, and bond preparation to defend your ability to remain in the U.S.</p>
                </article>
            </div>
        </div>
    </section>

    <section class="section alt">
        <div class="section-inner">
            <h2>Client Experiences</h2>
            <div class="testimonial">
                <p>“The team explained every step with patience and kept us updated from the first petition through the interview. We felt prepared and supported the entire time.”</p>
                <span class="author">— M. &amp; R., Seattle</span>
            </div>
        </div>
    </section>

    <section class="section" id="chatbot">
        <div class="section-inner">
            <h2>Ask Our Immigration Guide</h2>
            <p style="text-align:center; max-width:680px; margin:0 auto 2rem; color:var(--baj-text-light);">Use the interactive assistant to learn about timelines, fees, and next steps for your immigration goals. The chatbot provides educational information and reminders to connect with our attorneys for personal advice.</p>
            <?php echo do_shortcode( '[bajlaw_chatbot]' ); ?>
        </div>
    </section>

    <section class="section alt">
        <div class="section-inner contact-panel">
            <div class="panel">
                <h3>Schedule a Consultation</h3>
                <p>Call <a href="tel:12065550123">(206) 555-0123</a> or email <a href="mailto:intake@bajlawgroup.com">intake@bajlawgroup.com</a> to reserve a confidential meeting. We offer evening and weekend appointments by request.</p>
            </div>
            <div class="panel">
                <h3>Visit Our Office</h3>
                <p>1234 2nd Ave Suite 600<br>Seattle, WA 98101</p>
                <p><strong>Hours:</strong> Monday – Friday, 9am – 6pm PT</p>
            </div>
            <div class="panel">
                <h3>Resources &amp; Updates</h3>
                <p>Follow our updates on immigration policy changes, processing times, and success stories from the Baj Law Group community.</p>
            </div>
        </div>
    </section>
</main>

<?php get_footer(); ?>
