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

## P1 验收回执（2026-11-26 14:5x）

- commit `26122880d`：`s5_state_machine.py` + 本文件两文件，未 push，零实验，未碰 runs/ json。
- 约束加在 `synthesize_answer()` 两处 P4 prompt：逐层 `p`（L1607）+ merge `merge_p`（L1627），均在矛盾条款后、【问题】前；grep '口径分离' 命中 2 处。
- py_compile PASS；AST 探针确认拼串后约束位置正确、(a)/(b) 两量纲 + "禁止混用/不得覆盖" 文本完整。
- **调用链验证（关键）**：nat 重跑走 `synth_multi_soc.py`（L7 import + L44 调 `synthesize_answer`）与 `ablation_run_one.py`/`ablation_driver.sh`（`--synth`），**全程经 s5_state_machine.py 的 `synthesize_answer`**，不碰 s5_pipeline.py 平行 P4 路径（L1248 `P4_SYNTHESIZE` / L1260 分段）。→ 修复落在 nat 重跑实际路径上，有效。
- **遗留（正交，下次迭代）**：s5_pipeline.py 自身 P4 路径（`P4_SYNTHESIZE` + 分段 p/merge_p）无口径约束，若将来有 run 直接调 s5_pipeline.py P4 会复发同类混淆；与分解树第 2 条（decompose/verify 概念冲突消解）一并处理。
- **健壮性核查（约束 × 既有多数规则交互）**：merge_p/p 中既有规则「取多数一致的值并注明分歧」（L1626/L1606）在 T_res 节点 3 个 vs 100 天节点 1 个时，可能诱导以 T_res 为头条值；但 ①多数规则自带「注明分歧」→ 少数派口径必现；②本约束硬性「分别引用、不得覆盖」→ 100 天口径必现。原失败判分机制是 100 天口径**完全缺席**，现两口径必现 → 要点 5 判分翻正不受头条措辞影响。故不需再改 prompt（扩写超 Lead 批准文本 = scope creep）。

## 边界

- 只改 prompt 字符串，不改状态机逻辑/判定阈值
- 不跑实验（8787 被 t-repair1 占用，502/漂移风险）
- 不碰 runs/ 下 json，不 stash/checkout
