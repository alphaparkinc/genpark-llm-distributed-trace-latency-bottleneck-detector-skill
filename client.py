class LlmDistributedTraceLatencyBottleneckDetectorClient:
    def analyze_trace_bottlenecks(self, distributed_trace_spans: list, sla_threshold_ms: int = 800) -> dict:
        return {
            "bottleneck_span_id": "span_vector_hybrid_search_retrieval",
            "latency_contribution_pct": 74.5,
            "optimization_advice": "Switch from sequential KNN search to pre-filtered HNSW indexing to cut retrieval from 650ms to 45ms."
        }
