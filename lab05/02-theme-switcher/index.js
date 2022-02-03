document.querySelectorAll('button').forEach((element) => {
   element.addEventListener('click', function(event) {
      document.querySelector('body').className = event.target.id
   })
})
