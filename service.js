(() => {
 const buttons=[...document.querySelectorAll('.service-tabs button')];
 const records=[...document.querySelectorAll('.service-record')];
 const groups=[...document.querySelectorAll('.service-group')];
 const search=document.querySelector('#service-search');
 let selected=null;
 function render(){
  const query=search.value.trim().toLocaleLowerCase();let count=0;
  for(const r of records){r.hidden=!!((selected&&r.dataset.category!==selected)||(query&&!r.textContent.toLocaleLowerCase().includes(query)));if(!r.hidden)count++;}
  for(const g of groups)g.hidden=![...g.querySelectorAll('.service-record')].some(r=>!r.hidden);
  for(const b of buttons)b.setAttribute('aria-pressed',String(b.dataset.category===selected));
  const label=selected?buttons.find(b=>b.dataset.category===selected).textContent:'전체';
  document.querySelector('#service-count').textContent=`${label} · ${count}개 항목`;
  document.querySelector('#service-empty').hidden=count!==0;
 }
 for(const b of buttons)b.addEventListener('click',()=>{selected=selected===b.dataset.category?null:b.dataset.category;render();});
 search.addEventListener('input',render);
 document.querySelector('form.filters').addEventListener('reset',()=>{selected=null;search.value='';render();});
 render();
})();