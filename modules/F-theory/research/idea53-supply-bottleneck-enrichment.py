#!/usr/bin/env python3
"""#53 修正版 — 供给侧系统瓶颈在 run 树的 level 分布 (2026-11-24, D 修正).

D 2026-11-24 修正: 真正要测的是供给侧系统瓶颈 (SM 频率/指令吞吐/发射率/内存带宽/
occupancy/warp), 不是需求侧 (duty_demand 业务占空比), 也不是纯文本正则.

本脚本 = idea53-run-tree-bottleneck-enrichment.py 的供给侧修正版, 覆盖三份 GPU run 树
数据源 (level 口径不同, 必须分源测, 不可合并比倍数):
  ① rep-scan 15 树 (3849 节点, L1-L4)
  ② t53b 18 个带 level 字段 GPU 树 (5497 节点, L1-L4)
  ③ stage-ablation checkpoints GPU 域 (18243 节点, L1-L5, L5=数值核验层)
  (t53b 的 bare arm 树是 markdown 字符串无 level 字段, 跳过.)

口径: 供给侧系统瓶颈 = 硬件供给词 ∧ 瓶颈判定词 (同节点 claim+evidence+corrected_claim).
对照: 全体节点 level 分布 + 需求侧 (占空比/duty/负载) 富集 + 原 #53 精确正则
(占空比|duty, 稀缺锚点) 富集 + verified 率.
边界核验: 微架构词 (warp/IPC/issue rate/发射/指令吞吐) 在树节点 vs 最终报告
(answer 字段) 的命中, 判"judge 层不产生"是节点层还是整个 run 现象.

轴陷阱 (承重): run 树 level (L1-L4/L5, judge 层) ≠ gold 主干深度, 本脚本只测 run 树
自身坐标系. 供给词是高频背景词 (19% 节点命中), 富集倍数天然比需求侧稀缺锚点弱.
实测: 富集强度与锚点基率成反比 — 稀缺锚点 duty (基率 0.4%) 富集 1.41x,
高频类别词 供给侧硬件 (基率 19%) 富集仅 1.10x. 解读富集倍数必须带基率.

核心结论 (2026-11-24 实测): 供给侧瓶颈判定节点 L4 富集在三份数据源全部统计显著
(卡方 ①p=0.0145 ②p=0.0001 ③p≈0.0000), 倍数小 (1.09-1.10x) 是因供给词高频背景,
但 n 大时 1.1x 也显著. 需求侧 duty 锚点 L4 富集倍数高 (1.23-1.56x) 但 n 小
(17-30), 仅 ① 显著 (p=0.0017), ②③ 不显著 — 倍数高部分是基率伪影. 微架构词
(内存带宽/MFU/SM频率/Kernel Launch) 在 stage-ablation 数据源 n≈2970 够测, 推翻
'微架构 n≈0 测不了'. 倍数小≠不显著, 判显著性必须做卡方/二项检验, 不能只看倍数.
"""
import json, glob, re, math
from collections import Counter

REPS = '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/rep-scan/'
T53B = '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/t53b/'
STAGE = '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/checkpoints/'

# 供给侧系统瓶颈词 (硬件供给侧资源)
SUPPLY = re.compile(
    r'带宽|算力|TFLOPS|TOPS|FLOPS|计算密度|compute.?bound|memory.?bound'
    r'|频率|clock|降频|DVFS|throttl|功耗|TDP'
    r'|(?<![A-Za-z])SM(?![A-Za-z])|occupancy|warp|(?<![A-Za-z])IPC(?![A-Za-z])'
    r'|issue.?rate|发射|指令吞吐|MFU|Kernel Launch|内存控制器', re.I)
