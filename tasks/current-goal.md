# Goal: RV3B1-jaccard-adjudicate — M5 Jaccard 双口径人工裁决材料准备（runner 不代裁）

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 候选「RV3B1-jaccard-adjudicate」）
> 依据：batch1 revision-log M5 登记项 + DRAFT v2 L38/L311 双口径兜底落笔；pilot 开跑前必须收敛

## 【目标】
为成璐的 M5 人工裁决准备**完整决策材料**：finding #20 原文溯源（receipts/adversarial-check-rubric-v3.json finding idx 19）+ 双口径语义分析 + 三选项对照表（A 仅 run 间稳定性 / B 仅相邻档区分度 / C 维持双口径）+ 推荐与理由。**runner 只备料不代裁**——DRAFT v2 对应行改动与 revision-log M5 销账在成璐裁定后执行（本 goal 产出裁定模板，裁定本身是人工动作）。

**范围定位**：纯仓库内文本工作（溯源 + 分析 + 材料落盘），零外部依赖，工作量小。

## 【阶段】
纯仓库内推导。数据源（只读冻结）：`receipts/adversarial-check-rubric-v3.json`（finding #20 原文）/ `AUDIT-report.md` §2-O1（L77）/ `DRAFT-rubric-v3-v2.md` L38+L311 / `revision-log-batch1.md` M5 段。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/rubric-v3/jaccard-m5-adjudication-materials.md`（新建）
- 裁定模板 = 材料文档末节（三选项 + 勾选框 + 裁定后执行清单：DRAFT v2 L38 单口径改写 + L311 开放问题销账 + revision-log M5 销账，共 ~3 行 diff）

## 【验收标准】
- [ ] finding #20 原文 byte-exact 引用（issue + fix 全文，含四条判据 (a)-(d) 与低先验操作化定义）
- [ ] 关键发现落盘：#20 fix (c) 原文语义 = 「不同维度导出的候选集两两 Jaccard < 0.9」（跨维度去重），DRAFT v2 L38 双口径中「run 间稳定性」读法无 #20 原文支撑（系 AUDIT-report L77 压缩转述时引入的二义性）
- [ ] 三选项对照表（A/B/C：语义 / 可机判性 / 防刷分覆盖 / 对 pilot 的影响 / 风险）
- [ ] 推荐 + 理由（供成璐消费，非裁定）+ 裁定后执行清单（精确到行号与 diff 面）
- [ ] 冻结数据零触碰（git status 验证）；04.5 verdict pass
- [ ] queue 条目状态更新（本 goal 完成后标记「材料已备，待成璐裁定」——不划掉，因裁定未完成）

## 【失败降级】
- 若溯源发现 #20 原文支持双口径（与预判相反）→ 如实记录，三选项表按实际证据重排
- 若成璐裁定与本 goal 推荐不符 → 按裁定执行清单走，推荐段落保留为历史意见