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

4 个测试 run（S2/S3 × Q1/Q2）+ S3-Q5 重跑：
- ✅ 全部拿到真实 arXiv URL（如 `arxiv.org/abs/2608.15764v1`）
- ✅ 27b 输出质量提升：引用了具体带宽数值（3.35 TB/s vs 2.0 TB/s）、NVLink 900 GB/s
- ✅ M1 judge 判定 match（断言与 gold 一致）
- ⏳ 全量 90-run 评分进行中（~10 min）

## 对 PFB 流程的影响

- S2+ 臂现在有**真实联网调研能力**（arXiv + 直访）
- 后续重跑 S2-S5 可验证 H2/H3（调研/交叉验证阶段是否真的增益）
- arena agent 做文献调研时同样适用此通道（T24 task book 已更新）

## 局限

- arXiv API 关键词匹配精度有限（"H100 PCIe vs SXM" 会匹配到含 NVIDIA 的无关论文）
- 无通用搜索能力（只能访问预定义站点列表）
- 未来改进：让 27b 自己决定访问哪些 URL（agent 式调研）