# 02 — RV3G3cdx-batch2-schema-lint · 现状扫描

> goal: batch2 三输入文件 schema lint 独立化 · 分支 ralph/rv3g3cdx-batch2-schema-lint · 2026-10-30
> 方法：逐行盘点 assert-goldrank-crossdomain.py（282 行）的 schema 声明面与机判实现面，核查调用面。

## S1 — docstring 预注册 schema 提取（L11-35，权威源）

| 文件 | 必需性 | 结构（docstring 原文语义） | 字段级约束 |
|------|--------|---------------------------|-----------|
| hit-matrix-batch2.json | **必需**（缺 = ERROR） | `{run_id: {node_id: {"h": 0\|1, "evidence": str\|null}}}` | gold_nodes 声明成员必须在每个 run 出现（最小规模 ≥1 run × ≥5 gold 可定位）；h/evidence 字段本身**无类型检查**（docstring 注释：(a)/(b) 协议不消费 h 值，仅存在性校验防半套数据） |
| prior-estimates-batch2.json | **必需**（缺 = ERROR） | `{"nodes": {nid: {parent_id, p_tilde, w1, w2, parent_share}}, "gold_nodes": [nid×5], "prompt_version": str}` | nodes 必须为 object；每节点 `w1` 必需、`p_tilde` 键必需（null 允许）；gold_nodes 缺省 = 沿用第一域 GOLD_DOMAIN1（D1），显式给出则必须是 str list；换题面未声明 = ERROR fail-loud（**注：代码实际未实现此条**——见 S4 mismatch M1） |
| judge-blindtest-batch2.json | **可缺**（D5 降级） | `{"judge": str, "w3_full_ranking": [{node, p_tilde, w1, w2, w3}]}` | 存在时每条 entry 须含 node/w1/w2/w3 四键 |

## S2 — load_batch2() 机判实现盘点（L186-232）

现有检查链（按执行序）：
1. L188-189：`BATCH2.is_dir()` 假 → 返回 `(False, "batch2/ directory absent")` —— main 特判此 payload 走 SIGNAL exit 0
2. L192-203：三文件循环加载；hit-matrix/prior 缺失 → errs；blindtest 缺失 → 静默跳过（D5）；JSON 不可读 → errs
3. L207-209：prior `"nodes"` 键存在且为 dict
4. L210-214：gold_nodes 解析（None → 默认 / 非 str-list → error）
5. L215-220：每节点 `w1` 键 + `p_tilde` 键存在性
6. L221-225：hit_matrix 每 run 覆盖全部 gold 节点
7. L226-230：blindtest 每 entry 四键存在性

**关键结构事实**：lint 逻辑与 (a)/(b) 判定逻辑同函数耦合——`load_batch2()` 返回后 main 直接进 build_schemes/top10_gold_count，无「只校验不判定」的出口。目录不存在时 lint 路径被 SIGNAL 短路，**提供方无法在数据落盘前自验**。

## S3 — 调用面核查

- 全仓 grep `load_batch2` / `assert-goldrank-crossdomain`：唯一外部引用 = `assert-o3-claim-rejudge.py` L7 **docstring 文字提及**（exit code 约定先例），无 import、无 subprocess 调用。→ 改本脚本签名零外溢。
- 回归基线消费者：r145 X3 / r146 A1 七脚本表记录的是**无参调用**输出（SIGNAL 两行 + exit 0）。→ 无参行为必须 byte-exact 保持。
- 改动前基线实跑已捕获：`/tmp/cd-before.txt`（exit 0，两行输出，04 阶段 diff 用）。

## S4 — docstring↔代码 mismatch 清单（预登记，供 04.5 消费）

| # | 项 | docstring 声称 | 代码实际 | 处置 |
|---|----|---------------|---------|------|
| M1 | 换题面未声明 gold_nodes = ERROR fail-loud（L27-28） | 应报错 | 未实现——代码只看 gold_nodes 是否合法 list，不与题面版本对照（prompt_version 也未被任何检查消费） | 登记，不擅自扩规则（current-goal 失败降级第 2 条）；导出候选 |
| M2 | prompt_version 字段（L29） | 题面版本标识 | 无任何检查消费它 | 同 M1 口径 |
| M3 | hit-matrix h∈{0,1} / evidence 类型（L19） | 有类型声明 | 无类型检查（设计内：协议不消费 h 值） | 设计内，非缺陷，不改 |

## S5 — 方案选型（供 03 决策）

- **A（选定方向）**：crossdomain 脚本加 `--lint-only [--dir <path>]` 入口；`load_batch2()` 增加可选 `base_dir` 参数（默认现 BATCH2 常量），lint 模式复用同一检查链、逐文件输出 PASS/FAIL 汇总。无参路径零改动。
- B（降级备选，current-goal 预注册）：独立新脚本 assert-batch2-lint.py。仅在 A 引入无参行为漂移时启用。
- 样例矩阵放 `bench/rubric-v3/ablation/batch2-lint-samples/`（正样例 2 组 + 负样例 5 组），不进 batch2/ 真目录（防误触发主断言的 D5 降级态）。