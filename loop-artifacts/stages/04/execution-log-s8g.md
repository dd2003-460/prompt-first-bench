# S8G 执行日志 — v3 gold-gap P1+A2+A3 (prompt patch) + B2 (research hook 验证)

> 日期: 2026-11-06 · 执行 agent · 任务卡 tasks/v3-gold-gap.md
> 范围: 本轮只做 P1 prompt patch + research_hook 调研源补充 + Q5 单题最小验证，**不跑完整实验**（P3 留给下轮）
> 硬约束遵守: 未读取 gold/ 目录任何文件；prompt patch 全部用通用原则措辞（无 L_comm / C_FP/C_FN / gold 维度名或结构）；只改 prompt 模板与 research_hook 配置，未动 judge/score 逻辑。

## 1. 做了什么

### 1.1 Prompt patch（A1/A2/A3 → 新臂 S8G）
- 新增 `experiments/stage-ablation/arms_new/S8G-p1-patch.md`：S8G 臂定义文档（S5 基线 + 三条叠加规则）。
- 新增 `experiments/stage-ablation/s8g_pilot.py`：runner，`build_prompt("S5", qid)` 基础上把 P1_PATCH 插在阶段 04.5 之后、【待解问题】之前；支持 `--no-hook`（纯 prompt 效果测试）/ `--dry-run`。
- 三条规则（中文通用原则，无泄漏）：
  - **A1 维度完备性**：分解树前先列出该问题域标准理论框架的全部候选维度类别（决策论损失分解 / 贝叶斯更新误差来源分类等），逐项核对覆盖，缺失必须补入或显式说明不适用。
  - **A2 空缺强制**：场景未给定数值的参数必须进「空缺清单」并标「需实测/需外部数据」，禁止填默认值/估计值；每个数值断言二选一——(a) 真实可定位 URL，(b) 显式标「理论推导，无实测依据」；都不满足则删除或降级为定性。
  - **A3 交叉验证口径**：「两个独立来源一致」要求两来源来自不同知识类型（理论 vs 模拟；文献 A vs 文献 B 且角度不同）；同一文档不同章节不算两个来源。

### 1.2 Research hook 调研源补充（B）
`experiments/stage-ablation/research_hook.py`：
- `ARXIV_QUERIES["Q5"]` 增加 3 组统计方法论域精准查询词：`statistical methodology reproducibility crisis` / `multiple comparisons correction p-value` / `effect size estimation bias small studies`。
- `KNOWN_SITES["Q5"]` 增加 3 个存活站点（已逐个 `_fetch_page` 验证 alive=True）：Replication crisis (Wikipedia)、Multiple comparisons problem (Wikipedia)、Effect size (Wikipedia)。Ioannidis 2005 无 arXiv 原文，用 Replication crisis 条目覆盖（注释已注明）。
- **fallback**：arXiv 相关结果 <2 条时打印 `[RESEARCH-GAP] {qid}: arXiv returned only N relevant result(s)...`（stderr），不再静默继续。

### 1.3 验证运行（C）
- `runs-r293/S8G-Q5-r1.json`：S8G prompt × Q5 题面 × 本地 qwen3.8-27b（127.0.0.1:8787, temp=0, max_tokens=8000），**不带 research hook**（sources=[]，纯看 prompt 效果）。wall 82.5s，out 8000 tokens（触顶截断）。
- `runs-r293/research-data/Q5-hook-test.json`：research_hook 对 Q5 关键词实跑（max_results=5 默认档），返回 5 条真实 URL。
- `runs-r293/scores-S8G-r1.json`：score.py（v3 rubric，M1/M4 走本地 27b judge，conf cap 0.7）评分结果。

## 2. Q5 跑分结果（S8G-Q5-r1）

| 维度 | S8G r1 | S5 基线 (r1/r2/r3) | 备注 |
|------|--------|--------------------|------|
| M1 | 1.00 | 1.00 / 1.00 / 1.00 | judge 判 3/3 decidable correct（uncertain 不计入分母） |
| M2 | 0.654 | 0.583 / 0.571 / 0.636 | 略高于 S5 均值 0.597 |
| M3 | 1.00 | 1.00 ×3 | hedge_count ≥3 满额 |
| M4 | **1.00** | 0.00 / 1.00 / 1.00 | 5/5 gaps identified（含先验敏感性、小样本功效、MCMC 成本、制度约束、损失函数具体数值） |
| M5 | **0.00** | 0.00 / 0.30 / 0.30 | 无 sources 注入 + 输出中无数值断言带 URL/「理论推导」标签 → anchored_rate_weighted=0 |
| M6 | **0.00** | 1.00 ×3 | 本次刻意不带 hook（sources 为空）→ no URLs to check |
| **Total** | **0.6923** | 0.5619 / 0.822 / 0.8369（均值 0.740） | n=1，方向性参考 |

