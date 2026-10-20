from pathlib import Path
import json,html,csv,io
ROOT=Path(__file__).resolve().parent
TYPES={'journal':'학술지 논문','conference':'학회 발표·논문','chapter':'저서·챕터','report':'보고서','preprint':'프리프린트','thesis':'학위논문','other':'기타·서지 확인'}
def esc(x):return html.escape(str(x or ''),quote=True)
def link(url,label,cls=''):
 if not url.startswith(('https://','http://')):return ''
 return f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)} ↗</a>'
INDEXING=json.loads((ROOT/'journal_indexing.json').read_text(encoding='utf8'))['journals']

def indexing(r):
 if r['type']!='journal':return '', ''
 meta=INDEXING[r['venue'].casefold()]
 badges=[]
 for key,label in [('scie','SCIE'),('scopus','Scopus')]:
  status=meta[key]
  suffix='' if status=='yes' else (' 아님' if status=='no' else ' 미확인')
  if key=='scie' and status=='no' and meta['wos']:suffix+=' · '+meta['wos']
  badges.append(f'<span class="index-badge {key} {status}">{esc(label+suffix)}</span>')
 sources=''.join(link(url,'출처 '+str(i+1)) for i,url in enumerate(meta['sources']))
 details=f'<details class="index-evidence"><summary>저널 등재 근거</summary><p>{esc(meta["checked"])} 확인 · 저널 단위 정보이며 발행 당시 또는 개별 논문의 수록 여부는 별도 확인이 필요합니다. {esc(meta["note"])}</p><p>{sources}</p></details>'
 return ''.join(badges),details

def card(r):
 badges,evidence=indexing(r)
 venue=' · '.join(filter(None,[r['venue'],('Vol. '+r['volume']) if r['volume'] else '',('No. '+r['issue']) if r['issue'] else '',r['pages']]))
 notes=''.join('<li>'+esc(n)+'</li>' for n in r['notes'])
 sources=' '.join(link(s['url'],s.get('label','Scholar')+(' '+str(i+1) if len(r['sources'])>1 else '')) for i,s in enumerate(r['sources']))
 return f'''<article class="paper" data-year="{r['year'] or 'unknown'}" data-type="{r['type']}" data-review="{str(r['review']).lower()}">
 <div class="paper-top"><div class="paper-tags"><span class="type">{TYPES[r['type']]}</span>{badges}</div><span class="date">{esc(r['date'] or '연도 미상')}</span></div>
 <h3>{esc(r['title'])}</h3><p class="authors">{esc(r['authors'])}</p><p class="venue">{esc(venue or '게재처 확인 중')}</p>
 <div class="links">{link(r['url'],'DOI / 원문' if r['doi'] else '논문 보기')}{sources}</div>
 {evidence}
 {('<details class="record-notes"><summary>서지 확인 사항</summary><ul>'+notes+'</ul></details>') if notes else ''}
 </article>'''
def build():
 d=json.loads((ROOT/'papers_data.json').read_text(encoding='utf8'));records=d['records'];papers=[r for r in records if not r['review']];review=[r for r in records if r['review']]
 years=sorted({r['year'] for r in papers if r['year']},reverse=True)
 groups=''
 for year in [*years,None]:
  group=[r for r in papers if r['year']==year]
  if group:groups+=f'<section class="year-group" aria-label="{year or "연도 미상"}"><h2>{year or "연도 미상"}<span>{len(group)}개 항목</span></h2><div class="paper-list">'+''.join(card(r) for r in group)+'</div></section>'
 template=(ROOT/'papers.template.html').read_text(encoding='utf8')
 replacements={'__COUNT__':str(len(papers)),'__JOURNAL__':str(sum(r['type']=='journal' for r in papers)),'__SOURCE_COUNT__':str(d['source_count']),'__PROFILE__':esc(d['profile']),'__DATE__':d['retrieved'],'__YEARS__':''.join(f'<option value="{y}">{y}</option>' for y in years)+'<option value="unknown">연도 미상</option>','__TYPES__':''.join(f'<option value="{k}">{v}</option>' for k,v in TYPES.items()),'__GROUPS__':groups,'__REVIEW__':''.join(card(r) for r in review)}
 for key,value in replacements.items():template=template.replace(key,value)
 (ROOT/'papers.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf8')
 with (ROOT/'papers.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(['Title','Authors','Year','Date','Type','Venue','Volume','Issue','Pages','DOI','URL','Review required','Bibliographic sources'])
  for r in records:w.writerow([r['title'],r['authors'],r['year'],r['date'],TYPES[r['type']],r['venue'],r['volume'],r['issue'],r['pages'],r['doi'],r['url'],r['review'],' | '.join(s['url'] for s in r['sources'])])
if __name__=='__main__':build()
