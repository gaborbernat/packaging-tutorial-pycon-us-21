# Type hinting (and mypy)

[Talk for PyCon US 2019](https://www.youtube.com/watch?v=hTrjTAPnA_k/).

## Abstract

Type hinting for Python (as a linter tool) came out in September 2015 as part of Python 3.5 (and was championed by Guido
himself). Since then, variable annotations (plus, more recently, protocols) improved its capabilities even further. Over
the last two years, tools, such as mypy, could build on top of it. Slowly, these annotations have emerged from a proof
of concept state (e.g., mypy API planning) to becoming a stable feature.

In this presentation, I'll tell my story of using type hints for both adding type hinting and checking type correctness
for a library supporting both Python 2 and 3 and reusing this information to insert type data into the generated Sphinx
documentation automatically.
