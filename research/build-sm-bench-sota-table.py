#!/usr/bin/env python3
"""T53C: 生成 research/sm-bench-sota-table.json（可重跑，纯 stdlib）。

数据来源一律为本次会话实取的页面（arXiv HTML / 官网 / ICLR proceedings PDF），
每条带 source_url + 逐字摘录，便于 Lead 复算。版本口径见 contradictions.X1。
"""
import json
import os

Q = {
    "q1": "2024年 NVIDIA H200 GPU 的 TDP 是多少瓦？比 H100 SXM 高多少百分比？",
    "q2": "Transformer 原始论文中 multi-head attention 的 head 数是多少？GPT-3 用了多少？差几倍？",
    "q3": "HotpotQA 数据集有多少条标注？其中 compositional 类型占多少比例？",
    "q4": "LLaMA 2 70B 的参数量是多少？训练用了多少 token？",
    "q5": "DeepSeek-V3 的 MoE 总参数和激活参数分别是多少？ratio 是多少？",
}

NULL_REASON = (
    "公开榜单/论文均不发布这 5 道自定义题的逐题分数：题目为 pfb 自建 sm-bench，"
    "不属于任何公开 benchmark 的 test set。按任务书「找不到逐题分数就给 aggregate + 说明哪篇论文/哪个 leaderboard」"
    "与「没有公开 per-question 数据标 null 并说明」处理：逐题一律 null，不估算、不插值。"
)

DRB = "https://deepresearch-bench.github.io/"
ICLR = ("https://proceedings.iclr.cc/paper_files/paper/2026/file/"
        "465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf")
DEEP_RES = "https://arxiv.org/html/2504.03160"
TONGYI = "https://arxiv.org/html/2510.24701"


def row(name, url, bench, agg, extra, level, quote, notes):
    return {
        "name": name,
        "source_url": url,
        "benchmark": bench,
        "per_question_scores": {k: None for k in Q},
        "per_question_null_reason": NULL_REASON,
        "aggregate": agg,
        "other_metrics": extra,
        "evidence_level": level,
        "verbatim_excerpt": quote,
        "notes": notes,
    }


systems = []

# ── A. 短答案事实检索类（与 pfb 5 题同型）────────────────────────────
systems.append(row(
    "Tongyi DeepResearch (30B-A3B)",
    TONGYI,
    "GAIA(70.9) / HLE(32.9) / BrowseComp(43.4) / BrowseComp-ZH(46.7) / xbench-DeepSearch(75.0) / WebWalkerQA(72.2) / FRAMES(90.6)，Avg@3",
    {
        "em": None,
        "f1": None,
        "accuracy_mean_over_7_benchmarks": round((32.9 + 43.4 + 46.7 + 70.9 + 75.0 + 72.2 + 90.6) / 7, 2),
    },
    {
        "HLE": 32.9, "BrowseComp": 43.4, "BrowseComp-ZH": 46.7, "GAIA": 70.9,
        "xbench-DeepSearch": 75.0, "WebWalkerQA": 72.2, "FRAMES": 90.6,
    },
    "verified_primary_fulltext",
    "Tongyi DeepResearch (30B-A3B) | 32.9 | 43.4 | 46.7 | 70.9 | 75.0 | 72.2 | 90.6   (Table 1, arXiv:2510.24701)",
    "开源（GitHub Alibaba-NLP/DeepResearch + HF 权重 + 官方复现脚本）。Avg@3、128 次工具调用上限、128K 上下文。"
    "61.67 是本人对 7 个 accuracy 的算术平均（论文无此聚合），仅用于排序参考。",
))

