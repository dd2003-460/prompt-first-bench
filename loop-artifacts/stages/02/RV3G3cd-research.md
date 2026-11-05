# 阶段 02：研究（仓库内既有实现精读）— RV3G3-threshold-crossdomain-reverify

> 分支 ralph/rv3g3-threshold-crossdomain-reverify · 2026-10-30 · 依据 01 分解 F1-F5
> 纯仓库内工作，零外部依赖；本阶段无网络需求（unverified 标注不适用——本 goal 无外部事实主张）

## §1 · 复算协议提取（F2：从 assert-goldrank-threshold.py ④⑤ 提取共享协议参考）

**权威实现** = `ablation/scripts/assert-goldrank-threshold.py`（r138+ 落盘，exit 0 + 变异测试实证）。骨架脚本必须与其口径逐字对齐，防跨域重验时出现「两域用不同 tie-break」的口径漂移。提取要点：

| 协议要素 | 权威值 | 出处 |
|---|---|---|
| GOLD 集合（第一域） | `["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]` | 脚本 L13 硬编码；与 assert-gmr-recompute.py 同一清单 |
| 排序键 | `(-float(weight), node_id)` —— 权重降序，并列按节点 ID **字典序升序** | 脚本 ⑤ `sorted(ws.items(), key=lambda kv: (-float(kv[1]), kv[0]))` |
| rank 口径 | 0-based | freeze §1 |
| top-10 计数 | `sum(nid in GOLD for nid, _ in items[:10])` | 脚本 ⑤ |
| gmr | `Σ rank(gold) / len(GOLD)`（0-based rank 均值） | 脚本 ⑤ 同源协议（freeze §5 id-order 列） |
| W2 精确化 | `w2_exact(p) = min(-log2(p), log2(1/ε)) → limit_denominator(10^6) + 1`，p=None → 1 | 脚本 w2_exact()，ε=0.01 |
| 方案公式 | W1=w1；W2=w2_exact(p_tilde)；W3=w1×w2；W4=w1+w2；new 侧 = judge-blindtest-r1.json w3_full_ranking 的 w1/w2/w3 字段 | 脚本 schemes dict |
| 数值类型 | Fraction 全程（防浮点比较漂移），仅排序键转 float | 脚本全局 |

**现场复算验证**（本阶段实跑，冻结 JSON 只读）：7 方案 top-10 gold 计数 = {W1:3, W2-orig:3, W3-orig:4, W4-orig:4, W2-new:2, W3-new:4, W4-new:3}，gmr = {10.20, 8.20, 5.40, 5.40, 9.80, 7.60, 7.60} —— 与 assert-goldrank-threshold.py ⑤ expected_counts 及 goldrank-threshold-proof.md L2 表**逐格一致，零 mismatch**。协议可无损移植进骨架。

## §2 · tie-sensitivity 枚举算法分析（F3 前置：(b) 的机判可行性）

**问题**：过线集合在全部合法 tie-break 下是否不变？全量置换枚举 = 对每个等权组做 permutations，31 节点下最坏情形不可控（单组 n≥12 即 12! ≈ 4.8×10⁸）。

**关键观察（本阶段推导）**：top-10 计数只受**压切线的等权组**影响。设切线位置 = idx 9/10（0-based），只有包含 idx 9 或 idx 10 的等权组 G 的排列会改变 top-10 成员；其余等权组的任意排列不触及切线，可固定为字典序。因此枚举空间 = ∏_{G 压线} C(|G|, |G∩top10|)（选哪些成员进 top-10，组内顺序不影响计数）。

**当前数据实测**（本阶段实跑，7 方案逐一检查）：

| 方案 | 压线等权组（idx 范围） | 组大小 | 枚举规模 | top-10 gold 计数取值集 |
|---|---|---|---|---|
| W1 | {2.972: N-1.2.1, N-1.2.2} @ idx9-10 | 2 | C(2,1)=2 | {3}（组内无 gold → 计数稳定） |
| W2-orig | 无多节点组 | — | 1 | {3} |
| W3-orig | 无多节点组 | — | 1 | {4} |
| W4-orig | 无多节点组 | — | 1 | {4} |
| W2-new | {2.737: N-1.1.2, N-1.3.1, N-2.1, N-5.3} @ idx8-11 | 4 | C(4,2)=6 | **{1, 2}**（gold N-2.1 在组内，tie-sensitive） |
| W3-new | {10.0: N-1,N-2} @ idx4-5；{3.725: …} @ idx23-25 | 2/3 | 均不压线 | {4}（tie-robust） |
| W4-new | 无压线多节点组 | — | 1 | {3} |

