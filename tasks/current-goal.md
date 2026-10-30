# Goal: RV3G6-gmr-tiebreak-prereg — gmr 主判据预注册文档

> 创建：2026-10-30 · ralph loop runner（queue 队首）
> 依据：`bench/rubric-v3/AUDIT-report.md` §3.2/§3.3/§8 + goal-queue 候选描述

## 【目标】
把 AUDIT-report 中 gmr（gold mean rank）主判据的四个悬空件落为一份**判据冻结件** `bench/rubric-v3/gmr-criterion-freeze.md`，内容四块：
1. **tie-break 规则文字化**：节点 ID 字典序（引用 AUDIT-report §8 引用规则原文），说明为何不用分数并列时的其他 tie-break。
2. **过线阈值**：正式论证在 RV3G3-goldrank-threshold-proof 完成前**不写死数值**——本文件只登记「阈值 = RV3G3 产出值」的引用机制 + 当前锚点（超几何 n=31,k=5：E[X]≈1.61 / P(≥4)≈2.7%）+ 使用门禁（RV3G3 未完成前 gmr 不得用于正式判定）。
3. **退出条件文字化**：AUDIT-report §3.3 的退出条件逐条抄录为可机判 checklist（每条给触发条件+动作）。
4. **§8 引用规则落为判据冻结件**：gmr 数字引用时必须附限定语（相对 Lead-gold + 同族双 judge）的强制条款，byte-exact 抄录 AUDIT-report 对应段落。

## 【阶段】
rubric-v3 审计链修订落地环的第二个小 goal（batch1 已收口 r116）。纯仓库内文本工作，不改任何冻结数据。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00..04.5`（六阶段定义）
- `bench/rubric-v3/AUDIT-report.md`（上游定稿，§3.2/§3.3/§8 是主要消费对象）
- `bench/rubric-v3/DRAFT-rubric-v3-v2.md`（batch1 产物，O3 节引用 gmr 处需与本冻结件一致）

## 【验收标准】
- [ ] gmr-criterion-freeze.md 四块齐全，每块有 evidence（AUDIT-report 行号引用）
- [ ] 阈值不写死数值（只有引用机制+锚点+门禁三件套）
- [ ] 退出条件 checklist 每条可机判（grep 可定位）
- [ ] §8 限定语 byte-exact（python 字节比对）
- [ ] DRAFT v2 O3 节与冻结件无矛盾（人工核对记录在 execution-log）
- [ ] 冻结数据零修改（git status 验证 hit-matrix/prior-estimates/gold-tree/stats-* 无 diff）
- [ ] 04.5 反方复核 verdict pass

## 【失败降级】
- AUDIT-report 某段找不到 → 登记 unverified + 用现有材料兜底，不虚构
- web-llm 需要外部第二意见 → 登录过期则如实记录 unverified，不阻塞