systems.append(row(
    "OpenAI Deep Research (o3-based)",
    "https://openai.com/index/introducing-deep-research/",
    "GAIA text-only validation (pass@1) + Humanity's Last Exam",
    {"em": None, "f1": None, "gaia_pass1_avg": 67.36},
    {
        "GAIA_Level1": 74.29, "GAIA_Level2": 69.06, "GAIA_Level3": 47.6, "GAIA_avg_pass1": 67.36,
        "GAIA_avg_cons64": 72.57, "HLE": 26.6, "GAIA_previous_SOTA_avg": 63.64,
    },
    "verified_primary_fulltext",
    "| Deep Research (pass@1) | 74.29 | 69.06 | 47.6 | 67.36 |  ;  | Deep Research (cons@64) | 78.66 | 73.21 | 58.03 | 72.57 |  ;  | OpenAI deep research** | 26.6 |",
    "闭源、无逐题数据、无复现脚本。注意 distinguishing pass@1 67.36 与 cons@64 72.57——引用时必须写清口径，"
    "媒体常混用。Tongyi 报告 Table 1 转引为 GAIA 67.4 / BrowseComp 51.5 / HLE 26.6，与官方一致。",
))

systems.append(row(
    "DeepResearcher (RL, Qwen2.5-7B)",
    DEEP_RES,
    "NQ / TriviaQA / HotpotQA / 2WikiMultiHopQA（各 dev 采样 512 题）— F1 + MBE",
    {
        "em": None,
        "f1": None,
        "f1_mean_over_4_benchmarks": round((39.6 + 78.4 + 52.8 + 59.7) / 4, 2),
        "mbe_mean_over_4_benchmarks": round((61.9 + 85.0 + 64.3 + 66.6) / 4, 2),
    },
    {
        "NQ_F1": 39.6, "NQ_MBE": 61.9, "TQ_F1": 78.4, "TQ_MBE": 85.0,
        "HotpotQA_F1": 52.8, "HotpotQA_MBE": 64.3, "2Wiki_F1": 59.7, "2Wiki_MBE": 66.6,
    },
    "verified_primary_fulltext",
    "DeepResearcher | Web Search | 39.6 | 61.9 | 78.4 | 85.0 | 52.8 | 64.3 | 59.7 | 66.6   (Table 1, arXiv:2504.03160)",
    "本项目找到的**唯一**同时公开 NQ/TQ/HotpotQA/2Wiki 四项 F1 的 deepresearch agent，且是真实互联网环境（非本地 RAG）。"
    "论文只报 F1 与 MBE（GPT-4o-mini 判对错），不报 EM；57.63/69.45 是本人对 4 项算术平均。",
))

systems.append(row(
    "Search-R1 (base, Qwen2.5-7B)",
    DEEP_RES,
    "NQ / TQ / HotpotQA / 2Wiki（同上 512 题）— 数字转引自 DeepResearcher Table 1",
    {"em": None, "f1": None, "f1_mean_over_4_benchmarks": round((45.4 + 71.9 + 55.9 + 44.6) / 4, 2)},
    {"NQ_F1": 45.4, "TQ_F1": 71.9, "HotpotQA_F1": 55.9, "2Wiki_F1": 44.6},
    "secondary_table_in_primary_paper",
    "Search-r1-base | Local RAG | 45.4 | 60.0 | 71.9 | 76.2 | 55.9 | 63.0 | 44.6 | 47.9",
    "分布差异警告：Search-R1 在**本地 Wikipedia RAG** 上评测（直接拿到相关语料），HotpotQA F1 55.9 > DeepResearcher 52.8，"
    "但这不能解读为真网检索更强。",
))

systems.append(row(
    "R1-Searcher",
    DEEP_RES,
    "NQ / TQ / HotpotQA / 2Wiki（同上 512 题）— 数字转引自 DeepResearcher Table 1",
    {"em": None, "f1": None, "f1_mean_over_4_benchmarks": round((35.4 + 73.1 + 44.8 + 59.4) / 4, 2)},
    {"NQ_F1": 35.4, "TQ_F1": 73.1, "HotpotQA_F1": 44.8, "2Wiki_F1": 59.4},
    "secondary_table_in_primary_paper",
    "R1-Searcher | Web Search | 35.4 | 52.3 | 73.1 | 79.1 | 44.8 | 53.1 | 59.4 | 65.8",
    "受约束真网：query 强制追加 site:en.wikipedia.org，且只读前 3 页。",
))

