from pydantic import BaseModel, computed_field

from ..api.benchmark import Benchmark
from ._evaluation import Evaluation
from ._metrics._benchmark_metrics import BenchmarkMetrics


class BenchmarkOutput(BaseModel):
    info: Benchmark
    repeats: int = 1
    evaluations: list[Evaluation | None]

    @computed_field
    @property
    def metrics(self) -> BenchmarkMetrics:
        return BenchmarkMetrics(evals=self.evaluations)
