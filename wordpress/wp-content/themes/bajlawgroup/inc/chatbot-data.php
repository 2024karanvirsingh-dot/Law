<?php
/**
 * Chatbot knowledge base definitions.
 */

function bajlaw_get_chatbot_topics() {
    $tagline = 'We learn your history, prepare the paperwork, and keep you updated at every step.';

    return array(
        array(
            'name'        => 'greeting',
            'title'       => 'Welcome to the Baj Law Group immigration guide',
            'keywords'    => array( 'hello', 'hi', 'hey', 'greetings', 'hola' ),
            'response'    => 'Ask any question about visas, green cards, or defending your status and I will explain the basics.',
            'follow_up'   => 'You can type topics like family visa, work visa, green card, asylum, or citizenship to get started.',
            'timeline'    => null,
            'cost'        => null,
        ),
        array(
            'name'        => 'family_immigration',
            'title'       => 'Family Immigration',
            'keywords'    => array( 'spouse', 'marriage', 'fianc\u00e9', 'fiance', 'family', 'parent', 'child', 'petition', 'i-130', 'k1', 'k-1', 'relative' ),
            'response'    => 'Family members who are U.S. citizens or permanent residents can often sponsor loved ones. We collect proof of the relationship, help with forms like the I-130 or I-485, and get you ready for the interview. ' . $tagline,
            'follow_up'   => null,
            'timeline'    => 'Family cases move at different speeds depending on the visa category and consulate. We review processing times and build a schedule so you know what to expect.',
            'cost'        => 'During a consultation we break down government fees, legal fees, and payment plans so you can plan with confidence.',
        ),
        array(
            'name'        => 'employment_visa',
            'title'       => 'Employment Visas',
            'keywords'    => array( 'work', 'employment', 'employer', 'h1b', 'h-1b', 'l1', 'l-1', 'o1', 'o-1', 'tn', 'sponsor', 'job' ),
            'response'    => 'Work visas require a committed employer and strong planning. We coordinate with HR, file the prevailing wage steps, and prepare petitions that explain why you qualify. ' . $tagline,
            'follow_up'   => null,
            'timeline'    => 'Many work visas have strict filing windows. We map those dates so no deadlines are missed.',
            'cost'        => 'We create a proposal that clarifies legal fees, government costs, and premium processing options when available.',
        ),
        array(
            'name'        => 'green_card',
            'title'       => 'Green Cards',
            'keywords'    => array( 'green', 'permanent', 'residence', 'i-485', 'adjustment', 'residency' ),
            'response'    => 'Getting a green card usually happens in stages: petition, waiting for a visa number, and interview or consular processing. We organize evidence, prepare you for questions, and respond quickly to any requests. ' . $tagline,
            'follow_up'   => null,
            'timeline'    => 'Timelines depend on your priority date and whether you are adjusting in the U.S. or abroad. We review the Visa Bulletin and plan for each step.',
            'cost'        => 'You will see a summary of filing fees and an estimate of professional services before work begins.',
        ),
        array(
            'name'        => 'citizenship',
            'title'       => 'Citizenship & Naturalization',
            'keywords'    => array( 'citizenship', 'naturalization', 'n-400', 'civic', 'civics', 'oath' ),
            'response'    => 'Becoming a citizen unlocks travel flexibility and voting rights. We confirm eligibility, help collect proof of residence, and practice the interview with you.',
            'follow_up'   => null,
            'timeline'    => 'We track biometrics, interview scheduling, and oath ceremonies so you are never surprised.',
            'cost'        => 'We will outline USCIS fees and flexible payment options for legal services.',
        ),
        array(
            'name'        => 'humanitarian',
            'title'       => 'Humanitarian Options',
            'keywords'    => array( 'asylum', 'violence', 'vawa', 't visa', 'u visa', 'humanitarian', 'refugee', 'parole' ),
            'response'    => 'Humanitarian visas protect people escaping harm or exploitation. We take trauma-informed statements, gather corroborating evidence, and coordinate with support providers.',
            'follow_up'   => null,
            'timeline'    => 'Some filings can take years. We stay on top of requests for evidence and make sure safety planning comes first.',
            'cost'        => 'We discuss fee waivers and community grants so cost never blocks a survivor from seeking status.',
        ),
        array(
            'name'        => 'removal_defense',
            'title'       => 'Removal Defense',
            'keywords'    => array( 'court', 'removal', 'deportation', 'defense', 'notice to appear', 'nta', 'judge', 'ice' ),
            'response'    => 'In court we build a strategy, collect evidence, and prepare witnesses so the judge understands your story. We appear at every hearing with you.',
            'follow_up'   => null,
            'timeline'    => 'Court calendars can change quickly. We monitor the docket and call you immediately about updates.',
            'cost'        => 'Payment plans and sliding scale options keep legal representation within reach.',
        ),
        array(
            'name'        => 'detention',
            'title'       => 'Emergency & Detention',
            'keywords'    => array( 'detained', 'arrested', 'custody', 'raid', 'emergency', 'urgent', 'bond' ),
            'response'    => 'If someone is detained or facing an urgent deadline, call us right away at (206) 555-0123. We coordinate emergency representation, bond requests, and safety planning.',
            'follow_up'   => null,
            'timeline'    => null,
            'cost'        => null,
        ),
    );
}

function bajlaw_get_chatbot_disclaimer() {
    return 'This chat offers general guidance only and is not legal advice. For personal help, contact the Baj Law Group PLLC at (206) 555-0123 or visit bajlawgroup.com/contact.';
}

function bajlaw_get_chatbot_closing() {
    return 'Thank you for speaking with the Baj Law Group PLLC. When you are ready, reach out and we will create a plan together.';
}

function bajlaw_get_chatbot_emergency_message() {
    return 'If anyone is detained, arrested, or facing an urgent deadline, call (206) 555-0123 immediately. We will coordinate emergency assistance.';
}
