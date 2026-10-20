'use strict';
(() => {
 const search = document.getElementById('search');
 const year = document.getElementById('year');
 const type = document.getElementById('type');
 const cards = [...document.querySelectorAll('#groups .paper')];
 const groups = [...document.querySelectorAll('.year-group')];
 const normalize = text => text.normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
 const searchable = new Map(cards.map(card => [card, normalize(card.querySelector('h3').textContent + ' ' + card.querySelector('.authors').textContent + ' ' + card.querySelector('.venue').textContent)]));
 function filter() {
  const terms = normalize(search.value).split(' ').filter(Boolean);
  let count = 0;
  cards.forEach(card => {
   const matches = (year.value === 'all' || card.dataset.year === year.value) && (type.value === 'all' || card.dataset.type === type.value) && terms.every(term => searchable.get(card).includes(term));
   card.hidden = !matches; if (matches) count++;
  });
  groups.forEach(group => { const count = [...group.querySelectorAll('.paper')].filter(card => !card.hidden).length; group.hidden = count === 0; group.querySelector('h2 span').textContent = count + '개 항목'; });
  document.getElementById('result-count').textContent = count + ' / ' + cards.length + '개 항목';
  document.getElementById('no-results').hidden = count !== 0;
 }
 search.addEventListener('input', filter);year.addEventListener('change',filter);type.addEventListener('change',filter);
 document.querySelector('.filters').addEventListener('reset', () => { search.value='';year.value='all';type.value='all';filter(); });
 filter();
})();