# ── B. 长报告类（DeepResearch Bench / RACE，ICLR 2026 camera-ready 口径）──
systems.append(row(
    "LangChain Open Deep Research (backbone=GPT-5)",
    ICLR,
    "DeepResearch Bench（100 个 PhD 级任务，RACE + FACT），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 50.60},
    {
        "RACE_Comprehensiveness": 50.06, "RACE_Depth": 50.76,
        "RACE_Instruction_Following": 51.31, "RACE_Readability": 49.72,
        "FACT_citation_accuracy": 32.94, "FACT_effective_citations_per_task": 21.06,
    },
    "verified_primary_fulltext",
    "LangChain Open DeepResearch (GPT-5) | 50.60 | 50.06 | 50.76 | 51.31 | 49.72 | 32.94 | 21.06",
    "**开源框架 + 闭源 backbone**：RACE 超过 Gemini-2.5-Pro DR（49.71），但 FACT 引用准确率只有 32.94（多 agent 摘要层导致引用错位）。"
    "若 pfb 要「可复跑且分数高」，这是比 Tongyi 更强的候选，代价是绑定 GPT-5 API。",
))

systems.append(row(
    "Gemini-2.5-Pro Deep Research",
    ICLR,
    "DeepResearch Bench（RACE + FACT），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 49.71},
    {
        "RACE_Comprehensiveness": 49.51, "RACE_Depth": 49.45,
        "RACE_Instruction_Following": 50.12, "RACE_Readability": 50.00,
        "FACT_citation_accuracy": 78.30, "FACT_effective_citations_per_task": 165.34,
    },
    "verified_primary_fulltext",
    "Gemini-2.5-Pro Deep Research | 49.71 | 49.51 | 49.45 | 50.12 | 50.00 | 78.30 | 165.34",
    "有效引用数最高（165.34/任务）但引用准确率低于 Perplexity（82.63）→ 密度与精度互斥，做 M6 类指标时要分开报。",
))

systems.append(row(
    "OpenAI Deep Research (on DeepResearch Bench)",
    ICLR,
    "DeepResearch Bench（RACE + FACT），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 46.45},
    {
        "RACE_Comprehensiveness": 46.46, "RACE_Depth": 43.73,
        "RACE_Instruction_Following": 49.39, "RACE_Readability": 47.22,
        "FACT_citation_accuracy": 75.01, "FACT_effective_citations_per_task": 39.79,
    },
    "verified_primary_fulltext",
    "OpenAI Deep Research | 46.45 | 46.46 | 43.73 | 49.39 | 47.22 | 75.01 | 39.79",
    "同一系统 GAIA pass@1 67.36、DeepResearch Bench RACE 46.45：短答案对错 vs 长报告质量是两套能力，不可互换。"
    "注意官网页 v1 表给的是 46.98（版本漂移见 contradictions.X1）。",
))

systems.append(row(
    "Tongyi DeepResearch (on DeepResearch Bench)",
    ICLR,
    "DeepResearch Bench（RACE），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 40.46},
    {"RACE_Comprehensiveness": 39.46, "RACE_Depth": 34.44, "RACE_Instruction_Following": 46.22, "RACE_Readability": 44.27},
    "verified_primary_fulltext",
    "Tongyi DeepResearch | 40.46 | 39.46 | 34.44 | 46.22 | 44.27 | - | -",
    "FACT 为「-」：论文说明开源 RL 系统未按格式生成引用，无法抽取核验。这是选 baseline 时要预判的坑（pfb 的 M6 需要 URL）。",
))

systems.append(row(
    "DeepResearcher (on DeepResearch Bench)",
    ICLR,
    "DeepResearch Bench（RACE），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 10.77},
    {"RACE_Comprehensiveness": 8.66, "RACE_Depth": 5.96, "RACE_Instruction_Following": 15.57, "RACE_Readability": 15.65},
    "verified_primary_fulltext",
    "DeepResearcher | 10.77 | 8.66 | 5.96 | 15.57 | 15.65 | - | -",
    "**关键反例**：HotpotQA F1 52.8 的同一模型，RACE 只有 10.77（原文：frequently fails to generate complete, well-structured reports）"
    "→ 「短答案检索强」不代表「深研报告强」，选 baseline 必须先看 pfb 要评什么。",
))

