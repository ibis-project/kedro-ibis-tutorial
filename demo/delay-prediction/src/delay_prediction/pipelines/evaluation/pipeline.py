from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs=["pipe", "X_test", "y_test"],
            outputs=None,
        ),
    ])
