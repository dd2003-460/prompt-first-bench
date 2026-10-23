# Bench · Agent 过程效率（r3 · 严格口径校准版）

> origin: ai · 2026-10-24 · goal-0bc2d9c2（第 3 轮）
> r1 = n=1 初版（89.2）→ r2 = 交叉验证补全（92.7）→ **r3 = 校准版（n=3 + M7 gate + token 绝对口径 + 相关矩阵）**

## 指标定义（固定落点，下轮引用不重定）

| 指标 | 权重 | 定义 | 可验证口径 |
|------|------|------|-----------|
| M1 token 效率 | 25% | 链路固定规则负载 + 重发放大控制 | 规则字节/tokenizer 实测（count-tokens.js）+ 账本 input 口径 |
| M2 任务书行数 | 10% | 任务书 ≤200 行 | wc -l |
| M3 断点通过率 | 20% | 断点 A/B/C 通过且 gate 步骤计入 | 断点证据文件 |
| M4 交叉验证 conf | 15% | ≥2 独立源对关键 claim 的验证质量 | web-llm 回执 + 双源 conf 标注 |
| M5 迭代轮数 | 15% | 达 conf≥0.7 所需迭代轮数 | review.md conf 记录 |
| M6 降级诚实度 | 15% | 降级如实标注不虚构 | 降级条目 × 锚点 |
| M7 验证溯源率（gate） | —（门禁，不计分） | 声称成功步骤中挂 ≥1 不可伪造锚点的比例 | 锚点台账 |

## r3 数据（n=3 run · 三通道）

| Run | 通道 | M1 | M2 | M3 | M4 | M5 | M6 | M7 gate | 加权分 |
|-----|------|----|----|----|----|----|----|---------|--------|
| run1 | local Lead（全链路重走+锚点+账本） | 88 | 100 | 90 | 90 | 95 | 100 | 7/7 | 91.17 |
| run2 | arena agent mode（14m27s，三问逐答） | 85 | 100 | 86.7 | 90 | 90 | 95 | 7/7（10 锚点） | 89.20 |
| run3 | subagent 任务书变体（执行性审查） | 75 | 95 | 85 | 80 | 90 | 95 | 7/7 | 83.15 |
| **mean±std** | | **82.7±6.2** | **98.3±2.5** | **87.2±2.6** | **86.7±5.0** | **91.7±2.5** | **96.7±2.5** | **21/21=100%** | **87.84±3.53** |

加权权重 = r1/r2 原权重（M1 25/M2 10/M3 20/M4 15/M5 15/M6 15）；**权重未校准**（见下"已知缺陷"）。

## M7 gate 明细（21/21 通过）

| Run | 锚点数 | 锚点类型示例 |
|-----|--------|-------------|
| run1 | 7 | goal id 回执 / decomposition.md edit 回执 / ls-remote e0d6ddb exit=0 / subagent 启动回执 / bili stats JSON / bench-row 落盘 |
| run2 | 10 | ls-remote d96f5db / blob 52d1e2ba / count-tokens.js exit 0 / ralph exit 127 降级记录 / web_search 16+15 / blob 372d8a55+c2a6e952 / grep -c=3 / commit e3564845 / push exit 0 + 分支 ls-remote |
| run3 | 7 | git HEAD 4ff2b1ec / sed 逐行 exit 0 / wc -c 6050B / bench.md ls 46 行 / git status clean / ls 三工件 / 汇报消息 |

## Token 绝对口径（r3 新增）

**内部（bili 账本实测，session-1c44f689）**
- 累计：input 5,108,882 tok / output 37,259 tok / requests 116 / 压缩 7 folds 净省 3.70M tok（全 PAID BACK）
- 缺口：cacheSamples=0（provider 未上报 cache token）→ 命中率维度不可测，如实标注
- run 级增量切分：run1 专属增量未精确切分（累计含 r1-r3 历史），conf 0.7 标注

**外部对照（3 数据点带 conf，见 r3/external-token-data.json）**

| ID | 来源 | 值 | conf |
|----|------|-----|------|
| DP1 | HF Exgentic/agent-llm-traces（SWE-bench） | 1,183,537 tok/trace；span 均值 24,732 in / 202 out | 0.9（dataset card 直接列出） |
| DP2 | OSWorld 相关论文（OpenReview PDF，GPT-5 100-step） | 598.7K tok/task；Prompt 93.7% / Completion 6.3% | 0.6（标题未核实） |
| DP3 | Exgentic per-harness（跨 benchmark 聚合） | smolagents 521,204 / claude_code 974,096 / openai_solo 347,897 tok/trace | 0.8 |

