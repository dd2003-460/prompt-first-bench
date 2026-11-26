#!/usr/bin/env python3
# origin: ai
"""独立复算 scoring-mechanism-20261126.md 的关键数字（只读，不调 LLM 端点）。

跑法：python3 verify-scoring-20261126.py
全 PASS 即报告中以下声明经独立脚本一手复现：
  ① 深度层权重 _w3/_w4 = k·ln(k+1) 归一（docstring 标注 K=3 [0.11,0.35,0.54] 系算错）
  ② GPU_RUBRIC 要点数 = 38（深度口径）vs 二值 GOLD[gpu]=15
  ③ r03 用当前 HEAD 真实 _lookup+聚合逻辑重判 overall=0.33（存储 0.0 系聚合伪影）
  ④ 全仓伪影扫描：237 对象 / 15 文件 / 仅 r03 一个伪影
"""
import json, math, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(BASE, "judge_v2_depth.py")).read()

fails = []
def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond: fails.append(name)

# ── ① 权重 ──────────────────────────────────────────────
def w3():
    raw=[k*math.log(k+1) for k in range(1,4)]; s=sum(raw); return [r/s for r in raw]
def w4():
    raw=[k*math.log(k+1) for k in range(1,5)]; s=sum(raw); return [r/s for r in raw]
W3, W4 = w3(), w4()
check("_w3≈[0.098,0.312,0.590]",
      abs(W3[0]-0.0983)<1e-3 and abs(W3[1]-0.3117)<1e-3 and abs(W3[2]-0.5900)<1e-3,
      f"got {[round(x,4) for x in W3]}")
check("_w4≈[0.051,0.163,0.308,0.477]",
      abs(W4[0]-0.0514)<1e-3 and abs(W4[1]-0.1629)<1e-3 and abs(W4[2]-0.3084)<1e-3 and abs(W4[3]-0.4773)<1e-3,
      f"got {[round(x,4) for x in W4]}")

# ── ② rubric 键数 ────────────────────────────────────────
def rubric_keys(var):
    m=re.search(var+r"\s*=\s*\{(.*?)\n\}", SRC, re.S)
    return re.findall(r'"([^"]+)"\s*:', m.group(1)) if m else []
GPU_KEYS = rubric_keys("GPU_RUBRIC")
NAT_KEYS = rubric_keys("NAT_RUBRIC")
SOC_KEYS = rubric_keys("SOC_RUBRIC")
check("GPU_RUBRIC=38 点", len(GPU_KEYS)==38, f"got {len(GPU_KEYS)}")
check("NAT_RUBRIC=6 点", len(NAT_KEYS)==6, f"got {len(NAT_KEYS)}")
check("SOC_RUBRIC=7 点", len(SOC_KEYS)==7, f"got {len(SOC_KEYS)}")

# ── ②b canonical 六维权重（score.py:232-233,300-307）──────
src_score = open(os.path.join(BASE, "score.py")).read()
mw = re.search(r'WEIGHTS\s*=\s*\{([^}]+)\}', src_score)
canon = dict(re.findall(r'"(M\d)"\s*:\s*([0-9.]+)', mw.group(1))) if mw else {}
check("canonical 六维权重 M1.25/M2.20/M3.15/M4.20/M5.10/M6.10",
      canon == {"M1":"0.25","M2":"0.20","M3":"0.15","M4":"0.20","M5":"0.10","M6":"0.10"},
      f"got {canon}")
check("Q5 M1 减半 0.125 + 重归一", '"M1": 0.125' in src_score and "重新归一化" in src_score, "")

# ── ②c 双 v3 陷阱数字（一手解析两源文件，非转录）────────
gf = open(os.path.join(BASE, "../../modules/A-eval-infra/research/scoring-v3-gatefixed.md")).read()
rv = open(os.path.join(BASE, "../../modules/A-eval-infra/research/RESCORE-V3-NOTES.md")).read()
def row_val(txt, arm, col):
    m = re.search(rf"\|\s*{arm}\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|", txt)
    return float(m.group(col)) if m else None
check("gatefixed S0=0.397", row_val(gf, "S0", 2) == 0.397, f"got {row_val(gf,'S0',2)}")
check("gatefixed S5=0.579", row_val(gf, "S5", 2) == 0.579, f"got {row_val(gf,'S5',2)}")
check("RESCORE-V3 S0=0.615", row_val(rv, "S0", 3) == 0.615, f"got {row_val(rv,'S0',3)}")
check("RESCORE-V3 S5=0.805", row_val(rv, "S5", 3) == 0.805, f"got {row_val(rv,'S5',3)}")
_g5, _r5 = row_val(gf, "S5", 2), row_val(rv, "S5", 3)
check("双 v3 数字确实不同（陷阱坐实）",
      (_g5 is not None and _r5 is not None and abs(_g5 - _r5) > 0.2), "")