**与 S5 基线 (Q5≈0.55–0.84，均值 0.740) 对比**：S8G r1 = 0.692，低于 S5 均值约 0.05。但差距几乎全部来自 M5+M6（合计权重 0.20/归一后 ≈0.222）——这是本轮**刻意不带 hook** 的代价，不是 prompt patch 的净效果。若只看 M1–M4（patch 直接作用面）：S8G M2/M4 均 ≥ S5 各 rep，M1 持平满分。**结论：P1 patch 在 M4（缺口覆盖）上稳定拉满（5/5 gaps），M2 微升；M5 是当前最大短板。**

## 3. Research hook 召回情况（Q5）

实跑 `research_hook("Q5", "scientific research methodology hypothesis validation peer review best practices")`，13.0s，返回 **5 条真实 URL**（全部存活）：

| # | 类型 | URL | 相关性 |
|---|------|-----|--------|
| 1 | arxiv | http://arxiv.org/abs/2012.04464v3 | BFF 推断桥接（Bayesian/frequentist/fiducial）— 高相关 |
| 2 | arxiv | http://arxiv.org/abs/1109.5278v1 | 统计推断谨慎度控制 — 高相关 |
| 3 | arxiv | http://arxiv.org/abs/1401.3084v1 | Bayesian vs frequentist 区间估计比较 — 高相关 |
| 4 | direct_site | https://arxiv.org/abs/2305.06980 | ⚠️ 低相关（凝聚态物理 dislocation 论文，历史遗留误配，建议下轮替换） |
| 5 | direct_site | https://en.wikipedia.org/wiki/Bayesian_inference | 高相关 |

- 新增的 3 个 Wikipedia 站点（Replication crisis / Multiple comparisons / Effect size）均已验证存活，但在默认 `max_results=5` 档被 arXiv 3 条 + 旧站点占满而未进入返回集；`max_results=8` 档实测可全部召回（8/8 alive）。
- `[RESEARCH-GAP]` fallback 未触发（arXiv 相关结果 ≥2）。
- 已知缺陷：第 4 条 `2305.06980` 是 T30 时期错误指向（标题写 "LLM Training Efficiency" 实际是辐射物理论文）——**属于既有 bug，非本轮引入**，列入下一步修复。

## 4. 归因与下一步建议

**归因**：
1. Total 0.692 < 0.80 验收线的主因 = M5/M6 双零（无 hook 运行 + 无锚点）。这是设计内的隔离测试，不是 patch 失败。
2. 输出触顶 8000 tokens 截断（末尾停在 MCMC 成本讨论中段）——S8G prompt（9690 chars）比 S5（9221）长 469 chars，加上 A1 要求的维度枚举使生成更长，存在截断风险。
3. A2 合规信号弱：输出出现「空缺清单」2 次，但「理论推导，无实测依据」标注 0 次——模型倾向把不确定数值写成 uncertain 叙述而非按 A2 的二选一格式落标，导致 M5 anchored_rate=0。

**下一步（P3 实验轮）**：
1. **跑带 hook 的 S8G-Q5**（`python s8g_pilot.py --qs Q5 --reps 2`）：注入 5 条真实来源后重测 M5/M6，这才是 patch+hook 组合的真实分数，预期 M6 回到 ~1.0、M5 取决于模型是否引用注入来源。
2. **修 KNOWN_SITES["Q5"] 第 4 条**：把 `arxiv.org/abs/2305.06980`（误配）换成真正的方法论文献（如 Ioannidis 2005 的 PMC 页面或 OpenScience 可重复性项目页）。
3. **A2 强化**：若带 hook 跑仍 M5<0.3，在 P1_PATCH 里把「理论推导，无实测依据」改成强制输出格式示例（给一个叶子卡片样例），降低模型自由发挥空间。
4. **防截断**：S8G 调用把 `LLM_MAX_TOKENS` 提到 12000，或在 A1 里限制候选维度类别枚举 ≤6 项。
5. 按任务卡 P3a 扩到 Q1/Q4/Q5 × 2 rep 全量对比 S5/S7V/gold，再决定是否需要 P4 迭代（≤3 轮）。

## 5. Commit

- `2bc9bf5` S8G: P1 prompt patch + Q5 pilot r1 (total=0.692, M4=1.0 gap-full-coverage, M5/M6=0 no-sources) + research hook stat-method queries
  （含 arms_new/S8G-p1-patch.md、research_hook.py、runs-r293/S8G-Q5-r1.json、scores-S8G-r1.json、research-data/Q5-hook-test.json）
- 本 log + s8g_pilot.py + hook-test 复测（默认 max_results=5 档）见后续 commit。