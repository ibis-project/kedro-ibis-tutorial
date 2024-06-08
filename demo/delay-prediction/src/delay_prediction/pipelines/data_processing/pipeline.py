from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_flights


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_flights,
                inputs="flights",
                outputs="preprocessed_flights",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_flights", "weather"],
                outputs="model_input_table",
            ),
        ]
    )