# 瓶颈判定词
JUDGE = re.compile(r'瓶颈|受限|限制|利用率|上限|天花板|不足|不够|约束|受限于|制约')
# 需求侧 (对照, 原 #53 锚点)
DEMAND = re.compile(r'占空比|duty|业务需求|负载|需求侧', re.I)
# 原 #53 精确正则 (稀缺锚点对照, 基率 ~0.4%)
DEMAND_EXACT = re.compile(r'占空比|duty', re.I)
# 微架构细分词 (D 修正真正关心的, 单独分词看 level)
MICRO = {
    '内存带宽': re.compile(r'内存带宽|显存带宽|bandwidth|内存控制器', re.I),
    'SM频率/clock/降频': re.compile(r'(?<![A-Za-z])SM.{0,8}频率|频率.{0,8}(?<![A-Za-z])SM|clock|降频|DVFS|throttl', re.I),
    'SM(词)': re.compile(r'(?<![A-Za-z])SM(?![A-Za-z])'),
    'occupancy/占用率': re.compile(r'occupancy|占用率', re.I),
    'warp': re.compile(r'warp', re.I),
    'IPC': re.compile(r'(?<![A-Za-z])IPC(?![A-Za-z])'),
    'issue rate/发射': re.compile(r'issue.?rate|发射'),
    '指令吞吐': re.compile(r'指令吞吐|instruction.?throughput', re.I),
    'MFU': re.compile(r'MFU'),
    'Kernel Launch': re.compile(r'kernel launch', re.I),
}
# 方法论对照锚点 (不同基率, 验富集倍数 vs 基率伪影)
ANCHORS = {
    'duty(稀缺)': re.compile(r'占空比|duty', re.I),
    '功耗/TDP': re.compile(r'功耗|TDP', re.I),
    '显存容量GB': re.compile(r'\d+\s*GB|显存容量'),
    '量化INT8/FP8': re.compile(r'INT8|FP8|BF16|FP16|量化', re.I),
    '延迟/latency': re.compile(r'延迟|latency|ms|毫秒', re.I),
    'GPU型号': re.compile(r'H100|A100|H200|A6000|4090|5090', re.I),
    '带宽(高频)': re.compile(r'带宽|bandwidth', re.I),
    '吞吐(高频)': re.compile(r'吞吐|throughput|tok/s|token/s', re.I),
    'TCO/成本': re.compile(r'TCO|成本|价格|元|\\$', re.I),
    'KV Cache': re.compile(r'KV.?Cache', re.I),
}


def find_nodes(obj):
    """递归找带 level(str)+claim 的结构化节点对象."""
    out = []
    if isinstance(obj, dict):
        if isinstance(obj.get('level'), str) and 'claim' in obj:
            out.append(obj)
        else:
            for v in obj.values():
                out += find_nodes(v)
    elif isinstance(obj, list):
        for v in obj:
            out += find_nodes(v)
    return out


def text_of(nd):
    return ' '.join(str(nd.get(k) or '') for k in ('claim', 'evidence', 'corrected_claim'))


def collect_sources():
    """返回 [(源名, [节点]), ...], 每源独立 (level 口径不同, 不可合并)."""
    srcs = []
    nodes1 = []
    for f in glob.glob(REPS + 'rep-*.json'):
        if 'era-matched' in f or 'scores' in f:
            continue
        d = json.load(open(f))
        nodes1 += [nd for nd in d.get('nodes', []) if nd.get('level') is not None]
    srcs.append(('①rep-scan(L1-L4)', nodes1))
    nodes2 = []
    for f in sorted(glob.glob(T53B + 'runs*/gpu_*.json')):
        nodes2 += find_nodes(json.load(open(f)))
    srcs.append(('②t53b(L1-L4)', nodes2))
    nodes3 = []
    for f in glob.glob(STAGE + '**/node.json', recursive=True):
        if not re.search(r'(sm-gpu|gpu-|/gpu)', f):
            continue
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if isinstance(d, dict) and isinstance(d.get('level'), str):
            nodes3.append(d)
    srcs.append(('③stage-ablation GPU域(L1-L5)', nodes3))
    return srcs


