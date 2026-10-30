#!/usr/bin/env python3
"""Offline package snapshot checks; Python 3.9+, standard library only.
Run from any directory. Does not validate an actual exam dataset or model.
"""
import json,re,math,sys
from pathlib import Path
if sys.flags.optimize:
 raise SystemExit('Run without -O/PYTHONOPTIMIZE: assertions are required')
r=Path(__file__).resolve().parent
rows=[json.loads(x) for x in (r/'index.jsonl').read_text().splitlines()]
sources=json.loads((r/'sources.json').read_text());by={x['id']:x for x in rows};sb={x['id']:x for x in sources}
assert len(by)==len(rows)==65 and len(sb)==len(sources)==84
assert sum(x['stage']==1 for x in rows)==11
assert sum(x['stage']==2 for x in rows)==14
assert len({s['url'] for s in sources})==84
for s in sources:
 assert s['url'].startswith('https://') and s['used_for'] and s['checked_at']=='2026-10-30'
for x in rows:
 assert x['stage'] in (1,2,3,4,5) and x['schema_version']==1 and x['status']=='ready'
 assert x['scope']=={1:'general-fundamentals',2:'general-devices-process',3:'general-memory-operation',4:'general-packaging-reliability',5:'general-data-application'}[x['stage']]
 p=r/x['path'];assert p.is_file() and p.resolve().is_relative_to(r.resolve())
 t=p.read_text();assert x['id'] in t and x['title'] in t
 for field in ['aliases','keywords','source_ids','problem_signals','metrics']:assert x[field]
 for source in x['source_ids']:assert sb[source]['url'] in t
 for target in x['prerequisites']+x['related']:assert target in by and target!=x['id']
 for heading in ['## 혼동·적용 한계','## 과제에서 확인할 질문','## 출처']:assert heading in t
assert {x['path'] for x in rows}=={str(p.relative_to(r)) for d in ('fundamentals','devices-process','memory-operation','packaging-reliability','data-application') for p in (r/d).glob('*.md')}
def visit(i,stack):
 assert i not in stack,stack
 for j in by[i]['prerequisites']:visit(j,stack+[i])
for i in by:visit(i,[])
for p in r.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not target.startswith('https://'):assert (p.parent/target.split('#')[0]).exists(),(p,target)
queries=[('정전용량','F03'),('donor','F06'),('GiB','F07'),('MHz','F08'),('wafer','F09'),('NAND','F10'),('latency','F11'),('에너지','F04'),('공핍층','P01'),('Vth','P02'),('CMOS','P03'),('FEOL','P04'),('열산화','P05'),('ALD','P06'),('photoresist','P07'),('선택비','P08'),('implant','P09'),('CMP','P10'),('via','P11'),('overlay','P12'),('EPM','P13'),('particle','P14')]
assert sum(x['stage']==3 for x in rows)==13
queries += [('charge sharing','M01'),('rank','M02'),('tRCD','M03'),('tREFI','M04'),('MT/s','M05'),('charge trap','M06'),('OOB','M07'),('tPROG','M08'),('QLC','M09'),('read disturb','M10'),('SECDED','M11'),('WAF','M12'),('UBER','M13')]
assert sum(x['stage']==4 for x in rows)==15
queries += [('wide IO','H01'),('through silicon via','H02'),('interposer','H03'),('Cu-Cu','H04'),('TC-NCF','H05'),('CTE','H06'),('psi JT','H07'),('ESL','H08'),('KGD','H09'),('TDDB','H10'),('Human Body Model','H11'),('zero failure','H12'),('Weibull','H13'),('Arrhenius','H14'),('SAM','H15')]
assert sum(x['stage']==5 for x in rows)==12
queries += [('cardinality','D01'),('FPY','D02'),('Wilson','D03'),('UCL','D04'),('Cpk','D05'),('confounding','D06'),('asof','D07'),('GroupKFold','D08'),('precision','D09'),('RMSE','D10'),('novelty','D11'),('submission','D12')]
for query,want in queries:
 matches=[x['id'] for x in rows if query.casefold() in json.dumps(x,ensure_ascii=False).casefold()]
 assert want in matches,(query,matches)
