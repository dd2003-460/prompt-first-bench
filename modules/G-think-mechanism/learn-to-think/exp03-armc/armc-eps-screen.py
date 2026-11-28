#!/usr/bin/env python3
# origin: ai · 2026-11-25 · armC/armC' 判读机械初筛（flip 词表 + ε_pred gold 轴）
# 定位: 机械初筛，非终判。flip 用 T3 原词表 (scores_v2.md L92-94, A/B 基线同口径可比);
#   ε_pred 用 gold 轴 pattern 命中——机械 0 命中 ⇒ 未对齐 gold(可下结论);
#   机械有命中 ⇒ 需同族判官确认结构对齐(lossless-criterion-operationalization.md 口径)。
# 判据冻结: preregistration.md 38e6b34d6 (flip/爬层/预言力/边界) +
#   lossless-criterion-operationalization.md (ε_pred = 预言与 gold 结构对齐)。
# 用法: python3 armc-eps-screen.py <raw_outputs.json> [<more.json> ...]
#   兼容两种结构: {meta, samples:[...]} (armC) 或 [...] (T2 raw_outputs_v2)
import json, re, sys

# T3 原词表 (modules/G-think-mechanism/think-trigger/exp-results/scores_v2.md L92-94, 逐字)
CHAOS = ['李雅普诺夫', 'Lyapunov', '混沌', '吸引子', '相空间', '初始条件', '指数发散',
         'logistic', 'lorenz', '分岔', 'SDIC']
DMECH = ['landscape', '非凸', 'loss', '损失曲面', '凸优化', '损失景观', '损失函数']
DINFO = ['先验', '后验', '贝叶斯', '信息量', '信息增益']

# ε_pred gold 轴 (D 后半段: "优化和信息量有关, 先验近似0有效/先验信息量大 → 差不多算出来")
GOLD_AXES = {
    '信息论轴(gold②)': r'(信息量|先验|prior|information content|互信息|贝叶斯)',
    '条件数/曲率轴': r'(条件数|condition number|曲率|Hessian).{0,150}(收敛|误差|稳定|难)',
    'batch/噪声轴': r'(batch|mini.batch|噪声方差).{0,120}(反比|置信|采样|平均)',
    '强凸/局部凸轴': r'(强凸|局部凸|正定).{0,120}(一阶|梯度|可行|准确|稳定)',
}


def samples_of(path):
    d = json.load(open(path))
    return d['samples'] if isinstance(d, dict) and 'samples' in d else d


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    for path in sys.argv[1:]:
        print(f"===== {path} =====")
        for s in samples_of(path):
            t = (s.get('content') or '') + '\n' + (s.get('reasoning') or '')
            arm = s.get('arm', '?')
            run = s.get('run', '')
            c_ch, c_dm, c_di = (sum(t.count(w) for w in ws) for ws in (CHAOS, DMECH, DINFO))
            flip = 1 if c_dm > c_ch else 0
            print(f"  {arm}{run}: 混沌={c_ch} D机制={c_dm} D信息论={c_di} → flip={flip}")
            hits = {name: len(re.findall(pat, t)) for name, pat in GOLD_AXES.items()}
            info_hits = hits['信息论轴(gold②)']
            eps_mech = 'HIT(需判官确认)' if info_hits else '0(未对齐gold②)'
            print(f"      ε_pred 机械: 信息论轴={info_hits} → {eps_mech} | 其他轴={ {k:v for k,v in hits.items() if 'gold' not in k} }")
            # 信息论轴命中上下文(判官确认用)
            for m in re.finditer(r'.{60}(信息量|先验|prior).{60}', t):
                print(f"      ctx: …{m.group(0)}…")
                break


if __name__ == '__main__':
    main()
