# P4 口径分离修复（decomp + 任务表）

> origin: ai · 2026-11-26 · 依据 `experiments/stage-ablation/state-machine-status-20261126.md` §3 nat 根因诊断
> 根因（节点级证据）：nat 题要点 3/5 全 0 分——树里正确节点 N247（1/u=100 天更新间隔口径，verified）存在，但 P4 综合时选了 N28/N58/N60 的 T_res 驻留口径（1.5-3.7 天），把 dwell 和更新间隔混为一谈。

## 分解树

1. **P4 综合 prompt 口径分离**（本次执行）— 在 P4 综合 prompt 加硬约束：凡涉及"失效/老化/时间量级"的表述，必须区分并分别报告 ① dwell（对象在缓存/系统中的驻留时长）② 更新/失效间隔（内容多久后被替换），禁止混用同一量纲。
2. 树层概念冲突消解（decompose/verify prompt）— 下次迭代，与 1 正交但侵入更大，暂不做。
3. 8787 稳定窗口重跑 nat synth-multi — 依赖 t-repair1 arm（PID 28232）腾出 8787，本次不跑任何实验。

## 任务表

| # | 任务 | 执行 | 验收 |
|---|------|------|------|
| P1 | s5_state_machine.py P4 prompt 加口径分离约束 + 静态验证 + commit | sub | commit hash + 约束文本 grep 命中 + python 语法检查过 + 零实验运行 |

## 边界

- 只改 prompt 字符串，不改状态机逻辑/判定阈值
- 不跑实验（8787 被 t-repair1 占用，502/漂移风险）
- 不碰 runs/ 下 json，不 stash/checkout
