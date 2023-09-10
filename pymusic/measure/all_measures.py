from dataclasses import dataclass, field


@dataclass
class AllMeasuresBuilder:
    measures: list = field(default_factory=list)
    pass
