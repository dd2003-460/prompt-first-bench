# idea53 类工作：最小可行 / 可发表 / 零成本路径决策（2026-11-25）

> 问题：像 idea53 这种「前置工作 + toy + 闭式 + 精确零负控制」的小工作，
> 在**不花注册费/差旅/版面费**的硬约束下，最小可发表选择是什么？
> 结论先行：**arXiv（免费锁时间戳）+ TMLR（免费真发表）双层**，跳过 workshop。

---

## 一、为什么 workshop 不是最小选择（推翻上一轮推荐）

ICLR 2027 Workshop Proposal Guide 对 tiny/short paper track 的**硬性约束**：

> "Because ICLR tiny and short papers are a participatory initiative, **AI-generated papers are not allowed for these formats.** AI assistance is permitted, but submissions must be primarily human-authored, reflecting original thought and analysis."

> "The only exception is the Tiny Papers track, which does not permit AI-generated content due to requirements associated with its funding. In this iteration of ICLR workshops, **the conference will provide tools to flag AI-generated papers**, reviews, and meta-reviews."

来源：https://iclr.cc/Conferences/2027/WorkshopGuidelines

**这条直接卡住 idea53**：双版稿由 AI 主笔、arena 六轮审查，属于 AI-generated 高风险区，不是 "primarily human-authored"。上一轮 arena 推荐的三个 workshop 里最贴合的 "Science and Society of Modern AI（tiny ≤3 页）" 正好是 tiny track——**这条路要划掉**，除非人类作者大幅重写主体论证。

附带两个次级问题：
- ICLR workshop 全部线下（2027-04-29/30，San Francisco），不参会只能请人代贴 poster 或预录视频；虽然投稿本身免费，但"展示"价值打折。
- workshop 存档状态由各 workshop 自定（ICLR guide 要求组织者明示）；若是 archival，会**堵死 TMLR**（TMLR 明文不接受与已发表 archival 工作有文字/图/结果复用的投稿）。

**所以 workshop 在"最小 + 零成本 + 不堵后路"三项上全面劣于 arXiv+TMLR。**

---

## 二、为什么 arXiv + TMLR 是唯一同时满足三项的组合

| 约束 | arXiv | TMLR | ICLR tiny workshop | NeurIPS/ICML 主会 |
|---|---|---|---|---|
| 注册/差旅 | 0 | **0（不要求参会）** | 0 投稿，但线下 | 强制 ≥$285–700 + 差旅 |
| 版面费/APC | 0 | **0**（CC BY 4.0，版权归作者） | 0 | 0 |
| 同行评审 | 否（公开记录+时间戳） | **是（双盲、≥3 reviewer）** | 是但弱 | 是 |
| 接受 modest 贡献 | — | **明文接受**："Papers should be accepted... even if the contribution or significance of the work is modest" | 是 | 否，要 significance |
| 与前置稿重叠 | 允许 | **明文允许 arXiv 重叠** | 取决于 archival 状态 | 视为 prior work |
| AI-generated 限制 | 生成式 AI 不能列为作者，辅助写作允许 | 未见 tiny-track 式禁令 | **明文禁止 tiny 轨** | 各有 AI policy |

来源：
- arXiv 免费 + 版权：https://info.arxiv.org/help/submit/index.html ; https://jmlr.org/tmlr/author-guide.html
- TMLR 零 APC / 接受 modest / 允许 arXiv 重叠：https://jmlr.org/tmlr/editorial-policies.html ; https://jmlr.org/tmlr/author-guide.html
- TMLR 上行 J2C（约 10% 认证 → 三大会 poster，不再评审）：https://iclr.cc/public/JournalToConference

**TMLR 的定位与这个工作逐字对齐**："technical correctness over subjective significance" + "modest contribution 也可接受" + 拒 "bold statements unsupported by evidence"。idea53 的闭式模型 + 精确零负控制正是 technical correctness，不靠 significance 撑。

**arXiv 的作用不是发表，是免费锁公开时间戳**：替代 GitHub hash 时间戳（eb1b0598c < 718394ece），且 TMLR 明文允许 arXiv 重叠——两件事互不冲突，一次写作两处收益。

---

## 三、现有材料离"能投"还差什么（最小动作，不碰被锁文件）

**关键约束**：`submission/SHA256SUMS.txt` 锁了 `paper.tex`、`paper.pdf`、`body.tex`、`header.tex`、`formalism-skeleton.*`、`idea53-hds-recompute.py` 共 7 个文件——这是预注册优先级证据，**任何修改都会让 hash 对不上**。所以投稿版必须在 `manuscript-scoped/` 另起，不能原地改。

| 现有材料 | 状态 | 能否直接用 |
|---|---|---|
| `submission/paper.tex` | 英文 9 页、**0 图 0 引用**，且被 hash 锁 | 否（不能改） |
| `submission/paper-zh.tex/.pdf` | 中文 11 页、16 bibitem、7 cite、已编译 | 参考用；arXiv 要求英文版在前，中文不能单独投 |
| `submission-staging/references.bib` | 15 条已核验引用 + 一键合并脚本 | 是（但脚本写入被锁的 paper.tex，**不可执行**） |
| `manuscript-scoped/paper-en.md` | 英文 10 节，含 comparison table + 投稿口径 | 是，作为新稿底本 |
| `manuscript-scoped/fig1-scoring-protocol.tex` | 结构图 TikZ | 是，需转 PDF |
| `manuscript-scoped/paper-zh.md` | 中文内部稿 | 是（内部梳理，不投稿） |

**三步最小动作**：
1. 以 `manuscript-scoped/paper-en.md` 为底本，在 `manuscript-scoped/` 下生成一份 TMLR 格式 LaTeX（用 TMLR stylefile），把 `fig1` 转 PDF 插入，把 staging 的 15 条 bib 接进去。
2. 编译通过后先传 arXiv（`cs.LG` / `cs.PF`；免费，1–2 天公开），拿到 arXiv ID。
3. 用同一份稿投 TMLR（rolling，无固定截稿，0 费用，不要求参会）；arXiv ID 写在投稿备注里，不构成 dual submission。

**不做的事**：不执行 `merge_references.py`（会改被锁的 paper.tex）；不投 ICLR tiny track（AI-generated 禁令）；不投 NeurIPS 主会（强制到场+差旅）。

---

## 四、决策

**最小可行可发表无成本选择 = arXiv（锁日期、可引用）+ TMLR（真同行评审、0 元、不参会）双层，同一份英文稿。**

- 这不是"退而求其次"：TMLR 明文接受 modest contribution，恰好匹配"前置工作"定位；J2C 上行通道还留了 concert poster 的可能（需约 10% 的 certification）。
- workshop 不是更小，而是更险：tiny track 的 AI-generated 禁令 + archival 状态不确定 + 可能堵死 TMLR。
- 中文稿继续当内部梳理用；arXiv 若要放中文，必须英文在前、中文在后，双语合订。

## 未验证 / 需复核
- TMLR 对 AI-assisted writing 的具体披露要求：editorial policies 未见 tiny-track 式禁令，但投稿时可能需 AI use statement（参考 ICLR 2027 已强制），提交前查最新 author guide。
- arXiv cs.LG 新用户 endorsement 要求（若有账号历史通常免）。
- TMLR 2026-12 是否照例暂停投稿（2025 年是 12/2–1/5）——官网未公布 2026 安排，提交前确认。
