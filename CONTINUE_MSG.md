# CONTINUE_MSG — 2026-11-03 r261

## 本轮完成 (r261)
**J1v12 抽取协议冻结 + 稳定性验证（r260 measurement_warning 修复第一步）— 降级通道实跑，待 commit**：
- 动机：r260 seedc powerup G3 SIGNAL 定位根因 = J1v11 prompt 未约束条目抽取范围（judge 自行决定抽哪些/抽多少条 → per-run n 从 3 漂到 24）。J1v12 增加固定抽取协议修此方差
- 冻结面：calibration/judge-prompts-v12.json 落盘（J1-strict-v12 sha e255b4c21dfcc1d6；四类主张 a/b/c/d 全覆盖 + 不得跳过 + 不得合并 + X1..Xn 统一编号 + summary 报 n；三测定义/判定规则/输出格式骨架不变；不修改 judge-prompts.json 原冻结面）
- step1 稳定性验证 **PASS**：同一工件（A-full/D1/seeda-r1, output_chars=8007）J1v12 打 3 次 fresh context → n=[19,19,19]（方差=0），id set Jaccard overlap=1.0，score 恒 18/19。对比 J1v11 同工件 R4 stored n=7、seedc n=3（漂移 3→24）
- step2 跨版本对比 **PARTIAL**：6 cell（A-full/B-nofreeze/B-none × D1/D2）J1v12 vs J1v11(R4 stored) → Spearman ρ=-0.600（n=6，方向为负）；score compression：J1v12 range 0.944-1.000（spread 0.056）vs J1v11 range 0.375-0.857（spread 0.482）→ J1v12 在当前任务族上接近天花板，区分力不足
- 结论：J1v12 解决了「judge 抽哪些条目」的方差（稳定性达标），但不能直接替代 J1v11 做消融排名（区分力不够）。J1v12 与 M8-fixed 正交且都需要——J1v12 修 judge 侧方差，M8-fixed 建 ground truth（应该抽哪些条目）。step3 全量重放暂不做（等 M8-fixed 落地后再评估）
- 回执：receipt-r261-j1v12.json；queue 已登记

## 上轮完成 (r260)
**T8-C3-v3-seedc-powerup（第三 seed 功效提升 run）— 收口 push @ f0cb47e**：
- 18/18 run + J1v11/J2v11 双判 36/36 + cover brief_c 判读 18/18，零失败
- G3 SIGNAL：F1 三 seed 同向性 FAIL（D1 反向 0.0 vs R4 +0.391）；根因 = J1v11 条目抽取漂移 → M8-fixed 升级为一切后续消融前置条件
- 副产物：cover「高 cover ≠ 真核验」复现；J2v11 15/18 恒 1.0 无区分力再确认

## 当前状态
- pfb @ main 8b66020 pushed；**r261 产出待 commit**（judge-prompts-v12.json + receipt-r261 + queue + 本文件）
- T8 Part C exploratory 已收口（r245s）；confirmatory 解锁条件中异源 judge 仍 blocked-on-human，M8-fixed 现为最高优先
- decomp/research-prompt/persona-prompt-lab 可执行项清零（r259 确认）
- 卡人项不变：G1b family_check / B2 协议重设计候裁 / ORF arXiv 手动上传 / web-llm 登录

## 下一步
1. **commit + push r261 产出**（P0）：`git add experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-v12.json experiments/T8-matrix/runs/c3-v3/receipt-r261-j1v12.json tasks/goal-queue.md CONTINUE_MSG.md` → push
2. **T8-C3-v3-m8fixed-opportunity-table**（P1，queue 已登记）：独立标注员预建 D1/D2/D3 × brief_a/b/c 冻结机会表 + 等价 pattern 机判 assert + 盲双判复核模板——FAIL 1 修复，做完之前不再开新消融 run
3. G1b family_check 模型身份披露（blocked-on-human）
4. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）