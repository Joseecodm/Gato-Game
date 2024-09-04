const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav a');

const activateSection = (sectionId) => {
  sections.forEach(section => section.classList.remove('active'));
  document.getElementById(sectionId).classList.add('active');
}

navLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const sectionId = event.target.getAttribute('href').substring(1);
    activateSection(sectionId);
  });
});
