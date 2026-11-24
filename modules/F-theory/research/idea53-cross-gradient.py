#!/usr/bin/env python3
"""#53 交叉梯度测量 — V_coarse vs V_fine 的条件互信息 (纯 math, 闭式, 不消融不重跑).

claim (#53): 深层节点对微架构级瓶颈判断的增量贡献 > 浅层枚举.
测量设计 (arena 82a67df96 第四轮核验):
  V_coarse (C) = 资源类标签, 词表可测 = SUPPLY∧JUDGE 命中 (is_bottleneck 词表).
  V_fine (F)   = 机制级判断, 27b judge 打标 = 节点含'具体哪一环'定位语言
                 (容量vs带宽 / issue rate vs decode width / 标量vs张量 / FP16vsFP4占比)
                 且给定量或方向性判断 (慢40%/占78%/瓶颈80%+). 仅列候选=0.
                 V_fine ⊆ V_coarse: 机制级瓶颈判定是瓶颈判定的精化子集,
                 C=0 节点 F=0.
两条梯度 (节点级二值闭式互信息, n=节点数, underpowered 不成立):
  ① I(L; C)      = Σ_k P(L_k)·[H(C) - H(C|L_k)]            各层对 coarse 的信息贡献
  ② I(L; F|C)    = Σ_c P(c)·Σ_k P(k|c)·[H(F|C=c) - H(F|C=c,L_k)]
                   各层对 fine 的 *条件* 信息贡献 (已知 coarse 后, 层还剩多少信息).
预测: 浅层主导 coarse (枚举资源类候选), 深层主导 fine-conditional (机制级定位).
生死线: fine-conditional 梯度是否随深度升 — 不升则 #53 claim 死.
数据: 三份 GPU run 树 (rep-scan 15树 n=3849 / t53b 18树 n=5497 / stage-ablation
      GPU域 n=18243) + V_fine 标签 (idea53-vfine-labels.json, 27b judge 打标).
落盘: idea53-cross-gradient.json + idea53-cross-gradient.md (一行结论).
"""
import importlib.util, json, math, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_spec = importlib.util.spec_from_file_location('c', os.path.join(HERE, 'idea53_common.py'))
c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(c)

VFINE_PATH = os.path.join(HERE, 'idea53-vfine-labels.json')
OUT_JSON = os.path.join(HERE, 'idea53-cross-gradient.json')
OUT_MD = os.path.join(HERE, 'idea53-cross-gradient.md')