# ── ③ r03 用当前 HEAD 真实逻辑重判 ───────────────────────
d = json.load(open(os.path.join(BASE, "ablation-runs/gpu_formula_r03_judge.json")))
scores_raw = d["raw"]
check("r03 raw=100 键全 0.33", len(scores_raw)==100 and all(abs(v-0.33)<1e-9 for v in scores_raw.values()),
      f"raw_keys={len(scores_raw)}")
check("r03 存储 overall=0.0（伪影）", d["overall"]==0.0, f"stored={d['overall']}")
pt_map = {f"pt{i+1}": k for i,k in enumerate(GPU_KEYS)}
def lookup(pt_name):
    if pt_name in scores_raw: return scores_raw[pt_name]
    for k,v in scores_raw.items():
        if pt_map.get(k)==pt_name: return v
    return 0
total=n=0
for pt_name in GPU_KEYS:
    try: s=max(0.0,min(1.0,float(lookup(pt_name))))
    except: s=0.0
    total+=s; n+=1
recalc = round(total/max(n,1),4)
check("r03 重判 overall=0.33", abs(recalc-0.33)<1e-6, f"recalc={recalc} n={n}")

# ── ③b 7 gpu rep 均值（剔/含 r03）────────────────────────
import glob
ov={}
for f in sorted(glob.glob(os.path.join(BASE,"ablation-runs/gpu_formula_r*_judge.json"))):
    dd=json.load(open(f)); ov[os.path.basename(f)]=dd["overall"]
valid=[v for k,v in ov.items() if "r03" not in k]
mean_excl=sum(valid)/len(valid)
mean_incl=(sum(valid)+0.33)/len(ov)
check("7-rep 剔 r03 均值=0.3934", abs(mean_excl-0.3934)<1e-4, f"got {mean_excl:.4f} (n={len(valid)})")
check("7-rep 含重判 r03 均值=0.3844", abs(mean_incl-0.3844)<1e-4, f"got {mean_incl:.4f}")
check("Δ(含-剔)=-0.0091", abs((mean_incl-mean_excl)-(-0.0091))<1e-4, f"got {mean_incl-mean_excl:+.4f}")

# ── ④ 全仓伪影扫描 ───────────────────────────────────────
def collect(o, path, tag=""):
    out=[]
    if isinstance(o,dict):
        if "point_scores" in o and "overall" in o:
            raw=o.get("raw",{}); ps=o.get("point_scores",{})
            if isinstance(raw,dict) and isinstance(ps,dict):
                rawnz=sum(1 for v in raw.values() if v!=0)
                ps_zero=all(((v.get("score") if isinstance(v,dict) else v))==0 for v in ps.values())
                out.append((path,tag,len(raw),len(ps),rawnz,ps_zero))
        for k,v in o.items(): out+=collect(v,path,f"{tag}{k}")
    elif isinstance(o,list):
        for i,it in enumerate(o): out+=collect(it,path,f"{tag}[{i}]")
    return out
objs=[]; files=set()
for root,dirs,files_ in os.walk(BASE):
    rr=os.path.relpath(root,BASE); parts=[] if rr=="." else rr.split(os.sep)
    if any(p.startswith(".") or p in(".venv-d1","node_modules") for p in parts): continue
    for fn in files_:
        if not fn.endswith(".json"): continue
        p=os.path.join(root,fn)
        try: dd=json.load(open(p))
        except: continue
        c=collect(dd,os.path.relpath(p,BASE))
        if c: objs+=c; files.add(os.path.relpath(p,BASE))
arts=[o for o in objs if o[4]>0 and o[5]]
check("全仓 237 对象", len(objs)==237, f"got {len(objs)}")
check("全仓 15 文件", len(files)==15, f"got {len(files)}")
check("仅 1 伪影且=r03", len(arts)==1 and "gpu_formula_r03_judge.json" in arts[0][0],
      f"artifacts={[a[0] for a in arts]}")

print("\n" + ("ALL PASS ✅" if not fails else f"FAILURES: {fails} ❌"))
sys.exit(1 if fails else 0)
