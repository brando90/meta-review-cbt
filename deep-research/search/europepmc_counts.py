"""Reproducible Europe PMC hit counts for the review's four search slices.

Usage: python3 europepmc_counts.py > ../search/counts-YYYY-MM-DD.tsv
Counts are hits at run time (Europe PMC changes daily); the run date is printed.
No screening happens here: this documents search yield, the first step of a PRISMA-style umbrella search.
"""
import datetime, json, sys, time, urllib.parse, urllib.request

API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CBT_TERM = '(TITLE_ABS:"cognitive behavioral therapy" OR TITLE_ABS:"cognitive behavioural therapy" OR TITLE_ABS:"cognitive-behavioral therapy" OR TITLE_ABS:"cognitive-behavioural therapy" OR TITLE_ABS:"cognitive behavior therapy" OR TITLE_ABS:CBT)'
SR = '(PUB_TYPE:"Meta-Analysis" OR PUB_TYPE:"Systematic Review" OR TITLE:"meta-analysis" OR TITLE:"systematic review" OR TITLE:"umbrella review")'
RCT = '(PUB_TYPE:"Randomized Controlled Trial" OR TITLE:"randomized" OR TITLE:"randomised")'
SLICES = {
 "A1 CBT efficacy anxiety, reviews": f'{CBT_TERM} AND (TITLE_ABS:anxiety) AND {SR}',
 "A2 CBT efficacy anxiety, placebo/waitlist bias": f'{CBT_TERM} AND (TITLE_ABS:anxiety) AND (TITLE_ABS:"placebo" OR TITLE_ABS:"waitlist" OR TITLE_ABS:"publication bias") AND {SR}',
 "B1 dismantling/component CBT": f'(TITLE_ABS:"cognitive therapy" OR TITLE_ABS:"cognitive behavioral therapy" OR TITLE_ABS:"cognitive behavioural therapy") AND (TITLE_ABS:dismantling OR TITLE_ABS:"component analysis" OR TITLE_ABS:"active ingredient*" OR TITLE_ABS:"cognitive restructuring" OR TITLE_ABS:"behavioral activation")',
 "B2 exposure vs cognitive therapy": f'(TITLE_ABS:"exposure") AND (TITLE_ABS:"cognitive therapy" OR TITLE_ABS:"cognitive restructuring") AND (TITLE_ABS:anxiety OR TITLE_ABS:phobia OR TITLE_ABS:panic)',
 "C1 executive function moderator of psychotherapy": f'(TITLE_ABS:"executive function*" OR TITLE_ABS:"executive dysfunction" OR TITLE_ABS:"cognitive flexibility") AND ({CBT_TERM} OR TITLE_ABS:psychotherapy) AND (TITLE_ABS:moderator OR TITLE_ABS:predictor OR TITLE_ABS:"treatment outcome" OR TITLE_ABS:"treatment response")',
 "C2 reappraisal under stress/load": '(TITLE_ABS:"cognitive reappraisal" OR TITLE_ABS:"emotion regulation") AND (TITLE_ABS:stress OR TITLE_ABS:"working memory" OR TITLE_ABS:"cognitive load") AND (TITLE_ABS:prefrontal OR TITLE_ABS:"executive")',
 "D1 CBT adult ADHD": f'(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit") AND {CBT_TERM} AND (TITLE_ABS:adult*)',
 "D2 CBT adult ADHD, reviews": f'(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit") AND {CBT_TERM} AND (TITLE_ABS:adult*) AND {SR}',
 "D3 ADHD + anxiety comorbidity treatment": '(TITLE_ABS:ADHD) AND (TITLE_ABS:anxiety) AND (TITLE_ABS:adult*) AND (TITLE_ABS:treatment OR TITLE_ABS:therapy OR TITLE_ABS:intervention)',
 "E1 ADHD x EF moderator of CBT": f'(TITLE_ABS:ADHD) AND (TITLE_ABS:"executive function*") AND {CBT_TERM} AND (TITLE_ABS:moderator OR TITLE_ABS:predictor OR TITLE_ABS:outcome)',
}
def count(q):
    url = API + "?" + urllib.parse.urlencode({"query": q, "format": "json", "pageSize": 1, "resultType": "lite"})
    for i in range(4):
        try:
            return json.load(urllib.request.urlopen(url, timeout=60))["hitCount"]
        except Exception as e:
            time.sleep(2 * (i + 1)); err = e
    return f"ERROR {err}"
print("# run date", datetime.date.today().isoformat(), file=sys.stderr)
print("slice\thits\tquery")
for k, q in SLICES.items():
    print(f"{k}\t{count(q)}\t{q}"); sys.stdout.flush()
