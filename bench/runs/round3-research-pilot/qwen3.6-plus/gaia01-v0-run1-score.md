# GAIA-01 V0 run1 评分 — qwen3.6-plus

> origin: ai
> 评分对象：gaia01-v0-run1.md（local degraded:true，执行者自答）
> 评分时间：2026-10-23 06:26 Asia/Shanghai
> 评分方式：**探索性自评，非正式盲评**（执行者=被评答案的生成者；正式盲评留 round4 双评审）
> rubric：bench/rubric/scoring.md（100 分制 D1-D4）+ bench/rubric/research-rubric.md（D5 定稿）
> 冻结答案锚点：参考解 Claude Shannon（bench/tasks/research-questions.md GAIA-01 参考解）

## D1 答案正确性（40）

- 答案 = Claude Shannon，与参考解 **一致**（格式 First name Last name ✓）。
- 40/40

## D2 推理质量（25）

- 推理：一段式——"Shannon 是受访科学家之一，给出比其他人更近的 thinking machines/robots 预测"。**无中间推理展示**（未说明如何排除其他受访者、"更近"的判定依据是什么）。
- 答案直接断言结论，推理链隐含在"the one who gives the sooner prediction"的措辞中，但未展开比较过程。
- 14/25（答案对但推理黑箱——V0 裸 prompt 下模型的典型行为：直接给结论）

## D3 结构与可验证性（20）

- 结构：答案 + 一段解释，简洁。
- 可验证性：**零来源**（无视频 URL、无字幕出处、无文献）——"Shannon 给出更近预测"这一关键主张无法核验。
- 9/20

## D4 格式与完整度（15）

- 格式严格符合题面要求（First name Last name）；完整度：回答了问句，无冗余。
- 13/15

## D5 研究加分（0~+20，定稿五档）

**候选新结论清单**：

| 陈述 | 来源 | 抽查结果 | (a)新 (b)真 (c)独立 | 级别 |
|---|---|---|---|---|
| "Shannon 是 father of information theory" | 无来源 | 通识知识 | (a)是（超出题面，题面未提信息论）(b)弱（通识但无来源标注）(c)否（常识单源） | 不计（(b)无来源标注） |

- 无显式 ## 新结论 段（V0 未要求）；答案中仅一句通识性补充（father of information theory）无来源 → **D5 = 0 档（0 分）**
- 负向项：无伪新/假新（未标新，无证据链断裂）。

## 总分

| 项 | 分 |
|---|---|
| 基础分 D1+D2+D3+D4 | 76 |
| D5 bonus | +0 |
| 研究分 R | **76** |

判定：**partial（60-79）**（研究题试跑口径，非正式盲评）

## 备注

- V0 对照价值：裸 prompt 下答案对但**推理黑箱+零来源**——D2/D3 是 V0 的结构性短板。
- GAIA-01 的 V0 基础分（76）低于 BC-00 V0（81）：因推理展示更少（一段式 vs 线索整合段）。
