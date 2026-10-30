# origin: ai — 阶段 02：信息研究（RV3G3cdx-crossdomain-promptversion-mapping · r153）

> 研究路径 = 仓库内逐字取证（网络调研受限，无 ego-browser；本 goal 全部事实源在仓库内，无 unverified 外部项）。

## A1 · K1 gold 清单五源一致性逐字核验

| 源 | 位置 | 逐字值 | 一致 |
|----|------|--------|------|
| assert-goldrank-threshold.py | L25 | `GOLD = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]` | ✓ |
| assert-gmr-recompute.py | L13 | `GOLD = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]` | ✓ |
| assert-o3-claim-rejudge.py | L22 docstring | `限 v ∈ {N-2.1, N-3.2.2, N-2, N-4, N-1.3}（40 cell）` | ✓ |
| rejudge/sample-plan.json | gold_strict_nodes | `["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]` | ✓ |
| AUDIT-report.md | L100 | `gold strict 集 = {N-2.1, N-3.2.2, N-2, N-4, N-1.3}（r71b 冻结）` | ✓ |

**结论**：五源零分歧。机器核验命令留档：
`python3 -c "import json; print(json.load(open('bench/rubric-v3/ablation/rejudge/sample-plan.json'))['gold_strict_nodes'])"` → 与上表逐格一致（04 实跑复验）。

## A2 · K2 冻结事件溯源

`git log --oneline --all | grep r71b` → `ed552c4 r71b: 构念效度双口径核对 — 严格口径(含N-4/N-1.3)复算确认四方案计数 2/2/3/2 不变`。
AUDIT-report.md L100「（r71b 冻结）」为该事件的引用锚点。**映射表 domain1 条目的 frozen_at_commit = ed552c4**。
注：r71b 是「口径核对」commit（改 ablation-result.md + stats-w3w4.json），非首次落盘 commit——
首次落盘更早（r71 4aa32a2 收口 W3/W4 全量复算），但「strict 集含 N-4/N-1.3 的五节点口径」的裁定事件 = r71b，
映射表登记的是**口径冻结事件**而非文件创建事件，取 ed552c4 语义正确。矛盾风险挂 04.5 攻击项。

## A3 · K3/K4 变体矩阵冻结规则取证（byte-exact 摘录）

DRAFT-rubric-v3-v2.md §3.2（当前 main 版本行号）：
- L180：「所有变体共用**同一题面**（v3 基础题面，不含任何变体特有指令）……无 diff 记录的变体不得开跑。V0 必须在 v3 题面上同批次重跑（#27：不得复用 L1 旧题面数据进配对检验，L1 C9-plain 只作外部参照）」
- L184-L190：七变体行（V0-baseline/V1-full/V1-align/V2-nocoverage/V3-noboundary/V-sham/V3-sham）
- L197 D2 行 + 尾注：「冻结语义 = 收口 commit 的本文件快照，具体 hash 登记于 revision-log-batch1.md」

revision-log-batch1.md R-10 回填状态节：「冻结版本 = ralph/rv3g6-batch1 分支收口 commit
`61416b43f80e28d9785137f320003bf8e121d306`（r116）……取回方式：`git show 61416b4:bench/rubric-v3/DRAFT-rubric-v3-v2.md`」。

**关键推论（O1 处置依据）**：B10 规则说「所有变体共用同一 v3 基础题面」——即 **V0..V3-sham 六变体的
gold 对照物都是同一个 gold 树**（变体差异只在 prompt 侧指令段，题面主体与域不变 ⇒ gold 清单不变）。
故六变体占位条目的 gold_nodes 可直接预注册 = domain1 gold 清单，**这不是 runner 代裁新域 gold，
而是 B10 冻结规则的机械推论**（证据链：K3 L180 原文 + K4 冻结快照）。这是 O1 保守口径的合法性来源。

## A4 · K5 既有 run 题面归属取证

- TASK-ablation.md L12：「`prompt-V0.txt` — baseline 题面（C9-plain 档，无引导）」
- TASK-ablation.md 输入材料节：runs-C0-run1~run8 = 「同一 prompt 的 8 次独立 run」
- prompt-V0.txt 存在，md5 = 5e9459acc6c2ae151d3707dbedefbcf3，42 行；git 历史仅 aad07bd (r69) 一次落盘，此后零改动
- DRAFT v2 L180/L310：C9-plain = L1 旧题面，#27 裁定「只作外部参照不进配对检验」，V0 须用 v3 题面重跑

