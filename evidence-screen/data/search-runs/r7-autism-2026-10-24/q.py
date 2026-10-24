import json,urllib.request,urllib.parse,hashlib,sys,datetime
CBT='(TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT)'
AUT='(TITLE_ABS:autis* OR TITLE_ABS:"Asperger*")'
Q={
 'A1_autism_adult_trials': f'{AUT} AND TITLE_ABS:adult* AND {CBT} AND (TITLE_ABS:"randomi*" OR TITLE_ABS:"randomly" OR PUB_TYPE:"randomized controlled trial") AND FIRST_PDATE:[1900-01-01 TO 2026-10-24]',
 'A2_autism_cbt_reviews': f'{AUT} AND {CBT} AND (TITLE_ABS:"meta-analysis" OR TITLE_ABS:"systematic review") AND FIRST_PDATE:[1900-01-01 TO 2026-10-24]',
 'A3_autism_cbt_moderator': f'{AUT} AND {CBT} AND (TITLE_ABS:moderat* OR TITLE_ABS:predict* OR TITLE_ABS:"individual participant data" OR TITLE_ABS:"treatment response") AND FIRST_PDATE:[1900-01-01 TO 2026-10-24]',
 'A4_adhd_anxiety_adult_moderator': f'TITLE_ABS:(ADHD OR "attention deficit") AND TITLE_ABS:anxiety AND TITLE_ABS:adult* AND {CBT} AND (TITLE_ABS:moderat* OR TITLE_ABS:predict* OR TITLE_ABS:comorbid*) AND FIRST_PDATE:[1900-01-01 TO 2026-10-24]',
}
out={}
for k,q in Q.items():
    u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q,'format':'json','resultType':'lite','pageSize':100})
    b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'meta-review-cbt/0.2'}),timeout=60).read()
    open(f'r7/{k}.json','wb').write(b)
    d=json.loads(b); out[k]=d['hitCount']
    print(k,d['hitCount'],hashlib.sha256(b).hexdigest()[:12])
    for r in d['resultList']['result']:
        print('  ',r.get('pubYear'),r.get('id'),r.get('pubType','')[:30],'|',r['title'][:110])
json.dump({'queries':Q,'counts':out,'retrieved_utc':datetime.datetime.utcnow().isoformat()},open('r7/receipt.json','w'),indent=1)
