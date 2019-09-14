from video_indexer import VideoIndexer
import time

def extract_video_features(video_file_path):
    vi = VideoIndexer(
        vi_subscription_key='a2584f5eacf04e099da8e56d771f755b',
        vi_account_id='378fbaf6-660a-4aaf-90fb-1da9bde746ee',
        vi_location='trial'
    )
    video_id = vi.upload_to_video_indexer(
       input_filename=video_file_path,
       video_name=video_file_path,
       video_language='English'
    )
    time.sleep(600)
    metadata = vi.get_video_info(
        video_id,
        video_language='English'
    )
    features = vi.extract_summary_from_video_indexer_info(metadata)
    return features