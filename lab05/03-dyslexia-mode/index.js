const DYSLEXIA_MODE_TAG = 'dyslexia-mode'

document.addEventListener('DOMContentLoaded', function() {
  dyslexiaMode = localStorage.getItem(DYSLEXIA_MODE_TAG)
  if (dyslexiaMode === null) {
    localStorage.setItem(DYSLEXIA_MODE_TAG, 'default')
  }
  else {
    document.querySelector('body').className = dyslexiaMode
  }
})

document.querySelector('button').addEventListener('click', function() {
  if (localStorage.getItem(DYSLEXIA_MODE_TAG) === 'default') {
    localStorage.setItem(DYSLEXIA_MODE_TAG, 'dyslexia-mode')
    document.querySelector('body').className = 'dyslexia-mode'
  }
  else {
    localStorage.setItem(DYSLEXIA_MODE_TAG, 'default')
    document.querySelector('body').className = 'default'
  }
})
