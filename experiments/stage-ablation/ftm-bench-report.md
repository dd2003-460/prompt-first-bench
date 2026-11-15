# S5 SM F/T/M 三臂对比（gpu 题 · 2026-11-15）

> origin: ai（方法 persona 实验的 bench 评分）
> 关联：T53-decomp-state-machine、three_arm_compare.py

## 一句话

F（公式注入）verified 率 37.7%，T（文本臂）51.6%——T 比 F 高 14pp，说明文本臂的拆解质量优于公式臂。M（minimal）跑中，待补。

## 指标对比

| 指标 | F (formula) | T (textarm) | M (minimal) |
|---|---|---|---|
| 总节点数 | 53 | 124 | [待补] |
| verified 数 | 20 | 64 | [待补] |
| verified 率 | 37.7% | 51.6% | [待补] |
| degraded 数 | 27 | 54 | [待补] |
| degraded 率 | 50.9% | 43.5% | [待补] |
| pending 数 | 6 | 6 | [待补] |
| failed 数 | 0 | 0 | [待补] |
| quotient 边 | 7 | 9 | [待补] |
| cartesian 边 | 46 | 115 | [待补] |
| quotient 占比 | 13.2% | 7.3% | [待补] |
| rework 事件 | 32 | 72 | [待补] |
| 泄漏数 | 0 | 0 | [待补] |
| 终态 | rework | unknown | [待补] |

## 判读

- **T > F（verified 率 +14pp）**：文本臂的拆解质量优于公式臂。F 臂的公式注入可能限制了拆解的灵活性，导致更多节点 degraded。
- **F 的 quotient 占比更高（13.2% vs 7.3%）**：公式臂更倾向于做等价类合并，但合并质量不高（degraded 率高）。
- **T 的节点数更多（124 vs 53）**：文本臂拆解更细，但 verified 率也更高，说明细拆没有导致质量下降。
- **rework 事件**：T 的 rework 更多（72 vs 32），但这是节点数更多的自然结果，不是质量问题。

## 下一步

1. M 臂跑完 → 补上 M 列
2. M1/M2 启动 → 方法 persona 三臂对比
3. 三臂 judge + 对比表

## 数据文件

- `runs-s5-sm-gpu-formula-r2.json`（F 臂）
- `runs-s5-sm-gpu-textarm-r2.json`（T 臂）
- `runs-s5-sm-gpu-minimal.json`（M 臂，待生成）