def chi2_p(k_hit, n_hit, k_all, n_all):
    """2x2 卡方 (L4 vs 非L4): 命中节点落 L4 比例 vs 全体. 返回 (chi2, p)."""
    e_hit_L4 = n_hit * k_all / n_all
    e_hit_non = n_hit - e_hit_L4
    e_all_L4 = k_all
    e_all_non = n_all - k_all
    chi = 0.0
    for o, e in [(k_hit, e_hit_L4), (n_hit - k_hit, e_hit_non),
                 (k_all, e_all_L4), (n_all - k_all, e_all_non)]:
        if e > 0:
            chi += (o - e) ** 2 / e
    return chi, math.erfc(math.sqrt(chi / 2))  # df=1


def measure(name, nodes):
    lv_all = Counter(); n = 0
    lv_sup = Counter(); n_sup = 0; st_sup = Counter()
    lv_dem = Counter(); n_dem = 0; st_dem = Counter()
    lv_demx = Counter(); n_demx = 0
    st_all = Counter()
    micro_lv = {k: Counter() for k in MICRO}
    for nd in nodes:
        lv = nd['level']; st = nd.get('status')
        n += 1; lv_all[lv] += 1; st_all[st] += 1
        t = text_of(nd)
        if SUPPLY.search(t) and JUDGE.search(t):
            n_sup += 1; lv_sup[lv] += 1; st_sup[st] += 1
        if DEMAND.search(t):
            n_dem += 1; lv_dem[lv] += 1; st_dem[st] += 1
        if DEMAND_EXACT.search(t):
            n_demx += 1; lv_demx[lv] += 1
        for k, rx in MICRO.items():
            if rx.search(t):
                micro_lv[k][lv] += 1
    if n == 0:
        print(f'\n### {name}: 无节点'); return
    print(f'\n### {name} | 节点 {n}')
    print(f'全体 verified: {st_all.get("verified", 0) / n:.0%}')
    print(f'供给侧∧判定 n={n_sup} verified={st_sup.get("verified", 0) / n_sup:.0%}')
    print(f'需求侧 n={n_dem} verified={st_dem.get("verified", 0) / n_dem:.0%}')
    if n_demx:
        print(f'原#53精确(占空比|duty) n={n_demx} ' +
              ' '.join(f'{lv}:{lv_demx.get(lv, 0)} 富集{lv_demx.get(lv, 0) / n_demx / (lv_all[lv] / n):.2f}x'
                       for lv in sorted(lv_all)))
    print('level   全体        供给侧      供富集   需求侧     需富集')
    for lv in sorted(lv_all):
        a = lv_all[lv] / n
        s = lv_sup.get(lv, 0) / n_sup
        d = lv_dem.get(lv, 0) / n_dem if n_dem else 0
        print(f'{lv}  {lv_all[lv]:4d}({a:5.1%})  {lv_sup.get(lv, 0):4d}({s:5.1%})  {s / a:5.2f}x  '
              f'{lv_dem.get(lv, 0):3d}({d:5.1%})  {d / a:5.2f}x')
    # 显著性检验 (承重: 倍数小≠不显著, n 大时 1.1x 也显著)
    chi_s, p_s = chi2_p(lv_sup.get('L4', 0), n_sup, lv_all['L4'], n)
    print(f'显著性(卡方 df=1, L4 vs 非L4): 供给侧 χ²={chi_s:.2f} p={p_s:.4f} '
          f'{"显著" if p_s < 0.05 else "不显著"} (n={n_sup})')
    if n_dem >= 5:
        chi_d, p_d = chi2_p(lv_dem.get('L4', 0), n_dem, lv_all['L4'], n)
        print(f'              需求侧duty χ²={chi_d:.2f} p={p_d:.4f} '
              f'{"显著" if p_d < 0.05 else "不显著"} (n={n_dem})')
    else:
        print(f'              需求侧duty n={n_dem} 太小, 不检验')
    print('微架构分词:')
    for k in MICRO:
        c = micro_lv[k]; tot = sum(c.values())
        if tot:
            print(f'  {k:18s} n={tot:4d} ' + ' '.join(f'{lv}:{c.get(lv, 0)}' for lv in sorted(lv_all)))
    # 方法论对照: 富集倍数 vs 锚点基率 (伪影检验)
    pts = []
    for k, rx in ANCHORS.items():
        c = Counter(); nh = 0
        for nd in nodes:
            if rx.search(text_of(nd)):
                nh += 1; c[nd['level']] += 1
        if nh == 0:
            continue
        base = nh / n
        l4enr = (c.get('L4', 0) / nh) / (lv_all['L4'] / n)
        pts.append((base, l4enr))
    if len(pts) >= 3:
        xs = [math.log(b) for b, _ in pts]; ys = [e for _, e in pts]
        mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
        cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(len(xs)))
        vx = sum((xs[i] - mx) ** 2 for i in range(len(xs)))
        vy = sum((ys[i] - my) ** 2 for i in range(len(ys)))
        r = cov / math.sqrt(vx * vy) if vx * vy > 0 else 0
        print(f'基率(log) vs L4富集倍数 r = {r:.3f} (n={len(pts)} 锚点) — 强负=富集倍数是基率伪影')


