from client import LlmDistributedTraceLatencyBottleneckDetectorClient

def main():
    client = LlmDistributedTraceLatencyBottleneckDetectorClient()
    spans = [{"span": "auth", "ms": 12}, {"span": "vector_search", "ms": 650}, {"span": "llm_completion", "ms": 190}]
    res = client.analyze_trace_bottlenecks(spans)
    print(f"Bottleneck: {res['bottleneck_span_id']}")
    print(f"Latency Contribution: {res['latency_contribution_pct']}%")
    print(f"Optimization: {res['optimization_advice']}")

if __name__ == "__main__":
    main()
