/**
 * JusticeGram General UI Interactions
 */

document.addEventListener('DOMContentLoaded', function () {
  // Initialize Bootstrap tooltips if any
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Auto-dismiss alerts after 5 seconds
  const autoAlerts = document.querySelectorAll('.alert-dismissible');
  autoAlerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) {
        bsAlert.close();
      }
    }, 6000);
  });

  // Bookmark toggle buttons with asynchronous fetch
  const bookmarkButtons = document.querySelectorAll('.btn-bookmark-toggle');
  bookmarkButtons.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const url = this.getAttribute('data-url');
      const icon = this.querySelector('i');
      const textSpan = this.querySelector('.bookmark-text');

      if (!url) return;

      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
      .then(response => {
        if (response.redirected) {
          window.location.href = response.url;
          return;
        }
        return response.json();
      })
      .then(data => {
        if (data && data.success) {
          if (data.bookmarked) {
            btn.classList.add('btn-primary');
            btn.classList.remove('btn-outline-primary', 'btn-jg-outline');
            if (icon) {
              icon.classList.remove('bi-bookmark');
              icon.classList.add('bi-bookmark-fill');
            }
            if (textSpan) textSpan.textContent = 'Saved';
          } else {
            btn.classList.remove('btn-primary');
            btn.classList.add('btn-jg-outline');
            if (icon) {
              icon.classList.remove('bi-bookmark-fill');
              icon.classList.add('bi-bookmark');
            }
            if (textSpan) textSpan.textContent = 'Save';
          }
        }
      })
      .catch(err => console.error('Bookmark error:', err));
    });
  });

  // Copy helpline button helper
  const copyButtons = document.querySelectorAll('.btn-copy-helpline');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      const number = this.getAttribute('data-number');
      if (number) {
        navigator.clipboard.writeText(number).then(() => {
          const originalText = this.innerHTML;
          this.innerHTML = '<i class="bi bi-check-lg"></i> Copied!';
          setTimeout(() => {
            this.innerHTML = originalText;
          }, 2000);
        });
      }
    });
  });
});
