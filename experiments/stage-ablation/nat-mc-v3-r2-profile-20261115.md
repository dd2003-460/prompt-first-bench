# nat-mc-v3 r2 画像（2026-11-15 夜间提取）

> 来源：`experiments/stage-ablation/checkpoints/sm-nat-r2.json`（r2 ckpt，进程退出前未落 final json——同 r3/r5 模式：verify 阶段退出路径未走完落盘）
> qid=nat, objective_mode=method_challenge, round=2

## 核心数字

| 指标 | 值 | 备注 |
|---|---|---|
| 节点数 | 81 | |
| verified | 28 (34.6%) | 宽口径 |
| verified 中 logic-only | 25/28 (89.3%) | 无 retrieval_sources + "来源未直接覆盖" |
| degraded | 48 (59.3%) | |
| pending | 5 (6.2%) | |
| failed | 0 | |
| leaks | 0 | leak_hits_total=0 |
| rework_events | 52 | |
| contradiction_events | 3 | |
| edge_type | cartesian 43 / quotient 38 | **quotient 46.9% ⚠️ 远超 20% 阈值** |
| network_degraded | False | |

## 与 gpu 各臂对比（同口径）

| 臂 | n | verified(宽) | logic-only 占 verified | degraded | quotient 率 | leaks |
|---|---|---|---|---|---|---|
| gpu F-arm (163n) | 163 | 52 (31.9%) | 39/52 (75%) | 106 (65%) | 23/163 (14.1%) | 0 |
| gpu T-arm (124n) | 124 | 69 (55.6%) | 40/69 (58%) | 55 (44%) | — | 0 |
| gpu M-arm r2 (78n) | 78 | 19 (24.4%) | 6/19 (32%) | 53 (68%) | — | 0 |
| **nat v3 r2 (81n)** | **81** | **28 (34.6%)** | **25/28 (89.3%)** | **48 (59%)** | **38/81 (46.9%)** | **0** |

## 异常与观察

1. **quotient 率 46.9% 异常高**：nat 题（自然语言/分布建模域）的 claim 结构可能天然偏 quotient（商/比率类断言），但 46.9% 远超 r13 教训的 20% 阈值。需 D 判定：是题域特性（nat 题多比率/分布参数断言）还是 edge-reclassify 对中文 claim 误判。
2. **logic-only 占 verified 89.3%**：比 gpu F-arm (75%) 还高——中文 nat 题的检索通道（DDG lite 中文 + 白名单 csdn/zhihu 等）对分布建模/网络参数类 claim 命中率低，verify 大量走纯逻辑校验路径。与 11-12 drb-2 的"数据边界受限"模式一致。
3. **degraded 59.3% 低于 gpu F-arm 65%**：新白名单（10 中文域）+ DDG lite 统一通道可能有效，但样本小（81n）不下结论。
4. **进程退出无 final json**：同 r3/r5 模式——verify 阶段退出路径未走完落盘逻辑。r2 ckpt 完好可 resume。

## 待 D 判定

- [待D醒] quotient 46.9% 是否题域特性（nat 题多比率断言）还是 reclassify 误判——影响 edge-reclassify 规则是否需按题域分参数。
- [待D醒] nat 臂是否 resume 到 r3 出 final json（r2 ckpt 81n 完好），还是接受 r2 数据作三臂对比的 nat 侧样本。
- strict 口径（logic-only 剔除后 verified 率）是否作 bench 官方口径——nat 臂 strict = 3/81=3.7%，与 gpu F-arm 9.2% / T-arm 19.4% 同方向（nat 最低）。