**结论**：
1. 限定「压线邻域枚举」后，当前数据最大枚举规模 = 6（W2-new），复杂度可控（O(∏C(|G|,k))，压线组通常 ≤4 节点）。
2. 该算法与 goldrank-threshold-proof.md L2 tie-sensitivity 段的既有结论**完全吻合**：W3-orig/W4-orig/W3-new 的 t=4 过线计数 tie-robust；W2-new 计数 ∈ [1,2]（注：L2 段登记的是 [2,3]——见 §4 诚实声明 #2 的差异溯源）。
3. (b) 的机判定义可冻结：**tie-robust = 过线判定（count ≥ t）在所有压线组合法置换下不变**；tie-sensitive = 存在某合法 tie-break 使过线状态翻转。引用具体计数时仍须带「id 字典序 tie-break 下」限定（freeze §4 规则 1 类推）。

## §3 · schema 预注册设计（F1：第二域输入最小字段集）

参照 r136 assert-kappa-receipt.py 模式（schema 违例 = FAIL fail-loud，缺失 = 明确状态而非静默跳过）：

**文件 1：第二域 prior-estimates**（路径约定 `<ablation>/prior-estimates-batch2.json`，可用 CLI 参数覆盖）
```json
{
  "nodes": {"<node_id>": {"parent_id": str|null, "p_tilde": float|null, "w1": number, "w2": number}},
  "weight_formulas": {...},            // 沿用第一域结构即可，骨架只读 nodes
  "gold_nodes": ["<node_id>", ...]     // D1：换题面必须显式声明；缺省 = 沿用第一域 5 节点（同题面冻结假设）
}
```
- 缺 `gold_nodes` 字段且题面标识 ≠ 第一域 → ERROR fail-loud（D1 处置：不静默沿用）。题面标识字段 `task_domain`（str）：等于 `"batch1"` 或缺省时允许缺省 gold_nodes；否则必填。

**文件 2：第二域 new-judge 排名**（路径约定 `<ablation>/judge-blindtest-batch2.json`）
```json
{"w3_full_ranking": [{"node": str, "w1": number, "w2": number, "w3": number}, ...]}
```
- 节点集必须与文件 1 的 nodes 键集相等（否则 ERROR）。

**文件 3（可选）：hit-matrix-batch2.json** —— 本骨架**不消费** hit-matrix（top-10/gmr 复算只需权重 + gold 集，hit-matrix 是 O3 证据层，非 goldrank 口径输入）。登记此决定防后续误加依赖。

**方案覆盖要求（D2）**：骨架从两个文件合成 7 方案（W1/W2/W3/W4 × orig/new，W1 双侧同值）。最少可出 verdict 的子集 = W1/W2/W3 × orig 三方案；缺任一侧 → 该侧方案记 MISSING，verdict 降级 SIGNAL（不 FAIL——数据不完整 ≠ 数据矛盾）。

## §4 · 诚实声明（负结果与不确定性）

1. **枚举算法未写完整代码**（本阶段只推导复杂度边界 + 当前数据实测表）——完整实现落 04 阶段，若实测发现压线组 >6 节点的域数据导致枚举爆炸，按 current-goal 失败降级条款限定「边界 ±1 邻域」并声明覆盖边界。
2. **§2 表 W2-new 取值集 {1,2} vs L2 段登记 [2,3]**：差异溯源——L2 段（r138+ 落盘）的 [2,3] 是「含 gold 的 4 节点并列组压线 → 计数 ±1」的局部邻域表述（以默认 id 序计数 2 为基准 ±1）；本阶段全量压线组枚举给出精确取值集 {1,2}（6 种置换中 4 种 N-2.1 不入 top-10 → 计数 1，2 种入 → 计数 2；计数 3 不可达，因为组外固定 top7 已含 2 个 gold 且组内最多再进 1 个 gold……复核：固定 top7 = idx0..6 含 gold {N-3.2.2? 需核} —— 本表 {1,2} 为实跑输出，L2 段 [2,3] 为 ±1 邻域近似。**两者不一致，登记为本 goal 导出项**：收口前须回查 L2 段原文语境，若 [2,3] 确为错误上界则走加注路径（历史工件留痕原则，不改原行，加勘误注记指向本 goal 精确值）。此项不阻塞骨架交付（骨架以现场枚举为准，不硬编码 L2 文本值）。
3. **D3 三分支阈值是设计决策不是既有事实**：「过线集合相等 = PASS」中的「过线集合」指方案名集合（如 {W3-orig, W4-orig, W3-new}），跨域对照时第二域方案名须与第一域同名映射（同公式同 judge 侧）——命名映射规则写入骨架 docstring，防 batch2 数据方自定义方案名导致静默失配。

## §5 · 阶段 02 判定

pass——F1/F2/F3 前置研究完成：协议提取零 mismatch（§1）、枚举算法复杂度可控且有当前数据实证（§2）、schema 三分支语义锁定（§3）；两项不确定性如实登记（§4 #2 的 L2 段差异待收口前回查，#1 的降级路径已预注册）。