const checkbox = document.getElementById('lgpd');
const botao = document.getElementById('contact');

checkbox.addEventListener('change', () => {
  if (checkbox.checked) {
    botao.classList.remove('disabled');
  } else {
    botao.classList.add('disabled');
  }
});
