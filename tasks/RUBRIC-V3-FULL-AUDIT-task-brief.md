# origin: ai — 任务书：rubric-v3 完整消融推进 + 矛盾/漏洞/优化审计（研究级长任务）

> 给 ralph loop runner 的队首大 goal。这是「完整消融实验推进」类工作，不是 trivial 修补。
> 预计工作量：多个子 goal 串联，每个走完整 1-loop 六阶段。

## 【目标】
把 rubric-v3 从「草案 + O3 单点消融已做」推进到「可定稿的研究级证据包」：
1. **O3 消融深化**（已有 W0/W1/W2×8runs 数据，但构念效度被独立 judge 盲测否决 1/5）——找出否决的根因是公式问题、p̃ 估计问题、还是 gold-tree 标注问题，给出修复方案或正式降级结论
2. **W3/W4 权重方案补全**（stats-w3w4.json 已有初值但未走完验证链）
3. **跨 run 矛盾审计**：8 个 C0 run 之间的判定矛盾（同一节点有的 run h=1 有的 h=0，evidence 是否站得住）、hit-matrix 与 prior-estimates 的内部一致性
4. **漏洞清单**：对照 gap-analysis 的 Q2（为什么业界没做这么细）逐条检查我们的协议是否踩了同样的坑
5. **加速/优化机会**：哪些步骤可以机判化（参考 R5.2 系列的做法）、哪些可以并行

## 【输入材料】（都在 main 上）
- `bench/rubric-v3/DRAFT-rubric-v3.md`（origin/rubric-v3 分支，git show 取）— 完整草案含 O1-O4/P1-P4 定义、变体矩阵 V0-V3、候选集扩展指令
- `bench/rubric-v3/ablation/` — TASK-ablation.md（原任务书）+ gold-tree.md（31 节点）+ hit-matrix.json + prior-estimates.json + ablation-result.md + stats-recomputed.json + stats-w3w4.json + judge-blindtest-r1.json（独立 judge 盲测）+ runs-C0-run1..8.md
- `receipts/rubric-v3-gap-analysis.md`（git show aea3d6b:receipts/rubric-v3-gap-analysis.md）— 28 bench 对比 + Q2 业界停点分析
- `bench/self-opt-tester/bench.md` — 已知缺陷清单（M4 高估源等）
- `tasks/R5-judge-blindtest-task-brief.md` + `tasks/R5.1-second-scorer-task-brief.md` — 前序盲测协议（复用其盲打纪律）

## 【执行分解】（runner 按此拆子 goal，每个子 goal 单独走 1-loop）
- **G1 矛盾审计**：hit-matrix 8run×31node 全量重判抽检（随机 30% 节点独立重判，报一致率）+ prior-estimates 的 p̃ 分布合理性检查（有没有系统性偏高/偏低）+ 输出矛盾清单（每条带 evidence 引用）
- **G2 构念效度根因**：blindtest 1/5 否决的三个失败节点逐个解剖——是 w 算错了、h 判错了、还是 gold 标注本身有争议？给出根因分类 + 修复方案（改公式/改标注/接受降级）
- **G3 W3/W4 收尾**：stats-w3w4.json 的方案补完验证（对照 G2 根因判断哪个方案值得救）
- **G4 漏洞对照**：gap-analysis Q2 五条结构性解释逐条对照我们的协议，标「已规避/未规避/部分规避」+ 证据
- **G5 优化清单**：机判化候选（哪些判定能写成 assert 脚本）+ 并行化候选 + 成本估算
- **G6 综合报告**：`bench/rubric-v3/AUDIT-report.md` — 汇总 G1-G5，给出 rubric-v3 定稿建议（哪些维度保留/修改/废弃 + 理由），对标顶刊标准自评

## 【验收标准】
- 每个子 goal 有独立 loop-artifacts（01→04.5 全齐）+ commit + merge main
- G1 一致率数字可复算（抽检脚本落盘）
- G2 根因分类每条有 evidence（引用具体文件行号/JSON path）
- G6 报告含「与 ResearcherBench/RACE 的差异表」+「负面结果声明」（哪些假设被证伪，明确写出来不藏着）
- 全程不改冻结数据（hit-matrix/prior-estimates/gold-tree 只读；要改必须开新文件 + APPROVALS 登记）

## 【失败降级】
- 网络受限导致无法核外部文献 → 用仓库内 gap-analysis 已有 28 条 survey 数据，标注 unverified
- 某个子 goal 卡死（如 G2 根因不可判）→ 登记边界类型（信息边界/数学边界）后跳到下一个子 goal，不阻塞整链
- max-turns 耗尽 → 停在当前子 goal 收口处，queue 里留好断点，下次续跑

## 【选题依据】（为什么这不是 trivial 工作）
- 直接决定 rubric-v3 能否定稿 → 影响后续所有 pipeline 评分实验的效度
- 包含真正的研究判断（构念效度根因 = 方法论问题，不是工程修补）
- 对标 gap-analysis 的 28 bench 坐标系，产出可放进论文的证据链
- 负面结果同样有价值：如果 surprisal 加权确实不成立，正式降级比硬撑更有学术价值
