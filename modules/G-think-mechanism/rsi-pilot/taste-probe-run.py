#!/usr/bin/env python3
"""taste-probe: 27b 独立质疑 #53 现象, 看能否收敛到 D 的 taste 判断 (信息论 claim + 非线性测量).
Arm A = 27b + D式质疑机制规程; Arm B = 27b 裸基线. 盲输入不含 D 的结论."""
import json, urllib.request, time, os

API = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
OUT = os.path.dirname(os.path.abspath(__file__))

BLIND = """你是一位研究 AI 推理系统的研究员。下面是同事积累的一个实验现象，他想知道怎么把它做成一个站得住的研究 claim。

## 现象（已实测，三个独立数据源）
我们在分析 LLM 做 GPU 性能分析时的推理树（树 = 模型分解问题的层级结构，L1 最浅，L4 最深）。
"供给侧瓶颈判定节点" = 树中判定"哪个硬件资源是系统瓶颈"（SM 频率/内存带宽/指令吞吐/occupancy 等）的节点。
实测：这类节点在 L4（最深层）显著富集，三个独立数据源全部统计显著：
- 源①：L4 占该类节点 55.8%（全体 L4 占比 51.3%），χ²=5.98, p=0.0145
- 源②：L4 占 66.2%（全体 60.2%），χ²=16.13, p=0.0001
- 源③：L4 占 47.5%（全体 43.1%），χ²=28.51, p≈0.0000

## 原始问题（提出者原话）
"能否单独计算阐述发表，还是只能当故事动机？"
背景：提出者认为深层节点"对确定计算模型瓶颈的信息贡献可能更大"，想论证树结构的合理性（深层=瓶颈判定所在，浅层=枚举）。

## 你的任务
1. 先质疑这个现象和原始问题本身（前提对不对、问法对不对、有没有更根本的问题）
2. 给出你认为站得住的研究 claim（一句话）
3. 给出测量方式：用什么量、什么统计方法，为什么是这个
4. 说出你这个 claim 最大的可防御性风险（审稿人会打哪一刀）

直接回答，不要客套。"""

ARM_A_PRE = """# 操作规程：D 式质疑（必须按此执行）
## 机制（4 步）
1. 先验怀疑：看到任何想法/结论/实验设计，默认立场="这有漏洞"。不是"让我检查"，是"我假设它错，你说服我"。
2. 质疑前提（针对前提不是细节）：方向（这个问题问对了吗/前提对吗）、前人（有没有人已经解决了）、更快（有没有更低成本的路）、性价比（值不值得做）。
3. 自我反驳过滤：对每个质疑自己尝试反驳——能反驳=表面质疑丢弃；不能反驳=真质疑保留。注意：猜的但完全不能证伪=有效质疑（有效性取决于你自己能不能反驳它，不取决于它是否正确）。
4. 输出=检索信号：攻不破的质疑=停止条件+优化方向+检索触发（知道自己不知道→该查什么）。

## 分解=同机制另一面
先找"我不确定"的具体点，分解树从不确定点长出来。不确定点=分解节点=检索触发点。

## 质量标准
- 不要提出自己能反驳的质疑
- 对"如何思考"不完全肯定时，回到第一性原理而不是凭直觉
- 拆细≠新信息：代数展开=零增益；每个新断言必须携带条件熵意义上的新信息

按此规程处理下面的材料。

---

"""

def call(messages, max_tokens=3000, temperature=0):
    body = json.dumps({"model": MODEL, "messages": messages,
                       "max_tokens": max_tokens, "temperature": temperature}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                d = json.loads(r.read())
            ch = d["choices"][0]
            content = ch["message"].get("content") or ""
            reasoning = ch["message"].get("reasoning") or ""
            return {"content": content, "reasoning": reasoning,
                    "finish": ch.get("finish_reason")}
        except Exception as e:
            if attempt == 2:
                return {"content": "", "reasoning": "", "error": str(e)}
            time.sleep(5)

def run_arm(name, system_pre):
    messages = [{"role": "user", "content": system_pre + BLIND}]
    t0 = time.time()
    res = call(messages)
    res["elapsed_s"] = round(time.time() - t0, 1)
    path = f"{OUT}/taste-probe-{name}.txt"
    with open(path, "w") as f:
        f.write(f"# origin: ai (taste-probe {name}, {time.strftime('%Y-%m-%d %H:%M')})\n")
        f.write(f"# model={MODEL} finish={res.get('finish')} elapsed={res['elapsed_s']}s\n")
        if res.get("error"):
            f.write(f"ERROR: {res['error']}\n")
        else:
            f.write("\n## REASONING\n\n" + res["reasoning"] + "\n\n## CONTENT\n\n" + res["content"] + "\n")
    print(f"{name}: finish={res.get('finish')} elapsed={res['elapsed_s']}s "
          f"content_len={len(res.get('content',''))} reasoning_len={len(res.get('reasoning',''))}")

if __name__ == "__main__":
    run_arm("A", ARM_A_PRE)
    run_arm("B", "")
