from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'service_data.json').read_text(encoding='utf-8'))
CATS={'society':('학회·협회','Societies & Associations'),'editorial':('편집위원','Editorial Service'),'review':('장기평가·공공위원회','Review & Public Committees'),'international':('국제활동','International Service'),'award':('수상','Honors & Awards')}
esc=html.escape
sections=[]
for key,(label,en) in CATS.items():
 rows=[r for r in D['records'] if r['category']==key]
 cards=[]
 for r in rows:
  cards.append('<article class="service-record" data-category="'+key+'"><div class="service-main"><p class="organization">'+esc(r['organization'])+'</p><h3>'+esc(r['role'])+'</h3><p class="service-note">'+esc(r['note'])+'</p><details class="evidence"><summary>확인 근거</summary><ul>'+''.join('<li>'+esc(s)+'</li>' for s in r['sources'])+'</ul></details></div><p class="period"><span>기간 / 확인 연도</span>'+esc(r['period'])+'</p></article>')
 sections.append('<section class="service-group" data-category="'+key+'" aria-labelledby="heading-'+key+'"><div class="group-heading"><h2 id="heading-'+key+'">'+label+' <span>'+str(len(rows))+'</span></h2><p>'+en+'</p></div><div class="service-list">'+''.join(cards)+'</div></section>')
template=(ROOT/'service.template.html').read_text(encoding='utf-8')
replacements={'__COUNT__':str(len(D['records'])),'__DATE__':D['updated'],'__GROUPS__':''.join(sections),'__TABS__':''.join('<button type="button" data-category="'+k+'" aria-pressed="false" aria-controls="service-groups">'+v[0]+'</button>' for k,v in CATS.items())}
for key,val in replacements.items():template=template.replace(key,val)
(ROOT/'service.html').write_text(template,encoding='utf-8')
print('Built service.html:',len(D['records']),'records')
