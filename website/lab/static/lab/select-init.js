document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var options = document.querySelectorAll('select:first-child option');
    var instances = M.FormSelect.init(elems, options);
  });