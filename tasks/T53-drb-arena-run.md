# T53 — 让 arena 跑 DRB bench（用户 2026-11-13 指令）

## 问题重述
用户想看 LMArena agent mode 在 DeepResearch Bench 上的分数，对标 CellCog Max 56.72。
本地 S5 SM pipeline 同题已跑：drb-1 = 0.0、drb-2 = 0.0（病根=检索通道对中文题全盲），所以 arena 的分数同时是"外部参照系 + 我方弱项的外部验证"。

## 分解树
- A. 任务书（arena 能对齐验收口径的最小完整集）：题目原文（queries/*.json 里 zh prompt）+ 交付物定义（报告 md）+ 评分口径（四维 criteria.jsonl 逐条 0/1 加权，judge=本地 qwen3.8-27b drb_judge.py）+ 时间盒
- B. 派发通道：ego-browser 走 LMArena agent mode（skill arena-outsource SOP；tiptap 坑已知）
- C. 回收与判分：arena 产出报告 → 存 answers/arena-drb-N.md → 喂 drb_judge.py 出四维分 → 进 s5-sm-bench-report.md 对比表
- D. 泄漏控制：DRB 公开题存在训练数据泄漏可能——arena 侧无法排除（它的模型栈不透明），结果标注 "leak 不可控, conf 降档"；本地 run leaks=0 可对照
- E. 口径声明：judge 是同源 qwen（T8-C3-v3 blocked_human 未解），绝对分只能当横向比较用，不能对外报

## 缺口标注
- [待核验] arena agent mode 单次任务的时长/产出上限（agent mode 是否支持长程多步检索任务，还是只适合短问答）→ 派单前先用一个 smoke 题试
- [待核验] criteria.jsonl 是否在 drb-pilot/ 里有全部三题的官方判据文件（bench-report §0 说"逐题实测"，需确认落盘位置）
- [留空] arena 分数 __（跑完填）

## 执行顺序
1. 确认 criteria 文件位置 + 选 1 题做 smoke（建议 drb-2，题面相对收敛）
2. ego-browser 派 arena 任务卡（按 stage-gate 03-dispatch 模板四段式）
3. 等产出 → judge → 填表
4. 若 arena 分数显著 > 0 → 反推它检索通道强在哪，写回迭代日志 §4

# origin: ai · 2026-11-13