systems.append(row(
    "Perplexity Deep Research",
    ICLR,
    "DeepResearch Bench（RACE + FACT），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 40.46},
    {
        "RACE_Comprehensiveness": 39.10, "RACE_Depth": 35.65,
        "RACE_Instruction_Following": 46.11, "RACE_Readability": 43.08,
        "FACT_citation_accuracy": 82.63, "FACT_effective_citations_per_task": 31.20,
    },
    "verified_primary_fulltext",
    "Perplexity Deep Research | 40.46 | 39.10 | 35.65 | 46.11 | 43.08 | 82.63 | 31.20",
    "引用准确率第二（82.63）但有效引用少（31.20）。",
))

systems.append(row(
    "Kimi Researcher",
    ICLR,
    "DeepResearch Bench（RACE），ICLR 2026 版 Table 1",
    {"em": None, "f1": None, "race_overall": 44.64},
    {"RACE_Comprehensiveness": 44.96, "RACE_Depth": 41.97, "RACE_Instruction_Following": 47.14, "RACE_Readability": 45.59},
    "verified_primary_fulltext",
    "Kimi Researcher | 44.64 | 44.96 | 41.97 | 47.14 | 45.59 | - | -",
    "FACT 缺失原因同 Tongyi（官方 UI 无法解析引用链接）。",
))

per_question_mapping = {
    "q1": {
        "question_type": "单点事实 + 数值比较（H200 vs H100 SXM TDP）",
        "nearest_public_rows": ["DeepResearcher.NQ_F1", "DeepResearcher.TQ_F1", "Tongyi.FRAMES"],
        "why": "单跳数值事实；最接近 NQ/TriviaQA（单跳事实，F1 口径）与 FRAMES（多跳短答案，accuracy）。",
    },
    "q2": {
        "question_type": "双实体属性 + 比值（Transformer head 数 vs GPT-3 head 数）",
        "nearest_public_rows": ["DeepResearcher.HotpotQA_F1", "DeepResearcher.2Wiki_F1", "Tongyi.GAIA"],
        "why": "比较型双实体问题，结构最接近 HotpotQA comparison 子集与 2Wiki bridge-comparison。",
    },
    "q3": {
        "question_type": "数据集元信息（HotpotQA 标注条数 + compositional 比例）",
        "nearest_public_rows": ["DeepResearcher.HotpotQA_F1", "DeepResearcher.TQ_F1"],
        "why": "答案就在 HotpotQA 原论文里 → 考的是「记不记得文献」而非「会不会检索」。"
               "任何 deepresearch agent 都无特化优势，对 baseline 区分度低，建议在 sm-bench 里定位为「地板题」。",
    },
    "q4": {
        "question_type": "单点事实 + 数值（LLaMA 2 70B 参数量 / 训练 token）",
        "nearest_public_rows": ["DeepResearcher.NQ_F1", "Tongyi.FRAMES"],
        "why": "浅两跳单值事实，最接近 NQ 型。",
    },
    "q5": {
        "question_type": "单点事实 + 双数值 + 派生比值（DeepSeek-V3 总参/激活/ratio）",
        "nearest_public_rows": ["DeepResearcher.TQ_F1", "Tongyi.FRAMES"],
        "why": "需给两个数再算比值，接近 TriviaQA 细节题 + FRAMES 多属性题。",
    },
}

