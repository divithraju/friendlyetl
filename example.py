from friendlyetl import run_etl

run_etl(
    source_path="/home/divithraju/sales-data.csv",
    destination_path="/home/divithraju/data.xlsx",
    transform_condition="remove_duplicates,remove_nulls,handle_missing_data,validate_data"
)
