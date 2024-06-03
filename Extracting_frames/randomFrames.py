import cv2, os, random 
from ultralytics import YOLO


model = YOLO('yolov8n.pt')

def vid_to_frame(vid_path, output_folder, num_frames=30):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    cap = cv2.VideoCapture(vid_path)

    # get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # ensure num_frames does not exceed total_frames
    num_frames = min(num_frames, total_frames)

    # random frame indices
    selected_indices = set()
    while len(selected_indices) < num_frames:
        selected_indices.add(random.randint(0, total_frames - 1))

    success, image = cap.read()
    count = 0
    frame_index = 0

    while success and count < num_frames:
        if frame_index in selected_indices:
            results = model(image)

            for r in results[0].boxes:
                x1, y1, x2, y2 = map(int, r.xyxy[0])
                cls = int(r.cls[0])
                if cls == 0:
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(image, "Person", (x1, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
            
            # Save the frames
            frames = os.path.join(output_folder, f"frame_{frame_index:04d}.jpg")
            cv2.imwrite(frames, image)
            count += 1

        # Read the next frame
        success, image = cap.read()
        frame_index += 1
    
    cap.release()
    print(f"Extracted {count} frames randomly from {vid_path}")


vid_path = "C:/Users/ibroh/Downloads/Human.mp4"
output_folder = "C:/Users/ibroh/OneDrive/Desktop/Randomframes"

vid_to_frame(vid_path, output_folder)

