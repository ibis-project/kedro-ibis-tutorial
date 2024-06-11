"""Delay Prediction
"""

__version__ = "0.1"


def _auto_patch_ibis() -> None:
    import ibis.backends.postgres.compiler
    import ibis.common.exceptions as com

    def visit_Hash(self, op, *, arg):
        arg_dtype = op.arg.dtype

        if arg_dtype.is_int16():
            return self.f.hashint2extended(arg, 0)
        elif arg_dtype.is_int32():
            return self.f.hashint4extended(arg, 0)
        elif arg_dtype.is_int64():
            return self.f.hashint8extended(arg, 0)
        elif arg_dtype.is_float32():
            return self.f.hashfloat4extended(arg, 0)
        elif arg_dtype.is_float64():
            return self.f.hashfloat8extended(arg, 0)
        elif arg_dtype.is_string():
            return self.f.hashtextextended(arg, 0)
        elif arg_dtype.is_macaddr():
            return self.f.hashmacaddr8extended(arg, 0)

        raise com.UnsupportedOperationError(
            f"Hash({arg_dtype!r}) operation is not supported in the "
            f"{self.dialect} backend"
        )

    ibis.backends.postgres.compiler.PostgresCompiler.visit_Hash = visit_Hash


_auto_patch_ibis()
