# origin: ai — 任务书：T8-C3-v3 rubric v3.2 异源盲判 replay（arena agent mode）

> 派发目标：LMArena agent（pfb 仓库，复用既有会话）
> created: 2026-11-06
> 本任务只涉及 prompt-first-bench/arena/t38-rubric-v32-replay，忽略历史中其他仓库的消息。
> 背景：rubric v3.1 的 arena 异源复判（36/36 cell，`arena-hetero-judge-results-v31.jsonl`）暴露两个形式脆弱点：
> §6-A 首行 code-fence 路由崩塌（B-nofreeze/D1/stage01、B-none/D2/stage01 两 cell J1 全灭 0/28、0/22，Δ=−1.000，占全部偏差 6.2%）；
> §6-B 交叉引用 id 口径黑箱（7 cell 分歧）。rubric v3.2 已冻结修复这两处（修形式不修语义），本次 replay 验证修复在异源条件下是否成立。

## 【强制段】
你是 LMArena agent，工作仓库 = dd2003-460/prompt-first-bench，分支 `arena/t38-rubric-v32-replay`。先 `git fetch` 到最新并记录 HEAD。
严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造评分。
完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份（如可知）。

## 【目标】
用 rubric v3.2 对 T8-C3-v3 fullloop pilot 的 18 份阶段工件做独立双判官（J1-strict-v3.2 + J2-lenient-v3）逐条目盲判，
回答一个问题：**v3.2 的形式修复是否在异源条件下消除了 §6-A 围栏崩塌与 §6-B 口径分歧。**

## 【背景】≤10 行
- 实验：3 配置（A-full / B-nofreeze / B-none）× 2 域（D1-meeting-room / D2-file-collab）× 3 阶段（stage01/02/03）= 18 工件。
- 工件路径：`experiments/T8-matrix/runs/c3-v3/runs-fullloop/pilot/{config}/{domain}/stage{NN}.md`
- Judge prompts（终版 **v3.2**）：`experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.2.json` 的
  `prompts.J1-strict-v3.text`（sha256_16: **8d83a0e3f8ebfe33**，2,368 chars）和
  `prompts.J2-lenient-v3.text`（sha256_16: b229dcc9a14b2081，不变）。
  **核验**：读文件后先算 sha256 前缀，不符则停止并记录，不要凭记忆编造 prompt。
  **注意用 v3.2 不是 v3.1**——v3.2 改动仅两处：①分解类特例的 fence-skip 显式化（正例+反例）；②id 锚定规则加交叉引用 fail 子句+例外子句。
- 条目清单由你从工件正文提取（规则见下方【条目提取规则】），注入 prompt 末尾「条目清单：...」段
- 上一轮异源结果（**禁止先看分数**）：`arena-hetero-judge-results-v31.jsonl`。打完全部 36 cell 后才允许对照。

## 【条目提取规则】（与 r268/r277 replay 脚本同版正则策略）
从工件正文提取以下模式的 id：
- `[A-H]\d+(\.\d+)?`（如 A1, B2.1, F1.1）
- `U\d+|K\d+|Q\d+|P\d+`（如 U1, K3, Q2, P5）
- `GAP-\d+`（如 GAP-1）
- `OQ-\d+`（如 OQ-2）
- `Gap[- ]?\w+`（如 Gap-1, Gap_1）
- `主张\s*\d+` → Z{n}（如 主张3 → Z3）
- `来源\s*\d+` → Z{n}（如 来源2 → Z2）
- `方案\s*[A-Z]` 或 `候选\s*[A-Z]`（后跟空白/冒号/逗号）→ P-{X}（如 方案A → P-A）
去重后排序，作为「条目清单」注入 judge prompt。

## 【评分协议】（逐 cell 执行，与 v3.1 轮完全一致，只换 rubric 版本）
对每个 (config, domain, stage) 工件：
1. 读工件全文（`pilot/{config}/{domain}/stage{NN}.md`）
2. 按【条目提取规则】提取条目清单
3. 用 J1-strict-v3.2 prompt 判一遍 → 输出 JSON
4. 用 J2-lenient-v3 prompt 判一遍 → 输出 JSON
5. 两个 JSON 都 append 到结果文件

Judge prompt 使用方式：将 prompt text 作为 system message，user message = 工件全文 + "\n\n条目清单：" + 逗号分隔的 id 列表。

