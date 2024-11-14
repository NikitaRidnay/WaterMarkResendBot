Resending posts from private channels with customs watermarks
How it work:
1) Telethon use telegram client to get posts(messages) from private channel
2) Then bot download media files in pc or vps/vds folder
3) Script recognize watermark by trigger words by old owners using machine vision (by using easyOCR AI)
4) Add own watermark using opencv library and save as new file in folder
5) Then bot sends new messages with all media and text to target channels
6) Delete all unnecessary media files that have already been sent (using OS library)
