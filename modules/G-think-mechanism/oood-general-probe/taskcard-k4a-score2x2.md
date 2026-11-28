# 任务卡 K4a — 2×2 六臂机械记分（指标抽取 + gold unit 批判）
> 纯执行 sub。本卡是唯一指令来源。零改动生产文件。git commit 由你做。
> 前置: K2 完成（s1-sm-arm.json）+ K3 完成（k3-s0-hw.json/k3-s1-hw.json/k3-baseline-hw.txt）。缺一即停并汇报缺哪项。
> 目的: 给 K4b（Lead 判决）提供全部机械指标。你只抽指标+做批判，不做 transfer/handcrafted 判决。

## 输入（只读）
| 臂 | 文件 | 域 |
|---|---|---|
| S0 气象 | `experiments/stage-ablation/oood-probe/sm-arm.json` | 气象 |
| B 气象 | `experiments/stage-ablation/oood-probe/baseline-arm.txt` | 气象 |
| S1 气象 | `experiments/stage-ablation/oood-probe/s1-sm-arm.json` | 气象 |
| S0 硬件 | `experiments/stage-ablation/oood-probe/k3-s0-hw.json` | 硬件 |
| S1 硬件 | `experiments/stage-ablation/oood-probe/k3-s1-hw.json` | 硬件 |
| B 硬件 | `experiments/stage-ablation/oood-probe/k3-baseline-hw.txt` | 硬件 |
| P2 已有 | `experiments/stage-ablation/oood-probe/metrics-s0-cyclone.json` | （复用，不重算） |
| Q9 gold | `modules/B-pipeline-ablation/data/gold-q9-units.json`（37 units, 字段 unit_id/text/kind/weight/gate） | 硬件判据 |

## S1 写脚本 `oood-probe/score_k4a.py`（机械指标层）
对 6 臂各抽:
- `n_nodes`(SM 臂) / `chars`(B 臂) / `wall_sec` / `final_state`(SM)
- `status_dist`: {verified, degraded, pending}(SM 臂)
- `quant_claims`: claim 全文(或 B 臂全文)中含"数值+单位"的正则命中条数（单位: kt, km/h, %, W/m², W, MW, GW, hPa, °C, $, /h, /s, tok/s, GB, MB, TB, ms, s, h, 倍, x, 亿, 万, 节点, 层 等; 数值=[0-9]+(\.[0-9]+)?）
- `l1_claims`: L1 节点 claim 列表(SM 臂)
- `llm_calls`: 从对应 .log grep "call done" 计数（sm-arm.log / s1-sm-arm.log / k3-hw3.log 按臂段切分; B 臂=1）

## S2 气象列机制覆盖（4 机制 × 3 臂）
gold 4 机制（与 P2 同口径）: ①能量源丧失(潜热/热通量/能量/蒸发) ②地表摩擦(摩擦/粗糙) ③垂直风切变(切变) ④流出阻塞(辐散/流出/阻塞)。
对 S0/S1/B 三臂: 把该臂全部 claim 拼串（B 臂=全文），4 组关键词匹配 → `mech_hits[臂][机制]=true/false` + 命中片段。
**同义词人工复核位**: 匹配 false 的项，在 `mech_review[臂][机制]` 写一句"是否疑似同义表述+claim id"，不改判。

## S3 硬件列 gold unit 覆盖（37 units × 3 臂, LLM 批判）
用 `ablation_harness.call_llm`（temperature=0）批判:
- 每批 10 个 unit（37 units → 4 批: 10/10/10/7）
- prompt 模板: "你是判分员。下面是一道题的 gold 要点清单(10条)和一个候选答案(40个事实节点拼接)。逐条判断候选答案是否实质覆盖该要点(覆盖=1, 未覆盖或答错=0, 部分覆盖=0 并在 reason 说明)。输出 JSON: {\"scores\":[0/1...], \"reasons\":[每条≤20字...]}。要点清单: {units}。候选答案: {claims_concat}。"
- units 取 `text` 字段（截断 200 字/条）; claims_concat = 40 claim 全文拼接（截断 30000 字）
- 每臂每批 1 次 LLM 调用 → 3 臂 × 4 批 = 12 次调用
- 解析失败重试 1 次; 仍失败该批记 `parse_error` 不阻塞
- 产出: `unit_cov[臂] = {covered/37, unit_scores{}, reasons{}}`
- **gate units 单独计**: units 里 `gate=true` 的子集单独算覆盖率（`gate_cov[臂]`）

## S4 落盘 + commit
- `oood-probe/metrics-2x2.json`: 上述全部（6 臂指标 + 气象 mech + 硬件 unit_cov/gate_cov + P2 复用字段并入）
- 脚本 `score_k4a.py` 一起 commit
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech && git add experiments/stage-ablation/oood-probe/ && git commit -m "exp: K4a 2x2 六臂机械记分 (指标+气象4机制+硬件37unit批判)"
```

## 汇报（≤6 行）
1. 气象列: S0/S1/B 各 mech_cov(x/4) + quant_claims
2. 硬件列: S0/S1/B 各 unit_cov(x/37) + gate_cov
3. 6 臂 n_nodes/chars + llm_calls
4. parse_error 批次（若有）
5. metrics-2x2.json 路径 + commit hash
6. 任何异常（臂缺失/文件损坏/LLM 调用失败）

## 边界
- 不做 transfer/handcrafted 判决（K4b = Lead）
- 不碰生产文件 / run_q9_gated / checkpoints
- LLM 调用仅 S3 的 12 次（temperature=0），其余全机械
- 27b 输出上限: 全部结构化数据由脚本写盘, 你的输出流只放脚本代码+运行+6 行汇报
