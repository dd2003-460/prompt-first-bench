# origin: ai
# Workshop draft 压缩规划 — 2026-11-24

## 为什么现在做（CFP 无关）

投稿第 5 项缺口 = 长度/页数适配。draft 现状 **18,097 词 / 120,749 字符**。
workshop 论文惯例 4-8 页 ≈ 3-5K 词 → 超 4-6×。

CFP 复查（2026-11-24 ego-browser, icml.cc/Conferences/2027/Dates, source ①）：
- 主会 abstract 2027-01-14 AoE / full 2027-01-22 AoE；workshops 8/5-6。
- **workshop 专属 CFP 仍未发布**（与 11-23 笔记一致，核验日期刷新到 11-24）。
- **venue 已锚定 = ICML 2027 workshop**（draft notes "Venue target: ICML 2027 workshop"，非猜测）；workshop CFP 通常与主会同窗或略晚（主会 abstract 1/14 前会发）。
- 但压缩**方向**不依赖精确页数：workshop 几乎总是 4-8 页，砍什么/移 supplementary 现在就能定。
  精确页数只影响"砍到 4 页还是 6 页"，不影响"哪些段落该进 supplementary"。

## 结构分析（chars / words / 占比）

| 节 | chars | words | % | 压缩判定 |
|----|-------|-------|---|----------|
| Abstract | 8,608 | 1,282 | 7.1% | **砍 80%**：workshop 摘要 150-300 词，现 1,282 词。留 250 词核心 claim + 1 句 limitation。 |
| 1. Introduction | 3,248 | 478 | 2.7% | 保留，略压。 |
| 2. Setup | 6,001 | 879 | 5.0% | 保留，judge 定义可移 supplementary。 |
| 3. Related work | 5,692 | 815 | 4.7% | 保留（novelty 防御承重）。 |
| 4. Findings | 52,839 | 8,099 | **43.8%** | **主压缩目标**。L95 单行 24,488 字符 provenance 段 → 全移 supplementary。 |
| 5. Implications | 2,407 | 357 | 2.0% | 保留。 |
| 6. Limitations | 18,349 | 2,714 | 15.2% | **砍 60%**：workshop 不该 1/6 篇幅。留最狠 3-4 条 + 防御，其余移 supplementary。 |
| 7. Future work | 18,573 | 2,831 | 15.4% | **砍 70%**：同上。留 2-3 条最相关，其余移 supplementary。 |
| 8. Data & code | 1,217 | 138 | 1.0% | 保留。 |
| 9. References | 3,542 | 460 | 2.9% | 保留（21 refs 全留，投稿必需）。 |

## 巨型段落（>5000 字符单行）

| 行 | chars | 内容 | 处置 |
|----|-------|------|------|
| L9 | 8,591 | Abstract 本体 | 砍到 250 词 |
| L95 | 24,488 | §4 provenance 巨型段（judge_v2_depth 来源 + 数字核验层） | **全移 supplementary**（正文留 1 句"provenance 见 supplementary S-X"） |
| L119 | 6,013 | §4 finding 4（conclusion layer 0/15） | 压到 3 句 |
| L161 | 8,084 | §7 future work 首条 | 压到 2 句 |
| L163 | 8,855 | §8 data note（queued experiments） | 移 supplementary |

## 压缩目标（2026-11-24 11:30 词数模拟修正）

**词数模拟（source ① execute_code）**：总 18,148 词。四动作（provenance 3,770 词全移留 1 句 / abstract 1,282→250 / §6 2,714 砍 60% / §7 2,831 砍 70%）后 = **9,752 词**。

**规划原档位（3.5-6K）不可达**——四动作后还差 3.7-6.3K 词。缺口在 §4 Findings（43.8% 字符，provenance 移出后仍是大头）+ §2 Setup + §3 Related。

| 档位 | 词数 | 四动作后需再砍 | 来源 |
|------|------|--------------|------|
| A（保守） | ~6,000 | 3,752 | §4 非承重 finding 段 + §2 judge 定义 + §3 部分近邻 |
| B（标准） | ~4,500 | 5,252 | A + §4 更多 finding 移 supplementary |
| C（激进） | ~3,500 | 6,252 | B + §3 related 大幅压 |

**承重 claim 清单（subagent 在飞）决定哪些 §4 finding 可移**——承重 claim 必须正文可见，非承重的移 supplementary。

## 不动的承重件（压缩红线）

- 21 References 全留（投稿必需，字母序已验）。
- 承重数字（断点 325 / 阈值 0.3185 / n=3 cov 0.2174 / 1.21× se / cor 0.805）压缩后必须在正文可见，不能全移 supplementary。
- novelty 防御（related work 3 条 handoff 近邻定位）保留。
- §4.4 KV cache ≠ 树 JSON checkpoint treatment 界定保留（T-PR-17 建议 8）。
- 括号差 0 / 0 TODO 状态压缩后必须保持。

## 执行顺序（等 CFP + Q7 定型）

1. **等 Q7 落地**（~11h，15 runs）→ 定 §4/§7 的最终结论（Q7 是第三域，可能改 findings）。
2. **等 CFP 发布**（workshop 组织者单独发，通常晚于主会）→ 定页数档位 A/B/C。
3. 两条件满足后做压缩 pass：先移 supplementary（机械，可脚本化），再砍 abstract/limitations/future work（判断，Lead 做）。
4. 压缩后重跑四条件核验（结构/质询防御/承重数字/引用）+ 括号差 0 + 0 TODO。

## 现在能做的（CFP 无关，不等）

- 本规划落盘（已完成）。
- supplementary 索引文件扩展：把 L95/L163 等要移的段落预先编号（S-8/S-9...），压缩时直接搬。
- **不现在砍 draft 本体**：Q7 在飞，结论可能变，现在砍了 Q7 落地要重做。
