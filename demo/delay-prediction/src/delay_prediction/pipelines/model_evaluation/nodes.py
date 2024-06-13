from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

if TYPE_CHECKING:
    import ibis.expr.types as ir


logger = logging.getLogger(__name__)


def evaluate_model(
    pipe: Pipeline, X_test: ir.Table, y_test: ir.Column
):
    """Calculates and logs the coefficient of determination.

    Args:
        pipe: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = pipe.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    logger.info("Model has an accuracy of %.3f on test data.", score)
