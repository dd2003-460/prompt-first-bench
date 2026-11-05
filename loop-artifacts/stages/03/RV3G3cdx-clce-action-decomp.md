# 阶段 03 — RV3G3cdx-crossdomain-lint-coverage-expand · 动作分解（r150）

> 依据：02 扫描 + 02.5 裁定 Y1-Y5。唯一代码改动面 = `assert-goldrank-crossdomain.py`；byte-stable 面（S6 界定）零触碰。

## A1 — load_batch2 追加两项 schema 检查（Y1/Y2 落地）

插入位置 = gold_nodes 类型检查（L218）之后、节点级 w1/p_tilde 循环之前：
```python
    if gold is not None:                                   # Y1：仅显式声明时生效
        missing = [g for g in gold if g not in pe["nodes"]]
        if missing:
            return False, (f"prior-estimates-batch2.json: gold_nodes members absent "
                           f"from nodes key set: {missing}")
    pv = pe.get("prompt_version")                          # Y2：C-最小消费
    if pv is None or not isinstance(pv, str) or not pv.strip():
        return False, "prior-estimates-batch2.json: 'prompt_version' required (non-empty str)"
```
顺序论证：键集检查先于 prompt_version——数据语义错误（gold↔nodes 不一致）比元数据缺失更根本，且两检查互不干扰（各自独立 return）。

## A2 — 主 docstring 更新（(d) + M1/M2 如实化）

- exit code 节（L57-59）补 lint 模式行：`--lint-only 模式：0 = 全通过（含目录不存在 SIGNAL）/ 2 = schema 违例或不可读；lint 不跑 (a)/(b) 判定，永不 exit 1`。
- 输入 schema 节 prior 字段表：gold_nodes 行补「显式声明时成员须 ⊆ nodes 键集」；prompt_version 行改「存在性 + 非空 str 机判（M2 C-最小，r150）；完整题面版本↔gold 清单对照协议 = 导出候选（权威源映射表待第二域题面落盘时建立）」。
- L27-28 「换题面而未声明 = ERROR fail-loud」改为如实表述（Y3：不留虚假宣称）。

## A3 — 四个新负样例落盘 `batch2-lint-samples/`（X3 + Y4）

| 目录 | 文件构造 | 目标出口 |
|---|---|---|
| neg-json-unreadable/ | prior = 截断 JSON；hit-matrix 合法 | E3 unreadable |
| neg-nodes-not-dict/ | prior.nodes = list | E4 'nodes' object required |
| neg-goldnodes-badtype/ | prior.gold_nodes = str | E5 类型错 |
| neg-goldnode-not-in-nodes/ | prior 合法，gold_nodes 含 1 个 nodes 缺席 nid | 新出口（键集） |

每目录附 `README.md` 一行构造意图标注（持久落盘防 tmp 污染先例）。既有 7 样例零修改（Y3 实证已全含 prompt_version）。

## A4 — 全矩阵实跑 + byte-exact 回归

- 11 样例逐一 `--lint-only --dir`：neg×6 全 exit 2 指名道姓 / pos×2 全 exit 0 / 新增 neg×3 各命中目标出口；
- E1 默认态实跑（无参）exit 0 SIGNAL；
- **byte-exact**：A1/A2 改动前已快照无参调用 stdout（02 S2 基线同命令），改动后重跑逐字节 diff = 空。

## A5 — 回归基线 + 冻结面

- 八脚本基线（repo root）：七脚本 [0,0,0,1,0,0,0] + assert-queue-lint.py exit 0（3 SIGNAL）零漂移；
- `git diff main --stat -- hit-matrix.json prior-estimates.json gold-tree.md runs-C0-*` = 0 行；
- 改动面 ⊆ {assert-goldrank-crossdomain.py, batch2-lint-samples/{4 新目录}, stages/*, current-goal.md}。

## A6 — 收口

queue L23 `[ ]`→`[x]` + 结果注记 + 新导出候选 ≥1（预登记方向：M1 完整 fail-loud 协议——「题面版本↔gold_nodes 映射表」权威源建立 + 对照检查实现，激活条件 = 第二域题面落盘；与 RV3G3-batch2-arrival-closure 联动项）。merge main + push + closure gate 自检。