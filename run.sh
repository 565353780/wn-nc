XYZ_FOLDER_PATH=/home/chli/Downloads/
XYZ_FILE_ID=sample_9

python main_wnnc.py ${XYZ_FOLDER_PATH}${XYZ_FILE_ID}.xyz --width_config l0 --tqdm

./bin/main_GaussRecon_cpu -i ./results/${XYZ_FILE_ID}.xyz -o ./results/${XYZ_FILE_ID}.ply