**纪律**：
- 每批 ≤6 cell（3 工件 × 2 判官），打完一批立即 append 到结果文件并 commit（防丢；push 若 403 则在回执注明，Lead 会从对话提取）
- 同一 cell 只打一次分，不回头改
- 如果某工件正文中找不到某个提取出的 id，verdict=fail 且 note 写「正文未找到该条目」（与 prompt 规则一致）
- **重点观察（打分时自然发生，不用刻意）**：§6-A 两个围栏工件（B-nofreeze/D1/stage01、B-none/D2/stage01）首行是 ```markdown —— v3.2 规则要求跳过所有空行与 code-fence 标记行取第一个实质内容行。如实按规则执行即可，你的 verdict 就是 replay 的核心数据。

## 【执行分解】
- 批次 1：A-full/D1（stage01+02+03）× J1+J2 = 6 cell
- 批次 2：A-full/D2（stage01+02+03）× J1+J2 = 6 cell
- 批次 3：B-nofreeze/D1（stage01+02+03）× J1+J2 = 6 cell
- 批次 4：B-nofreeze/D2（stage01+02+03）× J1+J2 = 6 cell
- 批次 5：B-none/D1（stage01+02+03）× J1+J2 = 6 cell
- 批次 6：B-none/D2（stage01+02+03）× J1+J2 = 6 cell
- 每批结束：append `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-results-v32.jsonl`（一行一 JSON）→ commit

JSONL 格式（每行一个 JSON）：
```json
{"cell": "A-full/D1-meeting-room/stage01", "judge": "J1-strict-v3.2", "items": [{"id":"F1","verdict":"pass","tests_failed":[],"note":""}], "summary": {"total": 31, "passed": 28}, "model_identity": "<自报或 unknown>"}
```
注意 judge 字段写 `J1-strict-v3.2`（区别于 v31 文件的 `J1-strict-v3`）。

## 【失败降级】
- 工件缺失 → 该 cell 标 `"error": "artifact_missing"` 跳过，不阻塞
- 条目提取为空（工件无匹配 id）→ 该 cell 标 `"error": "no_items_extracted"` 跳过
- push 403（GitHub App token 只读）→ 继续本地 commit，回执注明"push 失败，数据在对话/本地 commit"，Lead 负责提取
- 中途 token 耗尽 → 停在当前批次收口处（jsonl 已落盘），回执注明完成到第几批
- 判分 JSON 解析失败 → 重试 1 次，仍失败标 `"error": "parse_fail"` 跳过

## 【交付物】（均在 pfb 仓库内）
1. `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-results-v32.jsonl`（36 行，18 cell × 2 judge，append-only；每批写完做行数唯一性校验：新总行数=旧+本批，校验输出留在 commit message）
2. `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-summary-v32.md`：
   - per-cell J1/J2 pass rate 表（18 行 × 2 列）
   - **§6-A 焦点核对**：B-nofreeze/D1/stage01 与 B-none/D2/stage01 两 cell 的 J1 pass rate（v3.1 轮为 0/28、0/22；验收线 ≥0.8）
   - **§6-B 焦点核对**：列出本轮 note 含「仅交叉引用」的 cell 数量（v3.1 轮为 7 cell 分歧）
   - 加权通过率（条目级）J1/J2/合计
   - G2 spread 复算（同 domain 内跨 3 config 的 J1 mean 差 + J2 mean 差，spread ≥ 0.10 = PASS）
   - 与 v3.1 异源结果的逐格 Δ 表（你的分数 vs `arena-hetero-judge-results-v31.jsonl`，只对照不看先验）
   - J1 vs J2 inter-judge κ（Cohen's kappa，条目级）
   - 自报模型身份 + 置信度声明

## 【给 Lead 的备注】
- 本任务是 v3.1 轮的**纯 rubric 版本升级 replay**：工件、条目提取、判官角色、批次划分全部不变，唯一变量是 J1 prompt（v3.1→v3.2）。
- 已知局限（Lead 侧裁定，不影响你打分）：两个围栏工件的首实质行分别是"# 阶段 02…"和"# 30人研发团队…"，按 v3.2 规则它们仍然不是分解类——这是语义决策（v3.3 范围），不是本次要修的。所以 §6-A 验收线 ≥0.8 可能因这两个工件仍被判非分解类而不达标；如实报告即可，Lead 会区分"形式修复生效但语义争议残留"与"形式修复未生效"。
- 结果将进 pfb 论文 rubric iteration section（v3.1→v3.2 消融证据）。