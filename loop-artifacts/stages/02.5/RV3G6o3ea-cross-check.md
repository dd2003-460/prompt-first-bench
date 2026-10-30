# 02.5 — RV3G6-o3-claim-rejudge-evidence-audit · 交叉核对

> goal: hit-matrix 98 个 h=1 evidence verbatim 合规审计 · 分支 ralph/rv3g6-o3-claim-rejudge-audit... (ralph/rv3g6-o3-claim-rejudge-evidence-audit) · 2026-10-30

## X1 — TASK-ablation 原文 vs 预注册判定语义（逐字对照）

TASK-ablation.md Step 1 原文：「每个 h=1 必须附 evidence，evidence 必须是 run 文件里真实存在的句子（不许改写）」+ 输出格式行「evidence: "产出中的原文片段≤40字"」。

| 预注册检查 | 原文依据 | 对齐性 |
|-----------|----------|--------|
| C1 非空 = FAIL | 「每个 h=1 必须附 evidence」 | ✓ 硬约束直译 |
| C2 连续子串 = FAIL | 「必须是 run 文件里真实存在的句子（不许改写）」 | ✓ 从严机判化（「句子」→「连续子串」，同 r141 X5 同款选择；比整句边界更宽松——不要求标点/句尾对齐，只禁改写与拼接） |
| C3 >40 字 = SIGNAL | 「≤40字」出现在**输出格式示例**而非验收条款 | ✓ 惯例非门禁 → SIGNAL 定位正确 |
| C4 张冠李戴 = FAIL | 「run 文件里」（所属 run 的隐含限定） | ✓ 子类单列，增强定位 |
| C5 h=0 带值 = SIGNAL | 原文无对应义务 | ✓ 冗余暴露非违规 |

## X2 — 重复 evidence 与 C4 逻辑的冲突排除

F2 发现 11 组跨 run 重复字符串（如「3090=350W」同时是 run2/run3/run4/run5 各自 evidence）。若 C4 实现为「evidence 在全局 run 文本中唯一归属才合法」，这 11 组将全部误报。预注册实现：**C4 仅在 C2 已 FAIL（evidence ∉ 所属 run）时触发**——在别的 run 找到该字符串才升级为「张冠李戴」诊断；C2 PASS 的 cell 即使字符串跨 run 重复也不报（各 run 独立写出相同短句 = 合法）。此逻辑写入 docstring 防实现漂移。

## X3 — V1 口径锁定理由

§3.2 声明 4 复算三口径（F3）均 ≠ 27。脚本采用 V1（assert-o3-claim-list.py 现行 per-line − 噪声豁免）的理由：(a) 与仓库内既有 assert 同源，避免第三个口径引入双源漂移；(b) V1 是**最严黑名单**（token 必须出自该节点自身行），V2/V3 的额外命中多为型号/比例类跨区 token，信号价值低。脚本输出同时报 V1 计数 + 声明值 27 的 mismatch 注记（事实暴露，不改冻结件）。

## X4 — 预期结果的风险声明

F2 初步扫描 98/98 子串 PASS——若 04 实跑确认全 PASS，本 goal 产出 = 「验证链补环」（把从未机判过的硬约束变成 exit 0 事实）+ 「27 不可复现」负面发现。这是**正面结果为主**的 goal，但研究质量线要求：PASS 不等于无发现——27 数字失实本身就是对 o3-claim-list §3.2 精确性的负面结果，必须如实落盘并导出勘误候选，不得因主 verdict PASS 而淡化。