def bintext(p):
    """二值熵 (bits). p 在 0/1 边界时熵为 0."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))

def load_fine():
    """V_fine 标签 {node_id: 0/1/None}. node_id = 'src#tree#sha1(text)[:12]'.
    与 idea53-vfine-label.py 的 collect_c1() 同键构造."""
    import hashlib
    labels = json.load(open(VFINE_PATH))
    return labels


def node_id(name, tid, text):
    import hashlib
    return hashlib.sha1((name + '|' + tid + '|' + text).encode()).hexdigest()[:12]


def collect_labeled():
    """返回 {源名: [(level, C, F), ...]} — 每节点 (层, V_coarse, V_fine).
    C=0 节点 F=0 (V_fine ⊆ V_coarse). judge 失败(None) 的 C=1 节点剔除 (不猜)."""
    labels = load_fine()
    trees = c.load_trees()
    out, n_drop = {}, 0
    for name, ts in trees.items():
        rows = []
        for tid, root, ns in ts:
            for nd in ns:
                t = c.text_of(nd)
                C = bool(c.SUPPLY.search(t) and c.JUDGE.search(t))
                if not C:
                    rows.append((nd['level'], 0, 0))
                    continue
                F = labels.get(node_id(name, tid, t))
                if F is None:
                    n_drop += 1
                    continue
                rows.append((nd['level'], 1, F))
        out[name] = rows
    return out, n_drop

def mi_layer_uncond(rows, label_idx):
    """I(L; X) 按层分解, X = rows[i][label_idx] (二值).
    返回 {层: {n, n_x, p_x, H_given, dH, P, contrib}}, 总 MI, H(X)."""
    n = len(rows)
    if n == 0:
        return {}, 0.0, 0.0
    pairs = [(r[0], r[label_idx]) for r in rows]
    levels = sorted({l for l, _ in pairs})
    n_x = sum(1 for _, x in pairs if x)
    p_x = n_x / n
    H_x = bintext(p_x)
    out, total = {}, 0.0
    for lv in levels:
        sub = [x for l, x in pairs if l == lv]
        n_lv = len(sub)
        p_lv_x = sum(sub) / n_lv
        H_given = bintext(p_lv_x)
        dH = H_x - H_given
        P_lv = n_lv / n
        contrib = P_lv * dH
        total += contrib
        out[lv] = dict(n=n_lv, n_x=sum(sub), p_x=p_lv_x, H_given=H_given,
                       dH=dH, P=P_lv, contrib=contrib)
    return out, total, H_x


def mi_layer_cond(rows):
    """I(L; F|C) 按层分解 (C=rows[i][1], F=rows[i][2]).
    I(L;F|C) = Σ_c P(c)·I(L;F|C=c) = Σ_c P(c)·Σ_k P(k|c)·[H(F|c) - H(F|c,k)].
    只在 C=1 子集上有信息 (C=0 时 F 恒 0, H(F|C=0)=0, 该分支贡献 0),
    所以实际 = P(C=1)·Σ_k P(k|C=1)·[H(F|C=1) - H(F|C=1,k)].
    返回 {层: {n_c1, n_f, p_f_given, H_given, dH, P_given_c1, contrib}}, 总 MI,
    H(F|C=1). 层在 C=1 子集中无节点 → 不出现 (P(k|c)=0)."""
    c1 = [r for r in rows if r[1] == 1]
    n_c1 = len(c1)
    if n_c1 == 0:
        return {}, 0.0, 0.0, 0
    n_f = sum(1 for r in c1 if r[2])
    p_f = n_f / n_c1
    H_f_given_c1 = bintext(p_f)
    p_c1 = n_c1 / len(rows)
    out, total = {}, 0.0
    levels = sorted({r[0] for r in c1})
    for lv in levels:
        sub = [r[2] for r in c1 if r[0] == lv]
        n_lv = len(sub)
        p_lv_f = sum(sub) / n_lv
        H_given = bintext(p_lv_f)
        dH = H_f_given_c1 - H_given
        P_given_c1 = n_lv / n_c1
        contrib = p_c1 * P_given_c1 * dH
        total += contrib
        out[lv] = dict(n_c1=n_lv, n_f=sum(sub), p_f_given=p_lv_f,
                       H_given=H_given, dH=dH, P_given_c1=P_given_c1,
                       contrib=contrib)
    return out, total, H_f_given_c1, n_c1

# ===PART4===

def depth_order(lv):
    return int(lv[1])

def main():
    data, n_drop = collect_labeled()
    out = {'n_dropped_unlabeled': n_drop, 'sources': {}}
    for name, rows in data.items():
        uc, i_c, h_c = mi_layer_uncond(rows, 1)   # I(L; C)
        cf, i_f, h_f, n_c1 = mi_layer_cond(rows)  # I(L; F|C)
        # 浅/深贡献份额: 浅=L1-L2, 深=L3+
        def share(d, deep_from=3):
            tot = sum(v['contrib'] for v in d.values())
            if tot <= 0:
                return None
            deep = sum(v['contrib'] for k, v in d.items() if depth_order(k) >= deep_from)
            return deep / tot
        out['sources'][name] = dict(
            n_nodes=len(rows), n_c1=n_c1,
            i_l_c=round(i_c, 6), i_l_f_given_c=round(i_f, 6),
            h_c=round(h_c, 6), h_f_given_c1=round(h_f, 6),
            per_layer_c=uc, per_layer_f_cond=cf,
            deep_share_c=share(uc), deep_share_f_cond=share(cf))
    json.dump(out, open(OUT_JSON, 'w'), ensure_ascii=False, indent=2)
    # 一行结论
    lines = []
    for name, s in out['sources'].items():
        dc, df = s['deep_share_c'], s['deep_share_f_cond']
        lines.append(f"{name}: I(L;C)={s['i_l_c']}b 深份额={dc}, "
                     f"I(L;F|C)={s['i_l_f_given_c']}b 深份额={df}")
    with open(OUT_MD, 'w') as f:
        f.write('#53 交叉梯度 (make-or-break): fine-conditional 深份额 > coarse 深份额 且随深度升 = claim 活\n\n')
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    print(f'[落盘] {OUT_JSON}')

if __name__ == '__main__':
    main()