stage1=[(6e-6/2e-3,.003),(1/2000,.0005),(20e-15*1,20e-15),(2*3,6),(1*8,8),(1e16*100**3,1e22),(16e9/8,2e9),(16e9/8/2**30,1.862645149230957),(8e9/8,1e9),(1/500e6,2e-9),(.5e-9/2e-9,.25),(100e6/2e9,.05)]
stage2=[(0-2,-2),(1.2-.4,.8),(1-.4,.6),(1.2-.4-.3,.5),(.1*10e-12*1**2*100e6,.0001),(.8**2,.64),(10-8,2),((10-8)/8,.25),(.08*100,8),(8/10,.8),(10*2,20),(100/10,10),(200/100,2),(10*2,20),(100e-7,1e-5),(1e13/1e-5,1e18),((120-90)/30,1),(2e-8*10e-6/(.01*1e-12),20),(32-30,2),(math.hypot(3,4),5),(90/100,.9),(95/100,.95),((50-10)/50,.8)]
stage3=[((20*1+180*.5)/200,.55),(.55-.5,.05),((20*0+180*.5)/200,.45),(8*8,64),(24*.625,15),(15+15,30),(15+15+15,45),(math.ceil(14/.625),23),(23*.625,14.375),(300/7500,.04),(3200e6*64/8,25.6e9),(8*64/8,64),(8/3.2e9,2.5e-9),(16/25.6,.625),(4*1024*128,512*1024),(4*1024*128*1000/2**20,500),(4096/200e6,20.48e-6),(50e-6+4096/200e6,70.48e-6),(2**3,8),(2**3-1,7),(2**4,16),(2**4-1,15),(1e6*3,3e6),(1e6*4,4e6),(4e6/3e6,4/3),(8/64,.125),(8/72,1/9),(25/10,2.5),(200/1e8,2e-6)]
assert 22*.625 < 14 <= 23*.625
assert round(4096/(70.48e-6)/1e6,2)==58.12
assert .5 < 1.2 < 2 # illustrative NAND threshold decision
for actual,expected in stage1+stage2+stage3:assert math.isclose(actual,expected,rel_tol=1e-12,abs_tol=0),(actual,expected)
assert 1-.4 >= 1.2-.4-.3 # NMOS saturation under stated model
for a in (0,1):
 for b in (0,1):assert (a^b)==int(a!=b)
stage4=[(16*2**30*8/8/2**30,16),(1024*4e9/8,512e9),(4*512e9,2.048e12),(50/5,10),(2e-8*50e-6/(math.pi*(2.5e-6)**2),.0509295817894065),((10/5)**2,4),(2/100,.02),(12e-6*100,.0012),(.0012*10e-3,12e-6),(40+5*6,70),(65+5*1,70),(5*.002,.01),(.2e-9*(.1/1e-9),.02),(.03/2,.015),(.99**8*.98,.9042898005393617),(.001/(.1*1e-8),1e6),((.33-.30)*1e3,30),(1000*.5,500),(2/1e6*1e9,2000),(math.exp(-2e-6*1000),.9980019986673331),(-math.log(.05)/1e6*1e9,2995.732273553991),(math.exp(-(.5)**2),.7788007830714049),(1000*math.sqrt(math.log(2)),832.5546111576977),(1-math.exp(-1),.6321205588285577),(55+273.15,328.15),(125+273.15,398.15),(math.exp(.7/8.617333262e-5*(1/328.15-1/398.15)),77.6453820553027)]
for actual,expected in stage4:assert math.isclose(actual,expected,rel_tol=1e-12,abs_tol=0),(actual,expected)
# Check reported rounded values against the actual published examples.
for i,values in {'H02':['0.05093'],'H09':['0.90429','90.43%'],'H12':['0.998002','2995.73'],'H13':['0.778801','832.55'],'H14':['77.65','7765']}.items():
 body=(r/by[i]['path']).read_text()
 for v in values:assert v in body,(i,v)
assert round(stage4[-1][0]*100)==7765
assert math.isclose(math.exp(-(-math.log(.05)/1e6)*1e6),.05)
def af(use,stress):return math.exp(.7/8.617333262e-5*(1/use-1/stress))
assert af(328.15,328.15)==1 and af(328.15,398.15)>1
assert math.isclose(af(328.15,398.15)*af(398.15,328.15),1)
for t in (100,500,1000):assert math.isclose(math.exp(-(t/1000)**1),math.exp(-.001*t))
print(f'PASS: {len(rows)} cards, {len(sources)} sources, IDs/links/references/acyclic prerequisites, {len(queries)} retrieval routes, {len(stage1)+len(stage2)+len(stage3)+len(stage4)} numeric checks, rounded examples, zero-failure bound, AF direction and Weibull exponential boundary')

# Execute synthetic multi-step examples, including intentionally invalid inputs.
import runpy
checks=runpy.run_path(str(r/'checks'/'application_checks.py'))
n=checks['run_checks']()
print(f'PASS: {n} synthetic application tests; no actual Probe/model validation')
