# CONTINUE_MSG — 2026-11-03 r262

## 本轮完成 (r262)
**T8-C3-v3-m8fixed-opportunity-table（M8-fixed 逐机会判定协议设计 + 验证 · FAIL 1 修复）— 降级通道实跑，待 commit**：
- 动机：r260 定位 J1v11 条目抽取漂移 → r261 J1v12 修了 judge 侧方差但区分力不够 → 根因是「应该抽哪些条目」没有 ground truth。M8-fixed = 独立标注员预建冻结机会表 + judge 只判表内条目
- 协议冻结：calibration/m8fixed-protocol-v1.json（sha ecdfb59edfdca704）——judge 只能判表内条目、三测作 fail 依据、阶段分层规则（phase 01 用 constraint 子集 / phase 03+ 用全表）、G1/G2/G3 门禁
- G1 稳定性 **PASS**：同一工件（A-full/D1/seeda-r1）M8-fixed 打 2 次 per-item verdict 一致率 9/9=1.0（≥0.90 threshold）
- G2 区分力 **FAIL**（关键发现）：
  - 全表版（9/10 项）：score spread 仅 0.044（0.556-0.600）——O04-O07 deliverable 项在所有 config 上全 fail（阶段 01 不可达），压缩分数范围
  - constraint-only 版（budget/scale/platform 3 项）：spread 0.0——所有 config 全部 3/3 pass
  - **根因确认**：检查 R4 全部 54 个工件 → 均为阶段 01+02 产出（目标分解+信息调研规划），无一到达阶段 03/04。Prompt freeze 组件明确写了「本阶段是因素分解，不是资料搜集」「不要求在本阶段给出阶段 02 才能取得的价格/性能/证据」
  - **推论**：之前所有 per-config Δ（包括 F1 freeze 主效应 +0.37~+0.39）测的是阶段 01/02 层面的弱信号被测量噪声淹没。消融对最终报告质量的影响需要跑完整 loop（01→04）才能测到。当前数据不能升级任何 confirmatory 声明
- 回执：receipt-r262-m8fixed.json（含 root_cause_confirmed 节）；queue 已登记

## 上轮完成 (r261)
**J1v12 抽取协议冻结 + 稳定性验证**：step1 PASS（n 方差=0, overlap=1.0）；step2 PARTIAL（ρ=-0.6, score compression）→ J1v12 修了 judge 侧方差但区分力不够，与 M8-fixed 正交且都需要

## 上上轮完成 (r260)
**T8-C3-v3-seedc-powerup（第三 seed 功效提升 run）**：18/18 run + 36/36 judge + cover 18/18 零失败；G3 SIGNAL：F1 三 seed 同向性 FAIL（D1 反向）；根因 = J1v11 条目抽取漂移 → M8-fixed 升级为前置条件

## 当前状态
- pfb @ main f36659d pushed；**r262 产出待 commit**（m8fixed-protocol-v1.json + receipt-r262 + queue + 本文件）
- **T8 实验线结论更新**：R4/R5/R6/seedc 全部数据基于阶段 01/02 工件，只能支撑「消融效果方向性存在但幅度小且被测量噪声淹没」。要测最终报告层面的消融效果需补跑完整 loop（01→04），这是新的 P1 决策点（需成璐拍板是否投入）
- T8 Part C exploratory 已收口（r245s）；confirmatory 四条件中异源 judge 仍 blocked-on-human
- decomp/research-prompt/persona-prompt-lab 可执行项清零
- 卡人项不变：G1b family_check / B2 协议重设计候裁 / ORF arXiv 手动上传 / web-llm 登录

## 下一步
1. **commit + push r262 产出**（P0）：`git add experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json experiments/T8-matrix/runs/c3-v3/receipt-r262-m8fixed.json tasks/goal-queue.md CONTINUE_MSG.md` → push
2. **T8 完整 loop 决策**（P1，需成璐拍板）：是否值得补跑 9 configs × 2 domains × 完整 loop（01→02→03→04）到最终报告再评分？成本估算：每 cell 约 4 阶段 × 2-3 min/阶段 ≈ 10-15 min，54 cells ≈ 9-13.5 h LLM 时间（本地 :8787 可跑但慢）。收益：第一次真正测到消融对最终报告质量的影响。如果成璐认为 T8 到此为止（exploratory 结论够用），则关闭 T8 实验线
3. G1b family_check 模型身份披露（blocked-on-human）
4. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）