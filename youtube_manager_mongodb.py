from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<db_password>@cluster0.namf7.mongodb.net/", tlsAllowInvalidCertificates=True)
# replace <db_password> with the actual password for connecting the db with username youtubepy from atlas mongodb
# not a good idea to include id and password in code files
# tlsAllowInvalidCertificates=True - not a good way to handle SSL

db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}. Name: {video['name']} and Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id': video_id})

def main():
    while True:
        print("\n YouTube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delet a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            new_name = input("Enter the updated video name: ")
            new_time = input("Enter the updated video duration: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
