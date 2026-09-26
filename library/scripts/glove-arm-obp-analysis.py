import csv, math
from collections import defaultdict

def load(p):
    with open(p, newline='') as f: return list(csv.DictReader(f))
poi, meta = load('/tmp/poi.csv'), load('/tmp/meta.csv')
m = {r['session_pitch']: r for r in meta}
rows=[]
for r in poi:
    k=r['session_pitch']
    if k in m:
        r=dict(r); r['user']=m[k]['user']; r['playing_level']=m[k]['playing_level']
        r['age_yrs']=m[k]['age_yrs']; rows.append(r)
print("joined pitches:", len(rows), " unique pitchers:", len({r['user'] for r in rows}))
pt=defaultdict(int)
for r in rows: pt[r['pitch_type']]+=1
print("pitch types:", dict(pt))
lv=defaultdict(int)
for r in rows: lv[r['playing_level']]+=1
print("playing level (pitches):", dict(lv))

def f(r,k):
    v=r.get(k,'')
    try: return float(v)
    except: return None

fb=[r for r in rows if r['pitch_type'].strip().upper() in ('FF','FB','FASTBALL')]
print("fastball pitches:", len(fb), "pitchers:", len({r['user'] for r in fb}))
sp=[f(r,'pitch_speed_mph') for r in fb]; sp=[x for x in sp if x]
def ms(x): 
    n=len(x); mu=sum(x)/n; sd=(sum((v-mu)**2 for v in x)/(n-1))**.5; return n,mu,sd
print("FB speed n/mean/sd: %d / %.2f / %.2f  min %.1f max %.1f"%(ms(sp)+(min(sp),max(sp))))
# per-pitcher means
def bypitcher(data, keys):
    agg=defaultdict(lambda: defaultdict(list))
    for r in data:
        for k in keys:
            v=f(r,k)
            if v is not None: agg[r['user']][k].append(v)
    out={}
    for u,d in agg.items():
        if all(k in d and d[k] for k in keys):
            out[u]={k: sum(d[k])/len(d[k]) for k in keys}
    return out

