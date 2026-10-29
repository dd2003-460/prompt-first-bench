# Goal: RUBRIC-V3-FULL-AUDIT / G4 漏洞对照（gap-analysis Q2 五条结构性解释 vs rubric-v3 协议）

> 创建：2026-10-30 · ralph loop runner（队首大 goal RUBRIC-V3-FULL-AUDIT 的子 goal G4）
> 依据：`tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md` G4 节 + gap-analysis 原文（git show aea3d6b）+ G1/G2/G3 产出

## 【目标】
任务书 G4 = 「gap-analysis Q2 五条结构性解释逐条对照我们的协议，标『已规避/未规避/部分规避』+ 证据」。交付：
1. **判定结果**：S1 构念错配 = 部分规避（未到期，第二格未执行；02.5 Q1 从「已规避」降级）/ S2 唯一 gold 路径偏置 = **未规避**（单源 gold + §4 补丁与 gold 同构 + O2 条款砍掉抗同源出口——系统性偏置来源）/ S3 标注/judge 可靠性成本 = 部分规避（降档：DRAFT ≥3 LLM 盲生成 p̃ 协议 vs 实际单 judge 自评）/ S4 可比性 vs 版本依赖 = 部分规避（子项分裂：版本依赖已管控、跨域可比性无机制）/ S5 surprisal 风险 = 部分规避（强度不足：三重事前防护被实证穿透）。
2. **核心模式识别**：三种「部分规避」结构不同（降档/覆盖缺失/强度不足），对应 G5 三类优化动作（强制机械化/补覆盖/加固阈值）。
3. **负面结果声明三条**：「S1 已规避」推翻、「paper 协议完整 = 风险受控」推翻、「blindtest = 独立校验」限定为同族。
4. **G5/G6 导出**：G5 三类优化输入 + G6 定稿硬约束（S2 → O3 数字必须声明「相对 Lead-gold」；adversarial-check 28 findings 需处置表至少 9 blocker）。
5. **交付物** `bench/rubric-v3/ablation/g4-vulnerability-crosscheck.md`。

## 【阶段】
rubric-v3 研究级审计链（G1-G6）的第四环。消费 gap-analysis 前瞻警告（aea3d6b 快照）+ DRAFT/TASK-ablation 原文 + adversarial-check receipt，回答「协议是否真的规避了已知结构性风险」——答案是零条完全已规避、一条未规避（S2）、四条部分规避且性质各异。本 goal 只做对照判定，不实施任何修复（B3 边界）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `git show aea3d6b:receipts/rubric-v3-gap-analysis.md`（Q2 五条原文，对照基线）
- `git show origin/rubric-v3:bench/rubric-v3/DRAFT-rubric-v3.md` + `.../ablation/{TASK-ablation,ablation-result}.md` + `git show origin/rubric-v3:receipts/adversarial-check-rubric-v3.json`（只读，git show 消费）
- `bench/rubric-v3/ablation/{prior-estimates,gold-tree,g2-rootcause,G1-contradiction-audit,g3-w3w4-completion}.md/json`（冻结只读）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `RV3G4-`
2. 01：四因素分解（F1 材料定位+三值判定规则 / F2 五条映射 / F3 去重 / F4 交付结构）+ 空缺 G1-G3
3. 02：web-llm 强制步骤执行并留回执（三 provider error → 记录失败继续）+ S1-S5 初判 + F3 去重表
4. 02.5：反方质询 Q1-Q4（S1 降级 / 证据硬度 / 标签区分度 / 规则偏差）+ 风险登记 R1-R6 + 对抗核验停止理由
5. 03：行动 DAG + 关键判读分支预注册（B1-B3）+ 边界（不改冻结文件与 DRAFT、不跑消融、不派 subagent、不逐条闭环 28 findings、不用模糊判定词）
6. 04：交付物落盘（四列汇总表 + 五节 + 负面结果三条 + G5/G6 导出）+ 诚实保留（κ 门禁 unverified / 28 findings 未闭环 / S2 修复不可本轮闭环 / 基线 aea3d6b / T17 缺席）
7. 04.5：反方检查五条 + verdict pass + repair_stage 无 + 给 G5 的下一步建议（三类优化消费 + 9 blocker 修复成本纳入估算对象）
8. 冻结数据零修改（git status 可查）
9. commit + push 分支 `ralph/rubric-v3-audit-g4` + ls-remote 验证 + merge main + queue 注记

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续，不阻塞
- evidence 引用失效（B1）→ 停收口回 02 修正并重走 02.5，不带错交付
- S2 修复依赖外部（R5.2-third-scorer）→ 只登记为 G6 硬约束，不实施
- merge 冲突（B2）→ 停手登记 APPROVALS，不 force