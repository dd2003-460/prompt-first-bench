# C3 对抗核验回执 · r49 (arena agent mode)
- 会话: 01a1855c-f77e-7068-a6c9-8267f771437d
- 任务卡: tasks/T8-C3-adversarial-check.md (6 质询方向)
- 判定: **PASS-with-fixes** — 方向可检验、无根本缺陷，但当前版本不能直接当确认性因果实验跑
- 6 条质询严重度: 高×4 (M8可变分母/统计功效/top-k同源偏差/对照设计), 中×2 (补偿效应/prompt位置混淆)
- 必改项 6 条 → 全部落进 T8-prompt-ablation.md C3 r50 修订
- 关键修正: M8 拆 truth+cover 联合判读; 配对任务块替代"Δ超方差"; A-full重复正名为重测对照; top-k降为探索性证据+hold-out域隔离
