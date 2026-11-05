# C3 v3 · G1 盲标+仲裁协议设计（阶段 01 工件）

**goal**: T8-C3-v3-paired-runs（WORK_QUEUE P1）· **子 goal**: G1 judge 盲标+仲裁备料
**日期**: 2026-10-31 · **执行**: Hermes keepalive r27 后轮
**状态**: 设计落盘；G1 实际执行被「judge 家族隔离」阻塞（见 §5），本工件 = 可重入执行清单 + 校准集冻结材料

## 0. 为什么先做 G1（动机）

C3 v3 的验收门禁顺序是 R5 judge 校准全过 → R1 三道地板 → R4 全因子 runs → 主分析。
R5 的第一道就是「换位双判 + κ≥0.6 + 长度去偏 + 家族隔离」。不做 G1 直接跑 48 个 paired run，
等于用未校准的尺子量 48 次——裁决器有偏差时所有 M8 分数一起漂，事后无法区分「配置效应」和「评分器偏差」。
所以 G1 不是流程装饰，是整个实验有效性的前置条件。

## 1. 术语定义（首次出现处）

- **M8-truth**：已执行核验条目的真实性率——每条核验主张过三测（具体性/可证伪/反事实）后的加权通过率。衡量「说了的核验是不是真的」。
- **M8-cover**：核验机会覆盖率——以任务输入预定义的「核验机会集」（开跑前冻结的应核验条目清单）为分母，遗漏/未执行计 0。防止「删掉 evidence 组件后难项退出分母、M8 反而抬高」的遗漏规避。
- **κ (Cohen's kappa)**：两个裁判去掉瞎蒙成分后的真实一致程度。0=纯随机一致，1=完全一致。R5 门槛 ≥0.6（中等以上一致才允许进确认性实验）。
- **双判**：同一份工件让两个独立裁决器各打一遍，比一致性。
- **家族隔离**：裁决器模型 ≠ 被测生成模型（qwen3.8-27b 是 Qwen 家族，裁决器必须非 Qwen），防同源偏好（裁判偏爱自家模型的写法）。
- **盲法**：裁决器不知道工件来自哪个 prompt 配置（A-full/B-nofreeze/...），只看到编号样本，防预期偏差。
- **仲裁**：双判分歧超阈值时由第三裁决器或 Lead 人工裁定，产出唯一金标准分。

## 2. 校准集构成（覆盖全部配置，R5 要求）

校准集 = 每个配置至少 1 个已有/将产出的完整工件。当前可用资产盘点：

| 配置 | 现有工件 | 来源 |
|---|---|---|
| A-full | T7.1 会议室预约系统全流程（stages/T7.1-*）+ T8-matrix-run-r1 网盘选型域 | 已完成，M8=1.00/1.00（conf-0.2 自复核） |
| B-sham | 无（需新跑 1 个 run 或用 sham 替换文本构造半合成件） | 待产 |
| B-none / B-nofreeze / ... | 无（paired runs 未开跑） | 待产 |

**结论**：校准集不能等 48 个 run 全跑完再建（成本翻倍且循环依赖）。采用两阶段：
- **G1a（现在可做）**：用 A-full 双域工件 + 阳性对照件（§4）+ 阴性对照件（sham 半合成）做「评分器内部一致性」校准——同族内双判 κ、长度相关性、扰动稳定性。这一步不依赖异源 judge，ninfer 单模型双 prompt 即可起步。
- **G1b（blocked-on-human）**：异源 judge 实测——需要 ≥1 个非 Qwen 家族的 LLM 服务（arena 通道或用户提供的 API key）。G1a 的 rubric 与切分方案冻结后，G1b 只需换 judge 重打同一批工件，成本可控。

## 3. M8 二分类化方案（质询点 3 的回应）

R5 要 κ≥0.6，但 M8 是 0-1 连续加权分。κ 需要类别变量，切分点引入任意性——处理：
1. **主口径不用原始 κ**：对连续分算 **ICC(2,1)（组内相关系数）** 作为一致性主指标（连续型对应物，无切分点问题），门槛 ICC ≥ 0.6。
2. **辅口径保留 κ**：按三测结果二值化（条目通过=1 / 不通过=0，逐条目级而非工件级），Cohen's κ 作交叉参照。条目级二值化规则在 intermediate-rounds-audit.md 三测中已定义，无新增任意性。
3. **双口径都报**：任一 <0.6 → 修 rubric；两者方向矛盾 → 登记边界，Lead 裁定。

## 4. 阳性对照件（评分器敏感度 · c3-diffs.md 已冻结）

取 T7.1 02.5 X5（Whatspot 月费五源矛盾 $25/$30/$2.50/$19/$16，原判定 U4 未核验）：
- 植入方式：把处置标记从「判为未核验 U4」改为「已解释：采信 S18 $25/月」，保留原始冲突数据不动。
- 预期：正确评分器应识别该退化（truth 分下降 + 指出「处置与证据不符」）。
- 失败判据：judge 给退化件 truth 分 ≥ 原件 → 评分器无敏感度 → 停止 M8 因果判读（c3-diffs.md 阳性对照节同款规则）。

## 5. 阻塞与降级路径

**硬阻塞**：G1b 家族隔离需要非 Qwen 裁决器。现状：
- ninfer :8000 只有 qwen3.8-27b（Qwen 家族）→ 只能做 G1a 同族双判（不同 prompt/温度，非同源隔离）
- arena 通道：curl -I https://arena.ai 返回 403（疑似 WAF/地区拦截），ego-lite 进程活着但未验证登录态 → 走 arena-outsource SOP 故障处置阶梯（先查工具网络，别找用户扫码）
- 用户决策项（CONTINUE_MSG 阻塞区已登记）：提供异源 API key 或授权 arena 通道

**降级声明**：若 G1b 持续不可达，C3 v3 只能出「同族 judge 下的方向性证据」，conf 降档标注（同 RV3G6-gmr-caliber-u3 web-llm unverified 模式），不得写「judge 校准全过」。

## 6. 下一步（G1a 可立即执行的清单）

1. 冻结校准集 v1：T7.1 全套 7 工件 + T8r1 全套 7 工件 + 阳性对照件（X5 植入版）+ sham 半合成件（B-sham prompt 跑 1 个 decomp 题，暂用 ninfer 同族）
2. 双判实现：ninfer :8000 同模型、两套 judge prompt（J1 严格版/J2 宽松版）、temperature=0、max_tokens≥2048
3. 计算：逐条目二值 κ + 工件级 ICC + Spearman(judge 分, 工件 token 数) 长度检查 + CALM 扰动（换措辞重打 1 次看分差）
4. 回执 JSON 落盘 receipts/c3v3-g1a-judge-calibration.json（kind: "ralph_web_llm_cross_check" 同构字段）
5. κ/ICC 全过 → 解锁 R4 全因子 runs 开跑许可（仍缺 G1b 异源，最终 verdict 标 partial）；不过 → 修 rubric 迭代

## 7. 禁区复核

- 冻结面零触碰承诺：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / DRAFT-rubric-v3-v2.md 等零改动
- c3-diffs.md 只读消费（阳性对照植入在其规定范围内，新文件承载，不改原文）
- 本工件纯新增，无行为变化

## 8. 本轮落盘清单（G1 备料 · 可重入）

| 工件 | 路径 | 验证 |
|---|---|---|
| G1 协议设计（本文件） | loop-artifacts/stages/01/C3v3-G1-blind-label-design.md | §2-§7 齐 |
| 阳性对照件（X5 植入版） | experiments/T8-matrix/runs/c3-v3/calibration/positive-control-x5-mutated.md | 仅 L15(X5 行)改动，sha 6a6ab4d8→03603991，+36 bytes；原件零触碰 |
| 8 配置 prompt 变体 + B-sham | experiments/T8-matrix/runs/c3-v3/prompts/<config>/{freeze,evidence,owner}.md + MANIFEST.json | A-full 与 loop/prompt-first/ 原文 byte-exact 断言通过；sham token 数 112 = freeze 行 112（±0%，在 ±10% 冻结容差内）；每配置三文件 sha256 前 16 位入 MANIFEST |

**G1a 未开跑原因**：ninfer :8000 本机无响应（curl 超时），远程 100.112.53.47:8000 连通性未验证——属算力通道问题，非设计阻塞。G1a 执行清单（§6）已冻结，通道恢复后按序跑即可，无需重新设计。

**G1b 仍 blocked-on-human**：异源 judge（非 Qwen 家族）需用户决策（arena 通道或 API key）。arena.ai 直连 403（疑似 WAF），ego-lite 进程活着但登录态未验证——按 arena-outsource SOP 故障阶梯，先查工具网络再考虑找人，本轮不升级。
