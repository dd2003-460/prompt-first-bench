# 复测判别：full run nat 树用探针宽关键词清单重测（Type B 诊断存疑）

> origin: ai · 2026-11-26 18:35 · 纯提取+小判断。任务卡是唯一指令来源。

## 要判别的矛盾

探针（obj-inject-probe-20261126.md）：OFF 臂（无 objective 注入）L2 长出 9/19 老化节点（1%/λ/失效/100 天级）。
诊断（nat-failure-mode-20261126.md）：full run（runs-s5-sm-nat.json，278 节点）老化 0 命中 → 判 Type B 维度盲区（根因=objective 未注入）。
矛盾：两臂都无注入，探针有命中、full run 没有。

候选解释（判别哪个，不许猜）：
- H1 口径伪影：诊断用窄 11 词清单（频率表专项词），探针用宽 10 词清单。full run 其实有老化表述节点，0 命中是清单伪影 → 真失败点在 P4 综合而非分解
- H2 L1 骨架差异：full run 的 L1（5 节点）没把 1%/天立成一等维度；探针 L1（4 节点，取自 sm-nat-r1）立了 → 失败在 L1 生成
- H3 采样方差：L1 相同、L2 采样不同

## 步骤

1. 写脚本到 `/Users/a1-6/.hermes/cache/scratch/remeasure_fullrun.py`：
   - 解析 `experiments/stage-ablation/runs-s5-sm-nat.json` → 全部节点 {id, level, claim}
   - 关键词清单**逐字取自** obj-inject-probe-20261126.md §2 那一行（频率表/频率计数/频率老化/aging/decay/衰减/100 天/1%/λ/失效/stale，以文件原文为准，先 read 该行）
   - 输出：总命中数 + 按 level 分布 + 前 10 个命中节点（id + claim 前 100 字）→ 写 `/Users/a1-6/.hermes/cache/scratch/remeasure_fullrun_result.json`
2. 同脚本提取 full run 的 L1 全部节点 claim（5 个）+ L2 全部节点 claim（23 个）→ 同 JSON
3. 解析 `/Users/a1-6/.hermes/cache/scratch/probe_obj_inject_result.json` → 探针 L1 的 4 节点 claim → 同 JSON
4. 对照（读 JSON 后人工判断，≤10 行文字）：full run L1 vs 探针 L1 覆盖的维度是否相同？full run L1 里有没有 1%/天更新率约束的一等表述？
5. 判定 H1/H2/H3（或"证据不足"），一行结论 + 证据
6. 在 `experiments/stage-ablation/obj-inject-probe-20261126.md` 末尾追加 `## §5 复测判别（full run 宽口径重测）`（≤25 行）：重测命中数/分层 + L1 对照表（两臂各一行概括）+ H 判定一行 + 对 Fix ① 的含义一行（Type B 是否仍是根因 / 修复 ① 是否对症）
7. `git add experiments/stage-ablation/obj-inject-probe-20261126.md && git commit -m 'analysis(stage-ablation): full run 宽口径重测——判别 Type B 诊断(H1 口径/H2 L1/H3 采样)'`，**不 push**

## 验收

- remeasure_fullrun_result.json 存在（含命中数/L1 对照）
- 报告 §5 存在且 H 判定明确（H1/H2/H3/证据不足 四选一）
- commit hash
- summary ≤6 行：重测命中数（总+分层）+ L1 是否同骨架 + H 判定 + 对 Fix ① 含义 + commit hash

## 边界

- 只读 pfb 内两个 json + scratch 两个文件；只写报告一个文件（追加 §5）+ scratch 脚本/JSON
- 不改 s5_state_machine.py / 不跑 LLM / 不 push / 不碰其他分支
