# 阶段 02：研究盘点 — RV3G4-prior-source-assert

> goal: G4 强制机械化候选落地（prior-estimates.json 独立源 provenance assert）· 分支 ralph/rv3g4-prior-source-assert · 2026-10-30
> 依据：01 目标分解 J1-J4 预注册 + F2 输入盘点

## §1 · 事实盘点（全部只读，evidence 带 JSON path / 行号）

### S1 · prior-estimates.json 现状

| 项 | 值 | evidence |
|----|-----|----------|
| 顶层键（10 个） | epsilon / weight_formula / root_policy / nodes / declared_gold_node_count / identified_gold_node_count / unidentified_node_count / source_baseline_commit / weight_formulas / missing_share_policy | python json.loads 全量遍历 |
| p̃ 估计来源字段 | **不存在**（无 source / provenance / generated_by / judge 任何变体） | 顶层键枚举零命中 |
| 唯一版本锚点 | `source_baseline_commit: "8ee73de"`（指向 gold-tree 基线 commit，非 p̃ 生成者标识） | prior-estimates.json:source_baseline_commit |
| 节点数 | nodes = 35 键（declared_gold_node_count=35, identified=31, unidentified=4） | prior-estimates.json 计数键 |
| p̃ 生成协议 | TASK-ablation.md L27：「你（作为 judge LLM）对每个节点回答…给 p̃ 估计（0-1）…存 prior-estimates.json」——单 judge 一次落盘，任务书未要求多源 | bench/rubric-v3/ablation/TASK-ablation.md L27 |

### S2 · judge-blindtest-r1.json 现状（第二估计过程）

| 项 | 值 | evidence |
|----|-----|----------|
| judge 自声明 | `"qwen3.8-27b (Claude Code ralph loop channel, fresh-context subagent)"` | judge-blindtest-r1.json:judge |
| 盲性协议 | protocol.blindness：「estimation executed by fresh-context subagent that never read prior-estimates.json; main session only supplied node text + parent context + gold-mark presence + 8-run hit counts」 | judge-blindtest-r1.json:protocol.blindness |
| 覆盖范围 | nodes 全 35 键（含 N-0 p_tilde=null），每节点 p_tilde/w2/rationale | python 遍历 |
| 与 primary 的关系 | cross_judge_spearman 字段存在（两 judge p̃ 序列的 Spearman ρ 已算）；original_judge_reference 只含 w3_top5/marked_count_strict/overlap（参考摘要，非完整 p̃ 数组） | judge-blindtest-r1.json 顶层键 |
| 家族归属 | qwen3.8-27b = Qwen 家族；primary（Lead 主会话）同为 Qwen 家族 → **双源同族** | judge 字符串 + Lead 运行环境（本工作区模型配置） |

### S3 · G4 导出原文（本 goal 授权链）

- g4-vulnerability-crosscheck.md L100：「强制机械化类（S3 降档）：哪些纸面防护值得做成 assert 脚本强制执行——候选：**p̃ 估计必须来自 ≥N 个独立生成源的频率统计（否则 prior-estimates.json 拒收）**、κ 门禁回执必须随评分文件落盘（缺回执 = 评分无效）。参考 R5.2 系列 assert-* 脚本模式。」
- 判定汇总 S4 行（L16）：「prior-estimates.json source_baseline_commit/epsilon 字段（版本依赖已管控）」——G4 当时认定版本依赖子项已管控，但**生成源数量维度从未被任何机判覆盖**（这正是 S3 降档教训：纸面协议零防护力直到被执行）。

### S4 · R5.2 系列 assert 模式参照

| 脚本 | 模式要素 | 本 goal 沿用 |
|------|----------|--------------|
| assert-w2-formula.py | exit 0/1；逐节点 PASS/FAIL 行；冻结 commit 快照对照（git show）；容差常量显式 | exit 语义 + 行输出格式 |
| assert-gmr-recompute.py | 内容锚定定位（不依赖行号）；变异测试在临时副本执行 | 内容锚定 + 变异方法 |
| assert-psf-freeze.py（r129） | ROOT = parents[4] 相对解析；检查分组 ①②③；RESULT 汇总行 | 结构模板直接参照 |

## §2 · 判断确认（01 预注册 J1-J4 复核）

- **J1 signal-only 维持**：verdict 模式会追溯冻结件致全部既有统计失效（超出授权）；signal-only 对当前文件 PASS + 未来单源文件 FAIL，防护力等价。verdict 模式留作后续候选（改一处常量）。
- **J2 N_MIN=2 维持**：最小可验证阈值；≥3 是 rubric-v3 遗留 #1 的正式实验标准（另开 goal）。
- **J3 judge_id 去重口径维持**：家族隔离降级为人工声明（D2 note）+ 04.5 复核项。
- **J4 APPROVALS 登记维持**：prior-estimates.json 属冻结数据，追加顶层元数据键需登记；改动纯新增，消费侧脚本（assert-w2-formula / assert-w3w4-recompute）重跑 exit 0 证明零影响。

## §3 · 设计结论（供 03 行动分解）

1. 脚本名 `assert-prior-source.py`，落 `bench/rubric-v3/ablation/scripts/`。
2. 三组检查：① provenance 对象存在 + independent_sources 非空列表；② 每条 source 有 judge_id（非空 str）+ artifact（相对 ROOT 可解析且 is_file()）+ blind-reestimate 条目 judge_id 与 judge-blindtest-r1.json:judge byte-exact；③ judge_id 去重数 ≥ N_MIN=2。
3. 输出首行标注 SIGNAL ONLY（R2 缓解）。
4. prior-estimates.json 追加 `p_tilde_provenance` 块（judge_id 程序化提取，note 显式声明 family-independent: false）。
5. 消费侧回归：assert-w2-formula.py + assert-w3w4-recompute.py 重跑 exit 0。
