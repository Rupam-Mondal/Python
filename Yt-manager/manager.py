import json

def load_data():
    try:
        with open('Youtube.txt' , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open('youtube.txt' , 'w') as file:
        json.dump(videos , file)

def list_all_videos(videos):
    for index,video in  enumerate(videos , start=1):
        print(f"{index}. {video['name']} , Duration : {video['time']}")

def add_video(videos):
    name = input("Enter video name = ")
    time = input("Enter video time = ")
    videos.append({'name' : name , 'time' : time})
    save_data(videos)


def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():  
    videos = load_data()
    while True:
        print("\n Youtube manager | choose an option \n")
        print("1. List all favourite videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app")

        choice = int(input("Enter your choice = "))

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()