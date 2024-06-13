from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs="model_input_table",
                outputs=["X_train", "X_test", "y_train", "y_test"],
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="pipe",
            ),
        ]
    )
