CREATE EXTERNAL TABLE IF NOT EXISTS `db_csv`.`data` (
 `id` string,
 `cliente` string,
 `f_slicitud` string,
 `monto` string,
 `cuota` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ('field.delim' = ',')
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://bucket-aws-1/csv_output/'
TBLPROPERTIES ('classification' = 'csv');
