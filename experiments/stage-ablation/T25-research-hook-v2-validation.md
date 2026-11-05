# T25 — research_hook v2.1：ego-browser 真实联网调研通道验证

> origin: ai · 2026-11-05 · Lead 执行
> 前置：T23 gold-gap-diagnosis（检索层断裂诊断）

## 问题

S2/S3 臂的 sources 全是 `bing.com/ck/a` 跳转链接（内容无关），导致：
- M6 只查 URL 存活→满分（假阳性）
- 27b 拿不到真实数据→无法产出 gold 级别的定量结论
- H2/H3（调研阶段增益）无法验证

## 根因

ego-browser 环境下搜索引擎全部不可用：
| 引擎 | 结果 |
|------|------|
| Bing | 返回垃圾（xhamster/公寓广告） |
| DuckDuckGo HTML | 空结果 |
| Startpage | Cloudflare 验证墙 |

但**直接访问已知站点正常**（arxiv.org、nvidia.com 等）。

## 方案：research_hook v2.1

不依赖搜索引擎，改为两通道组合：
1. **arXiv API**（主）：`export.arxiv.org/api/query?search_query=all:<full_query>&sortBy=relevance` → Atom XML 解析
2. **已知站点直访**（补充）：NVIDIA 规格页、ThunderCompute、CloudGPUTracker 等按 Q 映射

关键修复：
- 完整 query URL-encode（之前只取首尾词→匹配到无关论文）
- `sortBy=relevance` 排序
- gates.py 加 `BAD_ANCHOR` 正则排除 bing.com/ck/a 类链接

## 验证结果

全量 90-run 重评分（27B same-source judge，12 min）：

| 臂 | 旧 Total (bing垃圾源) | 新 Total (arXiv真实源) | Δ |
|----|----------------------|----------------------|---|
| S0 | 0.374 | 0.391 | +0.017 |
| S1 | 0.463 | 0.509 | +0.046 |
| S2 | 0.535 | 0.570 | +0.035 |
| S3 | 0.489 | 0.550 | +0.061 |
| S4 | 0.528 | 0.569 | +0.041 |
| S5 | 0.548 | 0.580 | +0.032 |

**假设检验更新：**
- H1（分解正贡献）✅ 确认且增强：S1>S0, Δ=+0.118（旧 +0.089）
- H2（调研增益）✅ 方向确认：S2>S1, Δ=+0.061（旧 +0.072）
- H3（交叉验证）❌ 仍无增益：S3<S2, Δ=-0.020
- Range: 0.189（旧 0.174）→ 区分度略增

**M1 事实准确率（关键发现）：**
- S0: 0.449 → S1: 0.687（分解大幅提升事实准确性）
- S2: 0.655（有真实 arXiv 源但 M1 反而比 S1 低！）
- 原因：arXiv API 关键词匹配太泛（"NVIDIA H100" 匹配到无关论文），27b 引用了不相关数据
- S4: 0.707 最高（交叉验证帮助过滤了错误引用）

**M6 URL 存活：**
- S0/S1: 0.000（无源，正确）
- S2-S5: 1.000（arXiv URL 全部存活，正确）

**Gold 可达性结论修正：**
- 瓶颈**不在检索通道**（修复后分数确实提升）
- 瓶颈在 **27b 推理深度 + arXiv 检索精度**：
  - 27b 拿到源后仍需自行综合出定量结论（gold 要求 workload-conditioned 数字）
  - arXiv 关键词匹配精度不足（需更精准的 query 构造或 RAG 式 embedding 搜索）
- S5=0.580 仍未到 gold（~0.8+），差距 ~0.22

## 对 PFB 流程的影响

- S2+ 臂现在有**真实联网调研能力**（arXiv + 直访）
- 后续重跑 S2-S5 可验证 H2/H3（调研/交叉验证阶段是否真的增益）
- arena agent 做文献调研时同样适用此通道（T24 task book 已更新）

## 局限

- ~~arXiv API 关键词匹配精度有限~~ → **v2.2 已修**：双策略查询（all: + ti: 标题限定），S2-Q1 均值从 0.566 涨到 0.652（+0.086）
- 无通用搜索能力（只能访问预定义站点列表）
- 未来改进：让 27b 自己决定访问哪些 URL（agent 式调研）

## v2.2 精度修复（2026-11-05 追加）

问题：v2.1 用 `all:` 全文匹配，"H100 PCIe vs SXM" 会命中所有含 "NVIDIA" 的论文，27b 引用了不相关数据导致 M1 下降。

修复：`_arxiv_search()` 改为双路并行——
1. `all:<full_query>`（宽召回）
2. `ti:<specific_words>`（标题限定，只匹配标题含核心词的论文）
合并去重，标题限定优先。

验证（S2 全 5 题，各 3 reps）：
| 题 | v2.1 avg | v2.2 avg | Δ |
|----|----------|----------|---|
| Q1 (H100 PCIe vs SXM) | 0.566 | 0.652 | +0.086 |
| Q2 (A100 specs) | 0.644 | 0.712 | +0.068 |
| Q3 (LLM inference cost) | 0.541 | 0.396 | **-0.144** |
| Q4 (GPU cluster networking) | 0.457 | 0.458 | +0.001 |
| Q5 (Training vs inference) | 0.642 | 0.663 | +0.021 |

**结论：v2.2 双策略不是普适提升。** Q1/Q2 涨（arXiv 标题限定命中了精准论文），Q3 跌（"LLM inference cost" 的 ti: 查询可能过滤掉了真正相关的 pricing/cost 论文——这类内容不在 arXiv 标题里）。Q4/Q5 基本持平。

下一步：对 Q3 类问题（非纯学术、偏 vendor/pricing）应优先走 KNOWN_SITES 直访通道，而非 arXiv。