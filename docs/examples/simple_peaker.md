``` python
--8<-- "examples/00_simple_peaker.py:10"
```

1. Strategies are implemented by subclassing from `BaseStrategy`.
2. Strategy decision points are labelled with the `action` decorator, and given custom labels.
3. When backtesting, schedules must be set for each decision point.
