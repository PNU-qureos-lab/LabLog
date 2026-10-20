'use strict';
(() => {
 const search = document.getElementById('search');
 const year = document.getElementById('year');
 const tabs = [...document.querySelectorAll('[role="tab"]')];
 const panel = document.getElementById('publication-panel');
 const cards = [...document.querySelectorAll('#groups .paper')];
 const groups = [...document.querySelectorAll('.year-group')];
 let category = 'journal';
 const normalize = text => text.normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
 const searchable = new Map(cards.map(card => [card, normalize(card.querySelector('h3').textContent + ' ' + card.querySelector('.authors').textContent + ' ' + card.querySelector('.venue').textContent)]));
 const inCategory = card => category === 'other' ? !['journal','conference'].includes(card.dataset.type) : card.dataset.type === category;
 function filter() {
  const terms = normalize(search.value).split(' ').filter(Boolean);
  let count = 0;
  cards.forEach(card => {
   const matches = inCategory(card) && (year.value === 'all' || card.dataset.year === year.value) && terms.every(term => searchable.get(card).includes(term));
   card.hidden = !matches; if (matches) count++;
  });
  groups.forEach(group => { const count = [...group.querySelectorAll('.paper')].filter(card => !card.hidden).length; group.hidden = count === 0; group.querySelector('h2 span').textContent = count + '개 항목'; });
  document.getElementById('result-count').textContent = count + ' / ' + cards.filter(inCategory).length + '개 항목';
  document.getElementById('no-results').hidden = count !== 0;
  document.querySelector('.review-section').hidden = category !== 'other';
 }
 function activate(tab) {
  category = tab.dataset.category;
  tabs.forEach(item => { item.setAttribute('aria-selected', String(item === tab)); item.tabIndex = item === tab ? 0 : -1; });
  panel.setAttribute('aria-labelledby', tab.id);
  filter();
 }
 tabs.forEach((tab,index) => {
  tab.addEventListener('click', () => activate(tab));
  tab.addEventListener('keydown', event => {
   let next;
   if(event.key === 'ArrowRight') next = (index + 1) % tabs.length;
   else if(event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
   else if(event.key === 'Home') next = 0;
   else if(event.key === 'End') next = tabs.length - 1;
   else return;
   event.preventDefault(); tabs[next].focus(); activate(tabs[next]);
  });
 });
 search.addEventListener('input', filter);year.addEventListener('change',filter);
 document.querySelector('.filters').addEventListener('reset', () => { search.value='';year.value='all';filter(); });
 filter();
})();
