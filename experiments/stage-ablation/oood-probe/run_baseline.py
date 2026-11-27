import sys, time
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation")
from ablation_harness import call_llm
q = open("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q10-oood-cyclone.txt").read().strip()
prompt = "直接回答下面的问题。要求：识别所有物理机制，每个机制给量化影响（数值/公式），指出主导机制，列出黑盒表。\n\n【问题】\n" + q
t0 = time.time()
out, _ = call_llm(prompt, max_tokens=8000, temperature=0.7, retries=2)
open("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/baseline-arm.txt", "w").write(out or "")
print("baseline done:", len(out or ""), "chars,", round(time.time()-t0, 1), "s")