contradictions = [
    {
        "id": "X1",
        "topic": "DeepResearch Bench 的 RACE 分数在三个来源之间不一致（版本漂移 + 第三方失真）",
        "values": {
            "官网页 v1（deepresearch-bench.github.io 当前表）": {"OpenAI DR": 46.98, "Gemini-2.5-Pro DR": 48.88, "Perplexity DR": 42.25, "Grok": 40.24},
            "ICLR 2026 camera-ready Table 1（本文件采用）": {"OpenAI DR": 46.45, "Gemini-2.5-Pro DR": 49.71, "Perplexity DR": 40.46, "Grok": 38.22, "Tongyi": 40.46, "DeepResearcher": 10.77, "LangChain ODR(GPT-5)": 50.60},
            "第三方 aiwiki.ai": {"OpenAI DR": 80.7, "Gemini-2.5-Pro DR": 82.3},
        },
        "explanation": "RACE 是「与参考报告比值」打分（S_final = S_int(tgt) / (S_int(tgt)+S_int(ref))），"
                       "换参考报告或换 judge 版本会整表平移；论文自己也说「应看排名与比例差，不看绝对值」。"
                       "aiwiki.ai 的 80.7/82.3 在任何一手来源中都找不到对应口径，无法复算。",
        "resolution": "本文件的 DeepResearch Bench 行**统一采用 ICLR 2026 camera-ready 表**（同一版本内部可比），"
                      "官网页 v1 的数值仅在 notes 里作为版本漂移记录；aiwiki.ai 判为不可用来源，不采信。"
                      "v1 与 camera-ready 的排名基本一致（Gemini > OpenAI > Perplexity > Grok），故结论不受影响。",
    },
    {
        "id": "X2",
        "topic": "GAIA 上 OpenAI Deep Research 的 67.36 vs 67.4",
        "values": {"openai.com blog": 67.36, "Tongyi 技术报告 Table 1": 67.4},
        "explanation": "四舍五入，非矛盾。",
        "resolution": "采信官方 67.36（pass@1）。",
    },
    {
        "id": "X3",
        "topic": "GAIA 分数口径混淆：pass@1 67.36 vs cons@64 72.57",
        "values": {"pass@1": 67.36, "cons@64": 72.57},
        "explanation": "官方 blog 同页并列两个口径；二手报道常只写 72.57 或 67.36 之一而不注明。",
        "resolution": "本文件 aggregate 只写 pass@1 67.36；cons@64 放 other_metrics 并显式命名。",
    },
    {
        "id": "X4",
        "topic": "同一模型「检索强」与「深研报告弱」并存",
        "values": {"DeepResearcher HotpotQA F1": 52.8, "DeepResearcher RACE": 10.77},
        "explanation": "任务形态不同：短答案 F1 只看最终答案；RACE 看长报告结构/覆盖/可读性。",
        "resolution": "这是选 baseline 的硬约束：pfb 的 5 题是短答案，不能用 RACE 排名选 baseline。",
    },
]

