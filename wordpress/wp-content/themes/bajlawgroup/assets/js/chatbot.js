(function () {
  const root = document.querySelector('.baj-chatbot');
  if (!root || typeof BajLawChatbotData === 'undefined') {
    return;
  }

  const messagesEl = root.querySelector('.baj-chatbot__messages');
  const form = root.querySelector('.baj-chatbot__form');
  const input = root.querySelector('.baj-chatbot__input');
  const suggestions = root.querySelector('.baj-chatbot__suggestions');

  const topics = BajLawChatbotData.topics || [];
  const disclaimer = BajLawChatbotData.disclaimer;
  const closing = BajLawChatbotData.closing;
  const emergency = BajLawChatbotData.emergency;

  const GOODBYE = ['bye', 'goodbye', 'quit', 'exit'];
  const TIMELINE = ['long', 'time', 'timeline', 'wait', 'processing', 'slow', 'status'];
  const COST = ['cost', 'fee', 'fees', 'price', 'pay', 'retainer', 'afford'];
  const EMERGENCY = ['detained', 'arrested', 'custody', 'raid', 'deadline', 'urgent', 'emergency'];

  const state = {
    disclaimerShared: false,
    lastTopic: null,
    lastTimeline: null,
    lastCost: null,
  };

  function normalize(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, ' ')
      .split(/\s+/)
      .filter(Boolean);
  }

  function renderMessage(content, author) {
    const li = document.createElement('li');
    li.className = `baj-chatbot__message baj-chatbot__message--${author}`;

    const bubble = document.createElement('div');
    bubble.className = 'baj-chatbot__bubble';
    bubble.innerHTML = content;
    li.appendChild(bubble);

    const meta = document.createElement('div');
    meta.className = 'baj-chatbot__meta';
    meta.textContent = author === 'bot' ? 'Baj Law Group assistant' : 'You';
    li.appendChild(meta);

    messagesEl.appendChild(li);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function scoreTopic(tokens, topic) {
    return topic.keywords.reduce((score, keyword) => (tokens.includes(keyword) ? score + 1 : score), 0);
  }

  function findBestTopic(tokens) {
    let best = null;
    let bestScore = 0;

    topics.forEach((topic) => {
      const score = scoreTopic(tokens, topic);
      if (score > bestScore) {
        best = topic;
        bestScore = score;
      }
    });

    return best;
  }

  function respondTo(tokens) {
    if (!state.disclaimerShared) {
      state.disclaimerShared = true;
      renderMessage(`<strong>Disclaimer:</strong> ${disclaimer}`, 'bot');
    }

    if (tokens.some((token) => GOODBYE.includes(token))) {
      renderMessage(closing, 'bot');
      return;
    }

    if (tokens.some((token) => EMERGENCY.includes(token))) {
      renderMessage(`<strong>Emergency:</strong> ${emergency}`, 'bot');
      return;
    }

    const topic = findBestTopic(tokens);

    if (topic) {
      state.lastTopic = topic;
      state.lastTimeline = topic.timeline;
      state.lastCost = topic.cost;

      renderMessage(`<strong>${topic.title}</strong><br>${topic.response}`, 'bot');

      if (topic.follow_up) {
        renderMessage(topic.follow_up, 'bot');
      }

      if (tokens.some((token) => TIMELINE.includes(token)) && topic.timeline) {
        renderMessage(`<em>Timeline:</em> ${topic.timeline}`, 'bot');
      }

      if (tokens.some((token) => COST.includes(token)) && topic.cost) {
        renderMessage(`<em>Costs:</em> ${topic.cost}`, 'bot');
      }

      return;
    }

    if (state.lastTopic) {
      if (tokens.some((token) => TIMELINE.includes(token)) && state.lastTimeline) {
        renderMessage(`<em>Timeline:</em> ${state.lastTimeline}`, 'bot');
        return;
      }

      if (tokens.some((token) => COST.includes(token)) && state.lastCost) {
        renderMessage(`<em>Costs:</em> ${state.lastCost}`, 'bot');
        return;
      }
    }

    renderMessage('I did not catch that. Could you rephrase or ask about family visas, work visas, green cards, or court defense?', 'bot');
  }

  function handleSubmit(event) {
    event.preventDefault();
    const text = input.value.trim();
    if (!text) {
      return;
    }

    renderMessage(text, 'user');
    input.value = '';

    const tokens = normalize(text);
    respondTo(tokens);
  }

  function seedConversation() {
    renderMessage('Hello! I\'m the Baj Law Group immigration assistant. How can I help you today?', 'bot');
    if (suggestions) {
      topics
        .filter((topic) => topic.name !== 'greeting')
        .slice(0, 6)
        .forEach((topic) => {
          const chip = document.createElement('button');
          chip.type = 'button';
          chip.className = 'baj-chatbot__chip';
          chip.textContent = topic.title;
          chip.addEventListener('click', () => {
            input.value = topic.title;
            form.dispatchEvent(new Event('submit', { cancelable: true }));
          });
          suggestions.appendChild(chip);
        });
    }
  }

  form.addEventListener('submit', handleSubmit);
  seedConversation();
})();
