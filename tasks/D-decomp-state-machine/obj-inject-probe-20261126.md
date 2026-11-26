# 探针：--obj-inject 对 nat 早期窗口维度生长的实证验证

> origin: ai · 2026-11-26 · 验证 `objective-inject-fix-20261126.md`（commit edce50b28）的效果

## 要回答的问题（一个）

`--obj-inject` ON 时，nat 题的 **LFU 频率表老化/失效机制维度**（关键词：频率表/频率计数/频率老化/aging/decay/衰减/100 天/1%/λ/失效/stale）在**早期 decompose 窗口**（前 2-3 轮）能否长出节点？OFF 臂作为对照。

## 背景事实（sub 不需再查）

- nat 失败模式 = b 型维度盲区：full run（runs-s5-sm-nat.json，278 节点）中老化机制 0 节点承载；根因 = L1 objective 不进后续 prompt（现已修复，edce50b28 加 --obj-inject，默认 OFF）
- objective 可从 `checkpoints/sm-nat-r1/meta.json`（或 `checkpoints/sm-nat-r1.json`）的 `objective` 字段加载——**两臂共用同一个 objective**（控制 L1 变量）
- 启动方式参照：`SM_SEED=42 python3 s5_state_machine.py <qid> --obj-mode=formula --synth`（ablation_driver.sh:43）；`--obj-inject` 是 flags 解析（:1743）
- qid→question 走 `s5_pipeline.QUESTIONS`（nat/soc/gpu 三键，s8b_pilot 导入）
- 8787 可用（vLLM qwen3.8-27b-mtp，max_model_len 262144）
- **frontier 机制**（s5_state_machine.py:1250-1255）：max_depth 硬顶 + frontier 只取最深层——probe 里若 frontier 选择依赖 verified 状态，verify 环节不能整个跳过（需读代码确认后再定）

## 探针设计

| 项 | 设定 |
|----|------|
| 臂 | ON（--obj-inject）/ OFF（默认），其余全同 |
| qid | `nat-probe-on` / `nat-probe-off`（新 qid，checkpoint 不与 sm-nat-* 冲突） |
| objective | 两臂均从 sm-nat-r1 checkpoint 加载同一份（不重跑 L1，省 1 次调用且控制变量） |
| 规模上限 | max_nodes≈60 或前 3 轮 decompose（先到为准）；若 verify 环节必须保留，总 LLM 调用 ≤80 次 / ≤40 分钟 |
| seed | SM_SEED=42 两臂相同 |
| 判定 | 各臂节点 claim 文本 grep 老化关键词清单；**ON 命中且 OFF 未命中（或显著少）= 修复有效**；两臂都命中或都没命中 =  inconclusive，如实报告 |

## 执行步骤

1. 读 `checkpoints/sm-nat-r1/meta.json`（或 .json 单文件版）取 objective 原文
2. 读 s5_state_machine.py 的 run 主循环（grep `def run\|while\|frontier` 定位，~100 行），确认：probe 模式下最少要跑哪些环节、verify 是否影响 frontier 推进、如何限制轮数/节点数（改 cfg 或 monkeypatch，**不改仓内代码**——probe 逻辑全在 scratch 脚本里）
3. 写 probe 脚本到 `/Users/a1-6/.hermes/cache/scratch/probe_obj_inject.py`：构造两臂 SM 实例 → 注入同一 objective → 跑 decompose（+必要的 verify）→ 收集全部节点 {id, level, claim} → grep 关键词 → 结果落 `/Users/a1-6/.hermes/cache/scratch/probe_obj_inject_result.json`（脚本生成，不经模型输出流）
4. 跑脚本（若预计 >15 分钟：`setsid nohup python3 ... > log 2>&1 &` 后台跑，轮询 result.json 出现）
5. 落盘报告 `experiments/stage-ablation/obj-inject-probe-20261126.md`（≤60 行）：§1 探针设计（臂/控制/调用数实测）/ §2 结果（各臂节点数 + 老化关键词命中节点 id+claim 前 80 字）/ §3 判定（一行，有效/inconclusive/无效）/ §4 局限（规模小/单 seed/未跑 full verify）
6. `git add experiments/stage-ablation/obj-inject-probe-20261126.md && git commit -m 'analysis(stage-ablation): obj-inject 探针——nat 老化维度早期窗口生长验证(ON/OFF 对照)'`，**不 push**

## 验收

- result.json 存在且两臂节点数 >0
- 报告 §3 判定行明确（三选一）
- commit hash
- summary ≤6 行：两臂节点数 + 老化命中（各臂）+ 判定 + commit hash

## 边界

- 不改 s5_state_machine.py / s5_pipeline.py（probe 逻辑全在 scratch）；不碰 sm-nat-* checkpoint；不 push；不 stash/checkout/切分支
- 8787 有其他服务共用，probe 调用量控制在 ≤80 次；跑完即止不留后台进程

## 任务表

| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
|------|------|--------|--------|---------|------|
| 读主循环定 probe 切法 | - | ~100 | 0 | 0 | sub-27b |
| probe 脚本 + 跑两臂 | 上 | ~50 | 0(scratch) | 0 | sub-27b |
| 报告 + commit | 上 | result.json | ~60 | 1 | sub-27b |