doc = {
    "task": "T53C-SOTA",
    "task_book": "tasks/T53C-sota-research.md",
    "generated_at_utc": "2026-11-11",
    "base_commit": "ac1b481",
    "branch": "arena/f65a5a27-prompt-first-bench",
    "question_set": Q,
    "provenance_policy": {
        "rule_1": "每个分数必须带 source_url；无 URL 的分数不落盘。",
        "rule_2": "逐题分数：公开数据不存在 → 一律 null + 写明原因，不估算。",
        "rule_3": "转引自他人论文表格的分数标 secondary_table_in_primary_paper，并写明原始评测环境差异。",
        "rule_4": "本人计算的聚合（如 4 项 F1 平均）单独命名，并注明「论文未给此聚合」。",
        "rule_5": "同一 benchmark 只用一个版本的表格做横向比较；版本差异写进 contradictions。",
    },
    "sota_systems": systems,
    "per_question_mapping": per_question_mapping,
    "contradictions": contradictions,
    "unverified_candidates": [
        {
            "name": "WebSailor-v2-30B-A3B (RL)",
            "claimed_score": {"GAIA_text_only_test_pass1": 74.1},
            "source_url": "https://www.sota2.com/research/sota/deep-research-on-gaia-text-only-original-test",
            "why_not_used": "仅第三方聚合站数据，未取到原论文表格；按「不编」原则不入主表。若采用需核 WebSailor 原论文。",
        },
        {
            "name": "GLM-4.5 / DeepSeek-V3.1 / Claude-4-Sonnet / OpenAI o3（通用 LLM + ReAct/搜索）",
            "claimed_score": {"GLM-4.5_GAIA": 66.0, "DeepSeek-V3.1_GAIA": 63.1, "Claude-4-Sonnet_GAIA": 68.3, "o3_GAIA": None,
                              "Tongyi_table_columns": "HLE/BrowseComp/BrowseComp-ZH/GAIA/xbench/WebWalkerQA/FRAMES"},
            "source_url": TONGYI,
            "why_not_used": "这些不是 deepresearch agent 而是「通用模型 + 搜索工具」，只适合做「agent 化是否带来增益」的对照，不入主表。",
        },
        {
            "name": "DeepSeek-V3.2 / MiroThinker / WebShaper 等 GAIA 榜选手",
            "claimed_score": {"see": "sota2 GAIA text-only leaderboard"},
            "source_url": "https://www.sota2.com/research/sota/deep-research-on-gaia-text-only-original-test",
            "why_not_used": "聚合站数据，未逐条回溯原报告；需要时按同一规则补核后再入表。",
        },
    ],
    "recommended_baseline": "Tongyi DeepResearch (30B-A3B)",
    "reasoning": (
        "选它作主 baseline 的四条理由："
        "① **开源 + 可复跑 + 多榜 SOTA 三者同时满足**：GAIA 70.9 / FRAMES 90.6 / WebWalkerQA 72.2 / xbench-DeepSearch 75.0，"
        "官方放权重与复现脚本（GitHub Alibaba-NLP/DeepResearch）；OpenAI Deep Research 闭源且无逐题数据，pfb 侧无法复跑；"
        "② **榜单类型匹配 pfb 的题型**：pfb 这 5 题是短答案事实检索（H200 TDP / Transformer head 数 / HotpotQA 规模 / LLaMA2 参数量 / DeepSeek-V3 参数），"
        "对应 GAIA(L1/L2)、FRAMES、WebWalkerQA 这类「短答案 + 可核验」集合，而不是 RACE 那种长报告评分；"
        "③ **成本可控**：30.5B 总参 / 3.3B 激活，单机可跑，比 o3-pro 级闭源 API 便宜一到两个数量级，适合 pfb 的多 seed 重复评测；"
        "④ **有完整对手表**（同报告 §4 Table 1 含 OpenAI / Gemini / Kimi / GLM / DeepSeek），pfb 的分数可以直接插进同一张表定位。"
        "配套建议：再拿 DeepResearcher(7B) 作**同口径副 baseline**——它是唯一公开 NQ/TQ/HotpotQA/2Wiki 四项 F1 的开源深研 agent，"
        "适合做「pfb 改进量 vs 同口径 SOTA」的比较。分工：Tongyi 定天花板，DeepResearcher 定同口径基线。"
        "不推荐用 DeepResearch Bench RACE 排名选主 baseline：DeepResearcher 的 RACE 只有 10.77 而 HotpotQA F1 有 52.8，"
        "说明 RACE 考的是长报告能力，与 pfb 的 5 题错配（详见 contradictions.X4）。"
    ),
    "alternatives": [
        {"name": "DeepResearcher (Qwen2.5-7B)", "when": "需要 EM/F1 同口径，或预算只够跑 7B 时",
         "anchor": "HotpotQA F1 52.8 / 2Wiki F1 59.7 / NQ F1 39.6 / TQ F1 78.4"},
        {"name": "LangChain Open Deep Research (GPT-5)", "when": "需要开源框架 + 最高 RACE（50.60），且接受绑定闭源 backbone",
         "anchor": "RACE 50.60（高于 Gemini-2.5-Pro DR 49.71），但 FACT 引用准确率仅 32.94"},
        {"name": "OpenAI Deep Research (o3)", "when": "需要闭源天花板参照（只能引用公开分数，不能复跑）",
         "anchor": "GAIA pass@1 67.36 / cons@64 72.57 / HLE 26.6"},
    ],
    "verification": {
        "systems_total": len(systems),
        "systems_with_url": sum(1 for s in systems if s["source_url"].startswith("http")),
        "systems_with_numeric_aggregate": sum(1 for s in systems if any(v is not None for v in s["aggregate"].values())),
        "systems_with_per_question_scores": 0,
    },
}

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sm-bench-sota-table.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
print("written", out)
print(json.dumps(doc["verification"], ensure_ascii=False))
