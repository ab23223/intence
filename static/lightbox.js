// Simple Lightbox Functionality
document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll('a[data-lightbox]');
  const lightboxContainer = document.createElement('div');
  const lightboxImage = document.createElement('img');

  lightboxContainer.id = 'lightbox';
  lightboxContainer.appendChild(lightboxImage);
  document.body.appendChild(lightboxContainer);

  links.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const src = link.getAttribute('href');
      lightboxImage.src = src;
      lightboxContainer.classList.add('active');
    });
  });

  lightboxContainer.addEventListener('click', () => {
    lightboxContainer.classList.remove('active');
  });
});