def pear(xs,ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    sx=(sum((a-mx)**2 for a in xs))**.5; sy=(sum((b-my)**2 for b in ys))**.5
    if sx==0 or sy==0: return 0.0
    return sum((a-mx)*(b-my) for a,b in zip(xs,ys))/(sx*sy)
def rank(v):
    idx=sorted(range(len(v)), key=lambda i:v[i]); r=[0]*len(v); i=0
    while i<len(v):
        j=i
        while j+1<len(v) and v[idx[j+1]]==v[idx[i]]: j+=1
        avg=(i+j)/2+1
        for k in range(i,j+1): r[idx[k]]=avg
        i=j+1
    return r
def spear(xs,ys): return pear(rank(xs),rank(ys))
def pval(r,n):
    if n<4: return float('nan')
    z=0.5*math.log((1+r)/(1-r))*math.sqrt(n-3)
    return 2*(1-0.5*(1+math.erf(abs(z)/math.sqrt(2))))
def critr(n,a):  # approx two-sided critical |r| via Fisher z
    from math import sqrt,exp
    # invert normal quantile
    def qn(p):
        # Acklam approx
        a_=[-3.969683028665376e+01,2.209460984245205e+02,-2.759285104469687e+02,1.383577518672690e+02,-3.066479806614716e+01,2.506628277459239e+00]
        b_=[-5.447609879822406e+01,1.615858368580409e+02,-1.556989798598866e+02,6.680131188771972e+01,-1.328068155288572e+01]
        c_=[-7.784894002430293e-03,-3.223964580411365e-01,-2.400758277161838e+00,-2.549732539343734e+00,4.374664141464968e+00,2.938163982698783e+00]
        d_=[7.784695709041462e-03,3.224671290700398e-01,2.445134137142996e+00,3.754408661907416e+00]
        pl=0.02425
        if p<pl:
            q=sqrt(-2*math.log(p)); return (((((c_[0]*q+c_[1])*q+c_[2])*q+c_[3])*q+c_[4])*q+c_[5])/((((d_[0]*q+d_[1])*q+d_[2])*q+d_[3])*q+1)
        if p<=1-pl:
            q=p-0.5; r2=q*q
            return (((((a_[0]*r2+a_[1])*r2+a_[2])*r2+a_[3])*r2+a_[4])*r2+a_[5])*q/(((((b_[0]*r2+b_[1])*r2+b_[2])*r2+b_[3])*r2+b_[4])*r2+1)
        q=sqrt(-2*math.log(1-p)); return -(((((c_[0]*q+c_[1])*q+c_[2])*q+c_[3])*q+c_[4])*q+c_[5])/((((d_[0]*q+d_[1])*q+d_[2])*q+d_[3])*q+1)
    z=qn(1-a/2)/sqrt(n-3); return (math.exp(2*z)-1)/(math.exp(2*z)+1)

GV=['glove_shoulder_horizontal_abduction_fp','glove_shoulder_abduction_fp','glove_shoulder_external_rotation_fp','glove_shoulder_abduction_mer']
OUT=['pitch_speed_mph','max_torso_rotational_velo','max_shoulder_internal_rotational_velo','elbow_varus_moment']

for label, data in (("ALL FASTBALLS", fb), ("FASTBALLS >=85 MPH", [r for r in fb if (f(r,'pitch_speed_mph') or 0)>=85])):
    P=bypitcher(data, GV+OUT)
    print("\n=== %s | pitcher-level, n pitchers = %d ==="%(label,len(P)))
    sps=[P[u]['pitch_speed_mph'] for u in P]
    print("   pitcher-mean FB speed: mean %.2f sd %.2f  range %.1f-%.1f"%(sum(sps)/len(sps),(sum((v-sum(sps)/len(sps))**2 for v in sps)/(len(sps)-1))**.5,min(sps),max(sps)))
    n=len(P)
    print("   crit |r| p<.05 = %.3f ; Bonferroni 16 tests p<.00313 = %.3f"%(critr(n,.05),critr(n,.05/16)))
    for g in GV:
        line=[]
        for o in OUT:
            xs=[P[u][g] for u in P]; ys=[P[u][o] for u in P]
            r=pear(xs,ys); rs=spear(xs,ys)
            line.append("%s r=%+.3f rs=%+.3f p=%.3f"%(o.replace('max_','').replace('_rotational_velo','_rv')[:22],r,rs,pval(r,n)))
        print("  %-42s %s"%(g,' | '.join(line)))

print("\n\n########## LINK 2: do the intermediate variables buy SPEED? ##########")
for label, data in (("ALL (n=100)", fb), (">=85 MPH", [r for r in fb if (f(r,'pitch_speed_mph') or 0)>=85])):
    P=bypitcher(data, ['pitch_speed_mph','max_torso_rotational_velo','max_shoulder_internal_rotational_velo','max_pelvis_rotational_velo'])
    n=len(P); print("\n-- %s  n pitchers=%d  crit|r|.05=%.3f"%(label,n,critr(n,.05)))
    for o in ['max_torso_rotational_velo','max_shoulder_internal_rotational_velo','max_pelvis_rotational_velo']:
        xs=[P[u][o] for u in P]; ys=[P[u]['pitch_speed_mph'] for u in P]
        print("   %-40s vs speed: r=%+.3f rs=%+.3f p=%.4f  R2=%.1f%%"%(o,pear(xs,ys),spear(xs,ys),pval(pear(xs,ys),n),100*pear(xs,ys)**2))

print("\n\n########## NAIVE PITCH-LEVEL vs CLUSTER-CORRECT (independence inflation) ##########")
sub=[r for r in fb if (f(r,'pitch_speed_mph') or 0)>=85]
for g in GV:
    xs=[f(r,g) for r in sub if f(r,g) is not None and f(r,'pitch_speed_mph') is not None]
    ys=[f(r,'pitch_speed_mph') for r in sub if f(r,g) is not None and f(r,'pitch_speed_mph') is not None]
    P=bypitcher(sub,[g,'pitch_speed_mph'])
    xa=[P[u][g] for u in P]; ya=[P[u]['pitch_speed_mph'] for u in P]
    print("  %-42s pitch-level n=%3d r=%+.3f p=%.3f  ||  pitcher-level n=%2d r=%+.3f p=%.3f"%(g,len(xs),pear(xs,ys),pval(pear(xs,ys),len(xs)),len(xa),pear(xa,ya),pval(pear(xa,ya),len(xa))))

print("\n\n########## NORMS + WITHIN-PITCHER RELIABILITY (>=85 mph subset) ##########")
print("  variable                                    n  mean     betwSD  withinSD  ICC(1)")
for g in GV+['max_torso_rotational_velo','shoulder_horizontal_abduction_fp','stride_length','arm_slot']:
    byp=defaultdict(list)
    for r in sub:
        v=f(r,g)
        if v is not None: byp[r['user']].append(v)
    byp={u:v for u,v in byp.items() if len(v)>=2}
    if not byp: continue
    means=[sum(v)/len(v) for v in byp.values()]
    allv=[x for v in byp.values() for x in v]
    gm=sum(allv)/len(allv)
    k=len(byp)
    # one-way random effects
    ni=[len(v) for v in byp.values()]
    n0=sum(ni)/k
    MSB=sum(len(v)*(sum(v)/len(v)-gm)**2 for v in byp.values())/(k-1)
    MSW=sum(sum((x-sum(v)/len(v))**2 for x in v) for v in byp.values())/(sum(ni)-k)
    icc=(MSB-MSW)/(MSB+(n0-1)*MSW) if (MSB+(n0-1)*MSW)!=0 else float('nan')
    bsd=(sum((m-sum(means)/k)**2 for m in means)/(k-1))**.5
    print("  %-42s %2d %8.2f %7.2f %8.2f %7.3f"%(g,k,gm,bsd,MSW**.5,icc))
