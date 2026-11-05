# 阶段 03：行动分解 — RUBRIC-V3-FULL-AUDIT / G3 W3/W4 收尾

> goal: rubric-v3-audit-g3 · 分支 ralph/rubric-v3-audit-g3 · 2026-10-30
> 上游: 01 因素分解（F1-F4）+ 02 证据固化 + 02.5 对抗核验（Q1-Q4 吸收，R1-R6 登记）

## DAG

| # | 行动 | owner | 依赖 | 验收方式 |
|---|------|-------|------|----------|
| A1 | 交付物 `bench/rubric-v3/ablation/g3-w3w4-completion.md`：F1 复验表（含任务书表述修正）+ F2 敏感性分级（W3 高 / W4 排序中·构念效度高双维度）+ F3 决策矩阵（O1 推荐子选项 gold 平均排名，O2 挂起，O3 可行+代价重估「校准损失为主」）+ 负面结果声明 | runner | 02/02.5 完成 | 文件落盘；每个数字可回溯到 stats-w3w4.json / judge-blindtest-r1.json / hit-matrix.json 路径或本 loop 复算脚本输出；post-hoc 口径选择显式声明段存在 |
| A2 | loop 工件 stages/01,02,02.5,04,04.5 五件齐全（RV3G3-* 命名） | runner | — | ls 确认五文件存在且各阶段判定行完整 |
| A3 | `tasks/current-goal.md` 改写为 G3 收口态（五字段格式） | runner | A1 | 文件内容 = G3 目标 + 已完成阶段 + 验收对照 |
| A4 | commit r110（A1+A2+A3）→ push → `git ls-remote` 验证 → merge main → push origin main | runner | A1-A3 | ls-remote 显示远端 sha == 本地 HEAD；main 合并后 `git log -1` = r110 |
| A5 | queue 更新 commit r110b：goal-queue.md 主 goal 进度注记追加 G3 完成行 + CONTINUE_MSG.md 重写（下一步 P0=G4）+ 新增 ≥1 候选 | runner | A4 | queue 无空档（新候选存在）；主 goal 保持未勾选（G4-G6 未完） |

## 关键判读分支预注册

- **B1**：若 A1 写作中发现 02 任一数字复算不一致 → 停止收口，回 02 修正并重新走 02.5（不允许带错收口）。当前状态：全部数字已二次复验（含 Q4 差值分布本轮刚纠正），预期不触发。
- **B2**：若 merge 冲突（其他会话动 main）→ 停手登记 APPROVALS，不 force。
- **B3**：G3 不定稿任何修复方案——决策矩阵只给「推荐路径（供 G6）」措辞，交付物标题级结论不得出现「定稿采用 X」。

## 不做的事（边界）

- 不改任何冻结文件（stats-w3w4.json / hit-matrix.json / prior-estimates.json / judge-blindtest-r1.json / gold-tree.md 只读；新数字一律进 g3-w3w4-completion.md）。
- 不动 gold set、不实施 O1/O2/O3 任何一项（实施与定稿权在 G6）。
- 不派 subagent（工具纪律）；web-llm 已按失败降级记录回执。
- 不对 ablation-result.md 做逐句叙述层核验（空缺 G3 已登记，留给 G6 引用时以 JSON 为准的纪律即可）。

## 判定

DAG 六项行动全有验收方式，依赖链线性无环；边界与 02.5 风险处置一一对应。→ 进入 04。