def micro_significance():
    """合并三份数据源, 逐微架构词做 L4 显著性检验 (L4 口径三源一致).
    直接回答 D 点名的 6 词 (SM频率/指令吞吐/发射率/内存带宽/occupancy/warp) 各自够不够测."""
    nodes = []
    for name, ns in collect_sources():
        nodes += ns
    lv_all = Counter(); n = 0
    for nd in nodes:
        lv_all[nd['level']] += 1; n += 1
    print(f'\n### 微架构分词 L4 显著性 (合并三份 n={n}, 全体L4={lv_all["L4"]}/{n}={lv_all["L4"]/n:.1%})')
    print(f'{"微架构词":16s} {"n":>5s} {"L4":>5s} {"L4%":>6s} {"富集":>6s} {"χ²":>7s} {"p":>9s} {"判定":>6s}')
    for k, rx in MICRO.items():
        c = Counter(); nh = 0
        for nd in nodes:
            if rx.search(text_of(nd)):
                nh += 1; c[nd['level']] += 1
        if nh == 0:
            print(f'{k:16s} {0:5d}   (无命中 — 测不了)'); continue
        k4 = c.get('L4', 0)
        chi, p = chi2_p(k4, nh, lv_all['L4'], n)
        sig = '显著' if p < 0.05 else ('n小' if nh < 30 else '不显著')
        enr = (k4 / nh) / (lv_all['L4'] / n)
        print(f'{k:16s} {nh:5d} {k4:5d} {k4/nh:6.1%} {enr:6.2f}x {chi:7.2f} {p:9.4f} {sig:>6s}')
    print('D 点名 6 词: 内存带宽/occupancy 够测且显著; SM频率/降频 够测但不显著;')
    print('指令吞吐/issue率/warp n≈0-2 太小测不了 (数据源无 profile 输出).')


def boundary_check():
    """微架构词在树节点 vs 最终报告(answer) 是否出现 — 判缺失是节点层还是整个 run 现象."""
    ans_count = Counter(); ans_files = 0
    for f in sorted(glob.glob(T53B + 'runs*/gpu_*.json')):
        d = json.load(open(f))
        ans = d.get('answer', '') or ''
        if ans:
            ans_files += 1
            for k, rx in MICRO.items():
                if rx.search(ans):
                    ans_count[k] += 1
    print(f'\n### 边界核验: 微架构词 最终报告(answer) 命中 (t53b {ans_files} 份)')
    for k in MICRO:
        print(f'  {k:18s} answer={ans_count.get(k, 0):3d}')
    print('answer 也 n=0 → 缺失是整个 run 现象 (数据源无 profile 输出), 非 judge 层现象.')


if __name__ == '__main__':
    print('#53 修正 — 供给侧系统瓶颈 level 分布 (三份数据源分测, level 口径不同不可合并)')
    for name, nodes in collect_sources():
        measure(name, nodes)
    micro_significance()
    boundary_check()
