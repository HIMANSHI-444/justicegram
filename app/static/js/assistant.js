/**
 * JusticeGram AI Legal Assistant Interactions
 */

document.addEventListener('DOMContentLoaded', function () {
  const queryTextarea = document.getElementById('query_text');
  const assistantForm = document.getElementById('assistantForm');
  const submitBtn = document.getElementById('btnSubmitQuery');
  const charCounter = document.getElementById('charCount');
  const loadingIndicator = document.getElementById('loadingIndicator');
  const promptPills = document.querySelectorAll('.sample-prompt-pill');

  // Character counter
  if (queryTextarea && charCounter) {
    const updateCount = () => {
      const len = queryTextarea.value.length;
      charCounter.textContent = `${len} / 3000`;
      if (len > 2800) {
        charCounter.classList.add('text-danger');
      } else {
        charCounter.classList.remove('text-danger');
      }
    };
    queryTextarea.addEventListener('input', updateCount);
    updateCount();
  }

  // Sample prompt selection
  promptPills.forEach(pill => {
    pill.addEventListener('click', function (e) {
      e.preventDefault();
      const promptContent = this.getAttribute('data-prompt');
      if (queryTextarea && promptContent) {
        queryTextarea.value = promptContent;
        queryTextarea.focus();
        if (charCounter) {
          charCounter.textContent = `${promptContent.length} / 3000`;
        }
        // Smoothly scroll to the form
        queryTextarea.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });

  // Submit button loading state
  if (assistantForm && submitBtn) {
    assistantForm.addEventListener('submit', function () {
      if (queryTextarea && queryTextarea.value.trim().length > 0) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = `
          <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
          Analyzing Legal Problem...
        `;
        if (loadingIndicator) {
          loadingIndicator.classList.remove('d-none');
        }
      }
    });
  }

  // AI Categorization accuracy feedback buttons
  const feedbackBtns = document.querySelectorAll('.btn-ai-feedback');
  feedbackBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      const queryId = this.getAttribute('data-query-id');
      const isAccurate = this.getAttribute('data-accurate') === 'true';
      const container = document.getElementById('feedbackContainer');

      if (!queryId) return;

      fetch('/api/assistant/feedback', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({
          query_id: queryId,
          accurate: isAccurate
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success && container) {
          container.innerHTML = `
            <div class="alert alert-success py-2 px-3 small d-inline-flex align-items-center mb-0">
              <i class="bi bi-check-circle-fill me-2"></i>
              Thank you! Your feedback helps refine our AI categorization model.
            </div>
          `;
        }
      })
      .catch(err => console.error('Feedback error:', err));
    });
  });
});
