# Hobby Hub

Hobby Hub is a dynamic platform designed to create a vibrant community where individuals passionate about various hobbies can come together. Users can explore a wide array of hobbies, connect with people globally, and share experiences, posts, and photos related to their interests. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features

- **Discover, Connect, Share**: Explore hobbies, connect with like-minded individuals, and share your experiences.
- **Tailored Experience**: Personalize your feed by selecting your hobbies during registration.
- **User Profiles**: Create and edit user profiles, follow and unfollow other users.
- **Home Feed and Explore**: See posts from people who share your interests and discover new hobbies.
- **Notifications and Messages**: Stay updated with notifications and communicate with other users.
- **Responsive Design**: Dynamic website layout suitable for all screen resolutions.
- **Image Compression**: Compress images by size and quality before uploading.
- **Post Management**: Like, repost, comment on posts, and delete your own posts.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RatikArora/Hobby-Hub.git
    cd "Hobby Hub"
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000`.

## Usage

### Registration and Login

- **Register**: Create a new account by providing a username, email, password, and selecting your hobbies.
- **Login**: Use your username and password to log in.

### Profile

- **View and Edit Profile**: View your profile, edit your details, and update your profile picture.
- **Follow and Unfollow Users**: Follow users who share your interests and get updates on their posts.

### Home Feed and Explore

- **Home Feed**: See posts from users who share your hobbies and from those you follow.
- **Explore**: Discover new posts and hobbies from users around the world.

### Post Management

- **Create Posts**: Share your experiences by creating new posts with text and images.
- **Interact with Posts**: Like, repost, and comment on posts.
- **Delete Posts**: Remove your own posts if needed.

### Notifications and Messages

- **Notifications**: Stay updated with new followers, likes, comments, and reposts.
- **Messages**: Communicate directly with other users through messages.

## Contributing

We welcome contributions to Hobby Hub! Here's how you can help:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix.
3. **Commit your changes**.
4. **Push to your branch**.
5. **Create a pull request**.

## Future Improvements

- **Image Compression**: Compress images by size and quality before uploading.
- **Responsive Design**: Use Tailwind CSS to make the website dynamic for every screen resolution.
- **Post Enhancements**: Add the ability to upload multiple photos, prevent empty posts, and use user-specific time zones.
- **Interaction Features**: Implement like, repost, and comment buttons, and allow users to delete their own posts only.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
