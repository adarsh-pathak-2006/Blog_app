document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('[data-nav]');
    const navToggle = document.querySelector('[data-nav-toggle]');
    const themeToggle = document.querySelector('[data-theme-toggle]');
    const scrollButtons = document.querySelectorAll('[data-scroll-target]');
    const searchInput = document.querySelector('[data-blog-search]');
    const cards = document.querySelectorAll('[data-blog-card]');
    const editorForm = document.querySelector('[data-editor-form]');
    const editorTitle = document.querySelector('[data-editor-title]');
    const editorContent = document.querySelector('[data-editor-content]');
    const previewTitle = document.querySelector('[data-preview-title]');
    const previewContent = document.querySelector('[data-preview-content]');
    const charCount = document.querySelector('[data-char-count]');

    const storedTheme = localStorage.getItem('blog-theme');
    if (storedTheme === 'dark') {
        document.body.classList.add('theme-dark');
    }

    if (navToggle && nav) {
        navToggle.addEventListener('click', () => {
            const isOpen = nav.classList.toggle('is-open');
            navToggle.setAttribute('aria-expanded', String(isOpen));
        });
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('theme-dark');
            const isDark = document.body.classList.contains('theme-dark');
            localStorage.setItem('blog-theme', isDark ? 'dark' : 'light');
        });
    }

    scrollButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const target = document.querySelector(button.dataset.scrollTarget);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    if (searchInput && cards.length) {
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.trim().toLowerCase();

            cards.forEach((card) => {
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(query) ? '' : 'none';
            });
        });
    }

    if (editorForm && editorTitle && editorContent && previewTitle && previewContent && charCount) {
        const syncPreview = () => {
            const title = editorTitle.value.trim();
            const content = editorContent.value.trim();

            previewTitle.textContent = title || 'Untitled post';
            previewContent.textContent = content || 'Your writing preview will appear here.';
            charCount.textContent = editorContent.value.length;
        };

        ['input', 'keyup', 'change'].forEach((eventName) => {
            editorTitle.addEventListener(eventName, syncPreview);
            editorContent.addEventListener(eventName, syncPreview);
        });

        syncPreview();
    }
});
