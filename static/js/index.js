// Copy the complete citation, with a fallback for local previews.
async function copyBibTeX() {
  const text = document.getElementById('bibtex-code').textContent;
  const button = document.querySelector('.copy-bibtex-btn');
  const label = button.querySelector('.copy-text');
  let copied = false;

  try {
    await navigator.clipboard.writeText(text);
    copied = true;
  } catch (_) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    try {
      copied = document.execCommand('copy');
    } finally {
      textarea.remove();
      button.focus();
    }
  }

  button.classList.toggle('copied', copied);
  label.textContent = copied ? 'Copied!' : 'Select and copy';
  setTimeout(() => {
    button.classList.remove('copied');
    label.textContent = 'Copy';
  }, 2000);
}

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'
  });
}

window.addEventListener('scroll', () => {
  document.querySelector('.scroll-to-top').classList.toggle('visible', window.scrollY > 300);
}, { passive: true });
