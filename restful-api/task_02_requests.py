import requests
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post['title'])
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save to CSV"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json()
            
            # Structure data for CSV
            csv_data = []
            for post in posts:
                csv_data.append({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
            
            # Write to CSV file
            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(csv_data)
            
            print("Data saved to posts.csv")
            
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")