# 阶段 01：目标分解 — RV3G4-prior-source-assert（G4 强制机械化候选落地）

> goal: assert 脚本校验 prior-estimates.json 必须记录 ≥N 个独立 p̃ 生成源（source 字段缺失/单源 = FAIL），参考 R5.2 系列 assert-* 模式 · 分支 ralph/rv3g4-prior-source-assert · 2026-10-30
> 上游：tasks/goal-queue.md 候选条目 + G4 交付物「给 G5 的导出」第一类（g4-vulnerability-crosscheck.md L100）+ S3 降档教训（纸面协议零防护力直到被执行）

## F1 · 交付物结构分解

| # | 交付物 | 内容 | 关键判读点 |
|---|--------|------|-----------|
| D1 | `bench/rubric-v3/ablation/scripts/assert-prior-source.py` | 三组检查：① prior-estimates.json 含 `p_tilde_provenance` 顶层对象且 `independent_sources` 为非空列表；② 每个 source 有 `judge_id`（非空字符串）+ `artifact`（指向仓库内实际存在的 JSON 文件，相对 ROOT 解析后 is_file()）；③ 独立性机判——≥2 个 source 的 judge_id 互不相同（去重后 len ≥ N_MIN=2）。任一不满足 exit 1 + 打印失败项 | exit code 语义与 R5.2 系列一致（0=PASS / 1=FAIL）；变异测试确认实义 |
| D2 | prior-estimates.json 补 `p_tilde_provenance` 元数据块 | 追加顶层键（不改任何既有键/节点值）：`{"independent_sources": [{"judge_id": "lead-original", "artifact": "prior-estimates.json", "role": "primary"}, {"judge_id": "qwen3.8-27b (fresh-context subagent, Claude Code ralph loop channel)", "artifact": "judge-blindtest-r1.json", "role": "blind-reestimate"}], "note": "..."}` | **诚实性红线**：两 source 同属 Qwen 家族 → note 必须显式声明「family-independent: false（双源均 Qwen 家族，跨家族隔离待 batch2 R-11）」；本 goal 只落盘事实，不粉饰独立性等级 |
| D3 | g4-vulnerability-crosscheck.md L100 候选状态更新 | 「候选」→「已落地（RV3G4-prior-source-assert，rXXX）」+ 一行说明（signal-only：provenance 存在性 + artifact 可解析 + judge_id 去重数 ≥2；家族隔离不在本脚本判定范围，见 D2 note） | grep 定点 |
| D4 | 六阶段工件 | 本文件 + 02/02.5/03/04/04.5（前缀 RV3G4psa）+ per-goal web-llm 回执 | 02 含 prior-estimates.json / judge-blindtest-r1.json 全量盘点 evidence |

## F2 · 输入盘点

| 输入 | 状态 | evidence |
|------|------|----------|
| prior-estimates.json 顶层结构 | ✅ 已读 | 10 个顶层键（epsilon/weight_formula/root_policy/nodes/declared_gold_node_count/identified_gold_node_count/unidentified_node_count/source_baseline_commit/weight_formulas/missing_share_policy），无 provenance 字段 |
| judge-blindtest-r1.json 结构 | ✅ 已读 | judge="qwen3.8-27b (Claude Code ralph loop channel, fresh-context subagent)" + protocol.blindness 声明 + nodes.*.p_tilde/w2/rationale |
| 两文件 judge 归属 | ✅ 已核实 | prior-estimates.json 由 Lead 主会话估计（TASK-ablation.md L27 任务书指定 judge LLM 执行）；judge-blindtest-r1.json 由 fresh-context subagent 盲估（protocol.blindness 自声明）——两个独立估计过程，但模型家族相同 |
| G4 导出原文 | ✅ 已读 | g4-vulnerability-crosscheck.md L100「p̃ 估计必须来自 ≥N 个独立生成源的频率统计（否则 prior-estimates.json 拒收）」 |
| R5.2 系列 assert 模式 | ✅ 已读 | assert-w2-formula.py / assert-gmr-recompute.py（exit 0/1 + PASS/FAIL 行输出 + 冻结 commit 快照对照） |

## F3 · 判断点识别

| # | 判断 | 选项空间 | 预注册倾向 |
|---|------|----------|-----------|
| J1 | signal-only vs verdict 二选一（queue 明写「在 01 定」） | A signal-only：脚本只验 provenance 元数据存在性 + artifact 可解析 + judge_id 去重数 ≥2，不对 p̃ 数值本身做门禁 / B verdict：缺 provenance 时直接拒收整个 prior-estimates.json（所有下游 W2/W3/W4 计算标记无效） | **A signal-only**——理由：(a) 现有 prior-estimates.json 是 batch1 冻结件，verdict 模式会立刻让全部既有统计失效，超出本 goal 授权范围；(b) G4 导出原文的「拒收」针对的是未来新产出的 prior 文件，不是追溯冻结件；(c) signal-only 下脚本对当前文件 PASS（补 D2 后）+ 对未来单源文件 FAIL，防护力等价且不破坏冻结链。若成璐要 verdict 模式，改脚本一处常量即可（登记为后续候选） |
| J2 | N_MIN（独立源下限）取值 | A 2（G4 导出原文「≥N」未定值，取最小可验证阈值）/ B 3（rubric-v3 遗留 #1「独立 judge 盲测」要求 ≥3） | **A 2**——B 是 rubric-v3 正式实验开跑前的更严标准（另开 goal 跟踪），本 goal 落地 G4 导出的最小机械化版本；J2 取值写入脚本常量 N_MIN=2 + 注释指向遗留 #1 |
| J3 | 独立性判定口径 | A judge_id 字符串去重数 / B judge_id + 模型家族双维度 | **A**——家族信息不在结构化字段里（只有 judge 描述字符串），机判家族需要 NLP 或人工维护映射表，超出 assert 脚本职责；家族隔离降级为 D2 note 的人工声明 + 04.5 复核项 |
| J4 | prior-estimates.json 修改是否违反冻结纪律 | A 追加顶层元数据键 = 冻结件修改，需 APPROVALS 登记 / B 元数据追加不改任何被消费字段（nodes/stats 复算脚本只读 nodes.*），实质零影响 | **A 从严**：runner 硬规则「冻结数据只读，要改必须开新文件 + APPROVALS.md 登记」。处置：APPROVALS.md 登记本追加（理由：G4 导出授权的机械化落地必需；改动 = 纯新增顶层键，断言脚本 assert-w2-formula.py / assert-w3w4-recompute.py 重跑 exit 0 证明消费侧零影响），同时脚本设计为「缺 provenance 不 FAIL 既有数值检查」避免双重惩罚 |

## F4 · 风险登记

| # | 风险 | 严重度 | 缓解 |
|----|------|--------|------|
| R1 | 补 provenance 时手敲 judge_id 与 judge-blindtest-r1.json 实际字段不一致 → 独立性声明失真 | 高 | judge_id 从 judge-blindtest-r1.json:judge 字段程序化提取写入（不手敲）；assert 检查②加一条：provenance 中 blind-reestimate 条目的 judge_id == judge-blindtest-r1.json:judge（byte-exact） |
| R2 | signal-only 被误读为「已通过独立性检验」 | 中 | 脚本输出行显式标注「SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict」；D2 note + 04 日志双处声明 |
| R3 | artifact 路径用绝对路径导致换机不可复现 | 低 | 约定相对 ROOT 路径；assert 按 Path(ROOT)/artifact 解析 |
