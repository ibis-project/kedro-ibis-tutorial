from __future__ import annotations

import random
from typing import TYPE_CHECKING

import ibis
import ibis_ml as ml
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

if TYPE_CHECKING:
    import ibis.expr.types as ir


def split_data(
    flight_data: ir.Table
) -> tuple[ir.Table, ir.Column, ir.Table, ir.Column]:
    """Splits data into training and test sets.

    Args:
        data: Data containing features and target.
    Returns:
        Split data.
    """
    flight_data_with_unique_key = flight_data.mutate(
        unique_key=ibis.literal(",").join(
            [flight_data.carrier, flight_data.flight.cast(str), flight_data.date.cast(str)]
        )
    )

    # Fix the random numbers by setting the seed
    # This enables the analysis to be reproducible when random numbers are used
    random.seed(222)

    # Put 3/4 of the data into the training set
    random_key = str(random.getrandbits(256))
    data_split = flight_data_with_unique_key.mutate(
        train=(flight_data_with_unique_key.unique_key + random_key).hash().abs() % 4 < 3
    )

    # Create data frames for the two sets:
    train_data = data_split[data_split.train].drop("unique_key", "train")
    test_data = data_split[~data_split.train].drop("unique_key", "train")

    X_train = train_data.drop("arr_delay")
    X_test = test_data.drop("arr_delay")
    y_train = train_data.arr_delay
    y_test = test_data.arr_delay
    return X_train, X_test, y_train, y_test


def train_model(X_train: ir.Table, y_train: ir.Column) -> Pipeline:
    """Trains the logistic regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for whether a plane arrived more than 30
            minutes late.

    Returns:
        Trained model.
    """
    flights_rec = ml.Recipe(
        ml.ExpandDate("date", components=["dow", "month"]),
        ml.Drop("date"),
        ml.TargetEncode(ml.nominal()),
        ml.DropZeroVariance(ml.everything()),
        ml.MutateAt("dep_time", ibis._.hour() * 60 + ibis._.minute()),
        ml.MutateAt(ml.timestamp(), ibis._.epoch_seconds()),
        # By default, PyTorch requires that the type of `X` is `np.float32`.
        # https://discuss.pytorch.org/t/mat1-and-mat2-must-have-the-same-dtype-but-got-double-and-float/197555/2
        ml.Cast(ml.numeric(), "float32"),
    )
    pipe = Pipeline([("flights_rec", flights_rec), ("lr_mod", LogisticRegression())])
    pipe.fit(X_train, y_train)
    return pipe
