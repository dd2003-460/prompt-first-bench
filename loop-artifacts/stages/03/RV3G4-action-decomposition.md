# 阶段 03：行动分解 — RUBRIC-V3-FULL-AUDIT / G4 漏洞对照

> goal: rubric-v3-audit-g4 · 分支 ralph/rubric-v3-audit-g4 · 2026-10-30
> 上游: 01 因素分解（F1-F4）+ 02 证据固化（S1-S5 判定 + F3 去重表）+ 02.5 对抗核验（Q1-Q4 吸收，R1-R6 登记）

## DAG

| # | 行动 | owner | 依赖 | 验收方式 |
|---|------|-------|------|----------|
| A1 | 交付物 `bench/rubric-v3/ablation/g4-vulnerability-crosscheck.md`：S1-S5 五节（解释摘要 + 暴露面 + 判定 + evidence）+ 判定汇总表（四列：判定 / 缺口性质 / 缺口位置 / evidence）+ 负面结果声明 + 给 G5/G6 的导出 | runner | 02/02.5 完成 | 文件落盘；每条判定有 ≥1 个可查 evidence（file:line / JSON path / git show 路径 / 前序工件引用）；S1 判定 = 部分规避（Q1 吸收后）；三种「部分」显式区分 |
| A2 | loop 工件 stages/01,02,02.5,04,04.5 五件齐全（RV3G4-* 命名） | runner | — | ls 确认存在且各阶段判定行完整 |
| A3 | `tasks/current-goal.md` 改写为 G4 收口态（五字段格式） | runner | A1 | 文件内容 = G4 目标 + 已完成阶段 + 验收对照 |
| A4 | commit r111（A1+A2+A3）→ push → `git ls-remote` 验证 → merge main → push origin main | runner | A1-A3 | ls-remote 远端 sha == 本地 HEAD；main `git log -1` = r111 |
| A5 | queue 更新 commit r111b：goal-queue.md 主 goal 进度注记追加 G4 完成行 + CONTINUE_MSG.md 重写（下一步 P0=G5）+ 新增 ≥1 候选 | runner | A4 | queue 无空档；主 goal 保持未勾选（G5-G6 未完） |

## 关键判读分支预注册

- **B1**：若 A1 写作中发现 02 某条 evidence 引用失效（文件/行号对不上）→ 停收口回 02 修正。当前状态：所有引用在 02 阶段已逐条实际读取验证（gap-analysis 全文 / DRAFT 全文 / TASK-ablation Step 2 / adversarial-check 28 findings 全量 / 冻结 JSON 元数据），预期不触发。
- **B2**：merge 冲突 → 停手登记 APPROVALS，不 force。
- **B3**：本 goal 只做对照判定，不实施任何修复、不修订 DRAFT、不动 gold set——S2「未规避」的处置（双 gold / 异源 judge）全部留给 G6 决策与后续 goal。

## 不做的事（边界）

- 不改任何冻结文件与 DRAFT-rubric-v3.md（只读消费，含 origin/rubric-v3 分支上的版本）。
- 不重新跑消融、不重估 p̃、不调用 web-llm 实测（回执失败已记录）。
- 不派 subagent（工具纪律）。
- 不对 adversarial-check 28 findings 做逐条闭环（属 G6 定稿范围），只引用 S2/S3 相关条目。
- 判定不使用「基本规避」「大致规避」等模糊词——三值 + 缺口性质列强制精确。

## 判定

DAG 五项行动全有验收方式，依赖链线性无环；边界与 02.5 风险处置一一对应（R1/R2 → B3 + 导出节；R3 → S3 措辞限定；R5 → A1 四列表格要求）。→ 进入 04。