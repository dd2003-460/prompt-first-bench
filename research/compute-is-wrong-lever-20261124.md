# origin: ai
# 方向判断：算力是错的杠杆（对 D autoresearch 目标的方向含义）
# 来源: pfb 三域数据 (GPU/Q6/Q7) · 2026-11-24 · 回应 D "没思考更大方向和 general 工作"

## 一句话判断

**"知道自己不知道"（gap 检测 / 元认知）不随算力 scaling，随架构。** 想提升它，加预算无效，只能改修复回路或换模型。

## 从数据怎么推出来（证据强度分层，12:16 矛盾修正后）

**12:16 修正**：初版把三域都说成"强化不变性"，错。draft 自己写了 Q6 监控轴 invariance **does not transfer**（"the invariance is thus currently a GPU-domain result"）。三域实际不一致：

1. **元认知预算不变量 = GPU 域结果，不是三域结果**：GPU 域监控轴（claim-field gap rate）跨预算档 0.105/0.106/0.114 平（ANOVA F(2,12)=0.036, p≫0.05）。underpowered null（21.5% power），只能读"没检测到"。
2. **Q6 是反例（低水平 + 50 档后非平）**：claim-field gap rate 0.073/0.003/0.016/0.026 @ 50/100/150/300（n=3/档，draft 原文），719 档 0.000/0.029/0.005（rep 间大 spread）。与 GPU 的 flat 0.105/0.106/0.114 不同形——**Q6 水平低一个量级且 50 档后非平**。draft 定性："the invariance is thus currently a GPU-domain result, which is exactly the cross-domain validation this scan was designed to test"。
3. **修复回路低产是唯一跨域复现的**：GPU 域 flagged 节点只回头修 1.6–3.7%（node-level era-scoped / global），Q6 复现 5.2%（32/621，同量级，draft 明确 "does transfer"）。树是"绕着 52.5% 未验证节点往前长"（5630/10730）。**这条是测出来的、有牙齿的、跨域复现的——是下面方向判断的真正承重证据，比 #1 的域内 null 强。**
4. **Q7 第三域初步**（n=7，12:10 口径修正后）：gap 字段 50 档 0.000×3 / 100 档 0.000/0.020/0.010 / 150 档 r1 0.0133。形状与 Q6 同（低水平、50 档后微升）而非与 GPU 同（高水平、平）——**若 15/15 确认，"不变性"进一步降级为 GPU 域特异，"低产修复回路"仍是跨域机制**。

## 对 D 目标意味着什么（预言力，可证伪）

D 的终极目标：在 4×V100 硬件上建 research 的 AGI——能自主做研究、知道自己缺什么的系统（防御性语言=调研入口）。

这条判断给出一个**硬边界条件 + 可检验预言**：

- **边界**：autoresearch 系统里最难的部分（自我认知的盲区）不随算力 scaling。算力是"覆盖宽度"的杠杆（cov 随 realized 节点升，三域形状一致），不是"自我认知精度"的杠杆。
- **预言 P1（可证伪）**：在同一模型+同一 prompt 架构下，把预算从 300 提到 719，gap 检测率（监控轴）不应显著上升。若显著上升 → 本判断错。
- **预言 P2（可证伪）**：改修复回路（提高 flagged 节点的回修率，如把 rework 触发从"低产尾"改成"强制回修"），gap 检测率应比加预算更敏感。若加预算比改回路更有效 → 本判断错。
- **设计含义**：D 的 autoresearch 系统，算力预算应花在"覆盖宽度"（多域、多节点），自我认知能力应花在"修复回路架构"（回修触发机制）+ 模型选择，而不是堆节点。

## 置信度 + 什么证据会推翻

- **conf 0.6**（方向判断，非单实验结论）。
- 会推翻的：① P1 被证伪（高预算 gap 率显著升）；② Q7 全量重算后 gap 出现预算趋势（与 GPU/Q6 相反）；③ 换更强模型后 gap 率随预算升（说明是模型能力瓶颈而非架构）。
- 当前最弱一环是 #1 的 underpowered null——Q7 15/15 + 更高 n 的 rep-scan 是关键补强。

## 与 draft 的关系

workshop draft 的 headline "budget buys breadth, not metacognition" 目前只当测量结果报。本 note 把它升级为**方向判断**：它不只是"我们测到预算不影响元认知"，而是"这对怎么建 autoresearch 系统意味着算力是错的杠杆"。draft §4/§5 可加一段指向（带 P1/P2 预言），把测量结果变成对 D 目标有预言力的设计约束——这是 general 的那一层，不是数字堆砌。
