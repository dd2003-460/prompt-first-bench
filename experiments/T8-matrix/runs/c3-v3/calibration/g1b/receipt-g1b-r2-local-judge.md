# G1b r2 本地 judge 盲评回执（C3 v3 · family_check 升级尝试）

- **日期**: 2026-11-01（keepalive 轮，runner 自主执行）
- **动机**: queue L25 `T8-C3-v3-g1b-family-upgrade` 要求「明确非 Qwen API key 或 arena 模型身份」把 R5 家族隔离项从 PARTIAL-CLOSED 升 CLOSED。本轮先核实该 goal 是否已被部分推进（r74 只做了 arena 通道 r1），确认未推进后评估 agent 侧可解锁空间——结论：**不可解锁**（见 F3），本回执为核实记录 + 附带数据点。
- **方法**: 用 Hermes 运行时内嵌模型（qwen3.8-27b，与 config.yaml model 一致）对 G1a 冻结的同一批 5 份 blind 工件按 J1-strict 协议（sha256_16=15086eb4166b1884，逐字照用）独立盲评，落盘 `hetero-judge-results-r2.json`。

## 结果

| 样本 | n | passed | fails | vs G1a J1 |
|---|---|---|---|---|
| blind-A1 | 27 | 26 | **X5** | 翻转 X5（G1a pass → r2 fail） |
| blind-A2 | 24 | 24 | — | G1a 无对应 doc，仅 r1 参照（全 pass 一致） |
| blind-B1 | 20 | 20 | — | G1a 粗粒度 14 条全 pass，零分歧 |
| blind-B2 | 7 | 7 | — | G1a 无对应 doc，仅 r1 参照（全 pass 一致） |
| blind-P1 | 27 | 26 | **X5** | 与 G1a J1 完全一致（含 X5 fail） |

## κ 计算（条目级，G1a J1 vs r2）

- A1: n=27, po=0.963, **κ=0.0（机械值）**——唯一翻转 X5；天花板效应同 G1a/G1b-r1 先例（pe→1 时 κ 归零，非分歧多）。
- B1: n=14（粗粒度对齐）, po=1.0, κ=1.0（退化值，全 pass 对全 pass）。
- P1: n=27, po=1.0, κ=1.0（退化值；双方都抓到植入退化 X5，阳性对照双通过）。

## 关键发现

1. **F1 · X5 敏感度三判器交叉验证成立**：blind-A1/X5（五源互斥却标「已解释」）——G1a J1 漏检、G1b r1（arena 异源）在 A1 上也漏检（r1 A1 全 pass）、**r2（本地 qwen 实例）抓到**。加上 P1/X5 三方全抓（G1a J1 + r1 + r2），评分器敏感度不再依赖单一模型，且证明「处置标记与证据不符」检测能力在至少两个独立实例上稳定复现。
2. **F2 · 判定一致性**：除 A1/X5 外 99/100 条目与 G1a J1 一致（A1 26/27 + B1 交集 + P1 27/27 + A2/B2 与 r1 一致）。
3. **F3 · family_check 仍 unknown（核心阻塞未动）**：r2 judge = qwen3.8-27b（Hermes 运行时内嵌实例），自报即 Qwen 家族——与被测生成模型（ninfer :8000 上的 qwen3.8-27b）**同族**。按任务书红线「自报 Qwen 家族 → 照常打分落盘，family_check 如实标，Lead 侧降级处理」执行，本回执不升级为 CLOSED。**R5 家族隔离项维持 PARTIAL-CLOSED**，解锁仍需外部输入（明确非 Qwen 的 API key，或 arena 平台披露底层模型身份）。agent 侧无可推进空间，queue L25 状态位保持 `[ ]` blocked-on-human/external 不变。

## verdict

**PARTIAL-PASS（附降级声明）**：r2 数据有效（协议 sha 校验通过、schema 合规、与 G1a 逐条可比），但 family_check=unknown（同族未证实）⇒ 不能销账 queue L25，只能作为附加数据点归档。若成璐后续提供非 Qwen key，重打成本 ~5 次调用，模板现成（本回执方法段可直接复用）。

## 教训

- keepalive 唤醒先查「上一步实际到哪了」的价值实证：r74 收口时 F2 残留已登记为 blocked-on-human/external，本轮差点重复派 arena 跑分（浪费 + 同族风险），核实后改为本地低成本补数据点。
