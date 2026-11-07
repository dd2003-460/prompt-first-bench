# T8-C3v3 rubric v3.2 replay — Lead 独立复算（不信 arena 自报）

> origin: ai · 2026-11-06 · Lead = Hermes qwen3.8-27b 会话
> 输入：`arena-hetero-judge-results-v32.jsonl`（arena 会话 01a1aee6 push，分支 `arena/2858680a-prompt-first-bench` @ 9046b35）vs `arena-hetero-judge-results-v31.jsonl`（基线）
> 工具：`validate_v32_replay.py`（6 项门禁）+ 本文件内联 python 复算（item 级配对、G2 spread、κ）

## 1. 完整性与一致性

- 36 行 / 18 cell / J1+J2 各 18，无重复 [A] PASS
- item 集合逐 cell 与 v3.1 **完全一致**（同 id 同数量）→ Δ 可比性成立
- 方法学红旗 [F]：无确定性脚本编码痕迹；但见 §4 的"同模型双角色"限制

## 2. 验收线核对（任务书口径）

| 验收项 | 判据 | 结果 |
|---|---|---|
| §6-A 围栏恢复 | 两 fence cell（v3.1 J1=0/31, 0/22）J1≥0.8 | **PASS**：均 1.0（31/31, 22/22） |
| §6-B 交叉引用 | 如实报告 | 6 cell（v3.1 亦 6；2 个移除 2 个新增——规则起了部分作用但未减少总数） |
| G2 spread ≥0.10 | per config/domain | **2/6**（v3.1 同口径也是 2/6；分布变了：v3.2 的 B-nofreeze/D2 与 B-none/D1 为 0.0） |
| κ（pooled item-level, n=401, tie-break N/A, 同模型双角色≠真 IRR） | 记录即可 | v3.2=0.559 vs v3.1=0.606 |

## 3. 条目加权通过率（pooled item-level, 非 cell 等权）

| 版本 | J1 | J2 | 备注 |
|---|---:|---:|---|
| v3.1 | 0.654 (262/401) | 0.805 (323/401) | 注意：summary-v31 曾记 0.638/0.798，与本 jsonl 复算差 ~1.6pp——以 jsonl 复算为准，旧 summary 数字存疑待核 |
| v3.2 | 0.886 (355/401) | 0.961 (385/401) | arena summary 记 351/380，差 4/5 条；Lead 复算以 jsonl 逐条计数为准 |

id 级翻转：J1 119/401、J2 77/401 —— 大量非围栏 cell 也发生翻转。

## 4. 关键限制（必须随分数一起引用）

1. **模型身份不可证**：jsonl 记 "Arena Agent Mode (model identity undisclosed)"。无法验证底层模型 ≠ 本地 Qwen 家族 → "异源"标签是平台自报，不是可证事实。
2. **同模型双角色**：J1/J2 由同一会话模型按两份 prompt 扮演 → κ=0.559 只是 rubric 间一致性，不是独立 judge 间 IRR。
3. **leniency drift 嫌疑**：11 个 cell 中 J1≡J2 全 item 一致（含全部 stage01 + B-none 三 cell）。严格/宽松两个角色在多数 cell 上没拉开差异，且整体通过率大幅上移（J1 +23.2pp），其中仅围栏修复可解释 ~1.5pp。**其余 ~21pp 提升无法归因于 rubric 改动本身**——更像 judge 漂移或工件解读变化。
4. **G2 未改善**：spread 达标数 2/6 → 2/6，且新出现两个 0.0 组（B-nofreeze/D2、B-none/D1），说明 J1/J2 在这些组上完全合流。

## 5. 结论

- **§6-A 围栏 bug 确认修复**（rubric 改动的直接目标达成，证据硬）。
- **"v3.2 整体质量提升"不能下**：分数大涨的主因不可归因，且 G2/κ 无改善、同模型限制未消除。
- 下一步若要坐实"异源可复现"，需要：(a) arena 披露或换用可标识模型族跑一遍；(b) 或接受当前数据只支持"rubric v3.2 修复了围栏判定 + 交叉引用规则部分生效"这一窄结论。