**结论**：既有 8 run 的题面 = C9-plain（pre-v3），**不是** v3 变体矩阵的任何成员。
映射表若把 C9-plain 标成 V0-baseline 会制造虚假血缘（V0 按 #27 尚未存在任何 run 数据）。
⇒ O1 处置定稿：C9-plain 独立条目 `pre-v3/C9-plain`（status=archived-reference），
六变体条目 status=pending-run（gold 预注册 = B10 推论，A3）。

## A5 · K6/K8 消费侧现状取证

- prior-estimates.json 顶层键 = [epsilon, weight_formula, root_policy, nodes, declared_gold_node_count,
  identified_gold_node_count, unidentified_node_count, source_baseline_commit, weight_formulas,
  missing_share_policy, p_tilde_provenance] —— **无 prompt_version、无 gold_nodes**（第一域数据早于 r150 schema 约定，K6 实证）
- assert-goldrank-crossdomain.py L228-235：Y1 键集检查（仅显式声明时）+ Y2 prompt_version 存在性/非空 str —— 现状基线
- load_batch2 返回契约 `(ok, data_dict_or_error_msg)`；错误消息风格 = `<文件名>: <字段> required/violation`（L231/L235 先例）

## A6 · 消费规则真值表穷举（F3 定稿输入）

设 P = pe.prompt_version（str 或 None），G = pe.gold_nodes（list 或 None），M = 映射表。
前提：P 缺失/空串/非 str 已由 Y2 先行拦截 exit 2（本检查不重复该职责）。

| # | P 状态 | G 状态 | 判定 | exit | 输出 |
|---|--------|--------|------|------|------|
| T1 | P ∈ M[domain] | G 声明，sorted(G)==sorted(M[P]) | PASS | 0 | `[PASS] gold-map: prompt_version=P 与 gold_nodes 一致（5 节点）` |
| T2 | P ∈ M[domain] | G 声明，集合不等 | FAIL | 2 | `[ERROR] gold-map mismatch: prompt_version=P 期望 gold_nodes=<M[P]>，实得 <G>`（指名道姓双向列出） |
| T3 | P ∉ M[domain]（且 domain 有表） | G 任意 | SIGNAL | 0 | `[SIGNAL] gold-map: prompt_version=P 未在映射表登记（新域/新版本）——建表后重跑；本轮不做清单对照（不代裁）` |
| T4 | P ∈ M[domain] | G 缺省（None） | SIGNAL | 0 | `[SIGNAL] gold-map: prompt_version=P 已登记但 gold_nodes 未显式声明——缺省沿用 GOLD_DOMAIN1，若 P 绑定清单 ≠ GOLD_DOMAIN1 请显式声明`（仅当 M[P]≠GOLD_DOMAIN1 时报；相等则静默 PASS） |
| T5 | domain 无表条目（纯新域） | G 任意 | SIGNAL | 0 | 同 T3 文案（合并：「prompt_version=P 所属 domain 未在映射表登记」） |
| T6 | 映射表文件缺失 | — | 降级 | 0 | `[INFO] gold-map: prompt-version-gold-map.json absent → 对照检查跳过（r153 前行为兼容态）`——**fail-safe：表缺失不误杀存量调用方** |
| T7 | 映射表 schema 违例 | — | ERROR | 2 | `[ERROR] gold-map schema violation: <msg>`（fail-loud，同 load_batch2 风格） |

**T4 细化裁定（O3 处置）**：T4 报 SIGNAL 的条件收窄为「M[P] ≠ GOLD_DOMAIN1（排序后）」——
若声明版本绑定的就是缺省清单本身，显式声明与否无语义差别，报 SIGNAL 是噪音。
此收窄方向 = 少报（SIGNAL 减少），非多报；误报风险 = 0（条件可机判精确）。挂 04.5。

