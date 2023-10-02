import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
# Script generated for node Amazon S3
AmazonS3_node163956 = glueContext.create_dynamic_frame.from_options(
 format_options={"quoteChar": '"', "withHeader": True, "separator": ";"},
 connection_type="s3",
 format="csv",
 connection_options={
 "paths": ["s3://bucket-aws-1/csv_input/Data.csv"],
 "recurse": True,
 },
 transformation_ctx="AmazonS3_node163956",
)
# Script generated for node Change Schema
ChangeSchema_node163956 = ApplyMapping.apply(
 frame=AmazonS3_node163956,
 mappings=[
 ("ID_cliente", "string", "ID_cliente", "string"),
 ("Cliente", "string", "Cliente", "string"),
 ("Fecha_solicitud", "string", "Fecha_solicitud", "string"),
 ("monto", "string", "monto", "string"),
 ("cuota", "string", "cuota", "string"),
 ],
 transformation_ctx="ChangeSchema_node163956",
)
# Script generated for node Amazon S3
AmazonS3_node163956 = glueContext.write_dynamic_frame.from_options(
 frame=ChangeSchema_node163956,
 connection_type="s3",
 format="csv",
 connection_options={
 "path": "s3://bucket-aws-1/csv_output/",
 "compression": "snappy",
 "partitionKeys": [],
 },
 transformation_ctx="AmazonS3_node163956",
)
job.commit()
