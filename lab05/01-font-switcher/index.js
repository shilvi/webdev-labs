const SCALE_FACTOR = 1.2

const getFontSize = (selector) =>
   parseFloat(window.getComputedStyle(document.querySelector(selector)).fontSize)

const makeBigger = () => {
   for (selector of ['h1', '.content']) {
      document.querySelector(selector).style.fontSize = `${getFontSize(selector) * SCALE_FACTOR}px`
   }
};

const makeSmaller = () => {
   for (selector of ['h1', '.content']) {
      document.querySelector(selector).style.fontSize = `${getFontSize(selector) / SCALE_FACTOR}px`
   }
};

document.querySelector('#a1').addEventListener('click', makeBigger);
document.querySelector('#a2').addEventListener('click', makeSmaller);
