### collection by a date range
python scrna_parser_runner.py parser -d 2020/04/23-2020/05/21 -el ../geo_gse_collection.txt
### collection by known GSE numbers
#python scrna_parser_runner.py known -i need_gse.txt -gc 0 -p ./geo_gse/ -o geo_gse_scrna_collection_all_new2.txt
### collection by a given direcotry where gse XML was saved
#python scrna_parser_runner.py local -p ./geo_gse -o geo_gse_scrna_collection.txt
