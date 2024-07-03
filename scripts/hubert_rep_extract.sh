CONFIG="config/spt_base_cfg.json"
# AUDIO_DIR="/remote-home/share/data/SpeechPretrain/LibriSpeech/LibriSpeech"
# REP_DIR="/remote-home/share/data/SpeechPretrain/hubert_rep/LibriSpeech"
AUDIO_DIR="/home/anthony/vocos/training_data"
REP_DIR="/home/anthony/taiwan-speech/hubert_rep/dummy"
EXTS="wav"
SPLIT_SEED=0
VALID_SET_SIZE=3



CUDA_VISIBLE_DEVICES=0 python scripts/hubert_rep_extract.py\
    --config ${CONFIG}\
    --audio_dir ${AUDIO_DIR}\
    --rep_dir ${REP_DIR}\
    --exts ${EXTS}\
    --split_seed ${SPLIT_SEED}\
    --valid_set_size ${VALID_SET_SIZE}