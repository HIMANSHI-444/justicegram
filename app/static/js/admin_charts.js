/**
 * JusticeGram Admin Dashboard Chart.js Visualizations
 */

document.addEventListener('DOMContentLoaded', function () {
  const categoryChartEl = document.getElementById('categoryDistributionChart');
  const lawyerTypeChartEl = document.getElementById('lawyerTypeChart');
  const inquiryStatusChartEl = document.getElementById('inquiryStatusChart');
  const confidenceChartEl = document.getElementById('confidenceDistributionChart');

  if (!categoryChartEl) return;

  fetch('/admin/api/stats')
    .then(res => res.json())
    .then(data => {
      // 1. Category Distribution (Doughnut Chart)
      if (categoryChartEl) {
        new Chart(categoryChartEl, {
          type: 'doughnut',
          data: {
            labels: data.categories.labels,
            datasets: [{
              data: data.categories.data,
              backgroundColor: [
                '#0d9488', '#14b8a6', '#0284c7', '#3b82f6', '#6366f1',
                '#8b5cf6', '#ec4899', '#f59e0b', '#10b981', '#64748b'
              ],
              borderWidth: 2,
              borderColor: '#ffffff'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'right',
                labels: { boxWidth: 12, font: { size: 11, family: 'Inter' } }
              }
            },
            cutout: '65%'
          }
        });
      }

      // 2. Lawyer Types (Pie Chart)
      if (lawyerTypeChartEl) {
        new Chart(lawyerTypeChartEl, {
          type: 'pie',
          data: {
            labels: data.lawyer_types.labels,
            datasets: [{
              data: data.lawyer_types.data,
              backgroundColor: ['#0d9488', '#1c2541'],
              borderWidth: 2,
              borderColor: '#ffffff'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'bottom',
                labels: { boxWidth: 12, font: { size: 11, family: 'Inter' } }
              }
            }
          }
        });
      }

      // 3. Inquiry Status (Bar Chart)
      if (inquiryStatusChartEl) {
        new Chart(inquiryStatusChartEl, {
          type: 'bar',
          data: {
            labels: data.inquiry_status.labels,
            datasets: [{
              label: 'Inquiries',
              data: data.inquiry_status.data,
              backgroundColor: ['#f59e0b', '#3b82f6', '#10b981', '#64748b'],
              borderRadius: 6
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false }
            },
            scales: {
              y: {
                beginAtZero: true,
                ticks: { stepSize: 1, font: { family: 'Inter' } },
                grid: { color: '#f1f5f9' }
              },
              x: {
                grid: { display: false },
                ticks: { font: { family: 'Inter' } }
              }
            }
          }
        });
      }

      // 4. AI Confidence Distribution (Bar Chart)
      if (confidenceChartEl) {
        new Chart(confidenceChartEl, {
          type: 'bar',
          data: {
            labels: data.confidence_distribution.labels,
            datasets: [{
              label: 'Queries',
              data: data.confidence_distribution.data,
              backgroundColor: '#0d9488',
              borderRadius: 6
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false }
            },
            scales: {
              y: {
                beginAtZero: true,
                ticks: { stepSize: 1, font: { family: 'Inter' } },
                grid: { color: '#f1f5f9' }
              },
              x: {
                grid: { display: false },
                ticks: { font: { family: 'Inter' } }
              }
            }
          }
        });
      }
    })
    .catch(err => console.error('Error fetching admin chart stats:', err));
});
