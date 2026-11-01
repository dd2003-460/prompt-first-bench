# rejudge-g1b 任务书（arena agent mode · judge 外包）

## 背景
pfb rubric-v3 的 G1 矛盾审计发现 3 个 flag（judge 先验 p̃ 与 8-run 实际命中率系统性偏差）。本轮用 arena Battle 双裁判对 75 个 cell 重新盲判，检验偏差是 judge 单点噪声还是结构性问题。

## 待评材料
- `bench/rubric-v3/ablation/runs-C0-run*.md`（8 份 run，每份含完整拆解树+证据）
- `bench/rubric-v3/ablation/rejudge-g1b/node-defs.json`（75 个 cell 的节点定义：cell_id = run/节点号 + node_definition 一句话）

## 评分规则（rubric）
对每个 cell 判断：**该 run 对该节点的拆解是否达到了 node_definition 描述的质量要求**。
- 2 = 达到（有具体数字/公式/来源支撑，且与节点定义一致）
- 1 = 部分达到（方向对但缺关键量化，或只有定性描述）
- 0 = 未达到（没拆到这个节点，或拆了但与定义不符/错误）
每条判定必须给 ≤15 字理由（引用 run 内的具体段落/数字）。

## 交付格式（严格 JSON，≤200 行）
```json
{"judgments": [{"cell_id": "run5/N-2.2", "score": 2, "reason": "带宽估算给了 936GB/s 实测值"}, ...]}
```
75 条全量输出，不许省略。不确定的标 score=null + reason="未验证"。

## 约束
- 只看 run 文件内写的东西，不许引入外部知识补分
- 中文回答
- 落盘硬约束：文件不存在 = 任务未完成
