# 当前 goal @ r161 (2026-11-01)

## 【目标】
G1b family_check 升级 + RV3G1 dual-rater 复核：Part A 模型自报+5 工件 J1-strict 重打（family_check unknown→CLOSED/PARTIAL/CONFLICT）；Part B 75 cell 异族第二裁判盲判 8 批，量化分歧方向。

## 【阶段】
A 取 goal ✅ → B 执行（任务书备料 ✅ 140ce26 @ arena 分支 / arena 派发 ✅ 会话 01a195cb 运行中 ⏳ / 产出核验 ⏳）→ C 收口找下一个

## 【SOP 索引】
tasks/G1B-FAMILY-UPGRADE-DUAL-RATER-task-brief.md + .claude/skills/arena-outsource/SKILL.md（门禁已过：台账✅/分支✅/会话绑定✅/prompt 仓库声明✅/回执指纹✅）

## 【验收标准】
Part A: hetero-judge-results-r2.json(5 工件) + family-upgrade-analysis.json(family_check_upgrade 结论 + X5 对比)。Part B: dr-b1..b8.json(75 条 h 判定) + dr-summary.json(flip 清单)。全部落 arena/4a614e63-prompt-first-bench + Lead 独立复算 agree_rate + merge main + queue 回填。

## 【失败降级】
arena 中途断线 → 已落盘批次保留，续派"从 dr-bN 继续"；全断 → 本地 qwen 自答 conf−0.2（但同族无升级价值，只补 Part B 不补 Part A）。
