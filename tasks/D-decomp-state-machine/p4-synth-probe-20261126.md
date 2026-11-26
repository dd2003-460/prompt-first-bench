# P2 synth_only 探针重跑（判别实验：口径分离软规则够不够）

> origin: ai · 2026-11-26 18:45 · 纯执行任务卡（唯一指令来源）。

## 背景（sub 不需再查）

- nat 278 节点树失败 = P4 综合丢失（gold 要点 5：树内 verified 节点 N247 含「u=1%/天 → 每 100 天失效」口径，P4 答案未引用、全文「100 天」0 命中）。
- 已实施的修复：commit `26122880d` 在 `synthesize_answer` 两处 P4 prompt 加了「dwell vs 更新/失效间隔必须分别报告、禁止混用量纲」硬约束（软规则：两口径同时在场时必分别报告）。**未跑过验证**。
- 本探针 = 判别实验：用当前代码（含软规则）重跑 nat P4 综合。
  - **翻正**（答案出现 100 天口径 / 引用 N247 / judge 要点 5 → 1）= 软规则足够，候选 A（口径清单硬召回，`p4-recall-fix-20261126.md` §3）**不加**（奥卡姆）。
  - **翻不正** = 口径根本没进 prompt（LLM 压缩遗忘/截断丢弃）→ 候选 A 是对症修复，上报 Lead 实施。

## 执行步骤（严格按序）

1. **备份基线**：`cp experiments/stage-ablation/runs-s5-sm-nat-synth.json experiments/stage-ablation/runs-s5-sm-nat-synth-baseline-20261126.json`（原失败证据，必须保留）。
2. **跑探针**：`cd experiments/stage-ablation && python3 synth_only.py runs-s5-sm-nat.json nat`（约 7 次本地 LLM 调用，走 8787 常驻代理，预计 5-15 分钟；终端 timeout 给 1800s。它会**覆盖** runs-s5-sm-nat-synth.json——基线已在步骤 1 备份，放心跑）。
3. **脚本对照**（结构化产出走脚本落盘，不手打）：写 `/Users/a1-6/.hermes/cache/scratch/p4_probe_compare.py`，读 baseline 与新 synth.json 两份，输出 `/Users/a1-6/.hermes/cache/scratch/p4_probe_compare.json`：{old_points: judge 逐点, new_points: judge 逐点, flipped: [翻正的要点], regressed: [回退的要点], old_has_100day: bool, new_has_100day: bool, new_cites_N247: bool, old_answer_len, new_answer_len}。
4. **写回执** `experiments/stage-ablation/p4-synth-probe-20261126.md`（≤40 行）：§1 跑法一行（命令+耗时+调用次数）/ §2 新旧 judge 逐点对照表（从 compare.json 生成）/ §3 100 天口径与 N247 引用（bool+答案原文片段 ≤2 句）/ §4 结论一行（翻正=软规则足够 / 翻不正=需候选 A，附回退要点清单如有）。
5. `git add experiments/stage-ablation/runs-s5-sm-nat-synth-baseline-20261126.json experiments/stage-ablation/runs-s5-sm-nat-synth.json experiments/stage-ablation/p4-synth-probe-20261126.md && git commit -m 'probe(stage-ablation): P2 synth_only 判别实验——口径分离软规则重跑 nat P4, 要点5 翻正与否'`，**不 push**。

## 验收

- baseline 备份文件存在（md5 与跑前原文件一致）
- 新 synth.json 已更新（mtime 新于跑前）
- 回执 §1-§4 齐全，§4 结论明确（二选一，不许含糊）
- commit hash
- summary ≤5 行：judge 要点 5 旧→新 + 100 天口径出现与否 + 有无回退要点 + 结论（软规则够/需候选 A）+ commit hash

## 边界

- **不改任何 .py**（探针只跑现有代码）；不重跑 SM（synth_only 复用现有树）；不 push；不 stash/checkout
- 8787 = 常驻 vLLM 代理（node 31906），只用不杀；模型名旧新不一致由代理自动纠正（已验证），不用管
- 若 synth_only 跑挂（502/超时/traceback）：重试 1 次；再挂 → 落盘 traceback 到回执 §1 并上报，**不盲跑**（LLM 调用总上限 14 次）
