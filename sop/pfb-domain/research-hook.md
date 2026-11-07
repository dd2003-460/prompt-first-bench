# Research Hook 架构

> origin: ai · 2026-11-07 · pfb 领域 SOP
> 为什么需要这份文件：research_hook 是 pfb 的"信息搜集引擎"——它决定模型在阶段 02 能查到什么。hook 设计不好，再好的 prompt 也查不到关键数据（D-face Q6/Q7 就是活例子：模型不是不想填数值，是 hook 没把定价页抓下来）。

## 双通道设计

```
阶段 02 触发
    ├── 通道 1: arXiv API（学术文献）
    │   └── ARXIV_QUERIES[qid] → search.arxiv.org/api
    │       返回 title + abstract + pdf_url
    │
    └── 通道 2: KNOWN_SITES 直访（商业/技术站点）
        └── _fetch_page(url) via ego-browser nodejs
            加载页面 → 等 2s → JS 提取文本
            → 关键词过滤 → 窗口去重 → snippet
```

**为什么两个通道**：arXiv 覆盖学术进展（方法、理论），但商业定价、产品规格、工程实践只在厂商官网。Q7（存储分层）的关键数值（HDD $28/TB、OSS ¥0.12/GB·月）只存在于阿里云/AWS 定价页，arXiv 上找不到。

## KNOWN_SITES 维护

每个 question 对应一组已验证可访问的 URL：

```python
KNOWN_SITES = {
    "Q6": [
        "https://aws.amazon.com/cloudfront/pricing/",
        "https://cloud.tencent.com/product/cdn",
    ],
    "Q7": [
        "https://www.aliyun.com/product/oss/pricing",
        "https://aws.amazon.com/s3/pricing/",
    ],
    # Q1-Q5: AI/ML 域，主要靠 arXiv，KNOWN_SITES 可选
}
```

**加新 URL 前必须验证**：ego-browser 打开确认 200 + 内容 > 200 chars。404 / JS-only 空页 / Cloudflare challenge 都算不可用。

**已知不可用**（别浪费时间试）：
- Cloudflare CDN product page（JS-rendered，_fetch_page 拿不到表格）
- Fastly CDN pricing（redirect 到登录）
- WD/Seagate pricing pages（404 或 region-blocked）

## _fetch_page 逻辑

```python
def _fetch_page(url):
    # ego-browser nodejs 加载
    # 等 2s（让 JS render）
    # 尝试选择器优先级：main → article → [role="main"] → .pricing-table → table
    # 选中元素 innerText > 200 chars → 用它
    # 否则 clone body, remove nav/footer/header, 用剩余 text
    # 返回 {title, bodyLen, sample: text.slice(0, 8000)}
```

**为什么用 ego-browser 而不是 requests**：大部分现代定价页是 JS-rendered 的 SPA。requests 拿到的是空 `<div id="app">`。ego-browser 驱动真实浏览器，能渲染 JS。代价是慢（每页 ~5s），但准确性值得。

**< 200 char fallback**：Aliyun OSS 页面曾返回 0 chars（CSS selector 没匹配到）。加了阈值：如果选中元素 < 200 chars，降级到 body 全文。

## HBM 窗口去重（commit 9b2f25d）

长页面（如 AWS S3 pricing 有 50+ 行表格）直接取 8000 chars 会截断在中间。改为：
1. 关键词 regex 匹配所有 hit 位置
2. 以 200-char bucket 为 key 去重（相邻 hit 合并为一个窗口）
3. 取最多 3 个非重叠窗口
4. 每个窗口 = hit 位置 ± 400 chars

**为什么 3 个窗口**：模型注意力有限，塞太多 snippet 反而稀释关键信息。3 × 800 chars = 2400 chars 上下文预算，够覆盖一个定价表的核心行。

**Mock 测试验证**：7 个 keyword hits → 正确提取 3 个非重叠窗口，重复 hit 被跳过。✅

## ARXIV_QUERIES

每个 question 有定制的 arXiv 搜索词：

```python
ARXIV_QUERIES = {
    "Q1": "LLM benchmark evaluation methodology",
    "Q3": "retrieval augmented generation factuality",
    "Q6": "CDN edge computing architecture cost optimization",
    "Q7": "data storage tiering cold warm hot hierarchy",
    ...
}
```

**改 query 时注意**：太宽泛（"machine learning"）→ 返回无关论文；太窄（"specific paper title"）→ 0 结果。甜点区是 3-5 个核心概念词的组合。

## FILTER_KEYWORDS

从 snippet 中提取相关窗口的 regex：

```python
FILTER_KEYWORDS = r"(price|cost|per GB|per TB|\$\d|¥\d|bandwidth|latency|PUE|tier|cache|hit rate|redundancy|overhead)"
```

**为什么包含定价模式**：D-face Q6/Q7 的 gold 叶子值大量是具体价格（$28/TB、¥0.12/GB·月）。初始 regex 只有技术术语，漏掉了所有数字型事实。加上 `\$\d|¥\d` 后覆盖率才上来。

## 已知局限

1. **模型不用 snippet 里的数值**：D-face v3 证明即使 snippet 包含了正确定价数据，27b 也不会把它填进答案。这是模型能力边界，不是 hook 问题。
2. **ego-browser 依赖桌面浏览器进程**：如果 ego lite 没开，_fetch_page 全部失败。降级方案：纯 arXiv 通道（丢失商业数据）。
3. **单页 8000 char 上限**：超长定价表（如 GCP 有 200+ SKU）会被截断。目前没解决方案，接受为 limitation。