**T6 降级条款理由**：映射表是本 goal 新建文件；若未来有人删表（或 checkout 到本 goal 之前的状态），
断言脚本不应因表缺失而 exit 2 打挂 batch2 主流程——表缺失 = 「对照能力不可用」，属降级运行态（SIGNAL/INFO），
非数据错配。与 m4-independent-source-definition.md D5 降级态归簇规则同族（W1 先例）。

## A7 · 映射表 schema 草案（F1 定稿）

```json
{
  "_schema": "prompt-version-gold-map/v1",
  "_doc": "「题面版本↔gold_nodes」权威源（RV3G3cdx-crossdomain-promptversion-mapping, r153）。消费方 = assert-goldrank-crossdomain.py load_batch2 对照检查。新增域/版本条目 = 数据到来时由对应 closure goal 同批追加（runner 不代裁新域 gold 内容，只登记结构）。",
  "domains": {
    "<domain_id>": {
      "label": "<人读标签>",
      "gold_source": {"path": "<gold-tree 相对路径>", "frozen_at_commit": "<hash>", "note": "<口径冻结事件>"},
      "versions": {
        "<prompt_version>": {
          "gold_nodes": ["<node_id>", ...],
          "status": "active | pending-run | archived-reference",
          "basis": "<该条目 gold 清单的证据锚点>"
        }
      }
    }
  }
}
```

字段必要性论证：
- `_schema`：版本标识，防 schema 演进时旧消费方误读（同 sample-plan.json schema_version 先例）
- `gold_source.frozen_at_commit`：溯源锚点（K2 机制），机判不消费、审计消费
- `status`：三态区分「已有 run 数据 / 预注册待开跑 / 历史参照」——T3/T4 判定不需要它，
  但防误用（pending-run 条目的 gold 是 B10 推论非实测，报告层须可区分）
- `basis`：每条目强制带证据锚点（研究级质量线：结论必须带 evidence）

**反方检验（F1c 混合方案否决理由）**：gold 清单指向 gold-tree 文件解析 = 引入 markdown 解析依赖
（gold-tree 是人读文档非 JSON，解析脆弱）+ 跨文件一致性二次漂移面。内联清单 + 溯源锚点分离
（机判吃内联、审计吃锚点）是零新增脆弱面的最小设计。

## A8 · 落盘位置裁定（O4）

`bench/rubric-v3/ablation/prompt-version-gold-map.json`：
- 与 batch2/ 约定目录同级 ⇒ load_batch2 以 `BASE / "prompt-version-gold-map.json"` 引用，零路径参数化改动
- 不放 scripts/（那是断言脚本区）；不放 bench/rubric-v3/ 根（那里是 rubric 文档区，ablation 数据属 ablation/）
- 命名避开既有 hit-matrix/prior-estimates/judge-blindtest 三件套（batch2 后缀家族），独立名防 glob 碰撞

## A9 · 负面结果与矛盾登记（不藏着）

1. **「映射表权威源」的权威性边界**：本表对 domain1 的权威性 = 五源一致性（A1）+ B10 推论（A3）双重支撑，
   但对**第二域及未来域**，本表只是结构容器——gold 内容由数据到来时的 closure goal 裁定填入。
   「权威源建立」的准确表述 = 「domain1 权威条目 + 消费协议 + 扩展槽位」，不是「全域权威已就位」。
2. **O1 的 C9-plain 归属**仍是判断而非事实：TASK-ablation.md 称其「C9-plain 档」，但 L1 原始任务书
   （decomp 侧）不在本仓可取证范围（research/deepresearch-bench-survey 分支提及，未核）——
   「C9-plain = pre-v3 独立版本」是基于 #27 裁定文本（L180/L310）的推论，unverified 程度低但非 byte-exact 闭环。
   挂 APPROVALS 供成璐复核（不阻塞）。
3. **r71b vs r71 冻结事件选择**（A2 注）：若成璐认为应登记 r71（4aa32a2，首次落盘事件）而非 r71b
   （口径裁定事件），映射表一行 diff 可改，消费逻辑零影响（frozen_at_commit 机判不消费）。

## A10 · 阶段 02 判定
全部事实源仓库内闭合，零外部 unverified（A9.2 为低度推论已如实标注）。03 可直接转动作分解。
