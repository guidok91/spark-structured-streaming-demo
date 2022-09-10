from pyspark.sql.types import FloatType, LongType, StringType, StructField, StructType

MOVIE_RATINGS_SOURCE_SCHEMA = StructType(
    [
        StructField("user_id", StringType()),
        StructField("movie_id", StringType()),
        StructField("rating", FloatType()),
        StructField("rating_timestamp", LongType()),
    ]
)