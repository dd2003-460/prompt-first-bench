# 02 — RV3G6-o3-claim-rejudge-evidence-audit · 信息研究

> goal: hit-matrix 98 个 h=1 evidence verbatim 合规审计 · 分支 ralph/rv3g6-o3-claim-rejudge-evidence-audit · 2026-10-30

## F1 — run 文件结构事实（机算）

| run | 字符数 | 行数 | CRLF |
|-----|--------|------|------|
| run1 | 13064 | 374 | 无 |
| run2 | 4222 | 215 | 无 |
| run3 | 3313 | 182 | 无 |
| run4 | 2698 | 136 | 无 |
| run5 | 2017 | 123 | 无 |
| run6 | 4553 | 196 | 无 |
| run7 | 5835 | 233 | 无 |
| run8 | 5073 | 224 | 无 |

全部 LF-only，无编码变体 → current-goal 失败降级条款第 1 条（CRLF/空白归一化双轨）**不触发**，子串检查用原始文本即可。

## F2 — evidence 分布事实（机算，98 个 h=1 cell）

- 长度：min 5 / max 38 / mean 14.3 字符 → **零 cell 超 40 字**（C3 SIGNAL 分支当前面不可达，需变异测试证明可达性——同 r130「变异测试实证 reconstructable 分支可达」先例）
- h=0 cell 带 evidence：**0 个**（C5 当前面不可达，同样需变异实证）
- 重复 evidence 字符串：11 组（如「3090=350W」「$0.1/kWh」「3 年折旧寿命」跨多 run 出现）——**合法现象**（不同 run 独立写出相同短句），非违规；但提示 C4 张冠李戴检查的判定逻辑必须按 (run, evidence) 归属判，不能按字符串全局唯一性判
- 初步子串扫描（本阶段现场执行，非最终 verdict）：98/98 evidence 均为所属 run 全文连续子串，零改写 → **预期实跑 PASS exit 0**（负面结果可能性未排除，以 04 实跑为准）

## F3 — §3.2 口径声明 4「27/98」数字溯源（重要发现）

o3-claim-list §3.2 声明 4：「已核：98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token」。独立复算三种提取口径：

| 口径 | 定义 | 计数 |
|------|------|------|
| V1 = assert-o3-claim-list.py 现行实现 | per-line（节点 ID 所在行）token − 噪声豁免（ID 分段 + 一级前缀 + {0,1,31,4,13}） | **13**/98 |
| V2 = 全文件 token − 同噪声豁免 | 不限定节点行 | **34**/98 |
| V3 = per-line token，无噪声豁免 | — | **35**/98 |

**27 与三个口径均不一致**。V1/V2 差异来源目视确认：V2 额外命中的 21 cell 几乎全是「3090」（GPU 型号，gold-tree OC-1 卡片区有该 token）、「100」（A100/V100 型号段）、「90/9」（90:9:1 缓存比例）、「20」（tok/s）等——即 gold-tree **其他区域**（卡片规格区/示例区）的数值进入黑名单后的跨区命中。V1→27 无任何可复现路径。

**定性**：27 是 o3-claim-list 起草期的一次**不可复现人工计数**（或用了未落盘的中间口径）。影响面评估：声明 4 的**结论方向不受影响**——它要论证的是「evidence 含 gold 数值 ≠ 泄漏通道（这些是 run 自产文本被冻结进 hit-matrix，属 #13 假命中证据而非答案注入）」，该论证对 13/27/34 任一计数都成立（机制说明与具体数字无关）。但**数字本身失实**，且该声明是冻结件（o3-claim-list §6：修改 = 新 goal + APPROVALS 登记）。

**处置预注册**：本 goal 脚本只报 V1 口径（与既有 assert 同源，防双源漂移）+ 把「27 不可复现」作为审计发现落盘 04 日志；o3-claim-list.md 的数字勘误**不在本 goal 执行**（冻结件修改走 APPROVALS 登记 + 可并入下次触碰该文件的 goal，或单立小 goal）——导出候选见 A6。

## F4 — 与 r141 标准的对齐性

r141 judge-protocol-batch1.md §3 硬约束 3 对**新** rejudge 结果要求「evidence 是 run_text 连续子串」。本 goal 对**旧** hit-matrix 施加同一标准（C2）——标准对称后，M1 identity 锚点的数据基础才完整。若实跑发现旧数据有 FAIL，则 r141 的 M1 复算（h_claim vs h_id）所比的 h_id 侧含不合规 cell，需在偏离报告中显式标注（当前预判全 PASS，该分支为防御性设计）。