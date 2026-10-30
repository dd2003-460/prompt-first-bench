# Goal: RV3G3cdx-queue-dedup-lint — queue 结构 lint（r149）

> 创建：2026-10-30 · ralph loop runner（queue 消费——r146 sweep 导出项，纯仓库内脚本工作）
> 依据：`tasks/goal-queue.md` 是 ralph loop 的唯一事实源队列文件，其**静态结构**此前无机器检查。历史先例两次人工去重（r105c/r102c），97d2adf 型漏翻的静态形态 = 「已完成」区出现带完整结果注记却仍 `[ ]` 的行。本 goal = 把静态结构检查机判化，与 queue-hygiene-sweep（动态 message↔状态一致性）互补。

## 【目标】
写 `bench/rubric-v3/ablation/scripts/assert-queue-lint.py`：对 `tasks/goal-queue.md` 做三项纯静态结构机判——
- **(a) 短名重复行**：同一 goal 短名在「待办 + 新导出候选」区出现 >1 次（已完成区豁免——吸收登记行合法；跨区重复需区分处理，见 02 裁定）；
- **(b) 状态位异常**：「已完成」区出现 `[ ]` 行；或任一行带完整结果注记（`**结果**：` 标记）却仍为 `[ ]`（97d2adf 静态形态）；
- **(c) 行格式完整性**：待办/新导出候选区每个 `- [ ]/[x]/[~]` 行的分隔符结构可解析（短名 | 一句话 | 产投比依据，允许结果注记追加）。

输出逐条 PASS/FAIL/SIGNAL + exit code（0 = 全通过 / 1 = FAIL 指名道姓 / 2 = 输入不可解析）。规则预注册于 docstring，byte-stable。

## 【阶段】
00 预检 → 01 分解（本文件）→ 02 现状扫描（queue 行格式实证枚举 + 既有七脚本模式参照 + 边界形态盘点）→ 02.5 交叉核对 → 03 动作分解 → 04 执行验证（实现 + 正/负样例矩阵实跑 + 变异测试）→ 04.5 反方复核 → 收口（queue 更新 + merge main）

## 【SOP 索引】
- `tasks/ralph-loop-runner.md` 阶段 B/C
- 被检对象：`tasks/goal-queue.md`（只读，冻结面不动）
- 参照先例：assert-closure-checklist.py（r148，exit 三分支 + docstring 预注册判定语义 byte-stable 模式）；assert-goldrank-crossdomain.py（check() 汇总 + SIGNAL 前缀分流约定）

## 【验收标准】
- [ ] 脚本落盘 `bench/rubric-v3/ablation/scripts/assert-queue-lint.py`，docstring 预注册 (a)(b)(c) 判定语义
- [ ] 当前 main 上 queue 实跑给出明确 verdict（预期：(a) 存在已知重复行 → 如实报告不粉饰；(b)(c) 按实况）
- [ ] 负样例矩阵（构造性，独立 tmp 分支或沙盒目录）：重复短名 / 已完成区 `[ ]` / 结果注记+`[ ]` / 格式残缺 各触发对应 FAIL exit 1
- [ ] exit 2 路径可达（空文件/非 markdown 输入）
- [ ] 冻结面零修改；改动面 ⊆ {新脚本, stages/*, current-goal.md, goal-queue.md}
- [ ] 七脚本回归基线 spot check 零漂移（exit=[0,0,0,1,0,0,0]）
- [ ] 04.5 verdict pass；queue 更新（本 goal `[x]` + 结果注记 + 新候选 ≥1）

## 【失败降级】
- 若 (a) 跨区重复的裁定歧义过大（待办 vs 已完成 vs 新导出候选三区的语义边界无法从现有先例推导）→ 降级为 SIGNAL-only（报告不拦截）+ 裁定材料落盘，不代裁
- 若 (c) 分隔符在历史行中存在过多合法变体（如 `~~删除线~~`、`[~]` 半态）→ 以「可解析即过、不可解析才 FAIL」最小规则收口，变体登记不扩规则
- 若实跑发现当前 queue 本身有未登记的结构缺陷 → 如实报告 + 修复建议导出候选，不在本 goal 内改 queue 数据行（防超范围）