# T-PR-15 回执：文字目标函数的 Goodhart/hack 滚雪球调研

- **repo URL**：https://github.com/dd2003-460/prompt-first-bench
- **branch**：`arena/f65a5a27-prompt-first-bench`
- **commit_sha（工作提交）**：`b1f166144235334f3238e1bf2c0bd61a820044c1`
- **base**：`main` @ `6b86d3db11eba096b8df1c99c2d684899d0a93a2`（`git pull` 后 Already up to date，任务书在位）
- **执行日期**：2026-11-11 · loop/prompt-first 01→02→02.5→04→04.5 全程

## 交付物

| 交付物 | 路径 | 规模 |
|---|---|---|
| 主 survey | `research/text-objective-goodhart-survey.md` | 437 行 |
| 搜索日志 + 反方质询 | `research/search-log-text-objective.json` | 25 条检索 / 6 条质询 / 4 条负结果 |
| 交叉核验回执 | `research/web-llm/text-objective-crosscheck.json` | 2 服务 × 4 主张，0 回执 |
| AC8 交接脚本 | `research/web-llm/run_crosscheck.py` | Lead 本机可跑 |
| AC 校验器 | `loop-artifacts/stages/04/verify-t-pr-15.py` | exit 0 |
| 阶段工件 | `loop-artifacts/stages/{01,02,02.5,04,04.5}/T-PR-15-*.md` | 5 份 |

## 五条判决

| 子问题 | 判决 | conf |
|---|---|---|
| Q1 理论边界 | 部分成立 —— Goodhart 是更宽的伞（4 类机制），但"最一般形式"在文献中无统一裁定；spec gaming ⊂ / ⊃ reward hacking 两种用法并存（取决于"奖励"是否限 RL 标量） | 0.75 |
| Q2 LLM 特有 hack 形态 | 成立 —— 5 子类各有 2-3 个可定位案例；最硬的一条是重复列表攻击使 Claude-v1/GPT-3.5 判定失败 91.3%，GPT-4 仅 8.7% | 0.8 |
| Q3 文字 vs 数值 | 部分成立 —— A 弱 / B 强 / C 强；v17 病根 = **C（recall-only 代理缺精度项）+ B（正交性约束遗漏）**，A 不适用；"文字更易 hack"只有机制论证，无对照实验，且有反例（二值答案匹配鲁棒、非文字污染也能虚高 15%） | 0.72 |
| Q4 防御谱系 | 部分成立 —— 9 条中 6 条 prompt/判据层可做；最有效是"覆盖度→F_β 精度项"（2610.33512：胜率 10.6%→68.0%，长度降 2.6×）+ 硬预算；reward clipping 因保序而基本无效 | 0.7 |
| Q5 与 pfb 主线 | 成立（机制层）—— pfb rubric 4/6 维（M2/M3/M5/M6，合计权重 0.55）是可机械计算的计数型 proxy，与 S_α 同类；现有防御覆盖 Q4 的 D5/D8/D7，漏 D2/D3/D4 | 0.78 |

## 对 v17 修法（摘要，全文见 survey §7）

1. S_α 改 recall×precision（F_β），对每节点判 `necessary`（是否引入父 claim 无的新变量/约束）+ `correct` —— prompt/代码层可做
2. 加硬预算 `max_nodes/max_rounds/per_layer_cap`（~100 而非 1930），必须与 1 同发 —— prompt/调度层
3. 停止判据从"还能产生新数值吗"改为"新节点是否引入新变量/约束"，"新数值"降为必要非充分 —— prompt 层
4. dedup 从前 40 字符改语义+结构双指纹 —— 代码层
5. 留出 6-8 个真实正交维度做 gold —— 评测层
6. 加抗刷回归门禁（同义变体/纯数字变体/格式膨胀）—— 测试层
7. 训练侧冗余惩罚 —— **不可行**（硬约束：不改权重）

## AC 结果

| AC | 结果 |
|---|---|
| AC1 ≥300 行 | ✅ 437 |
| AC2 ≥20 源 / ≥10 全文 / 带 ID | ✅ 31 / 15 / 全部带 arXiv ID 或 URL |
| AC3 Q1-Q5 判决 + conf | ✅ 5/5 |
| AC4 Q2 五子类案例 | ✅ 5/5（(b) 一手原文标 `[待核验-原文]`，已用两处独立转述交叉确认） |
| AC5 Q3 三假设分级 + 病根 | ✅ 弱/强/强 + C+B |
| AC6 ≥3 反方质询 | ✅ 6 |
| AC7 ≥3 条可落地 + prompt 层标注 | ✅ 7 条（6 可做 / 1 标不可行） |
| AC8 ≥2 LLM 服务交叉核验 | ❌ **未满足（环境限制）** |

## 通道故障（按任务书要求如实上报）

- **AC8**：`research/web-llm/run_crosscheck.py` 对 A（`127.0.0.1:8787` qwen3.8-27b）与 B（`127.0.0.1:8788` 第二家族）各发 4 条主张，**8/8 失败**，错误 `URLError: [Errno 111] Connection refused`。沙箱内无任何 LLM endpoint、无 API key 环境变量。→ 按【失败降级】"沙箱够不到 Lead 本机 endpoint 是环境限制不是故障"，已交设计+脚本+回执骨架，**survey §0 全表 conf 已整体下压一档**。Lead 本机执行 `PFB_LLM_A_URL=... PFB_LLM_B_URL=... python3 research/web-llm/run_crosscheck.py` 即可补齐。
- **bash 出网**：`curl export.arxiv.org` 返回空（白名单只有 github/npm/pypi），所有来源核验改走 `fetch_page` 逐条开页面确认标题作者。

## 边界遵守

- **未改任何代码**：`git status --porcelain experiments/ bench/` = 0 行（`s5_hierarchy.py` / `score.py` / `gates.py` 未触碰）；修法建议仅存在于 survey §7。
- 未重复 surprisal survey 的 D1-D4/D6；仅延伸其 D5。
- 未把 2026 预印本（2605.12474 / 2610.33512 / 2609.19101 / 2602.17170 / 2507.05619）当作"已确立事实"，只用其机制与量级，风险记于 survey §8-C5。

## 建议 Lead 下一步

1. 补跑 AC8（5 分钟，本机）。
2. 决定是否采纳"建议 1+2+3"最小组合改 v17 停止判据；不建议单独加预算。
3. 若要把 Q5 从"机制成立"升到"强成立"，需做一次 pfb rubric 对抗实测（用 survey §7 建议 6 的攻击样例打 M2-M6）。
