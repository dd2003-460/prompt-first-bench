# origin: ai — 任务书：T8-C3-v3 fullloop 异源 judge 复判（arena agent mode）

> 派发目标：LMArena agent（pfb 仓库，复用既有会话）
> 本任务只涉及 prompt-first-bench/main，忽略历史中其他仓库的消息。
> 背景：r277 收口报告确认同源 judge（qwen3.8-27b 既生成又裁判）是 conf 升档的唯一瓶颈。
> r268 同源重放显示 S02 长工件 J2 判分崩塌（κ<0.4），G2 spread 由噪声贡献。
> 异源 judge 对同一 18 工件复判 = 唯一解锁路径。

## 【强制段】
你是 LMArena agent，工作仓库 = dd2003-460/prompt-first-bench，分支 main。先 `git pull` 到最新。
严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造评分。
完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份（如可知）。

## 【目标】
对 T8-C3-v3 fullloop pilot 的 18 份阶段工件做独立双判官（J1-strict-v3 + J2-lenient-v3）逐条目审计，
作为本地 qwen3.8-27b 同源 judge 的异源交叉验证。若你能自报底层模型家族（非 Qwen family 即满足隔离要求），写进回执。

## 【背景】≤10行
- 实验：3 配置（A-full 完整 / B-nofreeze 删 freeze / B-none 全删）× 2 域（D1-meeting-room / D2-file-collab）× 3 阶段（stage01/02/03）= 18 工件。
- 工件路径：`experiments/T8-matrix/runs/c3-v3/runs-fullloop/pilot/{config}/{domain}/stage{NN}.md`
- Judge prompts（冻结版 v3-final）：`experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json` 的 `prompts.J1-strict-v3.text` 和 `prompts.J2-lenient-v3.text`
- 条目清单由你从工件正文提取（规则见下方【条目提取规则】），注入 prompt 末尾「条目清单：...」段
- 本地同源基线（r268）：`experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r268-same-source-replay.json`——你的任务不是复算它，而是独立重打
- **盲判纪律**：不要先看 r268 里的本地分数再打分。打完全部 36 cell（18 工件 × 2 判官）后再对照

## 【条目提取规则】（与 r268 replay 脚本同版正则策略）
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

## 【评分协议】（逐 cell 执行）
对每个 (config, domain, stage) 工件：
1. 读工件全文（`pilot/{config}/{domain}/stage{NN}.md`）
2. 按【条目提取规则】提取条目清单
3. 用 J1-strict-v3 prompt 判一遍 → 输出 JSON
4. 用 J2-lenient-v3 prompt 判一遍 → 输出 JSON
5. 两个 JSON 都 append 到结果文件

Judge prompt 使用方式：将 prompt text 作为 system message，user message = 工件全文 + "\n\n条目清单：" + 逗号分隔的 id 列表。

**纪律**：
- 每批 ≤6 cell（3 工件 × 2 判官），打完一批立即 append 到结果文件并 commit+push（防丢）
- 同一 cell 只打一次分，不回头改
- 如果某工件正文中找不到某个提取出的 id，verdict=fail 且 note 写「正文未找到该条目」（与 prompt 规则一致）

## 【执行分解】
- 批次 1：A-full/D1（stage01+02+03）× J1+J2 = 6 cell
- 批次 2：A-full/D2（stage01+02+03）× J1+J2 = 6 cell
- 批次 3：B-nofreeze/D1（stage01+02+03）× J1+J2 = 6 cell
- 批次 4：B-nofreeze/D2（stage01+02+03）× J1+J2 = 6 cell
- 批次 5：B-none/D1（stage01+02+03）× J1+J2 = 6 cell
- 批次 6：B-none/D2（stage01+02+03）× J1+J2 = 6 cell
- 每批结束：append `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-results.jsonl`（一行一 JSON）→ commit → push

JSONL 格式（每行一个 JSON）：
```json
{"cell": "A-full/D1-meeting-room/stage01", "judge": "J1-strict-v3", "items": [{"id":"F1","verdict":"pass","tests_failed":[],"note":""}], "summary": {"total": 31, "passed": 28}, "model_identity": "<自报或 unknown>"}
```

## 【失败降级】
- 工件缺失 → 该 cell 标 `"error": "artifact_missing"` 跳过，不阻塞
- 条目提取为空（工件无匹配 id）→ 该 cell 标 `"error": "no_items_extracted"` 跳过
- 中途 token 耗尽 → 停在当前批次收口处（jsonl 已落盘），回执注明完成到第几批
- 判分 JSON 解析失败 → 重试 1 次，仍失败标 `"error": "parse_fail"` 跳过

## 【交付物】（均在 pfb 仓库内）
- `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-results.jsonl`（36 行，18 cell × 2 judge）
- `experiments/T8-matrix/runs/c3-v3/runs-fullloop/arena-hetero-judge-summary.md`：
  - per-cell J1/J2 pass rate 表（18 行 × 2 列）
  - G2 spread 复算（同 domain 内跨 3 config 的 J1 mean 差 + J2 mean 差）
  - 与 r268 同源基线的逐格对照表（你的分数 vs 本地分数，Δ 列）
  - κ（Cohen's kappa，你的 J1 vs 本地 J1；你的 J2 vs 本地 J2）
  - 自报模型身份 + 置信度声明
- 回执：repo URL + branch(main) + 最终 commit_sha + 完成 batch 数 + 自报模型身份

## 【给 Lead 的备注】
- 边界：本任务只做 18 工件 × 2 判官的逐条目审计，不做 54-run 中间工件（R4/R5/R6）的复判（量太大，先验 fullloop 信号）
- 下一步归属：Lead 收到 jsonl 后本地复算 κ + G2 对比 + 与 r268 逐格对照 → 更新 T8-C3v3-final-conclusion 报告的 conf 层级
- 污染披露：本会话历史跑过 cross-judge 90/90 盲判（stage-ablation），定位 = 可复算样本，非完全 blind

## r269 本地降级复判（2026-11-04）

**Arena 通道故障**：ego-browser 打开 arena.ai/agent，登录态在（auth cookie），但会话列表为空（"No recent chats"）。之前的 pfb 仓库会话不在这个浏览器 profile 里，消息发不到 agent。根因：arena 会话与浏览器 profile 绑定，profile 切换/重置后会话丢失。

**降级方案**：qwen3.8-27b @ :8787 做 J1/J2 双判官，独立上下文 + temp=0。

**结果**（commit 7dd12cf）：
- κ mean = 0.4777（短工件 1.0，长工件 0~0.44）
- G2 = 10/12 PASS
- J2-lenient 在 S02 长工件上系统性崩塌（3 cell → 0），与 r268 一致
- J1-strict 更稳定（所有 18 cell ≥ 0.52）

**产出**：`runs-fullloop/receipt-r269-local-dual-judge.{jsonl,summary.md}`
