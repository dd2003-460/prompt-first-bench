# T23-v2 Hetero-Judge 回执（Arena agent · 2026-11-05）

> origin: ai（arena agent 产出，Lead 转录）
> commit_sha（agent 本地）: 11a12de7a8b7d55a171e9db16b9904899e43e8b8
> 产物: runs/hetero-judge-v2-results.json (69KB) + receipt-t23-v2.md（在 agent workspace，push 403 未落 pfb）
> 校验: per_artifact=18 (S0–S5 × Q1 × r1–r3) · dims=108 · NA=0 · JSON 解析通过

## 结果曲线（Q1, n=3/arm）

```
S0=0.639 → S1=0.452 → S2=0.670 → S3=0.709 → S4=0.563 → S5=0.695
        -0.187      +0.218      +0.038      -0.145      +0.131
```

| Arm | total | range | 剔除M2 | M1 | M2 | M3 | M4 | M5 | M6 |
|-----|-------|-------|--------|------|------|------|------|------|------|
| S0 | 0.639 | 0.075 | 0.567 | 0.667 | 1.000 | 1.000 | 0.167 | 0.000 | 0.000 |
| S1 | 0.452 | 0.000 | 0.543 | 0.714 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 |
| S2 | 0.670 | 0.222 | 0.605 | 0.889 | 1.000 | 0.511 | 0.583 | 0.160 | 0.200 |
| S3 | 0.709 | 0.093 | 0.650 | 0.644 | 1.000 | 0.733 | 0.833 | 0.093 | 0.133 |
| S4 | 0.563 | 0.272 | 0.609 | 0.589 | 0.333 | 1.000 | 0.667 | 0.209 | 0.000 |
| S5 | 0.695 | 0.103 | 0.633 | 0.633 | 1.000 | 1.000 | 0.833 | 0.299 | 0.000 |

## 假设判定

| # | 声明 | Δ | verdict |
|---|------|-----|---------|
| H1 | S1 > S0 | **−0.187** | **REFUTED**（同源 judge 是 +0.118，方向相反！） |
| H2 | S1→S2 最大正增益 | +0.218 | CONFIRMED（五段最大） |
| H3 | S2→S3 负或近零 | +0.038 | REFUTED（但幅度近零） |
| H4 | S4→S5 微正 | +0.131 | CONFIRMED |

R5 自查: all_above_085=false（最高 0.807），spread=0.3575 ≥0.15 → 未压平。对比半异源 7B 的 range=0.07，v2 放大了 5 倍——校准有效。

## 三个必须上报的发现

### 1. H1 降级为 INCONCLUSIVE（任务书降级条款触发）
M4(S1)_hetero = 0.000 vs M4(S1)_same = 0.950，Δ = −0.950 < −0.15 → 按验收项 4，H1 的「分解价值在暴露缺口」声明降级为 INCONCLUSIVE。

### 2. S1 低分是工件本身的病，不是 judge 漂移（三重叠加）
- S1 三份全文 **0 个 URL / 0 个锚点**（sources=[]）→ gates 判 M2=0.000
- S1 把 gold 列为缺口的「workload 未定」写成「在固定 Batch Size 及固定序列长度条件下」→ **把未知收成了已知**，严格 R4 下 M4=0/4，比 S0（1/4）还低
- S1 三份都断言「H100 PCIe 支持 900 GB/s NVLink」，gold 明确 PCIe 无 NVLink

剔除 M2（gate 假象）重算：S0=0.567 / S1=0.543，仍为 **−0.027**。负向不翻转，但幅度从 −0.187 收到 −0.027。

### 3. M6 是最大 judge 分歧，且异源是对的
5 个 arXiv ID 经 arXiv API 实查全部真实存在但**全部不支持断言**：

| ID | 真实内容 | 支持断言 |
|----|----------|----------|
| 2608.15764 | LDG 带宽随并发下降 35%，测 3 个 SXM5 die | ❌ |
| 2607.19353 | 机密计算（Intel TDX）开销 | ❌ |
| 2606.05868 | YouZhi —— 华为 Ascend NPU 评测 | ❌ |
| 2609.19657 | PrefixBench-H100, prefix reuse/TTFT | ❌ |
| 2605.18805 | ReCoAtlas 推荐 agent 基准 | ❌ |

同源 27B 给 S2–S5 的 M6=1.000（假阳性），异源给 0.000–0.200。S5-Q1-r1 自己写明「本次 ego-browser 检索返回的 5 条来源均为 Microsoft Office 相关页面」。S4/S5 多份 sources 是 bing 跳转解析后的 nvidia.com/en-us/ 通用主页——存活但不支持任何规格断言。

## 必须暴露的 gate 缺陷

gates.py 的 `has_any_anchor` 是**全文级**判断：只要文中出现任意一个 URL/datasheet 字样，就把全部数字记为有锚点。S0 仅因不确定性段落提到 "datasheet" 一词，28 个数字全判 anchored，M2=1.000——假高。同源 27B 用的是行级语义判断（S0 M2=0.037）。

这解释了 arm 级 Δ 里最大的两格：S0 total 异源比同源 +0.248、S3 +0.158，主要都是这个 gate 造成的。**建议先修 gate（改为行级/claim 级锚点匹配）再对外发布 H1 结论。**

## 已知弱点
- S1-r2 与 S1-r3 逐字重复（5537 字符完全一致）→ S1 range=0.000，有效独立样本实为 1，不能当 n=3
- 只有 Q1：H1 被推翻只在 GPU 硬件这题上成立，不得外推到 Q2–Q5
- conf 上限 0.7（Arena Agent Mode，底层模型不公开）

## push 状态
❌ 403（同 T24：Arena GitHub App token 对 pfb 只有读权限）。agent 本地 3 个 commit（T24×2 + T23-v2×1）待授权后 `git push origin arena/4a614e63-prompt-first-bench`。完整 results.json (69KB) 在 agent workspace，需授权拉取或让 agent 输出。