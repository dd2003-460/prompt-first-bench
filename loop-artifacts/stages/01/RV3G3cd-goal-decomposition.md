# 阶段 01：目标分解 — RV3G3-threshold-crossdomain-reverify

## 目标交付物

**assert 骨架脚本** `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（schema 预注册，同 r136 kappa-receipt 模式）+ 本 goal 六阶段工件。消费第二域 hit-matrix + 方案权重 JSON，机判 goldrank-threshold-proof.md L4.2 条件 (a)(b)：

- **(a)** t=4 过线集合跨域稳定（第二域 top-10 gold 计数复算 + 与第一域过线集合对照）
- **(b)** tie-sensitivity 审计：过线集合在全部合法 tie-break 下不变（全量置换枚举）

**不交付**：第二域实测数据（blocked-on-external，等 batch2）。当前脚本对 ablation 面常态输出 **SIGNAL blocked-on-external exit 0**（预期行为，同 r136 kappa-receipt 的 FAIL 常态——不伪造数据转绿）。

## 因素分解

| # | 因素 | 状态 |
|---|------|------|
| F1 | 输入 schema 预注册（第二域 hit-matrix / prior-estimates / 方案权重 JSON 的最小字段集） | 仓库内可推导（从现有 ablation 四文件反推最小公共 schema） |
| F2 | 复算协议冻结（top-10 计数 + gmr 排序 + tie-break 枚举，须与 assert-goldrank-threshold.py ⑤ 同协议防口径漂移） | 仓库内可推导（既有脚本即权威实现） |
| F3 | 判定语义（(a)/(b) 各自的 PASS/FAIL/SIGNAL 三分支定义 + 双域对照规则） | 需设计决策（本 goal 核心产出之一） |
| F4 | 第二域数据本体（hit-matrix-batch2.json 等） | **空缺 — 外部阻塞**（batch2 未到来） |
| F5 | 防漂移断言（骨架自身存在性 + schema 文档 token 检查，防后续篡改逃逸） | 仓库内可做 |

## 已知条件（仓库内事实源，全部只读）

- `bench/rubric-v3/goldrank-threshold-proof.md` L83：改回 top-10 主判据需 (a)(b)(c) 三条件；(a)(b) 为本 goal 机判对象，(c) 是 DRAFT 文本改写义务（非本 goal）
- `goldrank-threshold-proof.md` L2 tie-sensitivity 段：第一域 t=4 过线集合 {W3-orig, W4-orig, W3-new} 计数全部 tie-robust（全量合法 tie-break 置换枚举验证）
- `ablation/scripts/assert-goldrank-threshold.py` ⑤：top-10 复算协议 = 节点 ID 字典序 tie-break，与 assert-gmr-recompute.py 同协议；GOLD 集合 5 节点硬编码于该脚本（N-2.1, N-3.2.2, N-2, N-4, N-1.3）
- `ablation/hit-matrix.json`：run1..run8 → node → {h: 0|1, evidence: str|null}
- `ablation/prior-estimates.json`：nodes → {parent_id, p_tilde, reason, w2, parent_share, w1}；weight_formulas W0/W1/W2；W3=w1×w2、W4=w1+w2（g3-w3w4-completion.md L12-13 公式合成）
- r136 先例：assert-kappa-receipt.py 常态 FAIL exit 1（回执不存在）= 预期行为，闭环挂外部阻塞导出项

## 空缺清单

| 空缺 | 阻塞什么 | 处置 |
|------|---------|------|
| K1: 第二域 hit-matrix（batch2 runs） | (a)(b) 的实数判定 | 外部阻塞；骨架落 schema + 占位路径约定，数据到来后零改动接入 |
| K2: 第二域 gold 集合是否沿用第一域 5 节点 | (a) 的「过线集合」定义域 | **设计决策 D1**（见下）：默认沿用（同题面冻结），schema 允许显式覆盖并登记 |
| K3: 第二域方案权重 JSON 是否含 new-judge 侧 | (b) 的 tie 枚举范围 | **设计决策 D2**：schema 要求 orig/new 双侧对称（与第一域 7 方案对齐），缺失侧 = SIGNAL 降级 |
| K4: 「跨域稳定」的量化判据 | (a) 的 PASS 阈值 | **设计决策 D3**：过线集合相等 = PASS；仅计数相同但成员不同 = SIGNAL 人工裁决；成员不同且计数不同 = FAIL |

## 设计决策预注册（03 阶段执行，此处锁定方向防漂移）

- **D1**：gold 集合默认 = 第一域 5 节点（题面冻结，变体矩阵六变体同题面）；第二域若换题面则必须在新 JSON 显式声明 gold_nodes 字段，否则脚本 ERROR fail-loud（不静默沿用）
- **D2**：方案权重 JSON 最小 schema = `{schemes: {<name>: {formula: "W1"|"W2"|"W3"|"W4", judge: "orig"|"new"}}, ...}`；至少含 W1/W2/W3 × orig 三方案才出 verdict，缺 = SIGNAL
- **D3**：(a) 三分支如上表 K4；(b) 复用第一域枚举算法（边界节点 ±1 邻域的全部合法 tie-break 置换），tie-robust = 过线集合在所有置换下不变

## 阶段 02 研究入口

纯仓库内：精读 assert-goldrank-threshold.py ④⑤ 复算代码（提取为共享协议参考）、goldrank-threshold-proof.md L2 tie 枚举段、r136 assert-kappa-receipt.py 的 schema 预注册写法。无网络需求（标注 unverified 不适用——本 goal 无外部事实主张）。