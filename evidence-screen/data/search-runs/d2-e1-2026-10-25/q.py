"""Europe PMC rerun of slices D2 and E1 from deep-research/search/counts-2026-10-21.tsv, with abstracts (resultType=core). Usage: python3 q.py OUTDIR"""
import json,urllib.request,urllib.parse,hashlib,sys,datetime,csv
out=sys.argv[1]
want={'D2','E1'}
Q={r[0].split()[0]:r[2] for r in csv.reader(open('deep-research/search/counts-2026-10-21.tsv'),delimiter='\t') if r[0].split()[0] in want}
res={};counts={}
for k,q in Q.items():
    u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q,'format':'json','resultType':'core','pageSize':100})
    b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'meta-review-cbt/0.2'}),timeout=90).read()
    open(f'{out}/{k}.json','wb').write(b)
    d=json.loads(b); counts[k]=d['hitCount']
    print(k,d['hitCount'],hashlib.sha256(b).hexdigest()[:12],len(d['resultList']['result']))
json.dump({'queries':Q,'counts':counts,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},open(f'{out}/receipt.json','w'),indent=1)
