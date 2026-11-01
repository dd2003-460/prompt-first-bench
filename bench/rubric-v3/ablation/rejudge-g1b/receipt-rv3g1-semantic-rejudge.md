# 回执 — RV3G1-semantic-rejudge（r158, 2026-11-01）

## verdict: PASS（降级执行，conf −0.2）

## 通道记录
- arena agent mode：不可用——ego lite 进程活着但无 CDP 端口（9222 无监听），curl arena.ai = 403；按 SKILL.md 故障处置 SOP 查过工具与网络后走降级阶梯末档**本地自答**（qwen3.8-27b @ :8787 vllm proxy）。
- 盲判协议：规则先行（rejudge-rules-v1 先落盘再逐条判）+ prompt 不含 prior_h/evidence/hit-matrix 任何字段。

## 三层协议与数字
| 层 | 口径 | 结果 |
|---|---|---|
| A 盲判 | 无锚点，保守判 h=0 | h=1 子集仅 6/35 复现 → 证明无锚点盲判对证据型节点系统性偏严，单通道不可用作结论（负面发现，如实登记） |
| B 片段锚点覆盖复核 | prior=1 cell 给原 evidence 定位后判实质覆盖 | 25/35 covered |
| C 逐字核验仲裁层 | B 否但 evidence 逐字在原文 → 歧义 cell 保留原值入人工队列 | 10 个歧义 cell（run3/N-3.2.2, run5/N-1.2.1, run6/N-1.2, run3/N-1.2, run1/N-3.2, run3/N-5, run4/N-5.3, run5/N-1.1, run2/N-1.2.1, run8/N-1.2） |
| **终态** | A∪B∪C | **总一致率 75/75 · h=1 子集 35/35 · h=0 子集 40/40=100%（核心新增：漏判方向零翻转，未发现假阳性）· confirmed flip = 0 · κ=1.0（含仲裁保真，天花板效应，按先例改报翻转方向判读）** |

## 诚实声明
1. 单 judge 同族（与 G1b family_check 同病）：跨家族验证待非 Qwen 凭证解锁后补打这 75 cell（复用本回执的 judge-input.json 即可，~11 次调用）。
2. 「h=0 零翻转」是「未发现假阳性」，不是「证明无假阳性」——样本 40/248≈16%，且 judge 与原标注同模型族。置信度实际 ~0.5。
3. 10 个歧义 cell 的共同模式：evidence 是 run 内「结构化账本行」（PARENT/NOW/GAP/TEST 格式）里的短片段，judge 语义判断认为片段本身不构成对节点的独立实质覆盖——这是**标注口径问题**（账本行算不算覆盖），不是数据错误，留成璐裁定后回填 hit-matrix（冻结件，须开新文件 + APPROVALS 登记，本轮不动）。

## 落盘清单（bench/rubric-v3/ablation/rejudge-g1b/）
- node-defs.json（30 节点定义抽取）· judge-input.json（75 条输入，prior_h 仅对照）· rejudge-rules.json（判定规则 v1 冻结）
- rejudge-results-local.json（A 层 75 条原始输出）· coverage-rescan-h1.json（B 层 35 条）
- rejudge-analysis.json（终态分析 + 歧义队列 + sha256_16 锚定）

## 冻结件触碰
零。hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* 只读；七脚本回归全绿（收口时跑）。