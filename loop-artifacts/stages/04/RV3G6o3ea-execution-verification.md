# 04 — RV3G6-o3-claim-rejudge-evidence-audit · 执行验证日志

> goal: hit-matrix 98 个 h=1 evidence verbatim 合规审计 · 分支 ralph/rv3g6-o3-claim-rejudge-evidence-audit · 2026-10-30

## A1 — assert-hitmatrix-evidence.py 落盘 ✓

`bench/rubric-v3/ablation/scripts/assert-hitmatrix-evidence.py`（新增，唯一 scripts/ 增量）。docstring 预注册 C1-C5 判定语义与 01 阶段 §2 表一致；C4 触发条件锁定（仅 C2 FAIL 时诊断，不做全局唯一性——X2）写入 docstring；路径解析 `Path(__file__).resolve().parents[4]` 任意 cwd 可跑。V1 口径函数 `gold_numbers_per_node`/`noise_exempt` 与 assert-o3-claim-list.py 同逻辑逐行对照（per-line findall + ID 分段/一级前缀/{0,1,31,4,13} 豁免）。

## A2 — 实跑（live data）✓

```
$ python3 bench/rubric-v3/ablation/scripts/assert-hitmatrix-evidence.py
# hit-matrix evidence verbatim 审计 · h=1 98 cell / h=0 150 cell
  [PASS] run1/N-0  len=17        （98 行全 PASS，完整表见实跑 stdout）
  ...
# §3.2 声明 4 复算（V1 口径 = assert-o3-claim-list.py 同源 per-line − 噪声豁免）
  V1 计数 = 13/98 vs o3-claim-list §3.2 声明值 = 27（MISMATCH——...）
VERDICT: PASS（FAIL 0 / SIGNAL 0 / 审计 98 h=1 cell）
EXIT=0
```

**主 verdict：PASS exit 0**。98/98 h=1 evidence 均为所属 run 文件全文连续子串（verbatim 零改写/拼接/编造），零 C3/C5 SIGNAL。与 F2 预判一致——本 goal 产出定性为「验证链补环」：TASK-ablation Step 1 的 verbatim 硬约束从「从未机判」变为「exit 0 事实」。失败降级条款 2（发现真实违规 → APPROVALS 登记）**未触发**。

## A3 — 变异测试 M1-M4 ✓（fixture 全部测毕删除，git status 验证无留痕）

| 场景 | 构造 | 预期 | 实测 |
|------|------|------|------|
| M1 篡改 | run1/N-0 evidence 追加「（篡改）」→ 非子串 | C2 FAIL exit 1 | `[FAIL] C2 run1/N-0: evidence 非所属 run 连续子串（改写/拼接/编造）` VERDICT FAIL exit 1 ✓ |
| M2 张冠李戴 | run2 独有句「每完成一个任务的总成本」塞给 run1/N-0 | C4 FAIL exit 1 | `[FAIL] C4 run1/N-0: evidence 出自其他 run ['run2']（张冠李戴）` exit 1 ✓ |
| M3 超长 | run1 全文取 45 字符合法子串替换 run1/N-0 evidence | C3 SIGNAL、exit 仍 0 | `[SIGNAL] C3 run1/N-0: evidence 长 45 > 40 字（惯例超界，非门禁）` VERDICT PASS exit 0 ✓ |
| M4 h=0 带值 | run1/N-1（h=0）塞「冗余测试值」 | C5 SIGNAL exit 0 | `[SIGNAL] C5 run1/N-1: h=0 cell 带 evidence（冗余，非违规）` exit 0 ✓ |

实现注记：fixture 方案 = 复制脚本至 `scripts/_tmp_assert_hme.py`（保持 parents[4] 深度不变）+ HIT_MATRIX 指向 /tmp fixture JSON；测毕两文件即删。首版曾把副本放 /tmp 导致 parents[4] IndexError——已识别为测试脚手架问题（非交付物缺陷），改同深度放置后四场景一次通过。

## A4 — §3.2 声明 4「27/98」复算固化 ✓（负面发现）

三口径独立重算（与 02 F3 数字一致，交叉验证通过）：

| 口径 | 定义 | 计数 |
|------|------|------|
| V1 | per-line token − 噪声豁免（assert 现行同源） | **13**/98 |
| V2 | gold-tree 全文件 token − 同豁免 | **34**/98 |
| V3 | per-line token，无豁免 | **35**/98 |

**声明值 27 与三口径均不一致**。差异来源抽样实证（V2-only 命中样例）：run1/N-3.2「3090×2 带宽 2×936=1872 GB/s」（token '3090' 出自 gold-tree OC-1 卡片区而非 N-3.2 节点行）、run2/N-1.1.1「3090：~$1500/卡」、run1/N-5.3「90:9:1、64K 上下文」（'90'/'9' 为缓存比例，跨区 token）——即 V2 额外 21 例几乎全是型号/比例类跨区数值，V1→27 无任何可复现路径。V1 全部 13 例命中清单已落盘（含 run1/N-3.2.1「4bit ≈ 27e9×0.5 byte」等——注意其中 '27' 是 27B 模型规模自产文本，恰与声明值同数字，属巧合非溯源线索）。

**定性**：27 = o3-claim-list 起草期不可复现人工计数（或用了未落盘中间口径）。结论方向不受影响（声明 4 论证的是机制——evidence 含 gold 数值 ≠ 泄漏通道——对 13/27/34 任一计数都成立），但**数字本身失实**。处置按预注册：脚本只报 V1 + mismatch 注记；冻结件勘误不在本 goal 执行 → A6 导出候选。

## A5 — 冻结面零修改 + 回归 ✓

- `git status --porcelain`：仅 `?? bench/rubric-v3/ablation/scripts/assert-hitmatrix-evidence.py`（新增）；hit-matrix.json / o3-claim-list.md / gold-tree.md / runs-C0-* 零 diff
- fixture 留痕检查：scripts/_tmp* 与 /tmp/hm-m*.json 均不存在
- 既有断言回归（repo root 执行，基线维持）：

| 脚本 | exit | 末行 |
|------|------|------|
| assert-o3-claim-list.py | 0 | === 4/4 检查组 PASS · 0 明细项 FAIL === |
| assert-goldrank-threshold.py | 0 | SUMMARY: 31 PASS / 0 FAIL |
| assert-gmr-recompute.py | 0 | === 11 PASS / 0 FAIL === |
| assert-o3-claim-rejudge.py | 0 | [SIGNAL] blocked-on-external: rejudge-results.json absent（r141 常态输出不变） |

## A6 — queue 更新 + 候选导出

见 goal-queue.md diff：(a) 追加本 goal 完成条目；(b) 导出勘误候选 **RV3G6-o3-claim-list-erratum-27**（§3.2 声明 4「27」不可复现 → V1=13，冻结件修改需 APPROVALS 登记 + 成璐裁定，备料模式不代裁）；(c) batch2-closure 条目无需再动（r141 已注记 assert-o3-claim-rejudge.py 消费者，本脚本不消费 [SIGNAL] 分流——它自身就是信号源）。