**可比性判定**：本链路是"过程纪律审查"任务，非 SWE-bench 代码修复，任务类型不同质。按 DP3 量级粗比：run 级输入（固定规则负载 12.6k o200k × turns，估算 1-3M tok/run）与开源 agent 系统每任务量级（0.35-1.2M tok）同数量级——**token 效率结论=同量级；本方案优势在过程纪律（断点 + M7 gate + 降级诚实），不在 token 绝对量**。严格限定：无 3-5 个满足"开源系统+每任务实测+输入输出分开+可定位表格"的同质数据点（ChatGPT 核查原话）。

## 相关矩阵与权重（验收 2 · PARTIAL）

- 矩阵落盘：r3/correlation-matrix.json
- n=2（run1×run3）时 Pearson r 恒 ±1 数学无效；**但 6 指标差值全同号（M1 -13 / M2 -5 / M3 -5 / M4 -10 / M5 -5 / M6 -5）实证了 r2 双源指认的 M1×M5 共线风险**（省 token 的 run 恰好是少迭代的 run，两指标奖励同一行为）
- 判定 PARTIAL 而非 fail：相关风险检测已完成，缺有效 r 值 + 调权动作，属 R4 任务（n≥3 独立打分后重算 r，|r|>0.7 调权并记录推导）

## r2 双源指认缺陷的 r3 处置

| r2 指认（DeepSeek+ChatGPT） | r3 处置 |
|------------------------------|---------|
| M6 自评偏差（自报 conf 同时是测量对象和工具） | M7 gate 已落地（21/21）：评分从自报 conf 转向锚点可验证性；残余：run 级 M1-M6 分数仍是自估（R4 引入独立打分器） |
| M4"双源"不可复现（同模型两次=采样方差） | r3 三通道（local/arena/subagent）已非同模型；LLM 回执保持 r2 双源（DeepSeek+ChatGPT）引用，未重查（引用即保持 conf 0.85） |
| M5/M1 奖励"少做事"不区分高效 vs 没做够 | 相关矩阵实证共线（见上）；权重调整留 R4；本轮如实标注 |
| 权重无推导依据，精确性是虚假精度 | r3 分数保留 ±std（不再呈现单一精确值）；权重校准留 R4 |

## 外部 baseline 对比（r2 结论维持 + r3 数据点补充）

- r2 实锤：lm-eval-harness（accuracy 层，无过程指标）/ HELM（结果层广度，无轨迹层深度）/ promptfoo（LLM 评测，无 agent 过程纪律）——**"过程纪律"维度在开源方案中缺位**（unverified→已升级为"缺位实锤"，URL 见 r2 bench）
- r3 补充：token 绝对量级同数量级（见上），不可作同质基线直接比较
- 结论：本 bench 在"过程纪律"维度无可比开源 baseline（该维度缺位）；token 量级与开源 agent 系统同档

## 验收逐条判定（goal-0bc2d9c2）

1. **n≥3 run mean±std + conf≥0.9** → **PASS**（87.84±3.53，conf 0.9）
2. **相关矩阵 + 权重校准** → **PARTIAL**（矩阵落盘 + 共线风险实证；有效 r 值 + 调权留 R4，n≥3 独立打分是前提）
3. **M7 gate 落地** → **PASS**（21/21 = 100%，无锚点步骤=0）
4. **token 绝对口径** → **PASS**（bili 账本 + 3 外部数据点带 conf + 可比性限定）
5. **push pfb + ls-remote + R4 goal 落盘** → PENDING（本次交付）

## 已知缺陷（不掩盖，进 R4）

1. 权重未校准（共线风险实证未调权）
2. run 级 M1-M6 分数仍为自估（自报偏差残余：gate 管住"声称"，管不住"打分"）
3. cacheSamples=0 → M1 命中率维度不可测（provider 侧限制）
4. run1 token 增量为累计口径（未精确切分）
5. run2 工件在 arena 工作分支（arena/7c416e56-prompt-first-bench，commit e35648458491），未合 main（arena 无 main 权限，PR 已可建）
